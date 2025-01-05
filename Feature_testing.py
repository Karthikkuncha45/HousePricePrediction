# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import shap
import matplotlib.pyplot as plt

# Step 1: Load and combine datasets
# Replace 'city1.csv', 'city2.csv', ... with your dataset file paths
bang_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\bangalore.csv')
chen_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\chennai.csv')
delhi_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\delhi.csv')
hyd_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\hyd.csv')
kolk_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\kolkata.csv')
mumb_df = pd.read_csv('C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project - 1\\mumbai.csv')

# Combine all datasets into one
data = pd.concat([bang_df, chen_df, delhi_df, hyd_df, kolk_df, mumb_df])

# Step 2: Preprocessing
# Replace missing values

if 'Location' in data.columns:
    data.drop(columns=['Location'], inplace=True)


data.fillna(data.median(), inplace=True)

# Encode categorical variables
data = pd.get_dummies(data, drop_first=True)

# Step 3: Separate features and target
X = data.drop('Price', axis=1)  # Features (exclude 'price')
y = data['Price']               # Target (house price)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Step 6: Calculate Feature Importance
importance = model.feature_importances_
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importance}).sort_values(by='Importance', ascending=True)

# Display the feature importance
print("Feature Importance:")
print(feature_importance)

# Step 7: Visualize Feature Importance
plt.figure(figsize=(10, 6))
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Feature Importance")
plt.gca().invert_yaxis()  # Flip the bar chart
plt.show()

# Step 8: Use SHAP for Detailed Analysis
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)    

# SHAP Summary Plot
shap.summary_plot(shap_values, X_train)

# SHAP Feature Impact
shap.summary_plot(shap_values, X_train, plot_type="bar")
