import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from show_confusion_matrix import show_confusion_matrix

C = np.matrix('908,167;361,714')
show_confusion_matrix(C, ['Muon', 'Pion'])
