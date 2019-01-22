import re

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

from blog_back.models import User


class SessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        detail_path = '/blog_before/info/.*'
        path = request.path
        not_need_check = ['/blog_back/login/', '/blog_back/register/',
                          '/blog_before/index/',
                          '/blog_before/about/',
                          '/blog_before/time/',
                          '/blog_before/info/.*',
                          '/media/.*', '/static/.*']
        for check_path in not_need_check:
            if re.match(check_path, path):
                return None
        else:
            try:
                user_id = request.session['user_id']
                user = User.objects.filter(pk=user_id).first()
                request.user = user
                return None
            except Exception as e:
                return HttpResponseRedirect(reverse('blog_back:login'))
