# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:51:33 2017

@author: Yi Luo
"""

import subprocess
import sys
import os

#SEED DOMAINS
edu_domains = [
    # ted
    "https://www.ted.com/*"
    ]

# Fetching functions

def countPages (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c'
    index = 'CC-MAIN-2016-50'
    search_prefix = '*'
    options = '--show-num-pages'
    for domain in edu_domains:
        subprocess.call(str(command +' '+ index + ' ' + search_prefix + domain + ' ' + options), shell=True)

def getUrls (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c CC-MAIN-2016-50 '
    options = '-j -d'  #use -z for .gz compressed files
    outputFolder = "C:/Users/tradingroom/result3"     #create this directory manually
    for domain in edu_domains:
        subprocess.call(str(command + domain + ' ' + options + ' ' + outputFolder), shell=True)
        
#countPages(gov_domains)
getUrls(edu_domains)

