#it shows realtion between all the jobs and their median salaries in form of horizontal bar graph
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
job_salary=df.groupby('job_title_short')['salary_year_avg'].median().sort_values()
print(job_salary)
job_salary.plot(kind='barh')
plt.ylabel('job_titles')
plt.xlabel('salary($USD)')
plt.title('Median Salary by Job Title')
plt.show()
