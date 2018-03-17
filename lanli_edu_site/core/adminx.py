from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import School, Grade, Class, Lecture, LanliUser, Notification
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "兰里教育坊",
             "content": "<h3> 欢迎来到兰里教育坊! </h3><p>有需要请联系开发: <br/>手机号码 : 15995939903</p>"},
            # {"type": "chart", "model": "app.accessrecord", "chart": "user_count",
            #  "params": {"_p_date__gte": "2013-01-08", "p": 1, "_p_date__lt": "2013-01-29"}},
            {"type": "list", "model": "core.lecture", "params": {"o": "-expired_time"}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": Lecture}, {"model": LanliUser}, {"model": Notification}]},
            {"type": "addform", "model": School},
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    global_search_models = [Lecture, LanliUser]
    global_models_icon = {
        Lecture: "fa fa-laptop", LanliUser: "fa fa-cloud"
    }
    menu_style = 'default'  # 'accordion'


class MaintainInline(object):
    model = School
    extra = 1
    style = "accordion"


@xadmin.sites.register(School)
class SchoolAdmin(object):
    list_display = ("name", "address")
    list_display_links = ("name",)
    search_fields = ["name", "address"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True

    actions = [BatchChangeAction, ]


@xadmin.sites.register(Grade)
class GradeAdmin(object):

    list_display = (
        "name", "school",
    )
    list_display_links = ("name",)

    style_fields = {"name": "radio-inline"}

    reversion_enable = True


@xadmin.sites.register(Class)
class ClassAdmin(object):
    list_display = ("name", "grade")
    list_display_links = ("name",)

    search_fields = ["name"]
    style_fields = {"name": "checkbox-inline"}


@xadmin.sites.register(Lecture)
class LectureAdmin(object):
    list_display = (
        "title", "level", "group_id", "expired_time")
    list_display_links = ("title",)

    reversion_enable = True


"""
@xadmin.sites.register(LanliUser)
class LanliUserAdmin(object):
    list_display = (
        "username", "first_name", "last_name", "sex", "state", "money", "last_login_time")
    list_display_links = ("username",)

    reversion_enable = True
"""


@xadmin.sites.register(Notification)
class NotificationAdmin(object):

    list_display = ("title", "content")
    list_display_links = ("title",)
