from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^Hello', views.get_test),
    url(r'^Hello', views.post_test),
    url(r'^get-test', views.get_test),
    url(r'^make-room', views.make_room),
    url(r'^list-room', views.list_room),
]