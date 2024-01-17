import pandas as pd
from tqdm import tqdm

def create_RND(ol_1p):
    # AMDD
    ALL_RND, APP_RND, MAIN_RND, DSRT_RND, DRNK_RND = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    # Large-scale dataset divided in 11 batches
    for i in tqdm(range(1, 11)):
        inference_complete = pd.read_csv('inference_complete_' + str(i) + '.csv',
                                     low_memory=False, lineterminator='\n')
        # Discard detected outliers # 1pct from each tails
        ol_1p_index = inference_complete[inference_complete['establishment_id'].isin(ol_1p['establishment_id'])].index
        inference_complete.drop(ol_1p_index, inplace=True)
        # Divide it by AMDD
        appetizer = inference_complete[inference_complete['AMDD'] == 0]
        main = inference_complete[inference_complete['AMDD'] == 1]
        dessert = inference_complete[inference_complete['AMDD'] == 2]
        drink = inference_complete[inference_complete['AMDD'] == 3]
        # RRR Median of all menu for each restaurant
        RND_b1 = inference_complete[['Predicted_RRR', 'lower_ci', 'upper_ci', 'establishment_id',
                                 'location_latitude', 'location_longitude']]\
            .groupby(['establishment_id']).median(numeric_only=True)
        RND_b1['establishment_id'] = RND_b1.index
        RND_b1 = RND_b1.reset_index(drop=True)
        ALL_RND_b1 = RND_b1.rename(columns={"Predicted_RRR": "ALL_RND_pred"})
        ALL_RND = pd.concat([ALL_RND, ALL_RND_b1])
        # RRR Median of appetizer for each restaurant
        RND_b1 = appetizer[['Predicted_RRR', 'lower_ci', 'upper_ci', 'establishment_id',
                            'location_latitude', 'location_longitude']]\
            .groupby(['establishment_id']).median(numeric_only=True)
        RND_b1['establishment_id'] = RND_b1.index
        RND_b1 = RND_b1.reset_index(drop=True)
        APP_RND_b1 = RND_b1.rename(columns={"Predicted_RRR": "APP_RND_pred"})
        APP_RND = pd.concat([APP_RND, APP_RND_b1])
        # RRR Median of main dish for each restaurant
        RND_b1 = main[['Predicted_RRR', 'lower_ci', 'upper_ci', 'establishment_id',
                       'location_latitude', 'location_longitude']]\
            .groupby(['establishment_id']).median(numeric_only=True)
        RND_b1['establishment_id'] = RND_b1.index
        RND_b1 = RND_b1.reset_index(drop=True)
        MAIN_RND_b1 = RND_b1.rename(columns={"Predicted_RRR": "MAIN_RND_pred"})
        MAIN_RND = pd.concat([MAIN_RND, MAIN_RND_b1])
        # RRR Median of dessert dish for each restaurant
        RND_b1 = dessert[['Predicted_RRR', 'lower_ci', 'upper_ci', 'establishment_id',
                          'location_latitude', 'location_longitude']]\
            .groupby(['establishment_id']).median(numeric_only=True)
        RND_b1['establishment_id'] = RND_b1.index
        RND_b1 = RND_b1.reset_index(drop=True)
        DSRT_RND_b1 = RND_b1.rename(columns={"Predicted_RRR": "DSRT_RND_pred"})
        DSRT_RND = pd.concat([DSRT_RND, DSRT_RND_b1])
        # RRR Median of drink dish for each restaurant
        RND_b1 = drink[['Predicted_RRR', 'lower_ci', 'upper_ci', 'establishment_id',
                        'location_latitude', 'location_longitude']]\
            .groupby(['establishment_id']).median(numeric_only=True)
        RND_b1['establishment_id'] = RND_b1.index
        RND_b1 = RND_b1.reset_index(drop=True)
        DRNK_RND_b1 = RND_b1.rename(columns={"Predicted_RRR": "DRNK_RND_pred"})
        DRNK_RND = pd.concat([DRNK_RND, DRNK_RND_b1])
    # Export
    ALL_RND.to_csv('ALL_RND_pp98pct.csv', index=False)
    APP_RND.to_csv('APP_RND_pp98pct.csv', index=False)
    MAIN_RND.to_csv('MAIN_RND_pp98pct.csv', index=False)
    DSRT_RND.to_csv('DSRT_RND_pp98pct.csv', index=False)
    DRNK_RND.to_csv('DRNK_RND_pp98pct.csv', index=False)

if __name__ == "__main__":
    create_RND(pd.read_csv('ol_1p.csv'))