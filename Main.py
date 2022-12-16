import os

from py4j.java_gateway import JavaGateway
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from tkinter.filedialog import askdirectory

print("Please choose the directory to a java project for analyis")
path = askdirectory(title='Select Folder')
print(path)
LM_training_array = np.genfromtxt('DataSets\\Long_Method_code_metrics_values.csv', delimiter=',',
                               usecols=(5, 7, 22), skip_header=True)
LM_training_names = np.genfromtxt('DataSets\\Long_Method_code_metrics_values.csv', delimiter=',',
                               usecols=(1), dtype=None, encoding=None, skip_header=True)
# God_Class_code_metrics_values
GC_training_array = np.genfromtxt('DataSets\\God_Class_code_metrics_values.csv', delimiter=',',
                               usecols=(48, 7, 9,19, 44), skip_header=True)
GC_training_names = np.genfromtxt('DataSets\\God_Class_code_metrics_values.csv', delimiter=',',
                               usecols=(1), dtype=None, encoding=None, skip_header=True)
gateway = JavaGateway()  # connect to the JVM
random = gateway.jvm.java.util.Random()  # create a java.util.Random instance
addition_app = gateway.entry_point  # get the AdditionApplication instance
value = addition_app.addition(path, 'False', '0',
                              'True',
                              'bin\\sample')  # call the addition method
LM_df = pd.read_csv("bin\\samplemethod.csv")
LM_df = LM_df[['file', 'class', 'method', 'wmc', 'loc', 'maxNestedBlocksQty']]
GC_df = pd.read_csv("bin\\sampleclass.csv")
GC_df = GC_df[['file', 'class','wmc','tcc','totalMethodsQty','totalFieldsQty','loc']]
LM_testing_array = LM_df[['wmc', 'loc', 'maxNestedBlocksQty']]
LM_testing_array = LM_testing_array.to_numpy()
GC_testing_array = GC_df[['wmc','tcc','totalMethodsQty','totalFieldsQty','loc']]
GC_testing_array =GC_testing_array.fillna(0.0)
GC_testing_array = GC_testing_array.to_numpy()
LM_predicted_metrics = []
LM_predicted_values = []
LM_predicted_index = []
GC_predicted_metrics = []
GC_predicted_values = []
GC_predicted_index = []
LM_euc_dist = []
GC_euc_dist = []
print(GC_training_array)
for row in LM_testing_array:
    LM_result = euclidean_distances(LM_training_array, [row])
    LM_predicted_index.append(np.argmin(LM_result))
    LM_predicted_metrics.append(LM_training_array[np.argmin(LM_result)])
    LM_euc_dist.append(LM_result[np.argmin(LM_result)])
    LM_predicted_values.append(LM_training_names[np.argmin(LM_result)])


for row in GC_testing_array:
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(row)
    GC_result = euclidean_distances(GC_training_array, [row])
    GC_predicted_index.append(np.argmin(GC_result))
    GC_predicted_metrics.append(GC_training_array[np.argmin(GC_result)])
    GC_euc_dist.append(GC_result[np.argmin(GC_result)])
    GC_predicted_values.append(GC_training_names[np.argmin(GC_result)])

LM_df['Predicted_Values'] = LM_predicted_values
LM_df['Predicted_Index'] = LM_predicted_index
LM_df['Predicted_Metrics'] = LM_predicted_metrics
LM_df['Euclidean_dist'] = LM_euc_dist
LM_df = LM_df[['file', 'class', 'method', 'Predicted_Values', 'Predicted_Index', 'wmc', 'loc', 'maxNestedBlocksQty',
              'Predicted_Metrics', 'Euclidean_dist']]

GC_df['Predicted_Values'] = GC_predicted_values
GC_df['Predicted_Index'] = GC_predicted_index
GC_df['Predicted_Metrics'] = GC_predicted_metrics
GC_df['Euclidean_dist'] = GC_euc_dist
GC_df = GC_df[['file', 'class', 'Predicted_Values', 'Predicted_Index','wmc','tcc','totalMethodsQty','totalFieldsQty','loc',
              'Predicted_Metrics', 'Euclidean_dist']]
# finaldf = finaldf['Predicted_Values' != 'none']
LM_df.to_csv('Results\\LM-'+os.path.basename(os.path.normpath(path))+'.csv')
GC_df.to_csv('Results\\GC-'+os.path.basename(os.path.normpath(path))+'.csv')
