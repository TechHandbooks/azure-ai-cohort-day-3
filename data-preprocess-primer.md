# Hands-On Activity: Data Preprocessing
The objective of this activity is to practice data preprocessing techniques on a sample dataset.

# Table of Contents
 - [Steps](#steps)
   - [1. Load the Dataset](#1-load-the-dataset)
   - [2. Inspect the Data](#2-inspect-the-data)
   - [3. Handle Missing Values](#3-handle-missing-values)
   - [4. Remove Duplicates](#4-remove-duplicates)
   - [5. Standardize Formats](#5-standardize-formats)
   - [6. Encode Categorical variables](#6-encode-categorical-variables)
   - [7. Normalize/Standardize Data](#7-normalizestandardize-data)
 - [Full Code Example](#full-code-example)
   
# Steps
## 1. Load the Dataset
```
import pandas as pd
data = pd.read_csv('sample_data.csv')
```

## 2. Inspect the Data
```
print(data.head())
print(data.info())
```

## 3. Handle Missing Values
```
data.fillna(method='ffill', inplace=True)  # Forward fill
```

## 4. Remove Duplicates
```
data.drop_duplicates(inplace=True)
```

## 5. Standardize Formats
```
data['date'] = pd.to_datetime(data['date'])
```

## 6. Encode Categorical Variables
```
data = pd.get_dummies(data, columns=['category'])
```

## 7. Normalize/Standardize Data
```
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
```

# Full Code Example 
Here’s the complete code for reference:
```
import pandas as pd
data = pd.read_csv('sample_data.csv')
print(data.head())
print(data.info())
data.fillna(method='ffill', inplace=True)  # Forward fill
data.drop_duplicates(inplace=True)
data['date'] = pd.to_datetime(data['date'])
data = pd.get_dummies(data, columns=['category'])
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
```
