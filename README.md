# Evaluating the Nutritional Quality of a Food Environments

In this project, we evaluate the food envrionment in different level over all USA, from census tract-level to state-level, by predicting the nutritional quality of food envrionment using MINT: Menu Item to NutrienT, proposed by Seo et al.(2023). MINT is a pipeline designed to capture the nutritional quality of a restaurant through menu item names. MINT utilizes language model trained with domain-specific dataset, namely Recipe1M+, to produce embeddings for the each menu item based only on their names. We specifically use MINT to predict nutrient density score of menu item, RRR (Ratio of Recommended to Restricted nutrients), and use them to predict the overall nutrient density of each restaurant's menu offering. We define the restaurant-level nutrient density as RND (Restaurant Nutrient Density), which is a median of predicted RRR for each restaurant's menu. We expand this metric to food environment level, FEND (Food Environment Nutrient Density) which is a median of approximated RND within selected food environemnt.

## Description

We use a large-scale menu item dataset with ~75M menu items from across ~600K restaurants provided by Edamam Inc. We use orginal MINT from the Seo et al.(2023), as well as the extended version we propose in this project **MINT+**.
Details of the original model MINT is described below:


![MINT pipeline](https://github.com/alexdseo/mint/blob/main/figures/model_diagram.png)

(a) Word embedding model. We begin by extracting food names, ingredients, and recipes from the Recipe1M+ dataset, and use the concatenation of this text to train a FastText word embedding model. The food item embedding is the average embedding of each word in the food item. 

(b) Food category prediction model. We embed Edamam training data containing food items concatenated with item ingredients using a pre-trained MPNet model. We then cluster the training data using HDBSCAN, which we treat as a ground truth food category. We then use the FastText model to embed food items alone and train a model to predict the most likely cluster associated with each food name. 

(c) Nutrition Score Model. The Edamam dataset is used to train a nutrition score model in which food names embedded with FastText, are fed into models to predict the *Nutrient density scores*. The model first trained on the entire dataset is then fine-tuned on the ground-truth categories to create MINT.


MINT+ is a extended version of MINT where we utilize the menu description available from our large-scale dataset. We found this extension necessary as the 63% of the menu item dataset contains this useful menu description. However, since our training dataset that consists generic food item does not consists description of the food item, we generate the food item description using GPT3.5. After generating the description, we train two seperate model: original MINT, where we use only the food name to create embeddings and predict the nutrient density (RRR) of the food item. We use RecipeFT (FastText trained with Recipe1M+ dataset) to create embeddings for this model. MINT+, where we use food name and the generated description to create embeddings and predict the nutrient density (RRR) of the food item. We use pre-trained MPNET to create embeddings for this model. After training these models, we perform seperate inference where we use original MINT for the menu items without the description information, and MINT+ for the menu items with the description information.

Additon to the extension of MINT, we perform our analysis seperately depending on the menu item type: Appetizer, Main dish, Dessert, and Drink (AMDD). We create the AMDD labels on our training dataset by asking GPT3.5 "Is this food item appetizer, main dish, dessert, or a drink? Provide an answer with only one of these 4 answers". We then train the classifier using the training dataset's genertated pseudo-labels to perform inference on the large-scale menu item dataset to assign them a AMDD pseudolabels for each menu items.

## Installation

Our code was tested on `Python 3.9`, to install other requirements:
```setup
pip install -r requirements.txt
```

## Usage

MINT is trained with a high-quality dataset that contains generic food items - canonical foods, including everything from individual raw foods to complex meals – which includes their ingredients and nutrient composition information. We use this trained model to perform inference on large-scale menu item datasets. For more details about the datasets, please see [`data`].

MINT consists of 2 prediction models: the food category prediction model and the nutrition quality prediction model. MINT+ uses same architecture as MINT, but uses embeddings created using food name along with the GPT-generated description. For more details, please see [`modeling`]. 

