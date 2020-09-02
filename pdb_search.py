#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:46:21 2020

@author: peter
"""

import urllib
import urllib.request


url = 'http://www.rcsb.org/pdb/rest/search'

#this query searches for pdb files with >1 chain and at least 1 chain with <12 residues
queryText = """

<orgPdbCompositeQuery>

<queryRefinement>

<queryRefinementLevel>0</queryRefinementLevel>

<orgPdbQuery>

<queryType>org.pdb.query.simple.NumberOfChainsQuery</queryType>

<description>Number of Chains Search : Min Number of Chains=2</description>

<struct_asym.numChains.min>2</struct_asym.numChains.min>

</orgPdbQuery> 

</queryRefinement>

<queryRefinement>

<queryRefinementLevel>1</queryRefinementLevel>

<conjunctionType>and</conjunctionType>

<orgPdbQuery>

<queryType>org.pdb.query.simple.SequenceLengthQuery</queryType>

<description>Sequence Length Search : Min Sequence Length=1 Max Sequence Length=12</description>

<v_sequence.chainLength.min>1</v_sequence.chainLength.min>

<v_sequence.chainLength.max>12</v_sequence.chainLength.max>

</orgPdbQuery>

</queryRefinement>

</orgPdbCompositeQuery>

"""

print ("\nQUERY:\n", queryText, "\n")

print ("QUERYING PDB...\n")

queryText= queryText.encode('ascii')

req = urllib.request.Request(url, data=queryText)

f = urllib.request.urlopen(req)

result = f.read()

result = str(result)

hits = result.count('n')

result = result.replace("\\n", " ")
  
if result:
    print ("Found number of PDB entries: ", str(hits))
    with open("./pdbsearch_output.txt", "a") as myfile:
       myfile.write(result)
       myfile.close()
    
else:
    print ("Failed to retrieve results")