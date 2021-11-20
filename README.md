# Credit Default Prediction

## About


This project aims to build a classification model using \<unknown models> algorithm to predict potential credit default accounts of Taiwan's credit card clients'.

\<Tiffany Describes the outcome>

The data set is a Taiwan credit card data from April to September, 2005 sourced from the UCI machine learning repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/default|of|credit|card|clients). Although its original creators are unknown, previous studies strongly suggest it is a private data.

The data set consists of 25 columns partitioned into :

- One ID column

- Twenty three (23) explanatory columns

- One response column

#### Column Description


| Column Name        | Description                                   |
|--------------------|-----------------------------------------------|
| ID                 | Row observation number                        |
| LIMIT_BAL                 | Amount of the given credit in Dollars         | 
| SEX                 | Gender                                        |
| EDUCATION                 | Education Level                               |
| MARRIAGE                 | Martial Status                                |
| Age                 | Age                                           |
| PAY_0                 | Repayment status in September                 |
| PAY_2                 | Repayment status in August                    |
| PAY_3                 | Repayment status in July                      |
| PAY_4                 | Repayment status in June                      |
| PAY_5                | Repayment status in May                       |
| PAY_6                | Repayment status in April                     |
| BILL_AMT1                | Amount of bill statement in September         |
| BILL_AMT2                | Amount of bill statement in August            |
| BILL_AMT3               | Amount of bill statement in July              |
| BILL_AMT4                | Amount of bill statement in June              |
| BILL_AMT5                | Amount of bill statement in May               |
| BILL_AMT6                | Amount of bill statement in April             |
| PAY_AMT1                | Amount of previous payment in September       |
| PAY_AMT2               | Amount of previous payment in August          |
| PAY_AMT3           | Amount of previous payment in July            |
| PAY_AMT4                | Amount of previous payment in June            |
| PAY_AMT5                | Amount of previous payment in May             |
| PAY_AMT6                | Amount of previous payment in April           |
| default.payment.next.month                  | Defaults Payment         |

The columns are further defined below:

- ID: Row Identifier.

- LIMIT_BAL: Amount of the given credit (NT dollar): it includes both the individual costumer credit and his/her family (supplementary)

- SEX: The customer's gender: 1 depicts male and 2 depicts female.

- EDUCATION: The customer's education Level: 1 depicts graduate school, 2 depicts university, 3 depicts high school and 4 depicts others.

- MARRIAGE: The customer's Marital Status: 1 depicts married, 2 depicts single and 3 depicts others.

- AGE: The customer's age in years.

- PAY_0 - PAY_6: The repayment status. It is the customer's history of past payment from April to September, 2005. The measurement scale for the repayment status are:

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

    - 9 represents payment delay for nine months and above.

- BILL_AMT1 - BILL_AMT6: The amount of bill statement in dollars from April to September , 2005.

- PAY_AMT1 - PAY_AMT6: The amount of previous payment in dollars from April to September , 2005.

- default.payment.next.month: The default payment next month. 0 represents yes and 1 represents no.

## Report


The final report can be found [here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/src/credit_default_eda.ipynb)

## Usage


## Dependencies


## License
This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.


## References
   Lichman, M. (2013). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.
   
   The original dataset can be found [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00350/) at the UCI Machine Learning Repository.


