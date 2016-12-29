from django.conf.urls  import url
from members.views import MemberListAPIView
from members.views import MemberDetailAPIView


urlpatterns = [
    url(r'^$', MemberListAPIView.as_view(), name='member_list'),
    url(r'^(?P<pk>\d+)/$', MemberDetailAPIView.as_view(), name='member_detail'),
]
