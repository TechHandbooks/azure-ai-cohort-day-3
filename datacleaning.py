import pandas as pd

# Load the dataset
data = pd.read_csv('titanic.csv')

# Explore the data
print(data.head())
print(data.info())

# Fill missing Age values with median
data['Age'] = data['Age'].fillna(data['Age'].median())

# Drop rows with missing Embarked values
data = data.dropna(subset=['Embarked'])
data = data.drop_duplicates()

# Convert 'Sex' to numerical values
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data[['Age', 'Fare']] = scaler.fit_transform(data[['Age', 'Fare']])

# Create 'FamilySize' as a new feature
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
from sklearn.model_selection import train_test_split

X = data[['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize']]
y = data['Survived']  # Assuming Titanic dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
