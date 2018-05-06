from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from urllib import parse

from .utils import WechatLogin


from .models import School, Grade, Class, Lecture, LanliUser, Notification


def index(request):
    now = datetime.now()
    html = "<html><body>Hello World!<br/>It is now %s.</body></html>" % now
    return HttpResponse(html)


@login_required
def edu(request):
    return render(request, "core/index.html")


@login_required
def seminar(request):
    return render(request, "core/seminar.html")


@login_required
def lectures(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


@login_required
def lecture_detail(request, id):
    lecture = Lecture.objects.get(id=id)
    context = {
        "id": lecture.id,
        "title": lecture.title,
        "content": lecture.content
    }
    return render(request, "core/lecture_detail.html", context=context)


@login_required
@csrf_exempt
def lecture_signup(request):
    lecture_id = request.POST.get("lecture_id")
    lecture = Lecture.objects.get(id=lecture_id)
    request.user.attended_lectures.add(lecture)
    return JsonResponse({
            'code': 0,
            'data': None,
            'msg': "Lecture sign up successfully."
        })


@login_required
def experience(request):
    return render(request, "core/seminar.html")


@login_required
def photos(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


@login_required
def interaction(request):
    return render(request, "core/interaction.html")


@login_required
def teachers(request):
    return render(request, "core/seminar.html")


@login_required
def books(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


@login_required
def home_school(request):
    return render(request, "core/interaction.html")

@login_required
def home(request):
    context = {
    }
    return render(request, "core/home.html")


@login_required
def userinfo(request):
    context = {
        "sex": "男" if request.user.sex == 1 else "女" if request.user.sex == 2 else "未知",
        "type": "学生" if request.user.type == 1 else "老师"
    }
    return render(request, "core/userinfo.html", context=context)


@login_required
def history_lectures(request):
    my_lectures = request.user.attended_lectures.all()
    return render(request, "core/history_lectures.html", {"my_lectures": my_lectures})


@login_required
def study_history(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


@login_required
def notifications(request):
    return render(request, "core/interaction.html")


class WechatViewSet(View):
    wechat_api = WechatLogin()


class HomeAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/home/")
        return redirect(url)


class LecturesAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/lectures/")
        return redirect(url)


class SeminarAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/seminar/")
        return redirect(url)


class ExperienceAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/experience/")
        return redirect(url)


class PhotosAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/photos/")
        return redirect(url)


class TeachersAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/teachers/")
        return redirect(url)


class BooksAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/books/")
        return redirect(url)


class HomeSchoolAuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url("http://www.lanliedu.com/home-school/")
        return redirect(url)


class LoginView(WechatViewSet):
    def get(self, request):
        origin_url = parse.unquote(request.GET.get("next"))
        parsed = parse.urlparse(origin_url)
        code = parse.parse_qs(parsed.query)['code'][0]
        state = parse.parse_qs(parsed.query)['state'][0]
        token, openid = self.wechat_api.get_access_token(code)
        print("token: {}, openid:{}".format(token, openid))
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
            'username': user_info['openid'],
            'password': ''
        }
        if not LanliUser.objects.filter(username=user_data['username']).exists():
            user = LanliUser.objects.create(**user_data)
        else:
            user = LanliUser.objects.filter(username=user_data['username']).first()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        # user = authenticate(username=user_data['username'], password=user_data['password'])
        # print("user {} is authencated? {}".format(user_data['username'], user.is_authenticated()))
        login(request, user)
        # 授权登录成功，进入主页
        return redirect(parsed.path)

