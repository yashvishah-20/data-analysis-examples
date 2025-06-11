import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
job_counts=df.job_title_short.value_counts()
plt.bar(job_counts.index,job_counts)
plt.ylabel('Count of job postings')
plt.title('Postings by Job Title')
plt.xticks(rotation=45,ha='right')
plt.show()
