import pandas as pd
import matplotlib.pyplot as plt


data_path = '일별평균대기오염도_2022.csv'

df = pd.read_csv(data_path, encoding="cp949")

df = df[['측정일시','측정소명','미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

df = df.dropna()

df['측정일시'] = pd.to_datetime(df['측정일시'],format='%Y%m%d')

print(df.head(20))

df_monthly = df.resample('M',on='측정일시').mean(numeric_only=True)

plt.plot(df_monthly.index.month,df_monthly['미세먼지농도(㎍/㎥)'],label='PM10')

