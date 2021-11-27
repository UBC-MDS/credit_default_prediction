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
Type \| error (predicting no default payment, when in reality the client
made a default payment the following month), as opposed to Type \|\|
error (predicting default payment, when in reality no default payment
was made by the client), we are using *f*1 as our primary scoring
metric. Our model performed fairly well….

## Introduction

An account is considered the default when the client does not make the
minimum payment for a consecutive 6 months period. Predicting potential
credit default accounts is challenging but at the same time crucial for
credit card companies. The default can happen for various reasons: the
loss of a job, change in the financial market, personal difficulties,
inability to work, health issues, need to use the extra cash for other
bills, etc. All of the described can be considered as “out-of-control”
from the customers’ side. However, the default can also be intentional.
An example of intentional default is when the client knows that they are
no longer financially stable enough for the credit, but continue to use
it until the bank intervenes (Islam, Eberle, and Ghafoor 2018). The
existence of such loopholes makes it essential for creditors to detect
default accounts as soon as possible. In general, for creditors earlier
they detect the potential default accounts, the lower the losses for the
company (Nor, Ismail, and Yap 2019).

Here we ask if we can use a machine-learning algorithm to predict
whether the customer will do default payment next month or not. The
detection of default depends on extensive data profiling of customer’s
finance, including their age, payment history, marriage status, gender,
education. For the creditors, it is most important to have the model
that predicts the account’s next month’s status, especially if the
client is going to make a default payment. The correct prediction will
help creditors to plan their risk management and take according to
actions before the situation gets out of control.

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

The Logistic Regression algorithm was used to build a classification
model for the default credit card dataset to predict whether the client
will make a default payment or not in the next month (can be found in
the “default payment next month” column with binary label). All the
features included in the original dataset were used for tuning and
fitting the model. The hyperparameter *C* was chosen using 10
cross-validations with *f*1 score as scoring metrics. The Python
programming language (Van Rossum and Drake 2009) and the following
Python packages were used for the model analysis: docopt (Keleshev
2014), sklearn (Buitinck et al. 2013), altair (VanderPlas et al. 2018),
pandas (McKinney et al. 2010), numpy (Harris et al. 2020), os (Van
Rossum and Drake 2009), requests (Chandra and Varanasi 2015), pickle
(Van Rossum 2020), matplot (Hunter 2007), seaborn (Waskom et al. 2017);
as well as R programming language (R Core Team 2021) for generating this
report and the following packages: knitr (Xie 2014), tidyverse (Wickham
2017). The code used to perform the analysis and create the report can
be found [here](https://github.com/UBC-MDS/credit_default_prediction).

### Results & Discussion

-   EDA

-   Analysis

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
