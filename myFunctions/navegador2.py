def navegador_firefox(headless, geckodriver_version='v0.35.0') -> any:
    '''Função para abrir o navegador com todas config
    já configuradas
    
    params: 
        headless (bool): se o navegador deve ser aberto em modo headless
        geckodriver_version (str): versão do geckodriver a ser usada
    
    returns:
        object: driver do navegador Firefox
    '''

    import subprocess
    from selenium import webdriver
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.service import Service as GeckoService
    from .arrumaScrapper import tempo_espera_aleatorio
    import numpy
    from .arrumaScrapper import dir_download
    
    print('\n###############################\n')
    print('         Bem vindo(a)!           ')
    print('\n###############################\n')
    print('Abrindo navegador..\n')

    firefox_binary_path = '/usr/bin/firefox'
    
    # checa versão do seu firefox
    firefox_version_output = subprocess.check_output('firefox --version', shell=True, stderr=subprocess.STDOUT).decode().strip()
    firefox_version = firefox_version_output.split(' ')[-1]  # pega a versão do firefox
    print(f'Você está usando o Firefox versão: {firefox_version}\n')
    
    # configurando navegador
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_binary_path
    
    # configura preferências para downloads
    download_directory = "./download/"
    firefox_options.set_preference("browser.download.folderList", 2)  # usa o diretório de download customizado
    firefox_options.set_preference("browser.download.dir", download_directory)
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    if headless:
        firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-dev-shm-usage')
    firefox_options.add_argument("disable-infobars")

    # cria o serviço para o GECKODRIVER usando uma versão específica
    service = GeckoService(executable_path=GeckoDriverManager(version=geckodriver_version).install(), 
                           log_path='./downloads/geckodriver.log')

    # cria o driver do Firefox
    navegador = webdriver.Firefox(
        service=service,
        options=firefox_options
    )

    print('Navegador aberto.\n')
    tempo_espera_aleatorio(low=1, high=2)

    return navegador
