# Importing external library
import requests
import pandas as pd
import numpy as np
import sys



def decode(string_url):
    # Extracting data
    html = requests.get(string_url).content
    df_list = pd.read_html(html)
    extracted_data = df_list[-1]

    # Processing extracted_data and printing result on screen
    n = max(extracted_data[0][1:331].astype(int))
    m = max(extracted_data[2][1:331].astype(int))
    
    # initialising results matrix over y-axis then x-axis coordinates
    matrix_Y_X = np.full((m+1, n+1), "", dtype=str)
    
    coordinates = []
    values = [] 

    for row_index in range(1,332):
        y = int(extracted_data.iloc[row_index][2])
        x = int(extracted_data.iloc[row_index][0])
        coordinates.append((y,x))
        
        char = extracted_data.iloc[row_index][1]
        values.append('char')
        
    # updating the matrix
    for (b, a), value in zip(coordinates, values):
        matrix_Y_X[b, a] = value

    # printing matrix on the screen
    def print_dot(y, x):
        sys.stdout.write(f"\033[{y};{x}H{matrix_Y_X[y, x]}")

    # Example:
    for j in range(m+1):
        for i in range(n+1):
            print_dot(j, i)

    # Reset cursor position after drawing (may blur the printing)
    #print("\033[0;0H")
       
    # Returning and printing a result message after all tasks are completed successfully
    result = "Result printed on screen"
    print(result)
    return result

# Calling the function
decode('https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub')