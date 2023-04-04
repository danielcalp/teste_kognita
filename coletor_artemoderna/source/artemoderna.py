# -*- coding: utf-8 -*-
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup


def create_dict_extracted_data():
    dict_extracted_data = {
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
    return dict_extracted_data

# def 


class ArteModerna():
    """
    Main Class
    """
    # with open("C:\\Users\\Daniel\\Desktop\\teste_kognita\\kognita-da-teste\\Categorias_subcategorias.json", "w", encoding='utf-8') as outfile:
    #     json.dump(dict_identificação_imagens_pacientes, outfile, ensure_ascii=False)

    def start_requests(self):
        print('logic here')
        #####
        all_url_categories = []
        dict_extracted_data = create_dict_extracted_data()
        ###
        url_base = 'http://pstrial-2019-12-16.toscrape.com/browse/'
        s = requests.Session()
        response = s.get(url_base)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        categorias = soup.find('div', {'id': 'subcats'})
        lista_categorias = categorias.find_all('div')
        return lista_categorias
        #####
        # item_to_parse = 'http://pstrial-2019-12-16.toscrape.com/item/14879/Jacques_Tuboeuf'
        # item_parsed = self.parse_items(value_to_parse=item_to_parse)
        # all_parsed_items.append(item_parsed)
        # return all_parsed_items
    

    def parse_items(self, value_to_parse: str):
        print('parse individual arts here')
        print(value_to_parse)
        item_parsed = {'title': 'result'}
        return item_parsed