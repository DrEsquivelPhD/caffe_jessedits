import numpy as np
import sys 
import pandas as pd
import matplotlib.pyplot as plt

# read in csv as data frame
data_val = pd.read_csv('val_event.csv',delimiter=' ')
data_mu  = pd.read_csv('ylength_mu_michel.csv',delimiter=' ')
data_pi  = pd.read_csv('ylength_pi.csv',delimiter=' ')

mergedmu = data_val.merge(data_mu, on=['Subrun','Event','Type'])
mergedpi = data_val.merge(data_pi, on=['Subrun','Event','Type'])

# make histogram
plt.figure();

'''
Subtracting the probability from the prediction give a probability of being a muon from 0 to 1
I tried to match the color scheme of the hist you sent me, but you can change to whatever you want :)
'''
# first plot pions
# everything in [] are the conditions for how you select rows in pandas and the data.<whatever> is the column you select in data
plt.hist(np.abs(mergedpi.Pred[mergedpi.Type == 'Pion'] - mergedpi.Prob[mergedpi.Type == 'Pion']),bins=np.linspace(0,1,20),color='red',alpha=0.6,label='Pions');
# then plot muons
plt.hist(np.abs(mergedmu.Pred[mergedmu.Type == 'Muon'] - mergedmu.Prob[mergedmu.Type == 'Muon']),bins=np.linspace(0,1,20),color='blue',alpha=0.6,label='Muons');

plt.xlabel('Probability');
plt.ylabel('Event');
plt.legend(loc='upper center',frameon=False);

# uncomment to save
plt.savefig("probhist_primary.png")
