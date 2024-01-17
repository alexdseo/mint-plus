# Analysis

## Evaluating the USA food environmnet with Food Environment Nutrient Density (FEND) predicted using MINT+

From [`data`] and [`modeling`] process, we obtained a inference dataset with AMDD labels and predicted nutrient density (RRR). Now we use this dataset to evaluate the food environment in the United States. Before the main analysis of calculating Food Environemnt Nutrient Density (FEND), we have to post-processing on the dataset. Since the inference dataset is from real-world we do not expect to be very clean. For example, there are few incomplete set of restaurant data with very few number of menu items, non-restaurants such as supermarket or liquor store, restaurant data with repeated menu items. We aim to clean this dataset before using the dataset for analysis.

- `outlier_detection.py`: 
> This Python script runs a post processing process on the inference dataset. We simply discard the the 1% of the dataset from each tail from the distribution of number of menus for each each restaurants. This way, we could easily disregrad the incomplet menu, repeated menu, and supermarkets which have very large set of items. By running this file, it also produces Restaurant Nutrient Density (RND) dataset for each AMDD labels that will be used for the analysis to calculate FEND.

- `create_RND.py`: 
> This Python script produces a Restaurant Nutrient Density (RND) dataset for each AMDD label by taking a median of restaurant menu item's predicted RRR that will be used for the analysis to calculate FEND.

- `county_state_viz.ipynb`: 
> This notebook script we calculate FEND for the USA counties. To analyze it on different level of food environemnt, you can simply switch the geo dataset to your geo-level of interest. You could perform analyis from cenesus-tract-level, city-level, county-levle, and to state-level. The analysis includes calculating the FEND by taking a median of RNDs calculated from `post_processing.py` within each food environemnt, comparing them with health outcome dataset that we retrieved from [here](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2020-releas/mssc-ksj7/about_data), mapping them using the [cartographic boundary dataset](https://www2.census.gov/geo/tiger/GENZ2015/shp/cb_2015_us_county_500k.zip) that matches with the health outcome and inference data.

