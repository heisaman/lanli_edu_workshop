# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import index, edu, interaction, home, seminar, lectures, experience, photos, \
    teachers, books, home_school, userinfo, history_lectures, study_history, notifications,\
    HomeAuthView, LoginView, LecturesAuthView, SeminarAuthView, ExperienceAuthView, PhotosAuthView,\
    TeachersAuthView, BooksAuthView, HomeSchoolAuthView

urlpatterns = [
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),

    url(r'^$', index, name='index'),
    url(r'^edu/$', edu, name='page_edu'),
    url(r'^lectures/$', lectures, name='lectures'),
    url(r'^seminar/$', seminar, name='seminar'),
    url(r'^experience/$', experience, name='experience'),
    url(r'^photos/$', photos, name='photos'),
    url(r'^interaction/$', interaction, name='page_interaction'),
    url(r'^teachers/$', teachers, name='teachers'),
    url(r'^books/$', books, name='books'),
    url(r'^home-school/$', home_school, name='home_school'),
    url(r'^home/$', home, name='page_home'),
    url(r'^userinfo/$', userinfo, name='userinfo'),
    url(r'^history-lectures/$', history_lectures, name='history_lectures'),
    url(r'^study-history/$', study_history, name='study_history'),
    url(r'^notifications/$', notifications, name='notifications'),

    url(r'^lectures/auth/$', LecturesAuthView.as_view(), name='lectures_auth'),
    url(r'^seminar/auth/$', SeminarAuthView.as_view(), name='seminar_auth'),
    url(r'^experience/auth/$', ExperienceAuthView.as_view(), name='experience_auth'),
    url(r'^photos/auth/$', PhotosAuthView.as_view(), name='photos_auth'),
    url(r'^teachers/auth/$', TeachersAuthView.as_view(), name='teachers_auth'),
    url(r'^books/auth/$', BooksAuthView.as_view(), name='books_auth'),
    url(r'^home-school/auth/$', HomeSchoolAuthView.as_view(), name='home_school_auth'),
    url(r'^home/auth/$', HomeAuthView.as_view(), name='page_home_auth'),
    #url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    #url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    #url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    #url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    #url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    #url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    #url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    #url(r'^misc$', MiscView.as_view(), name='misc'),
]
