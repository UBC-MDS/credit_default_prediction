# Credit Default Prediction

- **Authors** : Arushi Ahuja, Karanpreet Kaur, Lianna Hovhannisyan, Taiwo Owoseni

## Introduction

This project aims to answer the question: "Will a customer default credit payment next month?" by building a classification model to predict potential credit default accounts of Taiwan's credit card clients.

A customer can default a credit payment for many reasons: it can be out of negligence, loss of job, health issues, need to use the extra cash for other bills or deliberately choosing to refuse to pay the credit even though they are financially capable. Credit companies are faced with the burden of "trusting" a customer would not default payment. Extensive data profiling the customer's finance is collected to decide if a customer would default or make payment the next month.

The data set is a Taiwan credit card data from April to September, 2005 sourced from the UCI machine learning repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/default|of|credit|card|clients).

The data set consists of 24 columns partitioned into :

- Twenty three (23) explanatory columns

- One response column

#### Column Description

The columns are further defined below:

- LIMIT_BAL: Amount of the given credit (NT dollar): it includes both the individual costumer credit and his/her family (supplementary)

- SEX: The customer's gender: 1 depicts male and 2 depicts female.

- EDUCATION: The customer's education Level: 1 depicts graduate school, 2 depicts university, 3 depicts high school and 4 depicts others.

- MARRIAGE: The customer's Marital Status: 1 depicts married, 2 depicts single and 3 depicts others.

- AGE: The customer's age in years.

- PAY_0 - PAY_6 : The repayment status. It is the customer's history of past payment from April to September, 2005. The measurement scale for the repayment status are:

    - -2 represents balance paid in full and no transactions in this period (we may refer to this credit card account as having been 'inactive' this period).

    - -1 represents pay duly, but customer's account has a positive balance at end of period due to recent transactions for which payment has not yet come due.

    - 0 represents customer paid the minimum due amount, but not the entire balance. This means that the customer paid enough for their account to remain in good standing, but did revolve a balance.

    - 1 represents payment delay for one month .

    - 2 represents payment delay for two months.

    - 3 represents payment delay for three months.

    - 4 represents payment delay for four months.

    - 5 represents payment delay for five months.

    - 6 represents payment delay for six months.

    - 7 represents payment delay for seven months.

    - 8 represents payment delay for eight months

    - 9 represents payment delay for nine months and above. <br>

- BILL_AMT1 - BILL_AMT6: The amount of bill statement in dollars from April to September , 2005.

- PAY_AMT1 - PAY_AMT6: The amount of previous payment in dollars from April to September , 2005.

- default.payment.next.month: The default payment in next month. 0 represents yes and 1 represents no.

We intend to use various machine learning classification algorithm such as KNN, Logisitic Regression and SVC (to mention a few) to select the best performing algorithm that predicts if a customer would default payment or not. Our data set would be splitted in the percentage ratio 80:20 . Where 80 percent will represent our train data and 20 percent will represent our test data. Due to the generalized nature of our case study we are prepared to encounter imbalanced class counts. We believe a large number of customer's would not default the payment next month and we will adequately put this into consideration when building our predictive model. The class counts will be presented as a table and used to inform whether we think there is a class imbalance problem. We will perform further exploratory data analysis to find missing values in our data set, understand the relationships that may exist among the features to see what we can learn about the data set.

We will carryout column transformations on features where neccessary, given that we have categorical features such as Marriage and Sex. When using KNN, we intend to perform normalization of dataset because KNN works on distance metrics. Since our data is large we will use a small number of folds 5 - 10 for every model. Apart from judging from the model's accuracy, we would select our best model by comparing the outcomes of our predictors using alternative scoring/evaluation metrics such as f1-score or recall. The predictor distributions across classes will be plotted as facetted (by predictor) ridge plots where the densities are coloured by class.

Finally, we will re-fit the training data set on our final model then evaluate the performance on the test data set on accuracy and alternative scoring/evaluation metrics such as f1-score or recall. 

## Report

The EDA report for the data set can be found [here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/src/credit_default_eda.ipynb).
## Usage
To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands at the command line/terminal from the root directory of this project:

```
python src/download_data.py --out_type=xls --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls --out_file=data/raw/default_credit_card_clients.csv

jupyter lab src/credit_default_eda.ipynb
```

## Dependencies
- Python 3.9 and Python packages:
  - matplotlib>=3.2.2
  - scikit-learn>=1.0
  - pandas>=1.3.*
  - requests>=2.24.0
  - docopt==0.6.2
  - openpyxl==3.0.9
  - xlrd==2.0.1
  - altair_saver==0.5.0
  - altair==4.1.0
  - altair-data-server==0.4.1
  - portpicker==1.5.0
  - jupyterlab==3.2.4


## License
This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

## References
   Lichman, M. (2013). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.
   
   The original dataset can be found [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00350/) at the UCI Machine Learning Repository.
