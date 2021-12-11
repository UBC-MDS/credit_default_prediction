# credit default prediction data pipe
# author: Karanpreet Kaur
# date: 2021-12-03

all: doc/report.md doc/report.html

# download data
data/raw/default_credit_card_clients.csv: src/download_data.py 
										  python src/download_data.py --out_type=csv --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls --out_file=data/raw/default_credit_card_clients.csv

# clean data  
data/preprocessed/cleaned_data.csv:	src/clean_split_data.py data/raw/default_credit_card_clients.csv
									python src/clean_split_data.py --input_path="data/raw/default_credit_card_clients.csv" --out_dir="data/preprocessed"

# transform data
data/preprocessed/transformed_train.csv	data/preprocessed/transformed_test.csv:	src/transform_data.py data/preprocessed/cleaned_data.csv
																				python src/transform_data.py --input_path="data/preprocessed/cleaned_data.csv" --out_dir="data/preprocessed"


# tune model
results/model: src/model.py data/preprocessed/transformed_train.csv data/preprocessed/transformed_test.csv
			   python src/model.py --train_path="data/preprocessed/transformed_train.csv" --test_path="data/preprocessed/transformed_test.csv" --out_dir="results/model/"

# create exploratory data analysis figure and write to file 
results/eda: src/eda_correlation_heatmap.py data/preprocessed/transformed_train.csv
			 python src/eda_correlation_heatmap.py --file_path="data/preprocessed/transformed_train.csv" --out_dir="results/eda/"
				
results/random_search.png:	src/random_search_eda.py results/eda
							python src/random_search_eda.py --file_path="results/model/random_search_cv_scores.csv" --out_dir="results/eda/"
													
# render final report
doc/report.md: results/model results/random_search.png results/eda doc/report.Rmd doc/default_prediction_refs.bib
										 Rscript -e "rmarkdown::render('doc/report.Rmd')"

doc/report.html: results/model results/random_search.png results/eda doc/report.Rmd doc/default_prediction_refs.bib
										   Rscript -e "rmarkdown::render('doc/report.Rmd', output_format = 'html_document')"

clean: 
	rm -rf data
	rm -rf results
	rm -rf doc/report.md doc/report.html			
