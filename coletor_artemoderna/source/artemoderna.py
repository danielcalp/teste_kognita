# -*- coding: utf-8 -*-
import pandas as pd


class ArteModerna:
    """
    Main Class
    """
    parameters_to_crawl = ['http://pstrial-2019-12-16.toscrape.com/browse/qingjapanese',
                           'http://pstrial-2019-12-16.toscrape.com/browse/unetete']

    def start_requests(self):
        print('logic here')
        all_parsed_items = []
        ###
        ###
        item_to_parse = 'http://pstrial-2019-12-16.toscrape.com/item/14879/Jacques_Tuboeuf'
        item_parsed = self.parse_items(value_to_parse=item_to_parse)
        all_parsed_items.append(item_parsed)
        return all_parsed_items

    def parse_items(self, value_to_parse: str):
        print('parse individual arts here')
        print(value_to_parse)
        item_parsed = {'title': 'result'}
        return item_parsed