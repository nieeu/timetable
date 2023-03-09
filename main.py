# Import Libraries

import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')


# Import dataset

df = pd.read_excel('Book2.xlsx')

# Clean only useful columns
cols = ['Mã học phần','Tên học phần', 'Mã lớp tín chỉ', 'Số tín chỉ','Giai đoạn', 'Thứ', 'Tiết bắt đầu', 'LỊCH HỌC', 'Mã lớp']
df_clean = df[cols]

df_clean.rename(columns={'Mã học phần': 'course_code', 'Tên học phần': 'course_name', 'Mã lớp tín chỉ': 'class_code',
                   'Số tín chỉ': 'num_of_credits', 'Giai đoạn': 'period', 'Thứ': 'weekday', 'Tiết bắt đầu': 'start',
                   'LỊCH HỌC': 'time', 'Mã lớp': 'code'}, inplace=True)

# Clean the dataset 
df_clean = df_clean[~df_clean['time'].isnull()]

list_blank = ['Thứ 2(01-03)', 'Thứ 2(04-06)', 'Thứ 2(10-12)', 'Thứ 3(01-03)','Thứ 2(07-09)']
df_clean['weekday'][df_clean['weekday'].isnull()] = df_clean['time'].map(lambda x: '2Ca1' if x == list_blank[0] else (
                                                '2Ca2' if x == list_blank[1] else(
                                                '2Ca4' if x == list_blank[2] else(
                                                '2Ca4' if x == list_blank[4] else '3Ca1'
                                                )
                                                )
                                                )
                                            )

df_clean['period_weekday'] =  df_clean['weekday'] + '.' + df_clean['period'].astype(str)
df_clean = df_clean[df_clean['period'].isin([1,2])]
df_clean['short_code'] = df_clean['course_code'] + '.' + df_clean['code'].astype(str) + '.' + df_clean['period'].astype(str)


# List of possible Class codes
import itertools
list_subjects = ['MKT407', 'KTE312', 'TMA404', 'KTE319', 'TMA311']
list_set = []
for i in list_subjects:
    set = df_clean['short_code'][df_clean['course_code']==i].unique().tolist()
    list_set.append(set)

all_list = [] 
for element in itertools.product(*list_set):
  all_list.append(element)

# List of class codes without overlaps
full_list=[]
for list in all_list:
      xls = pd.ExcelFile('Timetable Project.xlsx')
      df_main= pd.read_excel(xls, 'main')
      for x in list:
            
            list_slots = df_clean['period_weekday'][df_clean['short_code']==x].unique().tolist()
            df_main[x] = 0
            df_main[x] = df_main['Ca'].map(lambda x: 1 if x in list_slots else 0)

      df_main['Sum'] = df_main.sum(axis=1)
      
      if (df_main['Sum']<=1).all():
            full_list.append(list)
      else:
            pass

# print out possible timetables
for list in full_list:
    xls = pd.ExcelFile('Timetable Project.xlsx')
    df_output= pd.read_excel(xls, 'output')
    for x in list:

        ca_list = df_clean['period_weekday'][df_clean['short_code'] == x]
        for ca in ca_list:
            day = int(ca[0])
            slot = ca[1:]
            df_output[day][df_output['Ca']==slot] = x

    print(df_output)
    print('==============================================================================')

## Streamlit app