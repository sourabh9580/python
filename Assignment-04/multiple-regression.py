from sklearn import linear_model
import pandas as pd

# Read data from csv file
df = pd.read_csv('petrol_consumption.csv')

# Get x and y values
x = df[['Petrol_tax','Average_income','Paved_Highways','Population_Driver_licence(%)']].values
y = df['Petrol_Consumption'].values

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x, y)

# Predict petrol consumption for a petrol tax of 9.0, an average income of 3571, a number of paved highways of 1976, and a population of 0.525 for driver's license holders
print("Predicted Petrol Consumption: ",regr.predict([[9.0, 3571, 1976, 0.525]]))

# Apply linear regression to find the intercept
print("Intercept: ",regr.intercept_)