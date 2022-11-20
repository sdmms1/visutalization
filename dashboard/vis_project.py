# -*- coding: utf-8 -*-
"""vis_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8Gjjrokl99__Z0I3Q-QYJdI6HvSJyCU
"""

!pip install plotly_express



!pip install dash_bootstrap_components

import plotly_express as px
import pandas as pd
import plotly.graph_objs as go

d = pd.read_csv("total_sale_province_new (2).csv")
d.head(10)

d.dropna(axis='index',how='any',inplace=True)
d.head(10)

import operator
years=['2019','2020','2021','2022']
df=d[d['Province']=='Beijing']
for y in years:
    df_CB=df[df['Building Type'].isin(['Commercialized Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_CRB=df[df['Building Type'].isin(['Commercialized Residential Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_OB=df[df['Building Type'].isin(['Office Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_HBU=df[df['Building Type'].isin(['Houses for Business Use Sold'])&df['Date'].str.contains('|'.join(years))] 
df_CB

def paint_fig_ts(years=['2019','2020','2021','2022'],province='Beijing'):
  df=d[d['Province']==province]
  for y in years:
    df_CB=df[df['Building Type'].isin(['Commercialized Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_CRB=df[df['Building Type'].isin(['Commercialized Residential Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_OB=df[df['Building Type'].isin(['Office Buildings Sold'])&df['Date'].str.contains('|'.join(years))]
    df_HBU=df[df['Building Type'].isin(['Houses for Business Use Sold'])&df['Date'].str.contains('|'.join(years))] 

  #"#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe"
  colors={'Commercialized Buildings Sold':'#fd7f6f',
          'Commercialized Residential Buildings Sold':'#7eb0d5',
          'Office Buildings Sold':'#b2e061',
          'Houses for Business Use Sold':'#bd7ebe'}

  hover_text_CB=[]
  for index, row in df_CB.iterrows():
      hover_text_CB.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Total_Sale}(100 million yuan)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Total_Sale=row['Total Sale (100 million yuan)']

              ))
  hover_text_CRB=[]
  for index, row in df_CRB.iterrows():
      hover_text_CRB.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Total_Sale}(100 million yuan)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Total_Sale=row['Total Sale (100 million yuan)']

              ))
  hover_text_OB=[]
  for index, row in df_OB.iterrows():
      hover_text_OB.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Total_Sale}(100 million yuan)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Total_Sale=row['Total Sale (100 million yuan)']

              ))
  hover_text_HBU=[]
  for index, row in df_HBU.iterrows():
      hover_text_HBU.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Total_Sale}(100 million yuan)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Total_Sale=row['Total Sale (100 million yuan)']

              ))
      
  trace_ts_1=go.Scatter(x=df_CB["Date"],y=df_CB["Total Sale (100 million yuan)"],name="Commercialized Buildings",text=hover_text_CB,hoverinfo="text",mode="lines",marker_color='#fd7f6f')
  trace_ts_2=go.Scatter(x=df_CRB["Date"],y=df_CRB["Total Sale (100 million yuan)"],name="Commercialized Residential Buildings",mode="lines",text=hover_text_CRB,hoverinfo="text",marker_color='#7eb0d5')
  trace_ts_3=go.Scatter(x=df_OB["Date"],y=df_OB["Total Sale (100 million yuan)"],name="Office Buildings",mode="lines",text=hover_text_OB,hoverinfo="text",marker_color='#b2e061')
  trace_ts_4=go.Scatter(x=df_HBU["Date"],y=df_HBU["Total Sale (100 million yuan)"],name="Houses for Business Use",mode="lines",text=hover_text_HBU,hoverinfo="text",marker_color='#bd7ebe')

  trace_ts=[trace_ts_1,trace_ts_2,trace_ts_3,trace_ts_4]
  layout = go.Layout(
      
      barmode='stack',

      
      #title_text="Total Sales of Different Buildings per Month",
      #title_font_color='#425066'
  )
  fig_ts=go.Figure(data=trace_ts,layout=layout)
  return fig_ts


paint_fig_ts().show()

d_f = pd.read_csv("floor_space_province_new.csv")
d_f.head(10)

d_f.dropna(axis='index',how='any',inplace=True)
d_f.head(200)

List=['2019','2020']
d_f[d_f['Province']=='Beijing']

