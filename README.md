# Credit Default Prediction

## About

------------------------------------------------------------------------

This project aims to build a classification model using \<unknown models> algorithm to predict potential credit default accounts of Taiwan's credit card clients'.

\<Tiffany Describes the outcome>

The data set is a Taiwan credit card data from April to September, 2005 sourced from the UCI machine learning repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/default|of|credit|card|clients). Although its original creators are unknown, previous studies strongly suggest it is a private data.

The data set consists of 25 columns partitioned into :

- One ID column

- Twenty three (23) explanatory columns

- One response column

#### Column Description

|--------------------|-----------------------------------------------|
| Column Name        | Description                                   |
|====================|===============================================|
| ID                 | Row observation number                        |
|--------------------|-----------------------------------------------|
| X1                 | Amount of the given credit in Dollars         |
|--------------------|-----------------------------------------------|
| X2                 | Gender                                        |
|--------------------|-----------------------------------------------|
| X3                 | Education Level                               |
|--------------------|-----------------------------------------------|
| X4                 | Martial Status                                |
|--------------------|-----------------------------------------------|
| X5                 | Age                                           |
|--------------------|-----------------------------------------------|
| X6                 | Repayment status in September                 |
|--------------------|-----------------------------------------------|
| X7                 | Repayment status in August                    |
|--------------------|-----------------------------------------------|
| X8                 | Repayment status in July                      |
|--------------------|-----------------------------------------------|
| X9                 | Repayment status in June                      |
|--------------------|-----------------------------------------------|
| X10                | Repayment status in May                       |
|--------------------|-----------------------------------------------|
| X11                | Repayment status in April                     |
|--------------------|-----------------------------------------------|
| X12                | Amount of bill statement in September         |
|--------------------|-----------------------------------------------|
| X13                | Amount of bill statement in August            |
|--------------------|-----------------------------------------------|
| X14                | Amount of bill statement in July              |
|--------------------|-----------------------------------------------|
| X15                | Amount of bill statement in June              |
|--------------------|-----------------------------------------------|
| X16                | Amount of bill statement in May               |
|--------------------|-----------------------------------------------|
| X17                | Amount of bill statement in April             |
|--------------------|-----------------------------------------------|
| X18                | Amount of previous payment in September       |
|--------------------|-----------------------------------------------|
| X19                | Amount of previous payment in August          |
|--------------------|-----------------------------------------------|
| X20                | Amount of previous payment in July            |
|--------------------|-----------------------------------------------|
| X21                | Amount of previous payment in June            |
|--------------------|-----------------------------------------------|
| X22                | Amount of previous payment in May             |
|--------------------|-----------------------------------------------|
| X23                | Amount of previous payment in April           |
|--------------------|-----------------------------------------------|
| Y                  | Defaults Payment                              |
|--------------------|-----------------------------------------------|

The columns are further defined below:

- ID: Row Identifier.

- X1: Amount of the given credit (NT dollar): it includes both the individual costumer credit and his/her family (supplementary)

- X2: The customer's gender: 1 depicts male and 2 depicts female.

- X3: The customer's education Level: 1 depicts graduate school, 2 depicts university, 3 depicts high school and 4 depicts others.

- X4: The customer's Marital Status: 1 depicts married, 2 depicts single and 3 depicts others.

- X5: The customer's age in years.

- X6-X11: The repayment status. It is the customer's history of past payment from April to September, 2005. The measurement scale for the repayment status are:

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

- X12-X17: The amount of bill statement in dollars from April to September , 2005.

- X18-X23: The amount of previous payment in dollars from April to September , 2005.

- Y: The default payment . 0 represents yes and 1 represents no.

## Report

------------------------------------------------------------------------

The final report can be found \<no link>

## Usage

------------------------------------------------------------------------

## **Dependencies**

------------------------------------------------------------------------

## **License**

------------------------------------------------------------------------

## **References**

------------------------------------------------------------------------
