import pandas as pd

df = pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")

df['job_posted_date']=pd.to_datetime(df.job_posted_date)#converting string to datetime
df['job_posted_month']=df.job_posted_date.dt.month#making a new column for month
df.sort_values(by='job_posted_date', ascending=False, inplace=True)#sorting the date on the basisi of job_post_date
df.drop(labels='salary_hour_avg',axis=1,inplace=True)#deleting the column salary_hour_average because it has no data
df.dropna(subset=['salary_year_avg'],inplace=True)#deleting all the rows that has Na value in salary_year_avg
print(df)
print(df.info())
df.to_csv('cleaned.csv')#exporting it in csv format
