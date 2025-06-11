import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class ClonedSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o template solicitado existe
        path = request.path.lstrip('/') or 'index'
        template_path = os.path.join('copart_clone/templates/copart', f"{path}.html")
        
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type='text/html')
        
        # Se não encontrou, continua o processamento normal
        return None
