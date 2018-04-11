%reset
# import all the required packages
import shutil
import glob
import os 
import datetime as dti
import pandas as pd
import numpy as np

# define the basic directory
path='E:/OneDrive/OneDrive - Knights - University of Central Florida/UCF/Projects/Arterial Crash Risk Analysis/Data/Intersection'

# read the dictionary table for the folder name corresponding to tmc number
dictionary=pd.read_excel('E:/OneDrive/OneDrive - Knights - University of Central Florida/UCF/Projects/Arterial Crash Risk Analysis/Data/Intersection/Location/Signal_Operation_Location.xlsx')


# generate the tmc list
def generate_tmc_list():
    tmc_list=[]
    for i in range(53):
        tmc='tmc'+ str(i+1)
        tmc_list.append(tmc)
    return tmc_list 

tmc_list=generate_tmc_list()

# define the function to move files
def move_files(from_folder, to_folder, start_date, end_date):
    daterange = pd.date_range(start_date, end_date)
    for tmc in tmc_list:
        # retrieve the corridor_folder and intersection based on the dictionary
        corridor_folder=dictionary['Corridor Folder Name'][dictionary['ID'].tolist().index(tmc)]
        intersection = dictionary['InSync Archive Intersection'][dictionary['ID'].tolist().index(tmc)]
        
        # generate the History_path_from and TMC_path_from
        History_path_from = path + '/' + from_folder + '/' + corridor_folder + '/' + intersection + '/' + 'History'
        TMC_path_from = path + '/' + from_folder + '/' + corridor_folder + '/' + intersection + '/' + 'TMC'
         
        # generate the History_path_to and TMC_path_to
        History_path_to = path + '/' + to_folder + '/' + tmc + '/' + 'History'
        TMC_path_to = path + '/' + to_folder + '/' + tmc + '/' + 'TMC'
        for date in daterange:
            try:
                file_name = str(date)[0:10] +'.csv'
                file_path_History = History_path_from + '/' + file_name
                file_path_TMC = TMC_path_from + '/' + file_name
            
                shutil.move(file_path_History, History_path_to)
                shutil.move(file_path_TMC, TMC_path_to)
            except FileNotFoundError:
                pass


# define the original folder name
from_folder='InSync Archive_03232018'

# define the move to folder name
to_folder='InSync Archive_Updating'

# define the start_date
start_date=dti.date(2018, 2, 20)

# define the end_date
end_date=dti.date(2018, 3, 21)

# call the move file function
move_files(from_folder, to_folder, start_date, end_date)

