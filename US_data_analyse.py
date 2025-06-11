#analyses the date from database for the country US
import pandas as pd

df = pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
us_jobs = df[df['job_country'] == 'United States']
us_jobs.groupby('job_title_short')['salary_year_avg'].mean()
us_jobs.groupby('job_title_short')['salary_year_avg'].mean().sort_values(ascending=False)
us_jobs.groupby('job_title_short').size().sort_values(ascending=False)
us_jobs.groupby('job_title_short')['salary_year_avg'].agg(['median', 'min', 'max', 'count']).sort_values(by='median', ascending=False)
