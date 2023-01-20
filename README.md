![Cover image](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/CDSPP-Cover.png)

# Car Dekho Selling Price Prediction

A car price prediction model is a tool that uses historical data and other factors to predict the potential selling price of a specific car.

## Description

Car price prediction is a process of using machine learning techniques to predict the future selling price of a car based on historical data and various other factors such as model name, year of manufacturing, transmission type, seller type, fuel type, and condition of the car. This can be useful for car buyers, sellers, and dealers to estimate the value of a car or determine a fair price for buying or selling.

![Home page](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/home.png)


## About Dataset

This dataset contains information about used cars.
This data can be used for a lot of purposes such as price prediction to exemplify the use of linear regression in Machine Learning.

**The columns in the given dataset are as follows:**

- name
- year
- selling_price
- km_driven
- fuel
- seller_type
- transmission
- Owner

## Feature Selection

The process of feature selection in machine learning is used to identify and select the most relevant features from a dataset to improve the performance and efficiency of a machine learning model. It is an important step in the model building process as it can help to reduce overfitting, increase model interpretability, and improve the accuracy of predictions.

### Feature Selection methods use in this projects

#### correlation matrix

![heat map](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/heatmap.png)

A correlation matrix can be used to identify highly correlated features, which can then be removed or consolidated. Highly correlated features can cause a problem in machine learning models as they can introduce multicollinearity, which can lead to unstable and unreliable model estimates.

![con variable](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/con-ana.png)


#### Chi-squared test

The chi-squared test is a statistical test that is commonly used in feature selection for determining the relationship between variables in a dataset. The test can be used to evaluate the association between a categorical feature and a categorical target variable. It calculates the chi-squared statistic, which measures the deviation between the expected frequencies of the feature values and the observed frequencies in the target variable

![cat variable](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/cat-ana.png)

#### t-test

The t-test is a statistical test that is commonly used in feature selection for determining the relationship between a continuous feature and a continuous target variable. It compares the means of the feature values for different categories or levels of the target variable.

It's a good practice to use a combination of feature selection techniques and evaluate the performance of the model with each set of selected features. Finally, selecting the best set of features which provides better performance.

## Outlier Treatment

Outlier treatment is the process of identifying and handling extreme values or observations that are significantly different from other observations in a dataset. Outliers can have a significant impact on the results of data analysis and modeling, and can skew the mean and standard deviation of a dataset.

### Methods used to identify outliers

- **Visualization:** Outliers can be identified by creating visualizations such as box plots, scatter plots, and histograms to identify observations that fall outside of the typical range.

- **Interquartile range (IQR):** Outliers can be identified by calculating the interquartile range (IQR), which is the difference between the first and third quartile. Values that fall outside of 1.5 * IQR above the third quartile or 1.5 * IQR below the first quartile are considered outliers.

![Outlier](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/outliers.png)

### Methods used to treat outliers

- **Imputing the missing values:** This method can be used to replace outliers with the mean, median, or mode of the dataset.

![Outlier Treatment](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/outliers-tret.png)

## Features transformation and scaling

Feature transformation is the process of applying mathematical functions to the features in a dataset in order to change their distribution or to extract additional information from the data. Feature transformations are often used to improve the performance of machine learning models by making the features more suitable for the model.

- **Label encoding** is a method of converting categorical variables, represented as text values, into numerical values. It assigns a unique numerical value to each category or level of a categorical feature. This is often used as a preprocessing step before training a machine learning model.

- **One-hot encoding** : This method converts categorical features into numerical features by creating a new binary feature for each category.

- **Target encoding** is a technique used in machine learning to encode categorical variables. It replaces each category with the average value of the target variable for that category. This can improve the performance of a model by allowing it to better handle categorical variables. It is also known as mean encoding or probability encoding.

Feature scaling is the process of normalizing the range of values for each feature in a dataset. This is often done to ensure that all features are on a similar scale and to prevent some features from having a greater impact on the outcome of a machine learning model than others.

- **StandardScaler** is a pre-processing method in machine learning used to standardize a dataset by subtracting the mean and scaling to unit variance. It is commonly used for feature scaling before applying a supervised learning algorithm to a dataset. 

## Model Selection

### Selection of model

- **Linear regression** is a supervised machine learning algorithm that is used to predict a continuous dependent variable (i.e. a real value) based on one or more independent variables. It assumes a linear relationship between the independent variables and the dependent variable, and uses this relationship to fit a line through the data points. 

- **Decision Tree Regressor** is a type of supervised machine learning algorithm that is used for regression tasks. It is a decision tree algorithm where each internal node represents a feature and each leaf node represents a predicted value. The tree is constructed by recursively splitting the feature space into smaller regions, with each split chosen to minimize a certain impurity criterion such as mean squared error. 

