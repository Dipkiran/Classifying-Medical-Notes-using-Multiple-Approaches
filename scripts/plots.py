import os
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 16

class PlotReport():
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
    
    def get_confusion_matrix(self, pred_arg=False, test_arg=False):
        y_pred = self.model.predict(self.X_test)
        if pred_arg:
            y_pred = np.argmax(y_pred, axis=1)
        if test_arg:
            self.y_test = np.argmax(self.y_test, axis=1)
        self.cm = confusion_matrix(self.y_test, y_pred)
        print("\nClassification Report:")
        print(classification_report(self.y_test, y_pred))

    def print_confusion_matrix(self, fileName):
        self.get_labels()
        disp = ConfusionMatrixDisplay(confusion_matrix=self.cm, display_labels=self.df_labels['name'].values)
        disp.plot(cmap="Blues", xticks_rotation=45)
        plt.savefig(os.path.join("plots", fileName), bbox_inches='tight')
        plt.show()

    def get_labels(self):
        self.df_labels = pd.read_csv("data/medical_tc_labels.csv")
        self.df_labels.loc[self.df_labels['condition_label'] == 5, 'condition_label'] = 0
        self.df_labels['name'] = self.df_labels['condition_name'].str.split(n=1, expand=True)[0]
        self.df_labels = self.df_labels.sort_values(by='condition_label')