def paint_fig_fs(years=['2019','2020','2021','2022'],province='Country'):
  df_f=d_f[d_f['Province']==province]
  for y in years:
    df_CB_F=df_f[df_f['Building Type'].isin(['Commercialized Buildings Sold'])&df_f['Date'].str.contains('|'.join(years))]
    df_CRB_F=df_f[df_f['Building Type'].isin(['Commercialized Residential Buildings Sold','Commercialized Residential'])&df_f['Date'].str.contains('|'.join(years))]
    df_OB_F=df_f[df_f['Building Type'].isin(['Office Buildings'])&df_f['Date'].str.contains('|'.join(years))]
    df_HBU_F=df_f[df_f['Building Type'].isin(['Houses for Business Use'])&df_f['Date'].str.contains('|'.join(years))] 
  hover_text_CB_F=[]
  for index, row in df_CB_F.iterrows():
      hover_text_CB_F.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Floor_space}(10000 sq.m)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Floor_space=row['Floor Space Completed (10000 sq.m)']
              ))
  hover_text_CRB_F=[]
  for index, row in df_CRB_F.iterrows():
      hover_text_CRB_F.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Floor_space}(10000 sq.m)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Floor_space=row['Floor Space Completed (10000 sq.m)']

              ))
  hover_text_OB_F=[]
  for index, row in df_OB_F.iterrows():
      hover_text_OB_F.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Floor_space}(10000 sq.m)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Floor_space=row['Floor Space Completed (10000 sq.m)']

              ))
  hover_text_HBU_F=[]
  for index, row in df_HBU_F.iterrows():
      hover_text_HBU_F.append(('<b>{BuildingType}</b><br>'+
              '{Date}<br>'+
              '{Floor_space}(10000 sq.m)').format(
                  Date=row['Date'],
                  BuildingType=row['Building Type'],
                  Floor_space=row['Floor Space Completed (10000 sq.m)']

              ))
      
  trace_fs_1=go.Bar(x=df_CB_F["Date"],y=df_CB_F["Floor Space Completed (10000 sq.m)"],name="Commercialized Buildings Sold",hovertext=hover_text_CB_F,marker_color='#fd7f6f')
  trace_fs_2=go.Bar(x=df_CRB_F["Date"],y=df_CRB_F["Floor Space Completed (10000 sq.m)"],name="Commercialized Residential Buildings",hovertext=hover_text_CRB_F,text=[],hoverinfo="text",marker_color='#7eb0d5')
  trace_fs_3=go.Bar(x=df_OB_F["Date"],y=df_OB_F["Floor Space Completed (10000 sq.m)"],name="Office Buildings",hovertext=hover_text_OB_F,text=[],hoverinfo="text",marker_color='#b2e061')
  trace_fs_4=go.Bar(x=df_HBU_F["Date"],y=df_HBU_F["Floor Space Completed (10000 sq.m)"],name="Houses for Business Use",hovertext=hover_text_HBU_F,text=[],hoverinfo="text",marker_color='#bd7ebe')

  trace_fs=[trace_fs_1,trace_fs_2,trace_fs_3,trace_fs_4]
  layout = go.Layout(
      
      barmode='stack',
      
      #title_text="Floor Space Completed of Different Buildings per Month",
      #title_font_color="#425066"
      legend=dict(
      orientation="h",
      yanchor="bottom",
      y=1.02,
      xanchor="center",
      x=0.5,
      title_text=''
  )

      
  )
  fig_fs=go.Figure(data=trace_fs,layout=layout)
  return fig_fs
paint_fig_fs(['2020']).show()





def get_month_data(month='2022/08',province='Tianjin'):
  df_f=d_f[d_f['Province']==province]
  return df_f[df_f['Date'].str.contains(month)]

get_month_data('2022/03')

colors=[
        '#B0C4DE',
          '#B0C4DE',
          '#B0C4DE']
parent = ["", "",""]
layout_tree=go.Layout(
      
      title_text="Ratio of Floor Space Completed to Floor<br>Space Sold of Different Buildings per Month",
      title_font_color="#425066",
  
      ) 



  
def paint_figtreemap():
  hover_text=[]

  for index, row in get_month_data().iterrows():
        hover_text.append(('Month:{}<br>'+
                
                'Proportion:<b>{:.2%}</b>').format(
                    row['Date'],
                    
                    row['Proportion']

                ))
  trace_init=go.Treemap(  
        labels = get_month_data()['Building Type'],
        parents = parent,
        values = get_month_data()['Proportion'],
        marker_colors = colors,
        
        text=hover_text,
        hoverinfo="text"
    ) 

      
  figtreemap = go.Figure(data=trace_init,layout=layout_tree)
  return figtreemap




paint_figtreemap().show()

!pip install dash
!pip install jupyter_dash

#这个单元是查看一下fig_fs的hoverdata是什么样子

# from dash import dcc, html
# import pandas as pd
# from jupyter_dash import JupyterDash
# from dash.dependencies import Input, Output
# import json
# import copy 

# # prepare the data
# app = JupyterDash()
# app.layout = html.Div(
    
#     # add the bar chart to the layout
#     [dcc.Graph(
#         id='fig_fs',
#         figure=paint_fig_fs(['2019','Beijing'])
#     ),html.Div(id="output")]
# )

# @app.callback(Output("output", "children"), Input("fig_fs", "hoverData"))
# def display_hover_data(hoverData):
#     return json.dumps(hoverData, indent=2)

# app.run_server()

