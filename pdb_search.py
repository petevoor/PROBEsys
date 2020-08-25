#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:46:21 2020

@author: peter
"""

#below is the xml code for a PDB query for structures with >1 chain
"""
<orgPdbQuery>

<queryType>org.pdb.query.simple.NumberOfChainsQuery</queryType>

<description>Number of Chains Search : Min Number of Chains=2</description>

<struct_asym.numChains.min>2</struct_asym.numChains.min>

</orgPdbQuery>
"""

#below is the xml code for a PDB query for chains
"""
<orgPdbQuery>

<queryType>org.pdb.query.simple.SequenceLengthQuery</queryType>

<description>Sequence Length Search : Min Sequence Length=1 Max Sequence Length=12</description>

<v_sequence.chainLength.min>1</v_sequence.chainLength.min>

<v_sequence.chainLength.max>12</v_sequence.chainLength.max>

</orgPdbQuery>
"""

import xml #google  library documentation to see how to use

# if Alison can't find better guidance on the xml queries, will need to do two 
# separate ID pulls, then have a matching function see which IDs are in both

#below is an example of how to submit search queries with python
'''
import urllib2


url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<?xml version="1.0" encoding="UTF-8"?>

<orgPdbQuery>

<version>B0907</version>

<queryType>org.pdb.query.simple.ExpTypeQuery</queryType>

<description>Experimental Method Search: Experimental Method=SOLID-STATE NMR</description>

<mvStructure.expMethod.value>SOLID-STATE NMR</mvStructure.expMethod.value>

</orgPdbQuery>

"""


print "query:\n", queryText

print "querying PDB...\n"

req = urllib2.Request(url, data=queryText)

f = urllib2.urlopen(req)

result = f.read()


if result:

    print "Found number of PDB entries:", result.count('\n')

else:

    print "Failed to retrieve results"
'''