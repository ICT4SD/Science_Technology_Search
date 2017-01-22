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

###See an example of getting full text:

From the WARC files we obtains records of this format:

{"urlkey": "af,gov,afghanexperts)/", "timestamp": "20161207122240", "status": "200", "url": "http://afghanexperts.gov.af/", "filename": "crawl-data/CC-MAIN-2016-50/segments/1480698542112.77/warc/CC-MAIN-20161202170902-00193-ip-10-31-129-80.ec2.internal.warc.gz", "length": "5590", "mime": "text/html", "offset": "7633111", "digest": "OWUUY5VHCX62BY4CKETES3C7IKISLN5T"}

The full text will be in a WET file which is located in a path which can be derived from the WARC file by:

-replacing the "/warc/" folder by "/wet/"  and by
-changing the extension of the file downloaded from "....warc.gz" to "....warc.wet.gz"

So you can download the WET file (full text) which contains the full text of the URL above ("url": "http://afghanexperts.gov.af/") with this command:

$wget https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2016-50/segments/1480698542112.77/wet/CC-MAIN-20161202170902-00193-ip-10-31-129-80.ec2.internal.warc.wet.gz

Note that this WET file contains the full text of many more URLs so to get to your exact URL you must use the ("offset": "7633111") and  ("length": "5590") parameters when reading the file.

for example in python, after having downloadd and gunzip the file:

with open('CC-MAIN-20161202170902-00193-ip-10-31-129-80.ec2.internal.warc.wet') as f:
    # for line in f:      # uncomment these two lines to see the full text
    #     print (line)
    f.seek(7633111)       # use this line with the value of the offset parameter to open the file where your url is located
    print(f.read(5590))   # this is the lenght of your full text, from the lenght parameter
    
NOTE: the offset above is not workng properly, i believe its because the offset is valid for the compressed file. You can experiment with that.
