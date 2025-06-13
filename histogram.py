import ast
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
df_US=df[(df['job_title_short']=='Data Analyst')&(df['job_country']=='United States')].copy()
df_US = df_US.dropna(subset=['salary_year_avg'])
df_US['salary_year_avg'].plot(kind='hist',bins=30,edgecolor='black')
plt.title('Distribution of United States Data Analyst Yearly Salaries')
plt.xlabel('Yearly Salary')
plt.ylabel('Number of Jobs')
plt.show()
