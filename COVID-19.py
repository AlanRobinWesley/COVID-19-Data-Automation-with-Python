import plotly
import plotly.graph_objects as go
import pandas as pd

excel_file_1 = 'Data.xlsx'
df = pd.read_excel(excel_file_1)
print(df)

data = [go.Scatter( x=df['COUNTRY AND TERRITORY'], y=df['CASES'])]

fig = go.Figure(data)
fig.show()