import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output
from dash import html
import pandas as pd
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import copy
import re


year_list=['2019','2020','2021','2022']
provinces=['Country','Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'Inner Mongolia', 'Liaoning',
       'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui',
       'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong',
       'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan',
       'Tibet', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']

app = JupyterDash(external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div([
    dbc.Card([dbc.CardHeader("Total Sales of Different Buildings per Month"),
        dbc.CardBody(
            
            dbc.Row([
                
              dbc.Col([dbc.Row([dbc.Col(
                  dcc.RangeSlider(2019, 2022, step=None, marks={
        2019: '2019',
        2020: '2020',
        2021: '2021',
        2022: '2022',
        
    },value=[2019, 2022], id='year-range-slider')
                            #dbc.Checklist(
                                #id="YearChecklist",
                                #options=[{"label": e, "value": e} for e in year_list],
                                ##inline=True
                            #),
                        ),
                        dbc.Col(
                            dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in provinces],
            value='Country',
            multi=False
         )
                        )]),
                    
                    dcc.Graph(
        id='fig_ts',
        figure=paint_fig_ts())

              ],width=12)
                
            ]))]),
    dbc.Card([dbc.CardHeader("Floor Space Completed of Different Buildings per Month"),
        dbc.CardBody(
            
            dbc.Row(children=[
                
                dbc.Col(children=[
                    dbc.Row([dbc.Col(
                        dcc.RangeSlider(2019, 2022, step=None, marks={
        2019: '2019',
        2020: '2020',
        2021: '2021',
        2022: '2022',
        
    }, value=[2019, 2022],id='year-range-slider-fs')),dbc.Col(
        dcc.Dropdown(
            id='dropdown-fs',
            options=[{'label': i, 'value': i} for i in provinces],
            value='Country',
            multi=False,
            
         )
    )]
                            #dbc.Checklist(
                             #   id="YearChecklist_fs",
                              #  options=[{"label": e, "value": e} for e in year_list],
                               # inline=True
                            #),
                        ),
                    
                    dcc.Graph(
        id='fig_fs',
        figure=paint_fig_fs())],width=9

                ),
                dbc.Col(dcc.Graph(
        id='figtreemap',
        figure=paint_figtreemap()),width=3)]
                
            ))]),
           
            
           
])
@app.callback(
    Output("fig_ts", "figure"),   
    Input("year-range-slider", "value"),
    Input("dropdown", "value")
        
    
)
def update_line_graph(years,province):
    years_new=[]
    if not years and not province:
      return paint_fig_ts(['2019','2020','2021','2022'],'Country')
    else:
      for y in range(years[0],years[1]+1):
          years_new.append(str(y))
      
      return paint_fig_ts(years_new,province)



@app.callback(
    Output("fig_fs", "figure"),   
    Input("year-range-slider-fs", "value"),  
    Input("dropdown-fs", "value")
)
def update_bar_chart(years,province):
    years_new=[]
    if not years and not province:
      return paint_fig_fs()

    else:
      for y in range(years[0],years[1]+1):
          years_new.append(str(y))
      
      return paint_fig_fs(years_new,province)


@app.callback(
    Output('figtreemap', 'figure'),
    Input('fig_fs', 'hoverData'),
    Input('dropdown-fs', 'value')
)
def linkTreemapBarChart(hoverData,province): 
    # make a copy of the bar chart and color
    updateTree = copy.deepcopy(paint_figtreemap())
    updateColor = copy.deepcopy(colors)
    if hoverData is None:
      return updateTree
    else:
      hoverLabel = hoverData['points'][0]['label']
      data=get_month_data(hoverLabel,province)
      hover_info = hoverData['points'][0]['hovertext']
      buildingtype=re.search('<b>(.+?)</b>', hover_info).group(1)
      hover_text=[]
      for index, row in data.iterrows():
          hover_text.append(('Month:{}<br>'+
                  
                  'Proportion:<b>{:.2%}</b>').format(
                      row['Date'],
          
                      row['Proportion']

                  ))
      if province=='Contry':
        if (buildingtype in  ['Commercialized Residential']):
          updateColor[0]='#4682B4'
        elif (buildingtype == 'Houses for Business Use'):
          updateColor[1]='#4682B4'
        else:
          updateColor[2]='#4682B4'
      else:
        if (buildingtype in  ['Commercialized Residential Buildings Sold']):
          updateColor[1]='#4682B4'
        else:
          updateColor[0]='#4682B4'
        
     

      trace=go.Treemap(  
          labels = data['Building Type'],
          parents = parent,
          values = data['Proportion'],
          marker_colors = updateColor,
          
          text=hover_text,
          hoverinfo="text"
      ) 
      layout = go.Layout(margin = dict(t=50, l=25, r=25, b=25))
      return (go.Figure(data=trace,layout=layout_tree))
    
 



# Run app and display result inline in the notebook
app.run_server(mode='external')