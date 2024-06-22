# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:55:06 2024

utils script containig secondary functions called by the main script
"""


# Import required packages

def getInfo(df):
    """
    

    Parameters
    ----------
    df : Pandas data frame
        Data frame containing the informatio of the chart.

    Returns
    -------
    tasks : Pandas series
        Task names
    content : Pandas series
        Content of.the taks
    start : Pandas series
        Start date the tasks
    end : Pandas series
        End dates of the tasks.
    
    progression : Pandas series
        Progression of the tasks.

    """
    # Store the tasks in a variable
    tasks = df['Task'];
    
    # Same for content
    content = df['Content']
    
    # Start and end datas
    start = df['Start']; end = df['End'];
    
    # Finaly the progression of each task
    progression = df[df.columns[-1]]
    
    return tasks, content, start, end, progression

def readSettings(file_name):
    """
    

    Parameters
    ----------
    file_name : string
        Name of the file with user inputs.

    Returns
    -------
    excel_file : string
        Path or simply the name of the excel file.
    title_name : string
        Title of the chart.
    title_size : integer
        Font size of the title.
    font : string
        Type of font.
    font_size : integer
        Font size of labels and ticks in the chart.
    font_color : string
        Color of the fonts.
    colorbar_colouring : string
        DESCRIPTION.
    colobar_title_position : string
        Position of color bar title.
    chart_name : string
        Name for the generated chart

    """
    
    
    # Scan the file
    with open(file_name, "r") as f:
        # Read name of the excel file
        f.readline();
        excel_file = f.readline().strip("\n")
        
        # Get title of the chart and font size 
        f.readline();
        data = f.readline().strip("\n").split(',')
        title_name, title_size = data[0], int(data[1]);
        
        # Get type of font and size
        f.readline();
        data = f.readline().strip("\n").split(', ')
        font, font_size, font_color = data[0], int(data[1]), data[2]
        
        # Get colobar settings
        f.readline();
        data = f.readline().strip("\n").split(', ')
        colorbar_colouring, colobar_title_position = data[0], data[1]
        
        # Get name for the chart
        f.readline();
        chart_name = f.readline().strip("\n")
    
    
    
    return excel_file, title_name , title_size, font, font_size, font_color, colorbar_colouring, colobar_title_position, chart_name



if __name__ == "__main__":
    main()

