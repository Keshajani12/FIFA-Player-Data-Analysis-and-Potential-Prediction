import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Get data from csv file
df= pd.read_csv('fifa/fifa.csv')
print(df.head())
print(df.shape)
print(df.info)
print(df.describe())


# Drop columns which are not required
df.drop(['sofifa_id','joined','player_url','preferred_foot','weak_foot'] ,axis=1 ,inplace=True)
print(df.head())

# Find data based on age 
youngAge=df[df.age <= 40]
print(youngAge.head())
print(youngAge.shape)

minor= df[df.age <18]
print(minor.head())
print(minor.shape)

oldAge =df[df.age>40]
print(oldAge.head())
print(oldAge.shape)

# Find data based on nationality
nationality = df[df.nationality =='Argentina']
print(nationality.head())
print(nationality.shape)

nationalityFrance = df[df.nationality =='France']
print(nationalityFrance.head())
print(nationalityFrance.shape)
print(nationalityFrance.sort_values(by='wage_eur',ascending=False).head())

nationalityNetherlands = df[df.nationality == 'Netherlands']
print(nationalityNetherlands.head())
print(nationalityNetherlands.shape)

nationalityGermany = df[df.nationality == 'Germany']
print(nationalityGermany.head())
print(nationalityGermany.shape)

print(df.value_counts('nationality'))

#  Create Countplot using Seaborn
sns.countplot(data=df,x='age')
plt.show()

#  Create Barplot using Seaborn
sns.barplot(data=oldAge,x='short_name',y='wage_eur')
plt.show()

#  Sorting values based on shooting
shooting= df[['shooting','short_name']]
print(shooting.sort_values(by=['shooting'],ascending=False).head())

shooting1=df.sort_values(by=['shooting'],ascending=False)
fig=plt.figure(figsize=(10,15))
plt.title('Top 10 Best Shooting Players')
ax= sns.barplot(data=shooting1.iloc[:10],x='short_name',y='shooting',edgecolor='black',linewidth = 2)
plt.show()

#  Create Lineplot using Seaborn
sns.lineplot(data=nationalityNetherlands,x='age',y='league_rank',errorbar=None)
plt.show()

# Split data into X (age) and y (potential)
x= df[['age']]
y= df['potential']
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.3)
print(x_train.head())
print(x_test.head())

lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict = lr.predict(x_test)
print(y_test.head())
print(y_predict[:5])

# Find mean value using prediction and test value
mse=mean_squared_error(y_test,y_predict)
print(mse)

# Create a DataFrame to hold the actual and predicted Potential data
record = pd.DataFrame({
 'Actual Potential': y_test,
'Predicted Potential': y_predict
})

# Create a line plot using Seaborn
sns.lineplot(data=record)
plt.show()

