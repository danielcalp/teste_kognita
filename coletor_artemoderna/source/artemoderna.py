# -*- coding: utf-8 -*-
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup


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
    # with open("C:\\Users\\Daniel\\Desktop\\teste_kognita\\kognita-da-teste\\Categorias_subcategorias.json", "w", encoding='utf-8') as outfile:
    #     json.dump(dict_identificação_imagens_pacientes, outfile, ensure_ascii=False)

    def start_requests(self):
        # print('logic here')
        #####
        all_url_categories = []
        dict_extracted_data = create_dict_extract_data_image()
        ###
        url_base = 'http://pstrial-2019-12-16.toscrape.com/browse/'
        s = requests.Session()
        response = s.get(url_base)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        categorias = soup.find('div', {'id': 'subcats'})
        lista_categorias = categorias.find_all('div')
        dados_categoria = self.parse_categorie_list(lista_categorias)
        return dados_categoria
        #####
        # item_to_parse = 'http://pstrial-2019-12-16.toscrape.com/item/14879/Jacques_Tuboeuf'
        # item_parsed = self.parse_items(value_to_parse=item_to_parse)
        # all_parsed_items.append(item_parsed)
        # return all_parsed_items
    
    def parse_categorie_list(self, lista_categorias):
        lista_dicionarios = []
        for dados_categoria in lista_categorias:
            dict_extract_name_url = create_dict_extract_categories()
            # print(dados_categoria)
            nome_categoria = dados_categoria.find('h3').text
            url_categoria = dados_categoria.find('a').get('href')
            dict_extract_name_url['nome_categoria'] = nome_categoria
            dict_extract_name_url['url_categoria'] = url_categoria
            lista_subcategorias = dados_categoria.find_all('li')
            for subcategoria in lista_subcategorias:
                dict_extract_subcategorias = create_dict_extract_categories()
                nome_categoria = subcategoria.find('a').text
                url_categoria = subcategoria.find('a').get('href')
                dict_extract_subcategorias['nome_categoria'] = nome_categoria
                dict_extract_subcategorias['url_categoria'] = url_categoria
                dict_extract_name_url['subcategorias'].append(dict_extract_subcategorias)
                # print(nome_categoria)
                # print(url_categoria)
            lista_dicionarios.append(dict_extract_name_url)
            # print(lista_subcategorias)
        return lista_dicionarios

    def parse_items(self, value_to_parse: str):
        print('parse individual arts here')
        print(value_to_parse)
        item_parsed = {'title': 'result'}
        return item_parsed