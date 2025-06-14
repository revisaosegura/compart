import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class ClonedSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o template solicitado existe
        path = request.path.lstrip('/') or 'index'
<<<<<<< HEAD
        template_path = os.path.join('copart_clone/templates/copart', f"{path}.html")
=======

        if not path.endswith('.html'):
            path += '.html'
        template_path = os.path.join('copart_clone/templates/copart', path)
=======
        template_path = os.path.join('copart_clone/templates/copart', f"{path}.html")

>>>>>>> f419c2e9050c98a7117cabca7a287923894cdad6
        
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type='text/html')
        
        # Se não encontrou, continua o processamento normal
        return None
