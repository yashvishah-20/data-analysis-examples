#creates a line chart on sample dataset
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_posted_month'] = df['job_posted_date'].dt.month
print(df['job_posted_month'])

monthly_counts=df.job_posted_month.value_counts()
monthly_counts=monthly_counts.sort_index()
print(monthly_counts)
plt.plot(monthly_counts.index,monthly_counts)
plt.show()
