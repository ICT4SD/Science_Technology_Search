## Getting a list of urls from a dictionary of internet domains

import subprocess
import sys
import os

#SEED DOMAINS
gov_domains = [
    '.gov.af',
    # '.gob.mx',
    '.gob.ar'
    ]

# Fetching functions

def countPages (domains):
    command= 'cdx-index-client/cdx-index-client.py -c'
    index = 'CC-MAIN-2016-50 '
    search_prefix = '*'
    options = '--show-num-pages'
    for domain in gov_domains:
        subprocess.call(str(command +' '+ index + ' ' + search_prefix + domain + ' ' + options), shell=True)

def getUrls (domains):
    command= 'cdx-index-client/cdx-index-client.py -c'
    index = 'CC-MAIN-2016-50 '
    search_prefix = '*'
    options = '-j -d'  #use -z for .gz compressed files
    outputFolder = 'results'     #create this directory manually
    for domain in gov_domains:
        subprocess.call(str(command +' '+ index + ' ' + search_prefix + domain + ' ' + options + ' ' + outputFolder), shell=True)

#countPages(gov_domains)
getUrls(gov_domains)
