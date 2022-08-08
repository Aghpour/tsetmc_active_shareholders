import requests
import pandas as pd

url = 'http://www.tsetmc.com/Loader.aspx?ParTree=111C1614'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers)

# read table
table_list = pd.read_html(r.text)
df = pd.DataFrame(table_list[0])
# first row as header
df = df.rename(columns=df.iloc[0])
df = df.drop(df.index[0])
# split first column
df[['آیدی نماد', 'نام نماد']] = df['نام'].str.split(',', 1, expand=True)
df = df.drop(['آیدی نماد', 'نام'], axis=1)
# reorder column's positions
df = df[['نام نماد', 'سهامدار', 'تعداد سهام', 'تغییر']]
# export to csv
df.to_csv('active_shareholders.csv', index=False, header=True)
