from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

from blog_back.models import User


class SessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        if path in ['/blog_back/login/', '/blog_back/register/',
                    '/blog_before/index/',
                    '/blog_before/about/',
                    '/blog_before/time/',
                    '/blog_before/info/',
                    '/blog_before/media/.*/']:
            return None
        else:
            try:
                user_id = request.session['user_id']
                user = User.objects.filter(pk=user_id).first()
                request.user = user
                return None
            except Exception as e:
                return HttpResponseRedirect(reverse('blog_back:login'))
