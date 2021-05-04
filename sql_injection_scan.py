import requests
import re
import os

print('Teste de SQL INJECTION\n')

inicio = input('Digite a URL do site: ')

url = inicio

os.system('cls')

print('Injetando em {}'.format(url))

padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)

injecao = padrao.groups()[0] + '\''

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/72.0.3626.119 Safari/537.36'}

req = requests.get(injecao, headers=header)

html = req.text

if 'mysql_fetch_array()' in html:
    print('------Vulneravel------')
else:
    print('------Nao Vulneravel------')