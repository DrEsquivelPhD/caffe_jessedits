import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt

#read in csv as data frame

data_val = pd.read_csv('val_event.csv',delimiter=' ')
data_mu  = pd.read_csv('ylength_mu.csv',delimiter=' ')
data_pi  = pd.read_csv('ylength_pi.csv',delimiter=' ')

mergedmu = data_val.merge(data_mu, on=['Subrun','Event','Type'])
mergedpi = data_val.merge(data_pi, on=['Subrun','Event','Type'])

mergedmu.to_csv('mergedmu.csv', delimiter = ' ')
mergedpi.to_csv('mergedpi.csv', delimiter = ' ')

mergedmu = mergedmu.sort('Eng')
mergedpi = mergedpi.sort('Eng')

binsmu = np.linspace(mergedmu.Eng.min(),mergedmu.Eng.max(),10)
groupsmu = mergedmu.groupby(pd.cut(mergedmu.Eng,binsmu))
meanmu = np.abs(groupsmu.mean().Pred -groupsmu.mean().Prob)
meanmu_Eng = groupsmu.mean().Eng

binspi = np.linspace(mergedpi.Eng.min(),mergedpi.Eng.max(),10)
groupspi = mergedpi.groupby(pd.cut(mergedpi.Eng,binspi))
meanpi = np.abs(groupspi.mean().Pred -groupspi.mean().Prob)
meanpi_Eng = groupspi.mean().Eng

# make histogram
plt.figure();
print meanmu ,np.abs(groupsmu.Pred.std()-groupsmu.Prob.std()) 
print meanpi ,np.abs(groupspi.Pred.std()-groupspi.Prob.std())
'''
Subtracting the probability from the prediction give a probability of being a muon from 0 to 1
I tried to match the color scheme of the hist you sent me, but you can change to whatever you want :)
'''
# first plot pions
# everything in [] are the conditions for how you select rows in pandas and the data.<whatever> is the column you select in data
#plt.plot(np.array(mergedpi.length), np.array(np.abs(mergedpi.Pred[mergedpi.Type == 'Pion'] - mergedpi.Prob[mergedpi.Type == 'Pion'])),marker='o')
# then plot muons
#plt.plot(np.array(mergedmu.length), np.array(np.abs(mergedmu.Pred[mergedmu.Type == 'Muon'] - mergedmu.Prob[mergedmu.Type == 'Muon'])),marker='o')
#plt.errorbar(meanmu_length,meanmu,fmt='o',yerr=np.abs(groupsmu.Pred.std()-groupsmu.Prob.std()))
#plt.errorbar(meanpi_length,meanpi,fmt='o',yerr=np.abs(groupspi.Pred.std()-groupspi.Prob.std()))

plt.plot(np.array(meanmu_Eng), meanmu)#,bins=np.linspace(0,1,20),color='red',alpha=0.6,label='Muons');
plt.plot(np.array(meanpi_Eng), meanpi)#,bins=np.linspace(0,1,20),color='red',alpha=0.6,label='Muons');

#plt.np.histogram2d(mergedpi.length, np.abs(mergedpi.Pred[mergedpi.Type == 'Pion'] - mergedpi.Prob[mergedpi.Type == 'Pion']),color='red',alpha=0.6,label='Pions');
#plt.hist(mergedpi.length, np.abs(mergedpi.Pred[mergedpi.Type == 'Pion'] - mergedpi.Prob[mergedpi.Type == 'Pion']),bins=np.linspace(0,1,20),color='red',alpha=0.6,label='Pions');



plt.xlabel('Eng');
plt.ylabel('Probability');
plt.legend(loc='upper center',frameon=False);

# uncomment to save
plt.savefig("acc_eng_nomichel.pdf")
