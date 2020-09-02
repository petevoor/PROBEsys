#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:46:21 2020

@author: peter
"""

import urllib
import urllib.request



IDs = ['4A0T','1OX9']

def fetch(ID):
    url1 = 'http://www.rcsb.org/pdb/rest/customReport.csv?pdbids='
    url2 = '&customReportColumns=structureId,chainId,entityId,pubmedId,chainLength,Ka,Kd,source,sequence&service=wsdisplay&format=csv'
    
    url = url1 + ID + url2
    
    print ("FETCHING FROM PDB...\n")
    
    req = urllib.request.Request(url)

    f = urllib.request.urlopen(req)

    result = f.read()

    result = str(result)
  
    if result:
        with open("./pdbfetch_output_{}.txt".format(str(ID)), "a") as myfile:
            myfile.write(result)
            myfile.close()

for i in IDs:
    fetch(i)