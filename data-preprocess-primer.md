# Hands-On Activity: Data Preprocessing
The objective of this activity is to practice data preprocessing techniques on a sample dataset.

# Steps
## Load the Dataset
```
import pandas as pd
data = pd.read_csv('sample_data.csv')
```
## Inspect the Data:
```
print(data.head())
print(data.info())
```
## Handle Missing Values:
```
data.fillna(method='ffill', inplace=True)  # Forward fill
```
## Remove Duplicates:
```
data.drop_duplicates(inplace=True)
```
## Standardize Formats:
```
data['date'] = pd.to_datetime(data['date'])
```
## Encode Categorical Variables:
```
data = pd.get_dummies(data, columns=['category'])
```
## Normalize/Standardize Data:
```
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
```
