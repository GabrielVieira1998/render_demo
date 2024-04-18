import pandas as pd
import dash
from dash import html,  dcc, clientside_callback, Input, Output, State
from plotly import graph_objs as go
import plotly.graph_objs as go
# from js import jsPDF  # Import the jsPDF library from CDN
import numpy as np
# import html2pdf  # Library for HTML to PDF conversion
df_fund_data = pd.read_csv('assets/17534.csv')
#print(df_fund_data.head())

df_perf_summary = pd.read_csv('assets/17530.csv')
#print(df_perf_summary.head())

df_cal_year = pd.read_csv('assets/17528.csv')
#print(df_cal_year.head())

df_perf_pc = pd.read_csv('assets/17532.csv')
#print(df_perf_pc.head())
#print("-----------")
# Generate sample data for the line chart

########################

dates = pd.date_range(start='2006-01-01', end='2018-01-01', freq='2YE')
returns_3m_libor = np.linspace(100, 135, len(dates))  # Simulated return values for 3 Month Libor
returns_bond_portfolio = np.linspace(100, 130, len(dates))  # Simulated return values for Bond Portfolio

# Creating a DataFrame
df = pd.DataFrame({
    'Date': dates,
    '3 Month Libor': returns_3m_libor,
    'Absolute Return Bond II Portfolio Base Shares': returns_bond_portfolio
})

# Creating a line chart using Plotly
fig = go.Figure()

# Adding 3 Month Libor (dotted line)
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['3 Month Libor'],
    mode='lines+markers',
    name='3 Month Libor',
    line=dict(dash='dot'),
    showlegend=False
    
))

# Adding Bond Portfolio (filled line)
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Absolute Return Bond II Portfolio Base Shares'],
    mode='lines',
    name='Absolute Return Bond II Portfolio Base Shares',
    showlegend=False,
    fill='tozeroy'
))

dates = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='2YE')
# # Layout configurations without fixed width and height
fig.update_layout(
    autosize=True,
    xaxis_title='Date',
    yaxis_title='Return (%)',
    xaxis=dict(
        title_font=dict(size=8),  # Adjust x-axis title font size here
        tickfont=dict(size=8)     # Adjust x-axis tick label font size here
    ),
    yaxis=dict(
        title_font=dict(size=8),  # Adjust y-axis title font size here
        tickfont=dict(size=8)     # Adjust y-axis tick label font size here
    ),
    yaxis_range=[85, 135],
    xaxis_range=[df['Date'].min(), df['Date'].max()],  # Set the x-axis range to include all the available data
    margin=dict(l=0, r=0, t=5, b=50)

    # width=800,
    # height=200

)

def convert_plotly_fig_to_uri(fig):
    img_bytes = fig.to_image(format="png")
    img_data_uri = "data:image/png;base64," + base64.b64encode(img_bytes).decode()
    return img_data_uri




####################

# Data for the bar chart
sectors = ["Governments", "Asset-Back Securities (ABS)", "Residential Mortgages (RMBS)", 
           "Emerging Market Debt", "Corporate - High Yield", "Municipal", 
           "Commercial Mortgages (CMBS)", "Corporates - Inv. Grade", 
           "Covered Bonds", "Quasi-Governments", "Derivatives"]
values = [46.5, 18.7, 10.6, 4.7, 2.7, 1.4, 1.4, 0.8, 0.4, 0.3, 0.1]

# Creating the bar chart
fig_sector_allocation = go.Figure(data=[go.Bar(x=sectors, y=values)])

# Layout configurations
fig_sector_allocation.update_layout(
    autosize=True,
    # title='Sector Allocation (%)',
    xaxis_title='Sectors',
    yaxis_title='Percentage',
    xaxis=dict(
        title_font=dict(size=5),  # Adjust x-axis title font size here
        tickfont=dict(size=5)     # Adjust x-axis tick label font size here
    ),
    yaxis=dict(
        title_font=dict(size=8),  # Adjust y-axis title font size here
        tickfont=dict(size=8)     # Adjust y-axis tick label font size here
    ),
    margin=dict(l=0, r=0, t=5, b=50)
    # yaxis=dict(range=[0, max(values) + 10])  # Adding some space above the highest bar for clarity
)

##############################

# Data for the horizontal bar chart
currencies = ["US Dollar", "Swedish Krona", "Norwegian Krone", "Czech Koruna", 
              "Polish Zloty", "Mexican Peso", "Brazilian Real", "Hungarian Forint", 
              "Canadian Dollar", "Chinese Yuan", "Russian Ruble", "Other"]
values = [106.1, 8.9, 8, 6.6, 5.7, 4.2, 3.2, 2.3, 2.2, 1.8, 1.8, -50]

