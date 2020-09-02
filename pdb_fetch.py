#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:46:21 2020

@author: peter
"""

import urllib
import urllib.request



IDs = []

#open pdb search output file and add each PDB ID to the list "IDs"
with open("pdbsearch_output.txt") as IDinput:
    f = IDinput.read()
    f = f.replace(" ","\n")
    f = f.replace("b'","")
    f = f.replace("'","")

    IDs = f.splitlines()

#fetch function fetches data for a single pdb ID and stores it in a .txt file
def fetch(ID):
    url1 = 'http://www.rcsb.org/pdb/rest/customReport.csv?pdbids='
    url2 = '&customReportColumns=structureId,chainId,entityId,pubmedId,chainLength,Ka,Kd,source,sequence&service=wsdisplay&format=csv'
    
    url = url1 + ID + url2
    
    req = urllib.request.Request(url)

    f = urllib.request.urlopen(req)

    result = f.read()

    result = str(result)
  
    if result:
        with open("./fetch_outputs/pdbfetch_output_{}.txt".format(str(ID)), "a") as myfile:
            myfile.write(result)
            myfile.close()
            
print ("FETCHING FROM PDB...\n")

#performs fetch function on each PDB ID from the PDB search output
for i in IDs:
    fetch(i)
