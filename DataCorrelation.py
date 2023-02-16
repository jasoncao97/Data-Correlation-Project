import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

df = pd.read_csv('./movies.csv')


# Cleaning Data

df = df.dropna()


# Change Data Type of Columns 

df['budget'] = df['budget'].astype('Int64')

df['gross'] = df['gross'].astype('Int64')


# Create correct year column 

df['released'] = df['released'].astype(str)
results = []

for rel in df.released:
    if rel == 'nan':
        results.append('nan')
    else:
        date = rel.split(' ')
        if date[0].isnumeric():
            results.append(date[0])
        elif date[1].isnumeric():
            results.append(date[1])
        else:
            results.append(date[2])
    

df['yearcorrect'] = results
df['yearcorrect'] = df['yearcorrect'].astype(int)


# Order by Gross Revenue

# print(df.sort_values(by=['gross'], inplace=False, ascending=False))
 

# Export to Excel

excel = pd.ExcelWriter('movies_postpy.xlsx')
df.to_excel(excel, index=False)
excel.save()



# DATA CORRELATION SECTION


# Scatter Plot (refer to image1)

plt.scatter(x=df['budget'],y=df['gross'])
plt.title('Gross Earnings vs Budget')
plt.ylabel('Gross Earnings')
plt.xlabel('Budget for Film')

plt.show()
image1.png

# Regression Plot (refer to image2)

sns.regplot(x=df['budget'].astype(int),y= df['gross'].astype(int), line_kws= {'color':'blue'})
plt.show()


# Correlation - Heat Map (refer to image3)

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix For Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.show()


# Assigning Numeric Value for Each Unique Categorical Value (refer to image4)

df_numerized = df

for col in df_numerized.columns:
    if (df_numerized[col].dtype == 'object'):
        df_numerized[col] = df_numerized[col].astype('category')
        df_numerized[col] = df_numerized[col].cat.codes

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix For Movies')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.show()

# Looking at Pairs With a High Correlation (> 0.5) (refer to image5)

correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()

sorted_pairs = corr_pairs.sort_values()
high_corr = sorted_pairs[(sorted_pairs > 0.5)]
print(high_corr)
