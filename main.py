import requests
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

link = "https://repositorio.seade.gov.br/dataset/seade-investimentos/resource/3ee8eb9b-a3b5-4d53-925f-71e5dabb263c"

s = requests.Session()
s.verify = False
answer = s.get(link)

if answer.status_code == 200:
    page_data = answer.content
    html = page_data.decode()

    soup = BeautifulSoup(html, 'html.parser')
    atualizacoes = soup.find_all('tr')
    atualizacoes = [i.text for i in atualizacoes]
    ultima_att_site = atualizacoes[1].split('\n')[2]
    
    print(f'Atualizações:\n{atualizacoes}\n')
    print(f'Ultima att no site: {ultima_att_site}\n')

    # verifica se não alteraram algum item no site
    if atualizacoes[1].split('\n')[1] == "Dados atualizados pela última vez":
        ultima_att = atualizacoes[1].split('\n')[2]

        # abre o arquivo de metadados que estou salvando
        with open('./data/metadados.json', 'r') as f:
            metadados = json.load(f).get('ultima_att')

        # Se a data de att do site forem iguais a ultima que temos, ignora
        if ultima_att.strip() != metadados.strip():
            print('Temos atualizações novas')

            # salva a nova data de atualização
            with open('./data/metadados.json', 'w') as f:
                json.dump({'ultima_att': ultima_att}, f)

            try:
                print('Baixando novo arquivo...\n')
                
                # Encontra o div com a classe especificada
                div_element = soup.find("div", class_="module-content")
                link_element = div_element.find('a')
                url_download = link_element['href']
                
                print(f'\nBaixando arquivo:\n{url_download}')

                # salva o novo arquivo
                with open('./downloads/sepiesp_captados.csv', 'wb') as f:
                    f.write(s.get(url_download).content)
                    print('\nArquivo salvo com sucesso!\nNa pasta: ./downloads/sepiesp_captados.csv\n')

            except Exception as e: 
                raise (e)

        else:
            print('Site continua sem atualizações')

    else:
        raise ValueError('Mudou alguma coisa no site.')

else:
    print(answer.status_code)
    print(answer.text)