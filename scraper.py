import asyncio
import os
import sys
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurações
BASE_URL = 'https://www.copart.com.br'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
VIEWPORT = {'width': 1280, 'height': 1024}
TIMEOUT = 60000  # 60 segundos
MAX_RETRIES = 3
RETRY_DELAY = 10  # segundos

# Diretórios
SAVE_DIR = 'copart_clone/templates'
STATIC_DIR = 'copart_clone/static'

def install_playwright():
    """Instala os browsers do Playwright de forma confiável"""
    logger.info("Instalando Playwright browsers...")
    try:
        # Configura o caminho de instalação
        os.environ['PLAYWRIGHT_BROWSERS_PATH'] = os.path.join(os.getcwd(), '.playwright')
        
        # Instala via módulo para maior confiabilidade
        from playwright.__main__ import main
        import sys
        original_argv = sys.argv
        sys.argv = ['playwright', 'install']
        main()
        sys.argv = original_argv
        
        logger.info("Playwright instalado com sucesso!")
    except Exception as e:
        logger.error(f"Falha na instalação: {str(e)}")
        sys.exit(1)

def is_valid_url(url):
    """Verifica se a URL é válida para download"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False

async def download_asset(page, url, base_url):
    """Baixa um asset usando o Playwright"""
    if not is_valid_url(url):
        url = urljoin(base_url, url)
    
    if any(url.startswith(p) for p in ['data:', 'javascript:', 'mailto:', 'tel:']):
        return None, None
    
    try:
        response = await page.request.get(url)
        if response.status != 200:
            return None, None
            
        content = await response.body()
        if not content:
            return None, None
            
        content_type = response.headers.get('content-type', '')
        ext = mimetypes.guess_extension(content_type) or '.bin'
        
        parsed = urlparse(url)
        path = parsed.path.split('/')[-1] or 'asset'
        filename = f"{path.split('.')[0]}{ext}"
        filepath = os.path.join(STATIC_DIR, filename)
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(content)
            
        return url, filename
        
    except Exception as e:
        logger.warning(f"Erro ao baixar {url}: {str(e)}")
        return None, None

async def scrape_page():
    """Faz scraping da página principal"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=True,
                    timeout=TIMEOUT,
                    # Configurações específicas para ambientes restritos
                    args=[
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-dev-shm-usage'
                    ]
                )
                
                context = await browser.new_context(
                    user_agent=USER_AGENT,
                    viewport=VIEWPORT,
                    locale='pt-BR',
                    timezone_id='America/Sao_Paulo'
                )
                
                page = await context.new_page()
                
                try:
                    logger.info(f"Tentativa {attempt} para {BASE_URL}")
                    await page.goto(BASE_URL, timeout=TIMEOUT, wait_until='domcontentloaded')
                    
                    # Processamento da página...
                    # ... (mantenha o resto do seu código de scraping aqui)
                    
                    return True
                    
                finally:
                    await page.close()
                    await context.close()
                    await browser.close()
                    
        except Exception as e:
            logger.error(f"Erro na tentativa {attempt}: {str(e)}")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY * attempt)
            continue
            
    return False

async def main():
    """Função principal"""
    logger.info("Iniciando scraping...")
    success = await scrape_page()
    if success:
        logger.info("Scraping concluído com sucesso!")
    else:
        logger.error("Falha ao raspar a página após várias tentativas")
    return success

if __name__ == "__main__":
    # Verifica se é apenas para instalação
    if '--install-only' in sys.argv:
        install_playwright()
        sys.exit(0)
        
    # Verifica se os browsers estão instalados
    if not os.path.exists('/opt/render/.cache/ms-playwright'):
        logger.info("Browsers não detectados, instalando...")
        install_playwright()
    
    # Executa o scraping
    result = asyncio.run(main())
    sys.exit(0 if result else 1)
