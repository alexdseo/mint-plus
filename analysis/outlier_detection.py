import pandas as pd
from tqdm import tqdm

def outlier_detection():
    # Save number of menu per restaurant
    num_menu = pd.DataFrame()
    # Large-scale dataset divided in 11 batches
    for i in tqdm(range(1, 11)):
        inference_complete = pd.read_csv('inference_complete_' + str(i) + '.csv',
                                         low_memory=False, lineterminator='\n')
        num_menu_tmp = pd.DataFrame(inference_complete.groupby(['establishment_id']).count()['id'])
        # print(len(x))
        num_menu_tmp['establishment_id'] = num_menu_tmp.index
        num_menu_tmp = num_menu_tmp.reset_index(drop=True)
        num_menu = pd.concat([num_menu, num_menu_tmp])
    num_menu = num_menu.reset_index(drop=True)
    num_menu = num_menu[['establishment_id', 'id']]
    num_menu = num_menu.rename(columns={'id': 'count'})
    # <=5 and >=693 # 1% from each tails
    ol_1p = num_menu[(num_menu['count'] <= 5) | (num_menu['count'] >= 693)]['establishment_id']
    # Export
    ol_1p.to_csv('ol_1p.csv',index=False)

if __name__ == "__main__":
    outlier_detection()