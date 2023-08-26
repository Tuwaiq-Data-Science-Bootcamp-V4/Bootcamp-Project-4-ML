# Used car prices in Saudi Arabia :car: :oncoming_automobile:
## Team members:
- Arwa Alnamlan. 
- Alaa Alsalman.  
- Saeed Qahhas.
  
  All team members partcibate in data preprocessing, data cleaning, EDA, creat charts, standardize and split the data, and finally apply the ML model

# Introduction

The objective of this project is to perform an exploratory data analysis and machine learning on a dataset about Used car prices in Saudi Arabia to predict the Used car prices using Python Libraries such as NumPy, Pandas, Matplotlib, Seaborn, Plotly, and Scikit-learn. and find the appropriate regression model.


# Dataset Overview and Source

The dataset used for this project consists of information about used cars, The data attributes include Brand, Model, Year, Color, Options, Fuel_Type, Gear_Type, Engine_Size, Mileage, Region, Price, and Age. The dataset contains 7290 rows and 12 columns of used cars collected from syarah.com. 

The dataset was preprocessed and split into training and testing sets for model development and evaluation.

# Model Evaluation Results

The table below summarizes the final results of the machine learning models evaluated in this project:
We can see from the table that the best-performing model on all the data was the Random Forest Regression with  R Squared equal to 0.85, It is the best-performing model based on the results of the three metrics. Below we provide visualizations of the accuracies of the models, the visualizations provided for more clarity of the results. The results of the three models used in the below graphs are shown as ‘actual vs. predicted’ graphs that indicate the accuracies of the predictions made on the test data. To help interpret the meaning of these graphs, you can use the following statement: The more the data points are near the line, the more the accuracy score is.


| Regression model  | MAE | MSE | RMSE | R2 score |
| ----------- | ----------- | ----------- | ----------- | ----------- |
|Linear Regression Model| 0.38 | 0.24 | 0.49 | 0.59 |
|Decision Tree Regression Model | 0.24|0.14|0.38|  0.75|
|Random Forest Regression Model | 0.19|0.08|0.29|  0.85 |



## conclusion and recommendations 
In the future, we plan to work more on the models we built, As that, the model's accuracy was not satisfying and needs more work and tuning to its parameters and layers. Also, we plan to find other reliable websites in Saudi Arabia and web scrap more data from them and apply more advanced web scrapping and preprocessing techniques so that the results can be more and more accurate. In the end, working on this project has benefited us in a lot of areas and we will work on it in the future and try to improve it more


### Resource 
- https://dibyendudeb.com/comparing-machine-learning-regression-models-using-python/

