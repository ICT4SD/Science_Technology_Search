#This branch mention some tools which can be helpful for this project

The examples below use Anaconda Python:
### Install Anaconda

$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

$ bash miniconda.sh -p miniconda

###Fetching URLs from Common Crawl - url_fetch_commoncrawl.py
This shows an example of how to get URLs from common crawl. It's a wrapper for 
the work of "ikreymer". Thanks!!  

To get started you need a python 2.7 example.

a)Creating a new environment with Python 2.7

$ conda create -n cc27 python=2.7 requests beautiful-soup  ##cc27 is just a name, choose whatever you want

$ source activate cc27

###Clone utility to find URLs in Common Crawl See: https://github.com/ikreymer/cdx-index-client.git

$ git clone https://github.com/ikreymer/cdx-index-client.git

###Create a 'results' folder

$ mkdir results

###On url_fetch_commoncrawl.py modify the list of domain names you wish to crawl

###run the url_fetch_commoncrawl.py. This will take a while, specially if you have many domains

$ python url_fetch_commoncrawl.py

#Another tool
Working with WARC files can be tricky, the steps below how to take the files woth URLs obtained from the Common Crawl
can be manipulated using pandas. It uses a Python 3 environment which I called cc35:

###2) Creating a new conda environment with Python 3.5.

$ conda create --name cc35 zlib pandas numpy beautiful-soup

###Activating it

$ source activate cc35

###Processing URLs obtained from the CommomCrawl

$ python url_processing.py


# Finally, to get to clean text extacts from the common crawl, we need to get the WET files.
A nice example of how to get WET files see this nice blog:  
https://dmorgan.info/posts/common-crawl-python/

