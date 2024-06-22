"""
    Gantt_chart
    
"""
# Import required packages
import pandas as pd
import pathlib as Path
import plotly.express as px
import plotly
import plotly.graph_objects as go

# Import utils if needeed
import utils_Gantt as utils

def main():
    
    
    # Standalone input text file
    input_file = 'settings.txt'
    excel_file, title_name , title_size, font, font_size, font_color, colorbar_colouring, colobar_title_position, chart_name = utils.readSettings(input_file)
    
    # Open excel file as a data frame
    excel_file = 'Tasks.xlsx'
    df = pd.read_excel(excel_file)
    print(df)
    
    
    # Customised settings deefined by the user
    title_name, title_size = 'Thesis completion', 42;
    font, font_size = "serif", 20;
    
    
    # generate the chart
    arguments = (df, title_name , title_size, font, font_size, font_color, 
                 colorbar_colouring, colobar_title_position, chart_name)
    generateChart(*arguments)
    
    return


def generateChart(df, title_name , title_size, font, font_size, font_color, 
                  colorbar_colouring, colobar_title_position, chart_name):
    
    
    # Extract information from the data frame
    tasks, content, start, end, progression = utils.getInfo(df);
    
    # Generate the chart
    fig = px.timeline(df, x_start= start, x_end=end, y = content, 
                      color = progression, title = title_name,
                      color_continuous_scale = colorbar_colouring)
    
    # Customise
    fig.update_yaxes(autorange = 'reversed'); # reverse the heat map
    
    labels_config = dict(family=font, size=font_size, color = font_color)
    axis_config = dict(tickfont = dict(family=font, size=font_size, color = font_color));
    colorbar_config = dict( title = dict(font=dict(family=font, size=font_size),
                                       side = colobar_title_position) , 
                           tickfont=dict(family=font, size=font_size) )
    
    fig.update_layout( title_font_size = title_size, title_font_family=font,
                      font = labels_config,
                      yaxis = axis_config, xaxis = axis_config,
                      coloraxis_colorbar = colorbar_config)
    
    
    # Show the chart
    plotly.offline.plot(fig, filename = chart_name)
    
    
    return

if __name__ == "__main__":
    main()