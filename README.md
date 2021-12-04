
# Credit Default Payment Predictor

-   Authors: Arushi Ahuja, Karanpreet Kaur, Lianna Hovhannisyan, Taiwo
    Owoseni

Using Logistic Regression to predict whether the customer will do credit
default payment next month or not.

## About

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
metric. Our model performed fairly well on test data set with the *f*1
score being \~0.53. Our recall and precision rate are moderately high,
being \~0.48, \~0.59 respectively. The given scores are consistent with
the train data set scores, thus we can say that the model is
generalizable on unseen data. However, the scores are not high, and our
model is error prompt. The model can correctly classify default payments
roughly half of the time. The value of incorrectly identifying default
or no default can cause a lot of money and reputation to the company,
thus we recommend continuing study to improve this prediction model
before it is put into production in the credit companies. Some of the
improvement research topics can be feature engineering, bigger dataset
collected from other countries (China, Canada, Japan).

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

## Report

The final report can be found
[here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/doc/credit_default_prediction_report.md).

## Usage

– To replicate the analysis, clone this GitHub repository.

– To set up the necessary packages for running the project, download the
environment file from
[here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/environment.yaml):
hit “Raw” and then Ctrl/Cmnd + S to save it, or copy paste the content.
Then create a Python virtual environment by using conda with the
environment file you just downloaded:

    conda env create --file environment.yaml

– Run the following command from the environment where you have
JupyterLab installed (e.g. base).

    conda install nb_conda_kernels

After setting up the environment or downloading the dependencies, follow
up the instructions below.

Note: For the `credit_default_prediction_report.Rmd` to run, you need to
Specify that {reticulate} should use the miniconda version of Python
from this created environment in your `.Rprofile` file:

-   Type `usethis::edit_r_profile()` into the R console inside RStudio,
    and an `.Rprofile` file from your HOME directory should open in
    RStudio add this to your .Rprofile file:
    `Sys.setenv(RETICULATE_PYTHON = "path_to_miniconda's_python for credit_default_env")`
    replacing the path set before.

-   In Windows, you need `\\` instead of a  to separate the directories,
    for example your path should be like:
    `C:\\Users\\hp\\miniconda3\\envs\\credit_default_env\\python.exe`

– Run the following commands at the command line/terminal from the root
directory of this project:

    # download data
    python src/download_data.py --out_type=csv --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls --out_file=data/raw/default_credit_card_clients.csv

    # clean data  
    python src/clean_split_data.py --input_path="data/raw/default_credit_card_clients.csv" --out_dir="data/preprocessed"

    # transform data
    python src/transform_data.py --input_path="data/preprocessed/cleaned_data.csv" --out_dir="data/preprocessed"

    # run eda report
    jupyter lab src/credit_default_eda.ipynb

    # create exploratory data analysis figure and write to file 
    python src/credit_default_eda.py --file_path="data/preprocessed/cleaned_train.csv" --out_dir="results/"
    python src/random_search_eda.py --file_path="results/random_search_cv_scores.csv" --out_dir="results/"

    # tune model
    python src/credit_default_predict_model.py --train_path="data/preprocessed/transformed_train.csv" --test_path="data/preprocessed/transformed_test.csv" --out_dir="results/"

    # render final report
    Rscript -e "rmarkdown::render('doc/credit_default_prediction_report.Rmd', output_format = 'html_document')"

## Dependencies

-   ipykernel
-   python=3.8
-   matplotlib>=3.2.2
-   scikit-learn>=1.0
-   pandas>=1.3.\*
-   numpy
-   requests>=2.24.0
-   graphviz
-   python-graphviz
-   pip
-   seaborn
-   eli5
-   imbalanced-learn
-   ipython>=7.15
-   altair_saver
-   docopt==0.6.2
-   openpyxl==3.0.9
-   xlrd==2.0.1
-   altair==4.1.0
-   portpicker==1.5.0
-   jupyterlab==3.2.4
-   pip:
    -   mglearn
    -   psutil>=5.7.2

## License

This dataset is licensed under a Creative Commons Attribution 4.0
International (CC BY 4.0) license. This allows for the sharing and
adaptation of the datasets for any purpose, provided that the
appropriate credit is given.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-misc_default_of_credit_card_clients_350" class="csl-entry">

“<span class="nocase">default of credit card clients</span>.” 2016. UCI
Machine Learning Repository.

</div>

<div id="ref-Yeh2009TheCO" class="csl-entry">

Yeh, I-Cheng, and Che-hui Lien. 2009. “The Comparisons of Data Mining
Techniques for the Predictive Accuracy of Probability of Default of
Credit Card Clients.” *Expert Syst. Appl.* 36: 2473–80.

</div>

</div>
