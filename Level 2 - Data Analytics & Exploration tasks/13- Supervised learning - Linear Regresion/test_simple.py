from sklearn.datasets import load_diabetes
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = load_diabetes(as_frame=True).data[['s1','s2']]

# Plot data
plt.figure()
sns.scatterplot(data=df, x='s1', y='s2')
plt.show()
plt.close()

# To create our modelwe import LinearRegression
from sklearn.linear_model import LinearRegression

# To allow compatibility, we must ensure that our model 
# input are in the shape (n_samples,n_features)

X = df['s1'].values.reshape(-1,1) # create a 2D array
y = df['s2'].values

# Fit and predict
simple_model = LinearRegression()
simple_model.fit(X,y)
y_pred = simple_model.predict(X)

# Plot model and data
plt.figure()
sns.scatterplot(data=df, x='s1', y='s2')
plt.plot(X, y_pred)
plt.show()
plt.close()