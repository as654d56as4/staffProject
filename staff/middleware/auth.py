from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class AuthMiddleware(MiddlewareMixin):
    '''中间件1'''

    def process_request(self,request):
        if request.path_info == '/login/':
            return
        info=request.session.get("info")
        if info:
            return
        return redirect('/login/')