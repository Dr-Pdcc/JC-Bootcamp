import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import os
print(os.getcwd())

# Prepare the data
x = np.linspace(0, 100, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)

# Create a title
plt.title("My first matplotlin sine graph")

# Show the plot
plt.show()

# ==== Stacked area charts ==== #
# Generate random data
groupOne = np.random.randint(1, 10, 10)
groupTwo = np.random.randint(1, 10, 10)
groupThree = np.random.randint(1, 10, 10)

# Create the stacked area
y = np.row_stack((groupOne, groupTwo, groupThree))
x = np.arange(10)
y1, y2, y3 = (groupOne, groupTwo, groupThree)

fig, ax = plt.subplots()
ax. stackplot(x, y)

# Labels
plt.title("Stacked area chart example")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

# ==== Seaborn ==== #
#Load data 
ins_df = pd.read_csv('C:/Users/jorot/OneDrive/Escritorio/HyperionDev Data Science/Level 2 - Data Analytics & Exploration tasks/8- Data Visualisation - Python libraries/Advanced/insurance.csv')

# Plot scatterplot
'''
In matplotlib, the scatter() method would be most appropriate.
'''
plt.figure()
plt.scatter(ins_df['age'], ins_df['charges'])
plt.xlabel("age")
plt.ylabel("charges")
plt.show()
plt.close()

# Plot lineplot
plt.figure()
sns.lineplot(x='age', y='charges', data=ins_df)
plt.show()
plt.savefig('sns_lineplot.png')  # save as a png image file
plt.close()

# ==== Multi-plot grids ==== #
#Load data
titanic_df = pd.read_csv('C:/Users/jorot/OneDrive/Escritorio/HyperionDev Data Science/Level 2 - Data Analytics & Exploration tasks/8- Data Visualisation - Python libraries/Advanced/Titanic.csv')


# Plot FacetGrid plot
plt.figure()
fg = sns.FacetGrid(titanic_df, row="Sex", col="Pclass", hue="Survived",
                   margin_titles=True)
fg.map(sns.scatterplot, "Age", "Fare")
fg.add_legend()
plt.show()
plt.close()

# ==== Correlation Heatmaps ==== #
# Select columns of interest
age_bmi_charges = ins_df[['age', 'bmi', 'charges']]

# Plot correlation matrix
plt.figure()
corr_coeff_mat = age_bmi_charges.corr()
sns.heatmap(corr_coeff_mat, annot=True)
plt.show()
plt.close()