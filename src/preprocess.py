import pandas as pd

# Load dataset

dataset_path = "../dataset/raw/irrigation_prediction"



df = pd.read_csv(dataset_path)

df.head()