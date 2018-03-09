# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import hello, index, interaction, home, seminar

urlpatterns = [
    url(r'^$', hello, name='index'),
    url(r'^edu/$', index, name='page_edu'),
    url(r'^interaction/$', interaction, name='page_interaction'),
    url(r'^home/$', home, name='page_home'),
    url(r'^seminar/$', seminar, name='seminar'),
    #url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    #url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    #url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    #url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    #url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    #url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    #url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    #url(r'^misc$', MiscView.as_view(), name='misc'),
]
