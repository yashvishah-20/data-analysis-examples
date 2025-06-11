import pandas as pd

df = pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")

df['job_posted_date']=pd.to_datetime(df.job_posted_date)
print(df.describe())
print(df.count())
print(df['salary_year_avg'].median())
print(df['salary_year_avg'].min())#gives minimum salary ie 15000 that is too less so we will investigate it
min_salary=df['salary_year_avg'].idxmin()#stores the data of employee with minimum salary
print(df.iloc[min_salary])#prints it and the employee is from poland and with help of AI we get to know that 15000 is the maximum salary in that country
print(df['job_title_short'].unique())#stores the job_title in an array
print(df['job_title_short'].value_counts())#give unique counts of job
print(df.groupby('job_title_short')['salary_year_avg'].mean())#If we want to find the average yearly salary by job_title_short.
print(df.groupby('job_title_short')['salary_year_avg'].agg(['min', 'max']))#gives minimum and maximum values for every job_title_short
