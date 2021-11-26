
# Credit Default Payment Predictor

-   Authors: Arushi Ahuja, Karanpreet Kaur, Lianna Hovhannisyan, Taiwo
    Owoseni

Using Logistic Regression to predict whether the customer will do credit
default payment next month or not.

## About

In this project, we built a classification model using Logistic
Regression to predict if the credit account holders will make a default
payment or not next month. The model was trained on features that hold
information about the client’s last 6 months bill and payment history,
as well as several characteristics: age, marital status, gender, etc.
Overall, we are more interested in minimizing Type \| error (predicting
not default payment, when in reality client made a default payment next
month) and Type \|\| error (predicting default payment, when in reality
client did not do default next month), we are using primarily *f*1 as
scoring metric. Our model performed fairly well….

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
[here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/doc/).

## Usage

-   To replicate the analysis, clone this GitHub repository.

-   To set up the necessary packages for running the project, download
    the environment file from
    [here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/environment.yaml):
    hit “Raw” and then Ctrl/Cmnd + S to save it, or copy paste the
    content. Then create a Python virtual environment by using conda
    with the environment file you just downloaded:

<!-- -->

    conda env create --file environment.yaml

-   Run the following command from the environment where you have
    JupyterLab installed (e.g. base).

<!-- -->

    conda install nb_conda_kernels

If you wish to not use conda environment, please make sure you have all
the dependencies and packages installed in your local machine, found
[here](https://github.com/UBC-MDS/credit_default_prediction/blob/main/environment.yaml)
before running these commands.

After setting up the environment or downloading the dependencies, follow
up the instructions below.

-   Run the following commands at the command line/terminal from the
    root directory of this project:

<!-- -->

    # download data
    src/download_data.py --out_type=xls --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls --out_file=data/raw/default_credit_card_clients.csv

    # run eda report
    jupyter lab src/credit_default_eda.ipynb

    # clean data  
    python src/clean_split_data.py --input_path="data/raw/default_credit_card_clients.csv" --out_dir="data/preprocessed"

    # transform data
    python src/transformed_data.py --input_path="data/preprocessed/cleaned_data.csv" --out_dir="data/preprocessed"

    # create exploratory data analysis figure and write to file 

    # tune model
    python 

    # test model
    python 

    # render final report
    Rscript -e "rmarkdown::render('doc/credit_default_prediction_report.Rmd', output_format = 'github_document')"

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
