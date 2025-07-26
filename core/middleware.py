import os
from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class ClonedSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o template solicitado existe
        path = request.path.lstrip('/') or 'index'
        if not path.endswith('.html'):
            path += '.html'
        template_path = os.path.join(settings.BASE_DIR, 'copart_clone', 'templates', 'copart', path)
        
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type='text/html')
        
        # Se não encontrou, continua o processamento normal
        return None
