# Online News Popularity
Python project ESILV 12/22

Clémence Delouche, Léa Feldman et Guillaume Doria

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [To Do](#setup)
* [Conclusion](#conclusion)


## General info
This dataset summarizes a heterogeneous set of features about articles published by Mashable in a period of two years. The goal is to predict the number of shares in social networks (popularity).

### Data Set Informations 

Number of Attributes: 61 (58 predictive attributes, 2 non-predictive, 1 goal field)

* The articles were published by Mashable (www.mashable.com) and their content as the rights to reproduce it belongs to them. Hence, this dataset does not share the original content but some statistics associated with it. The original content be publicly accessed and retrieved using the provided urls.
* Acquisition date: January 8, 2015
* The estimated relative performance values were estimated by the authors using a Random Forest classifier and a rolling windows as assessment method. See their article for more details on how the relative performance values were set.
	
## Technologies
Our project is created with:
* Jupyter
* Django or Flask


## To Do 
* A PowerPoint explaining the ins and outs of the problem, your thoughts on the asked
question, the different variables you created, how the problem fits in the context of the
study, etc
* Data pre-processing: encoding, normalization, imputation…
* Data visualization (use matplotlib, seaborn, bokeh ...): show the link between
the variables and the target
* Modeling: use the scikit-learn library to try several algorithms, change the
hyper parameters, do a grid search, compare the results of your models using
graphics
* Transformation of the model into an API (Django or Flask)

## Conclusion 
As a conclusion, we can say that even if RandomForest is a better model than Linear Regression and Decision Tree, it does not really show good results despite the patern on the scatter plot. 


The predictions are quite close to the real values but there are still some big errors for certain. 
Next step for improvement could be a advanced GridSearch for more hyperparameters or test others machinelearning models.
Another way of improvement could be to remove more outliers. 


