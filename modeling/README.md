# Modeling

## Pipeline

Here we explain how to run the original MINT and MINT+ pipeline, to make the food category and nutrition density score prediction using available information about the menu item.

- `RRR_pred_FT_edn.py`: 
> This Python script runs a original MINT to predict the nutrient density for the data that does not have menu descriptions, it utilizes embeddings created from RecipeFT. It assigns food category pseudo-labels and predicted nutrient density for each item.
- `RRR_pred_MPNET_ednd.py`: 
> This Python script runs a MINT+ to predict the nutrient density for the data that does have menu descriptions, it utilizes embeddings created from pre-trained MPNET. It assigns food category pseudo-labels and predicted nutrient density for each item.

