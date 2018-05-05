from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.views.generic import View
from datetime import datetime

from .utils import WechatLogin


from .models import School, Grade, Class, Lecture, LanliUser, Notification


def index(request):
    now = datetime.now()
    html = "<html><body>Hello World!<br/>It is now %s.</body></html>" % now
    return HttpResponse(html)


def edu(request):
    return render(request, "core/index.html")


def seminar(request):
    return render(request, "core/seminar.html")


def lectures(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


def interaction(request):
    return render(request, "core/interaction.html")


@login_required
def home(request):
    return render(request, "core/home.html")


class WechatViewSet(View):
    wechat_api = WechatLogin()


class HomeAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/home/")
        return redirect(url)


class LoginView(WechatViewSet):
    def get(self, request):
        print("get_full_path: {}".format(request.get_full_path()))
        print("next parameter: {}".format(request.GET.get("next")))
        code = request.GET['code']
        token, openid = self.wechat_api.get_access_token(code)
        if token is None or openid is None:
            return HttpResponseServerError('get code error')
        user_info, error = self.wechat_api.get_user_info(token, openid)
        if error:
            return HttpResponseServerError('get access_token error')
        user_data = {
            'nickname': user_info['nickname'],
            'sex': user_info['sex'],
            'province': user_info['province'].encode('iso8859-1').decode('utf-8'),
            'city': user_info['city'].encode('iso8859-1').decode('utf-8'),
            'country': user_info['country'].encode('iso8859-1').decode('utf-8'),
            'avatar': user_info['headimgurl'],
            'openid': user_info['openid']
        }
        user = LanliUser.objects.filter(is_effective=True).filter(wechat=user_data['openid'])
        if user.count() == 0:
            user = LanliUser.objects.create(username=user_data['nickname'],
                                              wechat_avatar=user_data['avatar'],
                                              wechat=user_data['openid'],
                                              password='')
            login(request, user)
        else:
            login(request, user.first())
        # 授权登录成功，进入主页
        return home(request)