- **Random Forest Regressor** is an ensemble machine learning algorithm that is used for regression tasks. It is based on the decision tree algorithm, but instead of building a single decision tree, it builds multiple decision trees and combines their predictions to produce a final result.

- **Polynomial Regression** is a type of supervised machine learning algorithm that is used for regression tasks. It is similar to linear regression, but instead of fitting a straight line through the data points, it fits a polynomial equation of the form

### Evaluation of algorithm

![Outlier Treatment](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/result.png)

**The R-squared (R2)** is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s). It ranges between 0 and 1, where a value of 1 indicates that all variance in the dependent variable is predictable from the independent variable(s) and a value of 0 means that no variance in the dependent variable can be predicted from the independent variable(s). R2 is often used as a measure of how well a model fits the data, with a higher R2 indicating a better fit.

**R-squared values of Algorithms:**

- Linear Regression: 0.7323919717461974
- Decision Tree Regressor: 0.7199627508607279
- Random Forest Regressor: 0.7819483096663358
- Polynomial Regression: 0.7484567579169872

We chose the Random Forest Regressor because the highest R-squared value.

### Hyperparameter Tuning

Hyperparameter tuning is the process of selecting the best set of hyperparameters for a machine learning model. Hyperparameters are parameters that are not learned from the data, but are set before training the model.

**Random search:** This method randomly samples hyperparameter values from a predefined distribution. It is more efficient than grid search because it doesn't evaluate all possible combinations, but it still requires a large number of evaluations to find a good set of hyperparameters.

**Hyperparameters for Random Forest Regressor :**

- n_estimators: 200,
- min_samples_split: 5,
- min_samples_leaf: 10,
- max_features: 'auto',
- max_depth: None,
- bootstrap: True

R-squared value of Random Forest After Hyper Tuning: 0.783252078637896

## Web App for project

**Flask** is a web framework for building web applications using the Python programming language. It is a micro-framework that provides the basic functionality needed to build web applications, such as routing and request handling, without including a lot of additional features or libraries. This makes it lightweight and easy to use, but also allows for flexibility and customization.

![Value insertion](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/val.png)

After inserting values for the attribute such as the name of the car, transmission type, fuel type, seller type, and manufacturing year our flask web app will predict the selling price of the car.

![Predictions](https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction/blob/master/assets/res.png)


## Installation

### Get the Car Dekho Selling Price Prediction Repository now.

To download a Amadeus project, you can use the git clone command. This command creates a copy of the repository in a new directory on your local machine.
```
git clone https://github.com/nileshparab42/Car-Dekho-Selling-Price-Prediction.git
```
To set up the project, you can use the pip command to install the required packages specified in the requirements.txt file.
```
pip install -r requirements.txt
```
This will install all of the required packages for the project. If you are using a virtual environment for the project, you should activate the environment before running this command.
```
pip install virtualenv
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt
```
This will create a new virtual environment called myenv, activate it, and then install the required packages.

You can also specify the notebook file location or the working directory, after the command "jupyter notebook" or "jupyter lab" like:
```
jupyter notebook /path/to/notebook/directory
```
or
```
jupyter lab /path/to/notebook/directory
```
It will open the Jupyter notebook or lab in the specified directory, making it easier to navigate to the notebook you want to open.


### Installation of Car Dekho Selling Price Prediction web app

To install a Flask project, you can use the following commands in your command line interface:

Create a new directory for your project and navigate to it in the command line:
```
mkdir myproject
cd myproject
```
Create and activate a virtual environment using virtualenv:
```
virtualenv venv
source venv/bin/activate
```
or conda:

```
conda create --name myenv
conda activate myenv
```
Install Flask and any other required dependencies by running:
```
pip install flask
```
and
```
pip install -r requirements.txt
```
the project has a requirements file.

Create a new file named `app.py` or `main.py` in the project directory:
Copy code
```
touch app.py
```
In the `app.py` or `main.py` file, import Flask, create an instance of the Flask class, and define the routes and functions that will handle the requests.

Run the application by executing:

```
flask run
```
or

```
python app.py
```
or
```
python main.py
```

This will start the development server and make the application accessible at "http://localhost:5000"

If you want to deploy your application to a production environment, you can use a web server like Gunicorn or uWSGI to serve the application.
It's worth noting that you can also use frameworks like Flask-CLI or Flask-Script to create more advanced command-line scripts for your application.

## Authors

- [Nilesh Parab](https://github.com/nileshparab42) (Project Lead) - [Website](https://nileshparab10.blogspot.com/)
  

## Acknowledgements

- This project was inspired by the work of the [CodeWithHarry](https://www.youtube.com/@CodeWithHarry).
- We also used resources and tools from the [GeeksforGeeks](https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/) to develop and test our project.
