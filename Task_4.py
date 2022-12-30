import pandas as pd
from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt

#Merge two csv files
df = pd.concat(map(pd.read_csv, ['college_1.csv', 'college_2.csv']), ignore_index=True)

#Split that csv file into multiple categories
Reached_expectation=df[(df['CodeKata Score']>10000)&(df['CodeKata Score']<15000)]
Needs_Improvement=df[(df['CodeKata Score']>7000)&(df['CodeKata Score']<10000)]
Unsatisfactory=df[(df['CodeKata Score']<7000)]

Reached_expectation.to_csv('Reached_expectation.csv')
Needs_Improvement.to_csv('Needs_Improvement.csv')
Unsatisfactory.to_csv('Unsatisfactory.csv')

#Average of previous week geekions vs this week geekions 
df['Average_PreviousGeekionsAndCodekataScore'] = df[['Previous Geekions', 'CodeKata Score']].mean(axis=1)

#No of students participated
NumberofStudents=df['Name'].nunique()

#Average completion of python course or my_sql or python english or computational thinking
Python_Mean=df['python'].mean()
SQL_Mean=df['python'].mean()
PythonEn_Mean=df['python_en'].mean()
ComputationalThinking_Mean=df['computational_thinking'].mean()

#rising star of the week (top 3 candidate who performed well in that particular week)
df1=df.sort_values(by=('Rising'),ascending=False)
RisingStar=df1['Name'].head(3)

#Shining stars of the week (top 3 candidates who has highest geekions)
df2=df.sort_values(by=('Previous Geekions'),ascending=False)
ShiningStar=df2['Name'].head(3)

#Department wise codekata performence 
sums = df.groupby(df["Department"])["CodeKata Score"].sum()
pie(sums, labels=sums.index)
show()

#Department wise toppers
plt.bar(x=df['Department'],height=df['CodeKata Score']) 
