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

<orgPdbQuery>

<queryType>org.pdb.query.simple.NumberOfChainsQuery</queryType>

<description>Number of Chains Search : Min Number of Chains=2</description>

<struct_asym.numChains.min>2</struct_asym.numChains.min>

<queryType>org.pdb.query.simple.SequenceLengthQuery</queryType>

<description>Sequence Length Search : Min Sequence Length=1 Max Sequence Length=12</description>

<v_sequence.chainLength.min>1</v_sequence.chainLength.min>

<v_sequence.chainLength.max>12</v_sequence.chainLength.max>

</orgPdbQuery>