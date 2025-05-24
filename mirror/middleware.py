import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class ClonedSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o template solicitado existe
        path = request.path.lstrip('/')
        
        # Mapeamento de URLs para arquivos
        if not path or path == '/':
            path = 'index.html'
        elif path.endswith('/'):
            path = path.rstrip('/') + '.html'
        elif '.' not in os.path.basename(path):
            path += '.html'
            
        template_path = os.path.join('copart_clone/static', path)
        
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Verifica se é HTML para definir o content-type corretamente
                content_type = 'text/html' if path.endswith('.html') else 'text/plain'
                return HttpResponse(content, content_type=content_type)
        
        return None
