import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('tips.csv')
df = pd.DataFrame(data)

sel1 = df[df['total_bill'] > 20]
print(sel1)

sel2 = df.query("sex == 'Female'")
print(sel2)

sel3 = df.query("day=='Sun' and time =='Dinner'")
print(sel3)

sel4 = df[(df['tip']>5) & (df['size'].isin([3,4]))]
print(sel4)

sel5 = df[['total_bill','tip','size']]
print(sel5)