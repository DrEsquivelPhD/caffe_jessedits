import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from show_confusion_matrix import show_confusion_matrix

#C = np.matrix('908,167;361,714')
#C = np.matrix('4407,593;828,4172')
#C = np.matrix('4600,400;973,4027')
C = np.matrix('4627,373;863,4037')
show_confusion_matrix(C, ['Muon', 'Pion'])
