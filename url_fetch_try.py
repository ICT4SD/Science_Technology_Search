# -*- coding: utf-8 -*-

## Getting a list of urls from a dictionary of internet domains
"""
Created on Sat Jan 21 10:10:25 2017

@author: Liyi Li
"""
import subprocess
import sys
import os

#SEED DOMAINS
gov_domains = [
    # France
    ".gouv.fr",
    # China,
    ".gov.cn",
    #Russia
    ".gov.ru",
    #UK
    ".gov.uk",
    #Bolivia
    ".gob.bo",
    #Egypt
    ".gov.eg" ,
    #Italy
    ".gov.it",
    #Ethiopia
    ".gov.et",
    #Japan
    ".go.jp",
    #Kazakhstan
    ".gov.kz",
    #Senegal
    ".gouv.sn",
    #Ukraine
    ".gov.ua",
    #Uruguay
    ".gub.uy",
    #US
    ".gov"
    ]

# Fetching functions

def countPages (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c'
    index = 'CC-MAIN-2016-50'
    search_prefix = '*'
    options = '--show-num-pages'
    for domain in gov_domains:
        subprocess.call(str(command +' '+ index + ' ' + search_prefix + domain + ' ' + options), shell=True)

def getUrls (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c CC-MAIN-2016-50 *'
    options = '-z -j -d'  #use -z for .gz compressed files
    outputFolder = "D:\\result2"     #create this directory manually
    for domain in gov_domains:
        subprocess.call(str(command + domain + ' ' + options + ' ' + outputFolder), shell=True)
        
#countPages(gov_domains)
getUrls(gov_domains)
