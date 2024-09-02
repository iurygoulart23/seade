# Atualizador de Dados do Repositório SEADE

Este script Python verifica automaticamente se há atualizações no repositório de dados do SEADE e baixa o arquivo de dados mais recente, caso disponível. O script é configurado para monitorar uma página específica e comparar a data de atualização mais recente com a data armazenada localmente. Se uma nova atualização for detectada, o script baixa o novo arquivo e atualiza os metadados locais.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `BeautifulSoup` (parte do pacote `bs4`)
  - `urllib3`
  - `json`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install requests beautifulsoup4
```

## Estrutura do Projeto

```
/seade-updater
│
├── main.py                   # Script principal que executa a verificação e o download
├── /data
│   └── metadados.json        # Arquivo de metadados para armazenar a última data de atualização
└── /downloads
    └── sepiesp_captados.csv  # Arquivo de dados baixado
```

## Uso

1. **Crie as pastas necessárias**: Certifique-se de que os diretórios `data` e `downloads` existam na mesma pasta que o script `main.py`.

2. **Configure o arquivo de metadados**: Crie o arquivo `metadados.json` dentro da pasta `data` com o seguinte conteúdo:

```json
{
  "ultima_att": "20 de agosto de 2024"
}
```

Substitua `20 de agosto de 2024` pela última data de atualização conhecida.

3. **Execute o script**:

Execute o script `main.py` com Python:

```bash
python main.py
```

## Como Funciona

- O script acessa o link do repositório SEADE usando uma sessão HTTP.
- O conteúdo da página é analisado com o BeautifulSoup para localizar a data de atualização dos dados.
- A data de atualização encontrada é comparada com a data armazenada localmente (`metadados.json`).
- Se uma nova atualização for encontrada:
  - A nova data é salva no arquivo `metadados.json`.
  - O novo arquivo de dados é baixado e salvo na pasta `downloads`.

## Tratamento de Erros

- Se o site mudar ou o conteúdo desejado não for encontrado, uma mensagem de erro será exibida.
- Verificações são realizadas para garantir que os elementos necessários estejam presentes antes de tentar acessar seus atributos.

## Avisos

- Este script ignora os avisos de certificados SSL inseguros para simplificar o processo de requisição HTTP. Use com cautela em ambientes seguros.
- Certifique-se de que o site não bloqueie solicitações automatizadas ou tenha termos de uso que proíbam tal prática.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
