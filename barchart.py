#horizontal bar graph
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
job_counts=df.job_title_short.value_counts()
plt.barh(job_counts.index,job_counts)
plt.show()
