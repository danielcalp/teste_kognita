# -*- coding: utf-8 -*-
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from lxml import html, etree
from io import StringIO
import time
from concurrent.futures import ThreadPoolExecutor


def create_dict_extract_data_image():
    # extrair os dados do url no seguinte formato:
    dict_extract_data = {
        'ID' : '',
        'url': '',
        'artistas': '',
        'titulo': '',
        'preco': '',
        'imagem': '',
        'composicao': '',
        'descricao': '',
        'categorias': ''
    }
    return dict_extract_data

def create_dict_extract_categories():
    dict_extract_categories = {
        'nome_categoria': '',
        'url_categoria': '',
        'imagems': '',
        'subcategorias': [],
    }
    return dict_extract_categories


class ArteModerna():
    """
    Main Class
    """

    def start_requests(self):
        # print('logic here')
        #####
        ###
        url_base = 'http://pstrial-2019-12-16.toscrape.com/browse/'
        lista_categorias = self.html_get_categorias(url_base)
        lista_dicionarios_categorias = self.parse_categories_list(lista_categorias)
        for dicionario_categoria in lista_dicionarios_categorias:
            if dicionario_categoria['subcategorias'] == [None]:
                continue
            lista_subcategoria = dicionario_categoria['subcategorias']
            for subcategoria in lista_subcategoria:
                subcategoria = self.modify_dictionary_content(subcategoria, url_base)
                if subcategoria == False:
                    continue
                lista_subcategorias2 = subcategoria['subcategorias']
                for subcategoria2 in lista_subcategorias2:
                    subcategoria2 = self.modify_dictionary_content(subcategoria2, url_base)
                    if subcategoria2 == False:
                        continue
                    lista_subcategorias3 = subcategoria2['subcategorias']
                    for subcategoria3 in lista_subcategorias3:
                        subcategoria3 = self.modify_dictionary_content(subcategoria3, url_base)
                        if subcategoria3 == False:
                            continue
        for dicionario_categoria in lista_dicionarios_categorias:
            lista_artes = self.get_image_data(dicionario_categoria, url_base)
            break
        return lista_dicionarios_categorias, lista_artes
    

    def html_get_categorias(self, url_base):
        s = requests.Session()
        response = s.get(url_base)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        categorias = soup.find('div', {'id': 'subcats'})
        lista_categorias = categorias.find_all('div')
        lista_categorias_inuteis = ['In Sunsh', 'Summertime', 'Fragrant Ladies']
        for categoria in lista_categorias:
            for categoria_inutil in lista_categorias_inuteis:
                if categoria_inutil in categoria.text:
                    lista_categorias.remove(categoria)
        return lista_categorias

    def parse_categories_list(self, lista_categorias):
        # esse função recebe uma lista de categorias do request
        lista_dicionarios_categorias = []
        for dados_categoria in lista_categorias:
            dict_extract_name_url = create_dict_extract_categories()
            # print(dados_categoria)
            nome_categoria = dados_categoria.find('h3').text
            url_categoria = dados_categoria.find('a').get('href')
            dict_extract_name_url['nome_categoria'] = nome_categoria
            dict_extract_name_url['url_categoria'] = url_categoria
            lista_subcategorias = dados_categoria.find_all('li')
            # print(nome_categoria)
            # print(lista_subcategorias)
            if lista_subcategorias == []:
                dict_extract_name_url['subcategorias'].append(None)
            for subcategoria in lista_subcategorias:
                dict_extract_subcategorias = create_dict_extract_categories()
                nome_categoria = subcategoria.find('a').text
                url_categoria = subcategoria.find('a').get('href')
                dict_extract_subcategorias['nome_categoria'] = nome_categoria
                dict_extract_subcategorias['url_categoria'] = url_categoria
                dict_extract_name_url['subcategorias'].append(dict_extract_subcategorias)
                # print(nome_categoria)
                # print(url_categoria)
            lista_dicionarios_categorias.append(dict_extract_name_url)
            # print(lista_dicionarios_categorias)

        return lista_dicionarios_categorias

    def modify_dictionary_content(self, subcategoria, url_base):
        url_categoria = url_base.replace('/browse/', '') + subcategoria['url_categoria']
        lista_categorias = self.html_get_categorias(url_categoria)
        nova_lista_dicionarios_categorias = self.parse_categories_list(lista_categorias)
        subcategoria['subcategorias'] = nova_lista_dicionarios_categorias
        if nova_lista_dicionarios_categorias == []:
            subcategoria['subcategorias'] = [None]
            return False
        return subcategoria

    def get_image_data(self, dicionario_categoria, url_base):
        paginas = range(0,130)
        with ThreadPoolExecutor(max_workers=30) as executor:
            with requests.Session()as s:
                lista_artes = executor.map(self.request_get_page, [dicionario_categoria] * len(paginas), [s] * len(paginas), paginas)
        return lista_artes
    def request_get_page(self, dicionario_categoria, s, pagina):
        lista_artes = []
        url_base = url_base.replace('/browse/', '')
        url = url_base + dicionario_categoria['url_categoria'] + "?page=" + pagina
        response = s.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        conteudo = soup.find('div', {'id': 'body'})
        parser = html.fromstring(str(conteudo))
        lista_artes = parser.xpath('//*[@id="body"]/div[2]/a[position() > 1]')
        for arte in lista_artes:
            conteudo_artes = html.tostring(arte)
            string_text = conteudo_artes.decode('utf-8')
            url_arte = string_text.split('<a href="')[1].split('">')[0]
            response = s.get(url_base + url_arte)
            time.sleep(5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # html_content = response.content
            # lxml_tree = html.fromstring(html_content)
            id_imagem = str(soup.find('img')).split('/')[-2].split('.')[0]
            link_imagem = url_base + f"/content/{id_imagem}.jpg"
            artistas = soup.find('h2').text
            lista_artistas = []
            if 'Artist: ' in artistas:
                artistas = artistas.replace('Artist: ', '')
            if 'Engraver: ' in artistas:
                artistas = artistas.replace('Engraver: ', '')
            if 'Designer: ' in artistas:
                artistas = artistas.replace('Designer: ', '')
            if 'Publisher: ' in artistas:
                artistas = artistas.replace('Publisher: ', '')
            if 'Photographer: ' in artistas:
                artistas = artistas.replace('Photographer: ', '')
            if ';' in artistas:
                artistas = artistas.replace(';', ',')
            if ',' in artistas:
                artistas = artistas.split(',')
                for artista in artistas:
                    lista_artistas.append(artista)
            else:
                lista_artistas.append(artistas)
                
            titulo_imagem = soup.find('h1').text
            preco_imagem = soup.find('td', {'id': 'price'}).text
            url_arte = url_base + url_arte
            lista_composicoes = []
            composicao = soup.find('ul')
            composicoes = composicao.find_all('li')
            # print(composicoes)
            for composicao in composicoes:
                composicao_material = composicao.text.split(':')[0]
                composicao_porcentagem = composicao.text.split(':')[1]
                dict_composicoes = {}
                dict_composicoes[composicao_material] = composicao_porcentagem
                lista_composicoes.append(dict_composicoes)
            descricao_arte = soup.find('div', {'class': 'description'}).text
            categorias_arte = dicionario_categoria['url_categoria'].split('/')[1:]
            dict_extract_data = create_dict_extract_data_image()
            dict_extract_data['ID'] = id_imagem
            dict_extract_data['url'] = url_arte
            dict_extract_data['artistas'] = lista_artistas
            dict_extract_data['titulo'] = titulo_imagem
            dict_extract_data['preco'] = preco_imagem
            dict_extract_data['imagem'] = link_imagem
            dict_extract_data['composicao'] = lista_composicoes
            dict_extract_data['descricao'] = descricao_arte
            dict_extract_data['categorias'] = categorias_arte
            lista_artes.append(dict_extract_data)
        return lista_artes

