
# coding: utf-8

# In[2]:


VSV_Codons={"F":{"TTT":0.52,"TTC":0.48},
            "L":{"TTA":0.2,"TTG":0.23,"CTT":0.15,"CTC":0.14,"CTA":0.14,"CTG":0.13},
            "I":{"ATT":0.43,"ATC":0.32,"ATA":0.25},
            "M":{"ATG":1.0},
            "V":{"GTT":0.34,"GTC":0.23,"GTA":0.2,"GTG":0.23},
            "S":{"TCT":0.22,"TCC":0.16,"TCA":0.29,"TCG":0.06,"AGT":0.16,"AGC":0.1},
            "P":{"CCT":0.34,"CCC":0.18,"CCA":0.37,"CCG":0.12},
            "T":{"ACT":0.29,"ACC":0.19,"ACA":0.44,"ACG":0.07},
            "A":{"GCT":0.32,"GCC":0.18,"GCA":0.45,"GCG":0.05},
            "Y":{"TAT":0.61,"TAC":0.39},
            "*":{"TAA":0.68,"TGA":0.28,"TAG":0.04},
            "H":{"CAT":0.66,"CAC":0.34},
            "Q":{"CAA":0.57,"CAG":0.43},
            "N":{"AAT":0.72,"AAC":0.28},
            "K":{"AAA":0.62,"AAG":0.38},
            "D":{"GAT":0.6,"GAC":0.4},
            "E":{"GAA":0.62,"GAG":0.38},
            "C":{"TGT":0.58,"TGC":0.42},
            "W":{"TGG":1.0},
            "R":{"CGT":0.08,"CGC":0.02,"CGA":0.1,"CGG":0.08,"AGA":0.52,"AGG":0.2},
            "G":{"GGT":0.14,"GGC":0.08,"GGA":0.54,"GGG":0.24}}


# In[7]:


import random


# In[3]:


"""Creates a json formatted .txt file of VSV codon frequencies"""
import json
with open('VSV_Codon_Table.txt', 'w') as f:
  json.dump(VSV_Codons, f, ensure_ascii=False)


# In[4]:


Test_Seq='GGPGQKARLMAEALKEALAPVPIPFAAAQQRGPRKPI'


# In[5]:


"""uses montecarlo method to randomly select from a list of codons associated with each amino acid."""
def codon_select(probDict):
    import random
    r = random.random() #generates a random number between 0 and 1
    total = 0
    for value,prob in probDict.items(): #iterates through each possible codon and its associated probability
        if prob <= 0: continue # ignore items with a 0 weight.
        total += prob #
        if total>r: return value


# In[6]:


def codon_optimize(aa_string):
    codon_string=''
    for aa in aa_string:
        codon_string+=(codon_select(VSV_Codons[aa]))
    return codon_string
    


# In[72]:


codon_optimize(Test_Seq)


# In[14]:


random.random()


# In[11]:


VSV_Codons['T'].items()