# Creating the horizontal bar chart
fig_currency_weights = go.Figure(data=[go.Bar(y=currencies, x=values, orientation='h')])

# Layout configurations
fig_currency_weights.update_layout(
    autosize=True,
    # title='Top 10 Currency Weights (%)',
    yaxis_title='Currencies',
    xaxis_title='Percentage',
    xaxis=dict(range=[min(values) - 10, max(values) + 10],
               title_font=dict(size=8),  # Adjust x-axis title font size here
               tickfont=dict(size=8)     # Adjust x-axis tick label font size here
    ),  # Adjusting range to include negative values
    yaxis=dict(
        title_font=dict(size=8),  # Adjust y-axis title font size here
        tickfont=dict(size=8)     # Adjust y-axis tick label font size here
    ),
    margin=dict(l=0, r=0, t=5, b=50)

)

##########

credit_scores = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC", "CC", "C", "D", "NR", "Cash"]
values = [42.1, 3.7, 31.8, 1.9, 2.1, 1.6, 2.3, 1.1, 0.2, 0.1, 0.6, 12.6]

# Creating the horizontal bar chart
fig_credit_allocation = go.Figure(data=[go.Bar(y=credit_scores, x=values, orientation='h')])

# Layout configurations
fig_credit_allocation.update_layout(
    autosize=True,
    # title='Credit Allocation (%)',
    yaxis_title='Credit Score',
    xaxis_title='Percentage',
    xaxis=dict(range=[0, max(values) + 10],
               title_font=dict(size=8),  # Adjust x-axis title font size here
               tickfont=dict(size=8)     # Adjust x-axis tick label font size here
    ),  # Adjusting range to include all values
    yaxis=dict(
        title_font=dict(size=8),  # Adjust y-axis title font size here
        tickfont=dict(size=8)     # Adjust y-axis tick label font size here
    ),
    margin=dict(l=0, r=0, t=5, b=50)
)


# Use this function to convert your Plotly figures into image URIs before they are rendered in the layout.


# def make_dash_table(df):
#     ''' Return a dash definition of an HTML table for a Pandas dataframe '''
#     table = []
#     for i, row in df.iterrows():
#         background_color = 'white' if i % 2 == 0 else '#d1dae8'
#         html_row = []
#         for col in df.columns:
#             value = html.Td(str(row[col]))
#             html_row.append(value)
#         table.append(html.Tr(html_row, style={'backgroundColor': background_color}))
#     return table

def make_dash_table(df):
    ''' Return a list of HTML rows for a Pandas dataframe with no cell borders '''
    table = []
    for i, row in df.iterrows():
        background_color = 'white' if i % 2 == 0 else '#d1dae8'
        # Set the style for each td element to remove borders and add any additional styling
        html_row = [
            html.Td(row[col], style={
                # 'border': 'none',  # This will remove the border from the cell
                'textAlign': 'left' if idx == 0 else 'right'
                
                # 'padding': '5px'  # Add padding to cell if needed
            })
            for idx, col in enumerate(df.columns)
        ]
        table.append(html.Tr(html_row, style={'backgroundColor': background_color}))
    return table



# def make_dash_table(df):
#     ''' Return a dash definition of an HTML table for a Pandas dataframe '''
#     table = []
#     for i, row in df.iterrows():
#         background_color = 'white' if i % 2 == 0 else '#d1dae8'
#         html_row = [html.Tr([html.Td(col) for col in row], style={'backgroundColor': background_color})]
#         table.extend(html_row)
#     return table


modifed_perf_table = make_dash_table(df_perf_summary)

modifed_perf_table.insert(
    0, html.Tr([
        html.Td([]),
        html.Td(['Cumulative'], colSpan=4, style=dict(textAlign="center")),
        html.Td(['Annualised'], colSpan=4, style=dict(textAlign="center"))
    ], style=dict(background='white', fontWeight=600))
)

df_fund_info = pd.read_csv('assets/17544.csv')
#print(df_fund_info.head())
df_fund_characteristics = pd.read_csv('assets/17542.csv')
#print(df_fund_characteristics.head())
df_fund_facts = pd.read_csv('assets/17540.csv')
#print(df_fund_facts.head())
df_bond_allocation = pd.read_csv('assets/17538.csv')
#print(df_bond_allocation.head())

print(dash.__version__)

