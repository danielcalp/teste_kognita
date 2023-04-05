import pandas as pd
import json

from source.artemoderna import ArteModerna

if __name__ == '__main__':
    lista_dicionarios_categorias, lista_artes = ArteModerna().start_requests()
    with open("results.json", "w", encoding='utf-8') as outfile:
        json.dump(lista_dicionarios_categorias, outfile, ensure_ascii=False)
    with open("imagelist.json", "w", encoding='utf-8') as outfile:
        json.dump(lista_artes, outfile, ensure_ascii=False)
    df = pd.read_json("imagelist.json", 'r', encoding='utf-8')
    excel = df.to_excel('imagelist.xlsx', 'r', encoding='utf-8')
