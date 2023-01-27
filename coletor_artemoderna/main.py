import pandas as pd

from coletor_artemoderna.source.artemoderna import ArteModerna

if __name__ == '__main__':
    all_items_to_save = ArteModerna().start_requests()
    df = pd.DataFrame(all_items_to_save)
    df.to_csv('results.csv')

