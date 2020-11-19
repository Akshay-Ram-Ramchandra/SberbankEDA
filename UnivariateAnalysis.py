import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

# reading the dataframe
df = pd.read_csv('train.csv')

#creating univariate analysis function
def UniVariateAnalysis(vari):
