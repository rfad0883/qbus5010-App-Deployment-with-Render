from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df=pd.read_csv('B6.csv',delimiter=";")
#print(df.columns)
df['Percentage_Workload']=df['Daily_Workload']*100/df['Daily_Workload'].sum()
#print(df['Percentage_Workload'])
dfg = df.sort_values(by='Percentage_Workload',ascending=False)
dfg9 = dfg.head(9)


#print (dfg9)

df_others = dfg.drop(dfg9.index)
#df_remaining = df_others.tail()
#print(df_remaining)
#print('sisa',df_others)
total_remaining= df_others['Percentage_Workload'].sum()
combine_remaining= {'Oil_and_Gas_Company_Name':['other'],
    'Verification_per_Month':[0],
    'Daily_Workload':[0],
    'Percentage_Workload': total_remaining}


combine_remaining_df = pd.DataFrame(combine_remaining)
combine_data = pd.concat([dfg9, combine_remaining_df])
print('combine_data', combine_data)
dfsort = combine_data.sort_values(by='Percentage_Workload',ascending=True)

# dfg = df.groupby(['name']).size().to_frame().sort_values([0], ascending = False).head(10).reset_index()
#print(df['Percentage_Workload'])

def make_bar_chart():
    fig = px.bar(data_frame = dfsort, x='Percentage_Workload', y='Oil_and_Gas_Company_Name',
        orientation = 'h', color_discrete_map={'Percentage_Workload':'blue'})#,barmode='group')
    fig.update_traces(texttemplate='%{x:.2f}%', textposition = 'outside')
    #fig.update_xaxes(title_text='Percentage of Workload',title_font= dict(color='black'),tickfont=dict(color='black'))
    #fig.update_xaxes(title_text='Total 100%',title_font= dict(color='blue'),tickfont=dict(color='blue'))
    fig.update_yaxes(title_text='Oil and Gas Company')
    

    fig.update_layout()

    return fig
    
app.layout=html.Div([
    html.H1('Percentage of current on-going workload',style = {"textAlign":"center","font-size":"40px"}),
    dcc.Graph(id="horizontal_bar_graph", figure = make_bar_chart()),
    html.P('Total 100%',style = {"textAlign":"right","font-size":"15px","color":"blue","padding-right":"100px"})])

if __name__ == '__main__':
    app.run_server(debug=True)


