#scraping de imagens

import requests
from bs4 import BeautifulSoup as bs
import os

#site com as imagens
url = 'https://stocksnap.io/search/mountains'

#Baixando a pagina de parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#localizar todos os elementos com tag de imagem
image_tags = soup.findAll('img')

#criando diretório para as imagens
if not os.path.exists('montanhas'):
    os.makedirs('montanhas')

#movendo para um novo diretório
os.chdir('montanhas')

#variavel de nome do arquivo de imagem
x = 0

#salvando imagens
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('montanhas-' + str(x) + '.jpg', 'wb')as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
