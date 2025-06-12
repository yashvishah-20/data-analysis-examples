#this is a scatterd diagram
import ast
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
df=df[df['job_title_short']=='Data Analyst']
df_exploded=df.explode('job_skills')
skill_status=df_exploded.groupby('job_skills').agg(
	median_salary=('salary_year_avg','median'),
	skill_count=('job_skills','count'),
	)
skill_status=skill_status.sort_values(by='skill_count',ascending=False).head(10)
skill_status.plot(kind='scatter',x='skill_count',y='median_salary')
for i, txt in enumerate(skill_status.index):
    plt.text(skill_status['skill_count'].iloc[i], skill_status['median_salary'].iloc[i], txt)
plt.xlabel('Count of Job Postings')
plt.ylabel('Median Yearly Salary')
plt.title('Salary vs. Count of Top Skills in Data Analyst Jobs')
plt.tight_layout()
plt.show()
