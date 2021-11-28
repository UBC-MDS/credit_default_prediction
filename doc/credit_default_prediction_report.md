Predicting credit default payments from client’s payment history
================
Lianna Hovhannisyan, Arushi Ahuja, Taiwo Owoseni, Karanpreet Kaur
25/11/2021

-   [Summary](#summary)
-   [Introduction](#introduction)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
    -   [Results & Discussion](#results--discussion)
-   [References](#references)

## Summary

In this project, we built a classification model using Logistic
Regression to predict if credit account holders will make a default
payment next month. The model was trained on features that hold
information about the client’s last 6 months bill and payment history,
as well as several other characteristics such as: age, marital status,
education, and gender. Overall, we are more interested in minimizing
Type I error (predicting no default payment, when in reality the client
made a default payment the following month), as opposed to Type II error
(predicting default payment, when in reality no default payment was made
by the client), we are using *f*1 as our primary scoring metric. Our
model performed fairly well on test data set with the *f*1 score being
0.528. Our recall and precision rate are moderately high, being 0.587,
0.48 respectively. The given scores are consistent with the train data
set scores, thus we can say that the model is generalizable on unseen
data. However, the scores are not high, and our model is error prompt.
The model can correctly classify default payments roughly half of the
time. The value of incorrectly identifying default or no default can
cause a lot of money and reputation to the company, thus we recommend
continuing study to improve this prediction model before it is put into
production in the credit companies. Some of the improvement research
topics can be feature engineering, bigger dataset collected from other
countries (China, Canada, Japan).

## Introduction

An account makes a default payment when the minimum payment is not made
for a consecutive 6 months period. Predicting potential credit default
accounts is challenging but at the same time crucial for credit card
companies. The default can happen for various reasons: the loss of a
job, change in the financial market, personal difficulties, inability to
work, health issues, need to use the extra cash for other bills, etc.
All of the examples described can be considered as “out-of-control” from
the customers’ side. However, the default can also be intentional. An
example of intentional default is when the client knows that they are no
longer financially stable enough for credit, but continues to use credit
until the bank intervenes (Islam, Eberle, and Ghafoor 2018). The
existence of such loopholes makes it essential for creditors to detect
default accounts as soon as possible. In general for creditors, the
earlier they detect the potential default accounts, the lower their
losses will be (Nor, Ismail, and Yap 2019).

Here we ask if we can use machine-learning algorithms to predict whether
a customer will do a default payment next month or not. The detection of
default depends on extensive data profiling of customer’s finance, along
with other information such as their age, payment history, marriage
status, gender, education. For the creditors, it is most important to
have the model that predicts the account’s next month’s status,
especially if the client is going to make a default payment. The correct
prediction will help creditors to plan their risk management and take
steps before the situation gets out of control.

## Methods

### Data

The data set used in the project is created by Yeh, I. C., and Lien, C.
H (Yeh and Lien 2009), and made publicly available for download in UCI
Machine Learning Repository (“<span class="nocase">default of credit
card clients</span>” 2016). The data can be found
[here](https://archive-beta.ics.uci.edu/ml/datasets/default+of+credit+card+clients),
specifically [this
file](https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls).
The dataset is based on Taiwan’s credit card client default cases from
April to September. It has 30000 examples, and each example represents
particular client’s information. The dataset has 24 observations with
respective values such as gender, age, marital status, last 6 months
bills, last 6 months payments, etc, including the final default payment
of next month column: labeled 1 (client will make a default) and 0
(client will not make a default).

### Analysis

The Logistic Regression algorithm is one of the most popular ways to fit
models for categorical data, especially for binary response data in data
modeling. That is why it was used to build a classification model for
the default credit card dataset to predict whether the client will make
a default payment in the next month (can be found in the “default
payment next month” column with binary label). All the features included
in the original dataset were used for tuning and fitting the model. The
hyperparameter *C*, *c**l**a**s**s*\_*w**e**i**g**h**t* were chosen
using 10 cross-validations with *f*1 score as primary scoring metric
(recall and precision also considered). The Python programming language
(Van Rossum and Drake 2009) and the following Python packages were used
for the model analysis: docopt (Keleshev 2014), sklearn (Buitinck et al.
2013), altair (VanderPlas et al. 2018), pandas (McKinney et al. 2010),
numpy (Harris et al. 2020), os (Van Rossum and Drake 2009), requests
(Chandra and Varanasi 2015), pickle (Van Rossum 2020), matplot (Hunter
2007), seaborn (Waskom et al. 2017); as well as R programming language
(R Core Team 2021) for generating this report and the following
packages: knitr (Xie 2014), tidyverse (Wickham 2017). The code used to
perform the analysis and create the report can be found
[here](https://github.com/UBC-MDS/credit_default_prediction).

### Results & Discussion

In order to understand which features play an important role in the
decision making and prediction within the model, we will look at the
distributions of each feature individually either through bar graphs or
histograms depending on the type of feature, and we will also be
grouping them by the 2 target classes. Here the target classes are: “1”
if default payment was made meaning that the client did not pay their
credit on time, and “0” if no default payment was made meaning that the
client did pay their credit on time. It is important to note that
because this is the preliminary analysis before any transformations or
model making, the visualizations do not take into account the class
imbalance and so while we may come to conclusions about the features
right now, they may contain a certain amount of bias to them.

For the numerical features, we will be looking at their histograms and
will be mainly focusing on how the target classes overlap with each
other for each feature. Less overlap between target classes in general
would indicate to creating a more realistic model, this is because the
model would be able to easily classify the target classes given the
difference in values of the features for each target class. Furthermore,
this would give us an idea of which features we could potentially give
more importance to and exactly how to define our predictive model. From
Figure 1, we see that most features show very little overlap, telling us
that right now it would not be wise to remove any feature from the
analysis.

<img src="../results/histogram_numeric_feat.png" title="Figure 1. Comparison of distributions for the numerical features of the training data set grouped by target classes" alt="Figure 1. Comparison of distributions for the numerical features of the training data set grouped by target classes" width="100%" style="display: block; margin: auto;" />

For the ordinal and categorical features such as sex, education, and
whether a client has payed their past month credit or not, instead of
looking at the histograms, we instead will be looking at the bar graphs
in order to understand the proportions of the target classes in each of
the categories in all features. Since the categories for the features
are classified by numbers, here I will provide an explanation for what
the numbers represent in each feature:

-   SEX: 1 depicts male and 2 depicts female.
-   PAY_0 - PAY_6 : -2 represents balance paid in full and no
    transactions in this period (we may refer to this credit card
    account as having been ‘inactive’ this period).-1 represents pay
    duly, but customer’s account has a positive balance at end of period
    due to recent transactions for which payment has not yet come due. 0
    represents customer paid the minimum due amount, but not the entire
    balance. And finally, positive numbers represent payment delays by
    those many number of months, so for example PAY_0 is 1, then the
    payment is delayed by one month.
-   MARRIAGE: 1 depicts married, 2 depicts single and 3 depicts others.
-   EDUCATION: 1 depicts graduate school, 2 depicts university, 3
    depicts high school and 4 depicts others.

On looking at the bar graphs in Figure 2, it is hard to say which
features could play a more important role in the predictions, in general
we see that proportions for “0” target class are higher for each
category in all features.

<img src="../results/categorical_feat_graph.png" title="Figure 2. Comparison of proportions for the categorical and ordinal features of the training data set grouped by target classes" alt="Figure 2. Comparison of proportions for the categorical and ordinal features of the training data set grouped by target classes" width="100%" style="display: block; margin: auto;" />

The Logistic regression prediction model works fine on test data, with
test accuracy of **0.819** but as our project focuses on predicting the
clients with credit defaults and thus it’s very crucial for our model to
predict Defaulter class correctly and minimize the misclassification
errors. To identify the actual errors made by the model,we are checking
metrics **recall, precision and f1 score** for **Defaulter class** and
our model has these metrics values as **0.362, 0.651, 0.465**
respectively. It can be observed that the recall for Defaulter class is
significantly less than the precision and hence f1-score also reflects
that. The detailed classification of classes in terms of numbers can be
seen below.

<img src="credit_default_prediction_report_files/figure-gfm/confusion matrix for default model-1.png" title="Figure 3. Confusion matrix of Logistic Regression model with default parameters" alt="Figure 3. Confusion matrix of Logistic Regression model with default parameters" style="display: block; margin: auto;" />

The reason for such large number of Type II errors (False negatives)
could be due to class imbalance in dataset. So, to identify and minimize
the effect of imbalance, we further improved our model by the recall for
the model, we perfomed hyperparameter tuning on Logistic regression
model on hyperparameters (C and class_weight) using RandomizedSearchCV.
The model returned by random search trains on best parameters and hence
we used this model for scoring metrics. The random search gives **test
accuracy score** of **0.772** and metrics **recall, precision and
f1-score** for **Defaulter class** are **0.587, 0.48, 0.528**
respectively. Through hyperparameter tuning, we are able to achieve
higher recall and f1-score. There is always some trade-off between
recall and precision and hence the precision is lower for the tuned
model. The correct amount of trade-off or accepted recall and precision
score is somewhat business dependent as these scores highly impact the
business costs and strategies. The detailed classification of target can
be seen below:

<img src="credit_default_prediction_report_files/figure-gfm/confusion matrix for tuned model-3.png" title="Figure 4. Confusion matrix of tuned Logistic Regression model with hyperparameters" alt="Figure 4. Confusion matrix of tuned Logistic Regression model with hyperparameters" style="display: block; margin: auto;" />

To further improve this model in future with hopes that it will be used
for credit companies, there are several things we can suggest. Firstly,
feature engineering can help us boost our *f*1 score. We believe that
the expert knowledge will help to dive deeper into the problem and add
features such as the combination ratio of payment and bill, to help our
model to rank the features more accurately. Secondly, we will try other
classification algorithms such as Random Forest, with the hopes of
getting better score and less error pron model. Finally, we will collect
more data from other countries such as China, Canada, Japan to have
bigger understanding of the trends in default credit payment and train
our model with larger dataset.

Figure 3 gives a glimpse on how we went about finding the best
hyperparameters for the Logistic Regression model. Here the 2
hyperparameter we are finding values for are: - “C” which defines the
complexity of the model. Higher value of C means a more complex model. -
“class weights” which can be only two values “balanced” or None . If
“class weights” is “balanced” then that means we are treating all
features equally in the decision making process during prediction.

After carrying out Random Search cross validation with 10 folds, Figure
3 shows the different combination of the two hyperparamters along with
the scores of those models. We see that the model provides the best
score with “class weights” equal to “balanced” and “C” equal to 0.1.

<img src="../results/random_search.png" title="Figure 5. Comparison of scores while tuning hyperparamters for the Logistic Regression model" alt="Figure 5. Comparison of scores while tuning hyperparamters for the Logistic Regression model" width="60%" style="display: block; margin: auto;" />

## References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-sklearn_api" class="csl-entry">

Buitinck, Lars, Gilles Louppe, Mathieu Blondel, Fabian Pedregosa,
Andreas Mueller, Olivier Grisel, Vlad Niculae, et al. 2013. “API Design
for Machine Learning Software: Experiences from the Scikit-Learn
Project.” In *ECML PKDD Workshop: Languages for Data Mining and Machine
Learning*, 108–22.

</div>

<div id="ref-chandra2015python" class="csl-entry">

Chandra, Rakesh Vidya, and Bala Subrahmanyam Varanasi. 2015. *Python
Requests Essentials*. Packt Publishing Ltd.

</div>

<div id="ref-misc_default_of_credit_card_clients_350" class="csl-entry">

“<span class="nocase">default of credit card clients</span>.” 2016. UCI
Machine Learning Repository.

</div>

<div id="ref-2020NumPy-Array" class="csl-entry">

Harris, Charles R., K. Jarrod Millman, Stéfan J van der Walt, Ralf
Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020.
“Array Programming with NumPy.” *Nature* 585: 357–62.
<https://doi.org/10.1038/s41586-020-2649-2>.

</div>

<div id="ref-hunter2007matplotlib" class="csl-entry">

Hunter, John D. 2007. “Matplotlib: A 2d Graphics Environment.”
*Computing in Science & Engineering* 9 (3): 90–95.

</div>

<div id="ref-Islam2018CreditDM" class="csl-entry">

Islam, Sheikh Rabiul, William Eberle, and Sheikh Khaled Ghafoor. 2018.
“Credit Default Mining Using Combined Machine Learning and Heuristic
Approach.” *ArXiv* abs/1807.01176.

</div>

<div id="ref-docoptpython" class="csl-entry">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-mckinney2010data" class="csl-entry">

McKinney, Wes et al. 2010. “Data Structures for Statistical Computing in
Python.” In *Proceedings of the 9th Python in Science Conference*,
445:51–56. Austin, TX.

</div>

<div id="ref-SyedNor2019PersonalBP" class="csl-entry">

Nor, Sharifah Syed, Shafinar Ismail, and Bee Wah Yap. 2019. “Personal
Bankruptcy Prediction Using Decision Tree Model.” *Law & Economics
eJournal*.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2021. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-van1995python" class="csl-entry">

Van Rossum, Guido. 2020. *The Python Library Reference, Release 3.8.2*.
Python Software Foundation.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-vanderplas2018altair" class="csl-entry">

VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit
Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben
Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical
Visualizations for Python.” *Journal of Open Source Software* 3 (32):
1057.

</div>

<div id="ref-michael_waskom_2017_883859" class="csl-entry">

Waskom, Michael, Olga Botvinnik, Drew O’Kane, Paul Hobson, Saulius
Lukauskas, David C Gemperline, Tom Augspurger, et al. 2017.
*Mwaskom/Seaborn: V0.8.1 (September 2017)* (version v0.8.1). Zenodo.
<https://doi.org/10.5281/zenodo.883859>.

</div>

<div id="ref-tidyverse" class="csl-entry">

Wickham, Hadley. 2017. *Tidyverse: Easily Install and Load the
’Tidyverse’*. <https://CRAN.R-project.org/package=tidyverse>.

</div>

<div id="ref-knitr" class="csl-entry">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

<div id="ref-Yeh2009TheCO" class="csl-entry">

Yeh, I-Cheng, and Che-hui Lien. 2009. “The Comparisons of Data Mining
Techniques for the Predictive Accuracy of Probability of Default of
Credit Card Clients.” *Expert Syst. Appl.* 36: 2473–80.

</div>

</div>
