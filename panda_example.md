#this is a simple example of third party library called pandas in which we are calculating sume of amount spent from  a csv data
import pandas as pd
df = pd.read_csv(r"C:\Users\Yashvi\Downloads\sales_data.csv")
print(df)
total_amount = df['amount_spent'].sum()
print('total:',total_amount)
