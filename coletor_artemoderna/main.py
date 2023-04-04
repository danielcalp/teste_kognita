import pandas as pd

from source.artemoderna import ArteModerna

if __name__ == '__main__':
    all_items_to_save = ArteModerna().start_requests()
    print(all_items_to_save)
    # df = pd.DataFrame(all_items_to_save)
    # df.to_csv('results.csv')

