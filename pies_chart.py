import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Yashvi\Downloads\data_jobs.csv")
df_plot=df['job_title_short'].value_counts()
df_plot.plot(kind='pie',autopct='%.1f')
plt.title('Work from Home Status')
plt.ylabel('')
plt.show()
