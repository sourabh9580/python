import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Read data from csv file
df = pd.read_csv('breain_weight.csv',index_col=0)

# Get x and y values
x = df['Brain Weight'].values
y = df['Body Weight'].values

# Calculate slope and intercept
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed.
def myfunc(x):
    return slope * x + intercept

# Use the map function to apply the myfunc function to each value in x
mymodel = list(map(myfunc, x))

# Plot the original scatter plot
plt.scatter(x, y)

# Plot the regression line
plt.plot(x, mymodel)

# Show the graph
plt.show()

# Predict body weight for a brain weight of 15 grams
print("Predicted body weight: ",myfunc(15))
