import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path,encoding="UTF-8")
    df.insert(4,"Status",np.nan)
    conditions=[(df['SERVICE_NAME'] == 'Application Identity'),
                (df['SERVICE_NAME'] == 'Application Information'),
                (df['SERVICE_NAME'] == 'Application Management'),
                (df['SERVICE_NAME'] == 'ASP.NET State Service'),
                (df['SERVICE_NAME'] == 'Windows Audio Endpoint Builder'),
                (df['SERVICE_NAME'] == 'Windows Audio'),
                (df['SERVICE_NAME'] == 'Base Filtering Engine'),
                (df['SERVICE_NAME'] == 'Background intelligent Transfer Service'),
                (df['SERVICE_NAME'] == 'Computer Browser'),
                (df['SERVICE_NAME'] == 'Certificate Propagation'),
                (df['SERVICE_NAME'] == 'SQL Server VSS Writer'),
                ]
    values = ['Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-OS','Excluded-Other']
    df['STATUS'] = np.select(conditions,values)
    df.to_excel('out.xlsx')
    
browseButton_Excel = tk.Button(text='Import CSV File', command=getExcel, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
