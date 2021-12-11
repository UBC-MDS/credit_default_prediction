FROM jupyter/r-notebook

RUN conda install --yes docopt=0.6.*  \
                    pandas=1.3.*  \
                    scikit-learn=1.0.* \
                    altair=4.1.* \
                    altair_data_server=0.4.* \
                    altair_saver=0.5.*
                    

RUN pip install \
    'ipykernel'\
    'matplotlib>=3.2.2' \
    'numpy' \
    'requests>=2.24.0' \
    'graphviz'\
    'make'\
    'pip'\
    'eli5'\
    'seaborn'\
    'imbalanced-learn' \
    'ipython>=7.15' \
    'openpyxl==3.0.9' \
    'xlrd==2.0.1' \
    'portpicker==1.5.0' \
    'mglearn' \
    'psutil>=5.7.2'

RUN conda install --quiet --yes \
    'r-reticulate'