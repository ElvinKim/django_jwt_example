from django.conf.urls  import url
from members.views import *


urlpatterns = [
    url(r'^$', MemberListAPIView.as_view(), name='member_list'),
]
