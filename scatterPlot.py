import csv
import pandas as pd
import plotly.express as px
df=pd.read_csv('Coffee.csv')
fig=px.scatter(df,x='Coffee in ml',y='sleep in hours')
fig.show()
