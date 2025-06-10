#this is a simple example of numpy module
import numpy as np
job_titles=np.array(['Software Engineer', 'Data Analyst', 'Product Manager', 'HR Executive', 'Marketing Specialist','AI Engineer'])
base_salary = np.array([85000, 60000, 95000, 50000, 58000,np.nan])
bonus_rate = np.array([0.10, 0.07, 0.12, 0.05, 0.08,np.nan])

total_salaries=base_salary*(1+bonus_rate)
print(total_salaries)
mean_salary=np.nanmean(total_salaries)
print(mean_salary)