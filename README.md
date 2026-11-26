# Python Data Skills Archive

An archive of data science and simple machine learning programs in Python, making use of the *pandas* and *SciKit-Learn* libraries. These currently include:
* **Amazon Stats:** A Jupyter Notebook project using *pandas* to manipulate an Amazon Sales dataset imported from a csv file (see Resources). This includes cleaning the imported data, applying functions to existing columns to produce new ones, and grouping and aggregating data to see any trends.
* **LinearRegression:** A project with *matplotlib* plot output that makes use of some example linear regression data in a csv file (see Resources) which is plotted. Two linear regression models for the data are then created, one using an imported *SciKit-Learn* model and another using a from-scratch function imported from another file *ManualLinearRegression.py*.
* **YelpMultipleRegression:** A Jupyter Notebook project using an imported *SciKit-Learn* model to model Multiple Linear Regression on a Yelp ratings dataset (unfortunately the dataset cannot be distributed with the project). The *pandas* library was also used to get the DataFrames into a suitable state and then multiple models run using *SciKit-Learn*'s linear regression to test different combinations of independant variables, before using the best model to make a test prediction.

## Skills

This project serves as a practice on Python, data handling and simple machine learning. Skills developed and practiced include:

* General Python syntax, use of libraries, and execution using Jupyter and the command line.
* Data handling and manipulation with *pandas* 
* (Multiple) Linear regression modelling, both using *SciKit-Learn* and from scratch by applying the theory behind it.
* Basic data visualization with *matplotlib*.

## Version History

* 0.2
    * Added **YelpMultipleRegression:** project
* 0.1
    * Initial Version containing **Amazon Stats** & **LinearRegression**

## Resources
Resources used:

* Linear Regression dataset from Kaggle (https://www.kaggle.com/datasets/andonians/random-linear-regression/data)
* Amazon Sales Dataset from Kaggle (https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)