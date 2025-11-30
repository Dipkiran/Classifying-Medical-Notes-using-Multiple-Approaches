import pandas as pd

class ImportDataset():
    def __init__(self):
        self.df_train = pd.read_csv("data/medical_tc_train.csv")
        self.df_test = pd.read_csv("data/medical_tc_test.csv")

    def read_dataset(self):
        self.modify_labels()
        self.df = pd.concat([self.df_train, self.df_test], ignore_index=True)
        return self.df
    
    def modify_labels(self):
        self.df_train.loc[self.df_train['condition_label'] == 5, 'condition_label'] = 0.0
        self.df_test.loc[self.df_test['condition_label'] == 5, 'condition_label'] = 0.0