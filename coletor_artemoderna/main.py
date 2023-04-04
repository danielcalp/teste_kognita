import pandas as pd
import json

from source.artemoderna import ArteModerna

if __name__ == '__main__':
    all_items_to_save = ArteModerna().start_requests()
    print(all_items_to_save)
    # df = pd.DataFrame(all_items_to_save)
    # df.to_json('results.json')
    with open("results.json", "w", encoding='utf-8') as outfile:
        json.dump(all_items_to_save, outfile, ensure_ascii=False)

