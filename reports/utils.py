import os
import re
import sys

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from IPython.display import Markdown, display
from tabulate import tabulate
import textwrap

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

credential_file = "../../../.gsecrets/gsheets-credentials.json"

def access_google_sheet(sheet_id, sheet_name):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    
    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)
    
    # Authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # Open the spreadhseet
    sheet = client.open_by_key(sheet_id)
    
    # Get the right sheet within the spreadsheet
    worksheet = sheet.worksheet(sheet_name)
    
    # Get all values in the sheet
    data = worksheet.get_all_values()
    
    # Convert to a DataFrame
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]  # Set the first row as the header
    df = df[1:]  # Take the data less the header row
    
    # Optionally convert data types here as needed
    # e.g., df['ColumnName'] = pd.to_datetime(df['ColumnName'])
    
    return df

def get_capstone_df():
    gsheet_id = "11DCDeuW7qMPsTYWSGCcbydHgbcgFGy7pFadYP5PAcOI"
    gsheet_sheet = "Form Responses 1"

    df = access_google_sheet( gsheet_id, gsheet_sheet )
    return df