external_stylesheets = ['assets/stylesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
# app = dash.Dash('GS Bond II Portfolio')#, external_scripts=['/assets/custom_script.js'])


# Add the download button and callback function to the Dash app layout
app.layout = html.Div(id='pdf-content', children=[
   
    html.Button(children='CREATE PDF', id='run'),
    html.Div(id='pdf-download-link'),  # Placeholder for the PDF download link
    html.Div([#id='pdf-content', children=

                        
        html.Div([ # subpage 1

            # Row 1 (Header)

            html.Div([

                html.Div([      
                    html.H5('Goldman Sachs Strategic Absolute Return Bond II Portfolio', style={'fontSize': '1.5em', 'color': 'white'}),
                    html.H6('A sub-fund of Goldman Sachs Funds, SICAV', style={'color': 'white', 'opacity': 0.5}),
                    ], style={'background': 'navy', 'display': 'flex', 'flexDirection': 'column', 'padding': '5px', 'alignItems': 'center'}),


            ], style={'margin': '10px 10px 0px 0'}),

            # html.Br([]),

            # Row 2

            html.Div([     

                html.Div([
                    html.Div([
                        html.H6('Investor Profile', style={'font-size': '1.5em', 'color': 'white','margin-bottom': '0.5px','borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),

                        html.Strong('Investor objective'),
                        html.P('Capital appreciation and income.'),

                        html.Strong('Position in your overall investment portfolio*'),
                        html.P('The fund can complement your portfolio.'),

                        html.Strong('The fund is designed for:'),
                        html.P('The fund is designed for investors who are looking for a flexible \
                                global investment and sub-investment grade fixed income portfolio \
                                that has the ability to alter its exposure with an emphasis on interest \
                                rates, currencies and credit markets and that seeks to generate returns \
                                through different market conditions with a riskier investment strategy \
                                than GS Strategic Absolute Return Bond I Portfolio.'),
                    ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'flex-start', 'margin': '10px 50px 20px 0'}),  # Set flex-grow to 1 for text content

                    html.Div([

                        html.H6(["Performance (Indexed)"], style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0.5px', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                        # html.Iframe(
                        #     src="https://plot.ly/~jackp/17553.embed?modebar=false&link=false&autosize=true",
                        #     style=dict(border=0), width="100%", height="250", id='chart-1-iframe'
                        # ),
                        dcc.Graph(
                            figure=fig,  # 'fig' is the figure object for your chart
                            id='performance-indexed-chart',
                            style={'width': '500px', 'height': '200px'},  # Auto height for flexibility
                            config={'responsive': True},  # Ensures graph sizes responsively 
                               
                            # className='your-graph-class'
                        )
                    ], style={'flex': '1', 'margin': '10px'}),  # Set flex-grow to 1 for the chart

                ], style={'display': 'flex', 'flexDirection': 'row'}),  # Use flexbox layout ############## , className='flex-container'

            ]),# 'position': 'relative', 'top':'-3%'

            # Row 2.5
            html.Div([     

                html.Div([
                    html.H6('Performance (%)', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0.5px', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),  # Set the color of H6 to blue
                    html.Table(
                        make_dash_table(df_perf_pc),
                        style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}
                    )
                ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'flex-start', 'margin': '10px 50px 20px 0'}),  # Align items to start

                html.Div([
                    html.P("This is an actively managed fund that is not designed to track its reference benchmark. \
                        Therefore the performance of the fund and the performance of its reference benchmark \
                        may diverge. In addition stated reference benchmark returns do not reflect any management \
                        or other charges to the fund, whereas stated returns of the fund do."),
                    html.Strong("Past performance does not guarantee future results, which may vary. \
                        The value of investments and the income derived from investments will fluctuate and \
                        can go down as well as up. A loss of capital may occur.")
                ], style={'flex': '1', 'margin': '10px'})  # Set flex-grow to 1 for the text content and add padding

            ], style={'display': 'flex', 'flexDirection': 'row'}),  # Use flexbox layout

            # Row 3

            html.Div([             

                html.Div([
                    html.H6('Fund Data', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(make_dash_table(df_fund_data),
                               style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'})
                ], style={'flex': '1', 'margin': '10px 50px 20px 0'}),

                html.Div([
                    html.H6("Performance Summary (%)", style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(modifed_perf_table, style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}),

                    html.H6("Calendar Year Performance (%)", style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(make_dash_table(df_cal_year), style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'})
                ], style={'flex': '1', 'margin': '10px'}),                      

            ],style={'display': 'flex', 'flexDirection': 'row'}),                
           
        ], id='page1'),
       
    ]),  
                
    html.Div([ # page 2
                                       
        html.Div([ # subpage 2
                        
            # Row 1 (Header)
                        
            html.Div([

                html.Div([      
                    html.H5('Goldman Sachs Strategic Absolute Return Bond II Portfolio', style={'fontSize': '1.5em', 'color': 'white'}),
                    html.H6('A sub-fund of Goldman Sachs Funds, SICAV', style={'color': 'white', 'opacity': 0.5}),
                    ], style={'background': 'navy', 'padding': '10px', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

            ], style={'margin': '10px 10px 0px 0'}),
                        
            # Row 2
                        
            html.Div([

                # Column 1
                                
                html.Div([      
                    html.H6('Financial Information', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(make_dash_table(df_fund_info), style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}, id='table1'),
                                        
                    html.H6('Fund Characteristics', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(make_dash_table(df_fund_characteristics), style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}, id='table2'),
                                        
                    html.H6('Fund Facts', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    html.Table(make_dash_table(df_fund_facts), style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}, id='table3'),
                                        
                ]),
                                
                # Column 2

                html.Div([                                          
                    html.H6('Sector Allocation (%)', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    # html.Iframe(src="https://plot.ly/~jackp/17560.embed?modebar=false&link=false&autosize=true", \
                    #     style=dict(border=0), width="100%", height="250", id='chart-1'),
                    dcc.Graph(
                            figure=fig_sector_allocation,  # 'fig' is the figure object for your chart
                            id='sector-allocation-chart',
                            style={'width': '1045px', 'height': '120px'},
                            config={'responsive': True}  # Ensures graph sizes responsively     
                        ),
                    # html.H6('Country Bond Allocation (%)', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    # html.Table(make_dash_table(df_bond_allocation), style={'borderCollapse': 'collapse', 'width': '100%', 'backgroundColor': 'navy'}, id='table4'),
                                        
                ]), #style={'flex': '1', 'margin': '10px'}), --->> , style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'flex-start', 'margin': '10px 50px 20px 0'}
                                
                # Column 3
                
                html.Div([      
                    html.H5('Goldman Sachs Strategic Absolute Return Bond II Portfolio', style={'fontSize': '1.5em', 'color': 'white'}),
                    html.H6('A sub-fund of Goldman Sachs Funds, SICAV', style={'color': 'white', 'opacity': 0.5}),
                    ], style={'background': 'navy', 'padding': '10px', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

                          
                
                html.Div([            
                    html.H6('Top 10 Currency Weights (%)', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0.5px', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    # html.Iframe(src="https://plot.ly/~jackp/17555.embed?modebar=false&link=false&autosize=true", \
                    #     style=dict(border=0), width="100%", height="250", id='chart-2'),

                    dcc.Graph(
                            figure=fig_currency_weights,  # 'fig' is the figure object for your chart
                            id='currency-weights-chart',
                            style={'width': '1045px', 'height': '120px'},
                            config={'responsive': True}  # Ensures graph sizes responsively     
                        ),
                                        
                    html.H6('Credit Allocation (%)', style={'font-size': '1.5em', 'color': 'white', 'margin-bottom': '0.5px', 'borderCollapse': 'collapse', 'width': '100%','backgroundColor': 'navy'}),
                    # html.Iframe(src="https://plot.ly/~jackp/17557.embed?modebar=false&link=false&autosize=true", \
                    #     style=dict(border=0), width="100%", height="250", id='chart-3'),       
                    dcc.Graph(
                            figure=fig_credit_allocation,  # 'fig' is the figure object for your chart
                            id='credit-allocation-chart',
                            style={'width': '1045px', 'height': '120px'},
                            config={'responsive': True}  # Ensures graph sizes responsively    
                            
                        ),                                
                                                                                
                ]),      # , style={'width': '100%', 'display': 'flex', 'flexDirection': 'column'}                          

            ], style={'margin': '10px 10px 0px 0'}),                        
                        
        ], id='page2'),
                
    ], ),
   
])


app.clientside_callback(
    """
    function generatePDF(n_clicks) {
        if (n_clicks) {
            const runButton = document.getElementById('run');
            runButton.style.display = 'none';  // Hide the button before generating PDF

            const element = document.getElementById('pdf-content');
            

            var opt = {
                margin: [0, 0, 0, 0],  // Set some margin if needed
                filename: 'GS_Bond_II_Portfolio.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: {
                    scale: 3,
                    useCORS: true,
                    letterRendering: true,
                   
                    windowWidth: element.scrollWidth,
                    windowHeight: element.scrollHeight,
                    mediaType: 'print'  // Ensures print media styles are used
                },
                jsPDF: {
                    unit: 'in',
                    format: 'letter',
                    orientation: 'landscape'
                }
            };

            html2pdf().set(opt).from(element).save().then(function() {
                runButton.style.display = 'block';  // Restore button visibility after saving
            });
        }
    }
    """,
    Output('pdf-download-link', 'children'),
    [Input('run', 'n_clicks')],
    prevent_initial_call=True
)



if __name__ == '__main__':
    app.run_server(debug=True)
