# Copyright (c) UBC-DSCI Development Team.
FROM rocker/verse:4.0.0
RUN apt-get update --fix-missing \
	&& apt-get install -y \
		ca-certificates \
    libglib2.0-0 \
	 	libxext6 \
	  libsm6  \
	  libxrender1 \
		libxml2-dev
		
# install python3 & virtualenv
RUN apt-get install -y \
		python3-pip \
		python3-dev \
	&& pip3 install virtualenv
	
# install anaconda & put it in the PATH
RUN echo ‘export PATH=/opt/conda/bin:$PATH’ > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH /opt/conda/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/lib/R/lib/:${LD_LIBRARY_PATH}

RUN conda install --quiet --yes \
    'r-reticulate'
    
RUN conda install -c conda-forge altair_saver  

# install python packages
RUN pip install \
    'ipykernel'\
    'matplotlib>=3.2.2' \
    'scikit-learn==1.0.*' \
    'pandas>=1.3.*' \
    'numpy' \
    'requests>=2.24.0' \
    'graphviz'\
    'make'\
    'pip'\
    'eli5'\
    'seaborn'\
    'imbalanced-learn' \
    'ipython>=7.15' \
    'docopt==0.6.2' \
    'openpyxl==3.0.9' \
    'xlrd==2.0.1' \
    'altair==4.1.0' \
    'portpicker==1.5.0' \
    'jupyterlab==3.2.4' \
    'mglearn' \
    'psutil>=5.7.2'