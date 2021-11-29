import numpy as np
import pandas as pd
import xgboost as xgb
from fancyimpute import IterativeImputer
from sklearn.experimental import  enable_iterative_imputer
from sklearn.impute import IterativeImputer

df = pd.read_csv('DATA_P.csv', encoding='utf-8')

for i in range(len(df)):
  if df['PRES_NOTE'][i][:3] == '본운동':
    df['PRES_NOTE'][i] = ' / '+ df['PRES_NOTE'][i]

df['준비운동'] = df.PRES_NOTE.str.split(' / ').str[0]
df['본운동'] = df.PRES_NOTE.str.split(' / ').str[1]
df['마무리운동'] = df.PRES_NOTE.str.split(' / ').str[2]

df_1 = df['준비운동']
df_2 = df['본운동']
df_3 = df['마무리운동']

df['BP']=""


for i in range(len(df)):
  if df['ITEM_F006'][i] > 150 :
    df['BP'][i] = '3'
  elif df['ITEM_F005'][i] < 60 :
    df['BP'][i] = '1'
  else :
    df['BP'][i] = '2'


df = df.astype({'BP':'float64'})


for i in range(len(df)):
  if df['TEST_SEX'][i] =='M':
    if df['TEST_AGE'][i] < 30 :
      if df['ITEM_F003'][i] <= 14 :
        df['ITEM_F003'][i] = '1'
      elif df['ITEM_F003'][i] <= 22 :
        df['ITEM_F003'][i] = '2'
      elif df['ITEM_F003'][i] <= 27 :
        df['ITEM_F003'][i] = '3'
      elif df['ITEM_F003'][i] <= 37 :
        df['ITEM_F003'][i] = '4'
      elif df['ITEM_F003'][i] > 37 :
        df['ITEM_F003'][i] = '5'
    else :
      if df['ITEM_F003'][i] <= 17 :
        df['ITEM_F003'][i] = '1'
      elif df['ITEM_F003'][i] <= 25 :
        df['ITEM_F003'][i] = '2'
      elif df['ITEM_F003'][i] <= 30 :
        df['ITEM_F003'][i] = '3'
      elif df['ITEM_F003'][i] <= 40 :
        df['ITEM_F003'][i] = '4'
      elif df['ITEM_F003'][i] > 40 :
        df['ITEM_F003'][i] = '5'
  else:
    if df['TEST_AGE'][i] < 30 :
      if df['ITEM_F003'][i] <= 17 :
        df['ITEM_F003'][i] = '1'
      elif df['ITEM_F003'][i] <= 26 :
        df['ITEM_F003'][i] = '2'
      elif df['ITEM_F003'][i] <= 32 :
        df['ITEM_F003'][i] = '3'
      elif df['ITEM_F003'][i] <= 42 :
        df['ITEM_F003'][i] = '4'
      elif df['ITEM_F003'][i] > 42  :
        df['ITEM_F003'][i] = '5'
    else :
      if df['ITEM_F003'][i] <= 20 :
        df['ITEM_F003'][i] = '1'
      elif df['ITEM_F003'][i] <= 29 :
        df['ITEM_F003'][i] = '2'
      elif df['ITEM_F003'][i] <= 35 :
        df['ITEM_F003'][i] = '3'
      elif df['ITEM_F003'][i] <= 45 :
        df['ITEM_F003'][i] = '4'
      elif df['ITEM_F003'][i] > 45 :
        df['ITEM_F003'][i] = '5'

df = pd.get_dummies(df, columns = ['TEST_SEX'])

df_10 = df[(df['TEST_AGE'] < 20)]
df_20 = df[(df['TEST_AGE'] >= 20) & (df['TEST_AGE']<60)]
df_60 = df[(df['TEST_AGE'] >= 60)]

df_10 = df_10.drop(['ITEM_F005','ITEM_F006','ITEM_F007','ITEM_F008','ITEM_F009','ITEM_F010','ITEM_F011','ITEM_F013','ITEM_F014','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F018','ITEM_F020','ITEM_F021',
                    'ITEM_F023','ITEM_F024','ITEM_F025','ITEM_F026','ITEM_F027','ITEM_F028',
                    'ITEM_F029','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037',
                    'ITEM_F038','ITEM_F039','ITEM_F040','ITEM_F041','TEST_CNT', 'CENTER_NM','AGE_GBN','TEST_GBN', 'INPUT_GBN','CERT_GBN','TEST_YMD','TEST_AGE'],axis=1)


df_20 = df_20.drop(['ITEM_F005','ITEM_F006','ITEM_F007','ITEM_F008','ITEM_F009','ITEM_F010','ITEM_F011','ITEM_F013','ITEM_F014','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F018','ITEM_F020','ITEM_F021',
                    'ITEM_F023','ITEM_F024','ITEM_F025','ITEM_F026','ITEM_F027','ITEM_F028',
                    'ITEM_F029','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037','ITEM_F038',
                    'ITEM_F039','ITEM_F040','ITEM_F041','TEST_CNT', 'CENTER_NM','AGE_GBN','TEST_GBN', 'INPUT_GBN','CERT_GBN','TEST_YMD','TEST_AGE'],axis=1)


df_60 = df_60.drop(['ITEM_F005','ITEM_F006','ITEM_F007','ITEM_F008','ITEM_F009','ITEM_F010','ITEM_F011','ITEM_F013','ITEM_F014','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F020','ITEM_F021',
                    'ITEM_F022','ITEM_F024','ITEM_F025','ITEM_F028','ITEM_F018',
                    'ITEM_F029','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037',
                    'ITEM_F038','ITEM_F039','ITEM_F040','ITEM_F041','TEST_CNT', 'CENTER_NM','AGE_GBN','TEST_GBN', 'INPUT_GBN','CERT_GBN','TEST_YMD','TEST_AGE'],axis=1)


df_10['ITEM_F003'] = df_10['ITEM_F003'].fillna(3)

MICE_imputer = IterativeImputer()


df_10_X = df_10.iloc[:,[0,1,2,3,4,5,6,11,12,13]]
x_data_mice = df_10_X
x_data_mice.iloc[:,:] = MICE_imputer.fit_transform(x_data_mice)
df_10 = pd.concat([df_10_X,df_10.iloc[:,[7,8,9,10]]],axis=1)

df_20_X = df_20.iloc[:,[0,1,2,3,4,5,6,11,12,13]]
x_data_mice = df_20_X
x_data_mice.iloc[:,:] = MICE_imputer.fit_transform(x_data_mice)
df_20 = pd.concat([df_20_X,df_20.iloc[:,[7,8,9,10]]],axis=1)

df_60_X = df_60.iloc[:,[0,1,2,3,4,5,6,7,8,13,14,15]]
x_data_mice = df_60_X
x_data_mice.iloc[:,:] = MICE_imputer.fit_transform(x_data_mice)
df_60 = pd.concat([df_60_X,df_60.iloc[:,[9,10,11,12]]],axis=1)



df_pre_10 = df_10.drop(['PRES_NOTE','본운동','마무리운동'],axis=1)
df_mai_10 = df_10.drop(['PRES_NOTE','준비운동','마무리운동'],axis=1)
df_las_10 = df_10.drop(['PRES_NOTE','본운동','준비운동'],axis=1)

df_pre_20 = df_20.drop(['PRES_NOTE','본운동','마무리운동'],axis=1)
df_mai_20 = df_20.drop(['PRES_NOTE','준비운동','마무리운동'],axis=1)
df_las_20 = df_20.drop(['PRES_NOTE','본운동','준비운동'],axis=1)

df_pre_60 = df_60.drop(['PRES_NOTE','본운동','마무리운동'],axis=1)
df_mai_60 = df_60.drop(['PRES_NOTE','준비운동','마무리운동'],axis=1)
df_las_60 = df_60.drop(['PRES_NOTE','본운동','준비운동'],axis=1)

df_pre_10 = df_pre_10[df_pre_10['준비운동'] !='']
df_mai_10 = df_mai_10[df_mai_10['본운동'].isnull()==False]
df_las_10 = df_las_10[df_las_10['마무리운동'].isnull()==False]

df_pre_20 = df_pre_20[df_pre_20['준비운동'] !='']
df_mai_20 = df_mai_20[df_mai_20['본운동'].isnull()==False]
df_las_20 = df_las_20[df_las_20['마무리운동'].isnull()==False]

df_pre_60 = df_pre_60[df_pre_60['준비운동'] !='']
df_mai_60 = df_mai_60[df_mai_60['본운동'].isnull()==False]
df_las_60 = df_las_60[df_las_60['마무리운동'].isnull()==False]

df_y_pre_10 = df_pre_10['준비운동']
df_y_mai_10 = df_mai_10['본운동']
df_y_las_10 = df_las_10['마무리운동']

df_y_pre_20 = df_pre_20['준비운동']
df_y_mai_20 = df_mai_20['본운동']
df_y_las_20 = df_las_20['마무리운동']

df_y_pre_60 = df_pre_60['준비운동']
df_y_mai_60 = df_mai_60['본운동']
df_y_las_60 = df_las_60['마무리운동']


df_pre_10 = df_pre_10.drop(['준비운동'],axis=1)
df_mai_10 = df_mai_10.drop(['본운동'],axis=1)
df_las_10 = df_las_10.drop(['마무리운동'],axis=1)

df_pre_20 = df_pre_20.drop(['준비운동'],axis=1)
df_mai_20 = df_mai_20.drop(['본운동'],axis=1)
df_las_20 = df_las_20.drop(['마무리운동'],axis=1)

df_pre_60 = df_pre_60.drop(['준비운동'],axis=1)
df_mai_60 = df_mai_60.drop(['본운동'],axis=1)
df_las_60 = df_las_60.drop(['마무리운동'],axis=1)

df_y_pre_10 = df_y_pre_10.reset_index(drop=True)
df_y_pre_20 = df_y_pre_20.reset_index(drop=True)
df_y_pre_60 = df_y_pre_60.reset_index(drop=True)
df_y_mai_10 = df_y_mai_10.reset_index(drop=True)
df_y_mai_20 = df_y_mai_20.reset_index(drop=True)
df_y_mai_60 = df_y_mai_60.reset_index(drop=True)
df_y_las_10 = df_y_las_10.reset_index(drop=True)
df_y_las_20 = df_y_las_20.reset_index(drop=True)
df_y_las_60 = df_y_las_60.reset_index(drop=True)

df_pre_10 = df_pre_10.reset_index(drop=True)
df_pre_20 = df_pre_20.reset_index(drop=True)
df_pre_60 = df_pre_60.reset_index(drop=True)
df_mai_10 = df_mai_10.reset_index(drop=True)
df_mai_20 = df_mai_20.reset_index(drop=True)
df_mai_60 = df_mai_60.reset_index(drop=True)
df_las_10 = df_las_10.reset_index(drop=True)
df_las_20 = df_las_20.reset_index(drop=True)
df_las_60 = df_las_60.reset_index(drop=True)

for i in range(len(df_y_pre_10)):
  df_y_pre_10[i] = df_y_pre_10[i][5:]

for i in range(len(df_y_pre_20)):
  df_y_pre_20[i] = df_y_pre_20[i][5:]

for i in range(len(df_y_pre_60)):
  df_y_pre_60[i] = df_y_pre_60[i][5:]

for i in range(len(df_y_mai_10)):
  df_y_mai_10[i] = df_y_mai_10[i][4:]

for i in range(len(df_y_mai_20)):
  df_y_mai_20[i] = df_y_mai_20[i][4:]

for i in range(len(df_y_mai_60)):
  df_y_mai_60[i] = df_y_mai_60[i][4:]

for i in range(len(df_y_las_10)):
  df_y_las_10[i] = df_y_las_10[i][6:]

for i in range(len(df_y_las_20)):
  df_y_las_20[i] = df_y_las_20[i][6:]

for i in range(len(df_y_las_60)):
  df_y_las_60[i] = df_y_las_60[i][6:]

df_y_pre_10 =df_y_pre_10.str.split(',')
df_y_pre_20 =df_y_pre_20.str.split(',')
df_y_pre_60 =df_y_pre_60.str.split(',')

df_y_mai_10 =df_y_mai_10.str.split(',')
df_y_mai_20 =df_y_mai_20.str.split(',')
df_y_mai_60 =df_y_mai_60.str.split(',')

df_y_las_10 =df_y_las_10.str.split(',')
df_y_las_20 =df_y_las_20.str.split(',')
df_y_las_60 =df_y_las_60.str.split(',')

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['계단 두 칸씩 뛰기','계단 두발 뛰어 오르기','계단 뛰어 오르기','계단 오르기','계단 한발 뛰기']:
      df_y_mai_10[i][j] = '계단 올라갔다 내려오기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['고정식 트레드밀에서 걷기']:
      df_y_mai_10[i][j] = '트레드밀에서 걷기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['누워서 굽힌 다리 펴기', '누워서 다리 좌우로 움직이기','누워서 하늘 자전거']:
      df_y_mai_10[i][j] = '누워 무릎 기울기'
for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['누워서 다리 들어올리기']:
      df_y_mai_10[i][j] = '누워 다리 들어올리기' 


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['덤벨 잡고 한발 내밀어 굽혔다 펴기']:
      df_y_mai_10[i][j] = '덤벨 잡고 앉았다 일어서기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['무릎 아래에서 양옆으로 굴리기']:
      df_y_mai_10[i][j] = '무릎굽혀 원 그리기' 


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['바벨 당겨 올리기','바벨 잡고 들어올리기']:
      df_y_mai_10[i][j] = '바벨들어올리기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['버피운동']:
      df_y_mai_10[i][j] = '버피테스트'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['사다리 옆으로 발 옮기기','사다리 좌우 뛰기','사다리 운동  루틴프로그램']:
      df_y_mai_10[i][j] = '사다리 운동 루틴 프로그램'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['스텝박스 오르내리기 ','스텝퍼 뛰어서 넘어가기','스텝퍼 옆으로 뛰어넘기','스템퍼 올라가서 점프하여 착지하기']:
      df_y_mai_10[i][j] = '스텝퍼 뛰어서 오르내리기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['고정식 자전거 타기']:
      df_y_mai_10[i][j] = '실내 자전거타기'
for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['자전거타기']:
      df_y_mai_10[i][j] = '자전거타기'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['앉아서 다리 밀기 ','앉아서 다리 펴기','앉아서 밀기']:
      df_y_mai_10[i][j] = '앉아서 다리 밀기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['어깨 올리기']:
      df_y_mai_10[i][j] = '회전근개 스트레칭'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['엉덩이 스트레칭2']:
      df_y_mai_10[i][j] = '엉덩이 스트레칭'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['엎드려서 팔 다리 들기','엎드려서 다리 차 올리기']:
      df_y_mai_10[i][j] = '엎드려 팔다리 교차올리기'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['윗몸 말아 올리기', '윗몸 일으키기','윗몸말아올리기','상체 감아올리기']:
      df_y_mai_10[i][j] = '윗몸올리기'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['빠르게 걷기']:
      df_y_mai_10[i][j] = '조깅'

for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['줄넘기 운동','1단 줄넘기']:
      df_y_mai_10[i][j] = '줄넘기'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['콘운동  루틴프로그램']:
      df_y_mai_10[i][j] = '순간반응 콘 찍기'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['팔굽혀 펴기','벽에서 팔굽혀 펴기']:
      df_y_mai_10[i][j] = '팔굽혀펴기'


for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    if df_y_mai_10[i][j] in ['서서 팔꿈치 펴기','앉아서 팔꿈치 굽히기','앉아서 팔꿈치 굽히기/펴기']:
      df_y_mai_10[i][j] = '팔꿈치 굽히기' 


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['계단 두 칸씩 뛰기','계단 두발 뛰어 오르기','계단 뛰어 오르기','계단 오르기','계단 한발 뛰기']:
      df_y_mai_20[i][j] = '계단 올라갔다 내려오기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['고정식 트레드밀에서 걷기']:
      df_y_mai_20[i][j] = '트레드밀에서 걷기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['누워서 굽힌 다리 펴기', '누워서 다리 좌우로 움직이기','누워서 하늘 자전거']:
      df_y_mai_20[i][j] = '누워 무릎 기울기'
for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['누워서 다리 들어올리기']:
      df_y_mai_20[i][j] = '누워 다리 들어올리기' 


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['덤벨 잡고 한발 내밀어 굽혔다 펴기']:
      df_y_mai_20[i][j] = '덤벨 잡고 앉았다 일어서기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['무릎 아래에서 양옆으로 굴리기']:
      df_y_mai_20[i][j] = '무릎굽혀 원 그리기' 


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['바벨 당겨 올리기','바벨 잡고 들어올리기']:
      df_y_mai_20[i][j] = '바벨들어올리기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['버피운동']:
      df_y_mai_20[i][j] = '버피테스트'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['사다리 옆으로 발 옮기기','사다리 좌우 뛰기', '사다리 운동  루팀프로그램']:
      df_y_mai_20[i][j] = '사다리 운동 루틴 프로그램'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['스텝박스 오르내리기 ','스텝퍼 뛰어서 넘어가기','스텝퍼 옆으로 뛰어넘기','스템퍼 올라가서 점프하여 착지하기']:
      df_y_mai_20[i][j] = '스텝퍼 뛰어서 오르내리기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['고정식 자전거 타기']:
      df_y_mai_20[i][j] = '실내 자전거타기'
for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['자전거타기']:
      df_y_mai_20[i][j] = '자전거타기'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['앉아서 다리 밀기 ','앉아서 다리 펴기','앉아서 밀기']:
      df_y_mai_20[i][j] = '앉아서 다리 밀기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['어깨 올리기']:
      df_y_mai_20[i][j] = '회전근개 스트레칭'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['엉덩이 스트레칭2']:
      df_y_mai_20[i][j] = '엉덩이 스트레칭'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['엎드려서 팔 다리 들기','엎드려서 다리 차 올리기']:
      df_y_mai_20[i][j] = '엎드려 팔다리 교차올리기'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['윗몸 말아 올리기', '윗몸 일으키기','윗몸말아올리기','상체 감아올리기']:
      df_y_mai_20[i][j] = '윗몸올리기'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['빠르게 걷기']:
      df_y_mai_20[i][j] = '조깅'

for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['줄넘기 운동','1단 줄넘기']:
      df_y_mai_20[i][j] = '줄넘기'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['콘운동  루틴프로그램']:
      df_y_mai_20[i][j] = '순간반응 콘 찍기'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['팔굽혀 펴기','벽에서 팔굽혀 펴기']:
      df_y_mai_20[i][j] = '팔굽혀펴기'


for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    if df_y_mai_20[i][j] in ['서서 팔꿈치 펴기','앉아서 팔꿈치 굽히기','앉아서 팔꿈치 굽히기/펴기']:
      df_y_mai_20[i][j] = '팔꿈치 굽히기' 


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['계단 두 칸씩 뛰기','계단 두발 뛰어 오르기','계단 뛰어 오르기','계단 오르기','계단 한발 뛰기']:
      df_y_mai_60[i][j] = '계단 올라갔다 내려오기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['고정식 트레드밀에서 걷기']:
      df_y_mai_60[i][j] = '트레드밀에서 걷기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['누워서 굽힌 다리 펴기', '누워서 다리 좌우로 움직이기','누워서 하늘 자전거']:
      df_y_mai_60[i][j] = '누워 무릎 기울기'
for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['누워서 다리 들어올리기']:
      df_y_mai_60[i][j] = '누워 다리 들어올리기' 


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['덤벨 잡고 한발 내밀어 굽혔다 펴기']:
      df_y_mai_60[i][j] = '덤벨 잡고 앉았다 일어서기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['무릎 아래에서 양옆으로 굴리기']:
      df_y_mai_60[i][j] = '무릎굽혀 원 그리기' 


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['바벨 당겨 올리기','바벨 잡고 들어올리기']:
      df_y_mai_60[i][j] = '바벨들어올리기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['버피운동']:
      df_y_mai_60[i][j] = '버피테스트'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['사다리 옆으로 발 옮기기','사다리 좌우 뛰기','사다리 운동 루팀  프로그램']:
      df_y_mai_60[i][j] = '사다리 운동 루틴 프로그램'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['스텝박스 오르내리기 ','스텝퍼 뛰어서 넘어가기','스텝퍼 옆으로 뛰어넘기','스템퍼 올라가서 점프하여 착지하기']:
      df_y_mai_60[i][j] = '스텝퍼 뛰어서 오르내리기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['고정식 자전거 타기']:
      df_y_mai_60[i][j] = '실내 자전거타기'
for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['자전거타기']:
      df_y_mai_60[i][j] = '자전거타기'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['앉아서 다리 밀기 ','앉아서 다리 펴기','앉아서 밀기']:
      df_y_mai_60[i][j] = '앉아서 다리 밀기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['어깨 올리기']:
      df_y_mai_60[i][j] = '회전근개 스트레칭'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['엉덩이 스트레칭2']:
      df_y_mai_60[i][j] = '엉덩이 스트레칭'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['엎드려서 팔 다리 들기','엎드려서 다리 차 올리기']:
      df_y_mai_60[i][j] = '엎드려 팔다리 교차올리기'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['윗몸 말아 올리기', '윗몸 일으키기','윗몸말아올리기','상체 감아올리기']:
      df_y_mai_60[i][j] = '윗몸올리기'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['빠르게 걷기']:
      df_y_mai_60[i][j] = '조깅'

for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['줄넘기 운동','1단 줄넘기']:
      df_y_mai_60[i][j] = '줄넘기'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['콘운동  루틴프로그램']:
      df_y_mai_60[i][j] = '순간반응 콘 찍기'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['팔굽혀 펴기','벽에서 팔굽혀 펴기']:
      df_y_mai_60[i][j] = '팔굽혀펴기'


for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    if df_y_mai_60[i][j] in ['서서 팔꿈치 펴기','앉아서 팔꿈치 굽히기','앉아서 팔꿈치 굽히기/펴기']:
      df_y_mai_60[i][j] = '팔꿈치 굽히기' 

a=[]
for i in range(len(df_y_mai_10)):
  for j in range(len(df_y_mai_10[i])):
    a.append(df_y_mai_10[i][j])

b=[]
for i in range(len(df_y_mai_20)):
  for j in range(len(df_y_mai_20[i])):
    b.append(df_y_mai_20[i][j])

c=[]
for i in range(len(df_y_mai_60)):
  for j in range(len(df_y_mai_60[i])):
    c.append(df_y_mai_60[i][j])

ar = np.zeros((387, 117))
ar1 = np.zeros((826, 112))
ar2 = np.zeros((133, 99))

df_ar = pd.DataFrame(ar)
df_ar1 = pd.DataFrame(ar1)
df_ar2 = pd.DataFrame(ar2)

colname_a = list(set(a))
colname_b = list(set(b))
colname_c = list(set(c))
colname_a.sort()
colname_b.sort()
colname_c.sort()

df_ar.columns = colname_a
df_ar1.columns = colname_b
df_ar2.columns = colname_c

for i in df_ar.columns:
  for j in range(len(df_y_mai_10)):
    if i in df_y_mai_10[j] :
      df_ar[i][j] = 1

for i in df_ar1.columns:
  for j in range(len(df_y_mai_20)):
    if i in df_y_mai_20[j] :
      df_ar1[i][j] = 1

for i in df_ar2.columns:
  for j in range(len(df_y_mai_60)):
    if i in df_y_mai_60[j] :
      df_ar2[i][j] = 1

a1=[]
for i in range(len(df_y_pre_10)):
  for j in range(len(df_y_pre_10[i])):
    a1.append(df_y_pre_10[i][j])

b1=[]
for i in range(len(df_y_pre_20)):
  for j in range(len(df_y_pre_20[i])):
    b1.append(df_y_pre_20[i][j])

c1=[]
for i in range(len(df_y_pre_60)):
  for j in range(len(df_y_pre_60[i])):
    c1.append(df_y_pre_60[i][j])


aar = np.zeros((239, 65))
aar1 = np.zeros((517, 60))
aar2 = np.zeros((124, 37))

df_aar = pd.DataFrame(aar)
df_aar1 = pd.DataFrame(aar1)
df_aar2 = pd.DataFrame(aar2)

colname_a1 = list(set(a1))
colname_b1 = list(set(b1))
colname_c1 = list(set(c1))
colname_a1.sort()
colname_b1.sort()
colname_c1.sort()

df_aar.columns = colname_a1
df_aar1.columns = colname_b1
df_aar2.columns = colname_c1

for i in df_aar.columns:
  for j in range(len(df_y_pre_10)):
    if i in df_y_pre_10[j] :
      df_aar[i][j] = 1

for i in df_aar1.columns:
  for j in range(len(df_y_pre_20)):
    if i in df_y_pre_20[j] :
      df_aar1[i][j] = 1

for i in df_aar2.columns:
  for j in range(len(df_y_pre_60)):
    if i in df_y_pre_60[j] :
      df_aar2[i][j] = 1

a2=[]
for i in range(len(df_y_las_10)):
  for j in range(len(df_y_las_10[i])):
    a2.append(df_y_las_10[i][j])

b2=[]
for i in range(len(df_y_las_20)):
  for j in range(len(df_y_las_20[i])):
    b2.append(df_y_las_20[i][j])

c2=[]
for i in range(len(df_y_las_60)):
  for j in range(len(df_y_las_60[i])):
    c2.append(df_y_las_60[i][j])

aaar = np.zeros((214, 49))
aaar1 = np.zeros((426, 25))
aaar2 = np.zeros((106, 28))

df_aaar = pd.DataFrame(aaar)
df_aaar1 = pd.DataFrame(aaar1)
df_aaar2 = pd.DataFrame(aaar2)

colname_a2 = list(set(a2))
colname_b2 = list(set(b2))
colname_c2 = list(set(c2))
colname_a2.sort()
colname_b2.sort()
colname_c2.sort()

df_aaar.columns = colname_a2
df_aaar1.columns = colname_b2
df_aaar2.columns = colname_c2

for i in df_aaar.columns:
  for j in range(len(df_y_las_10)):
    if i in df_y_las_10[j] :
      df_aaar[i][j] = 1

for i in df_aaar1.columns:
  for j in range(len(df_y_las_20)):
    if i in df_y_las_20[j] :
      df_aaar1[i][j] = 1

for i in df_aaar2.columns:
  for j in range(len(df_y_las_60)):
    if i in df_y_las_60[j] :
      df_aaar2[i][j] = 1


xgb_model = xgb.XGBRegressor(objective='reg:squarederror',
                             learning_rate =0.1,
                             n_estimators=100,
                             max_depth=3,
                             gamma=0.1,  
)


AGE_NUM = 65

if AGE_NUM >= 60 : 
  x_jh = [174.7, 69.2, 2, 80.3, -24.5, 26,20,5,20, 2, 0,1]
  x_jh = pd.DataFrame(x_jh)
  x_jh = x_jh.transpose()
  x_jh.columns = ['ITEM_F001','ITEM_F002','ITEM_F003','ITEM_F004','ITEM_F012','ITEM_F019',
                'ITEM_F023','ITEM_F026','ITEM_F027','BP','TEST_SEX_F','TEST_SEX_M']
  x = x_jh
else :

  x_jh = [174.7, 69.2, 2, 80.3, -24.5, 26, 215, 2, 0,1]
  x_jh = pd.DataFrame(x_jh)
  x_jh = x_jh.transpose()
  x_jh.columns = ['ITEM_F001','ITEM_F002','ITEM_F003','ITEM_F004','ITEM_F012','ITEM_F019',
                  'ITEM_F022','BP','TEST_SEX_F','TEST_SEX_M']
  x = x_jh




if AGE_NUM < 20 :
  re = []
  for i in df_aar.columns:
    re.append(xgb_model.fit(df_pre_10, df_aar[i]).predict(x)[0])

  re1 = []
  for i in df_ar.columns:
    re1.append(xgb_model.fit(df_mai_10, df_ar[i]).predict(x)[0])

  re2 = []
  for i in df_aaar.columns:
    re2.append(xgb_model.fit(df_las_10, df_aaar[i]).predict(x)[0])

  p_ind=[]
  re_se = sorted(re)
  re_se.reverse()
  for i in re:
    p_ind.append(re_se.index(i)+1)

  p_ind1=[]
  re_se1 = sorted(re1)
  re_se1.reverse()
  for i in re1:
    p_ind1.append(re_se1.index(i)+1)

  p_ind2=[]
  re_se2 = sorted(re2)
  re_se2.reverse()
  for i in re2:
    p_ind2.append(re_se2.index(i)+1)

  aa=[]
  for i in range(len(p_ind)):
    if p_ind[i] <= 3:
      aa.append(i)

  bb=[]
  for i in range(len(p_ind1)):
    if p_ind1[i] <= 3:
      bb.append(i)

  cc=[]
  for i in range(len(p_ind2)):
    if p_ind2[i] <= 3:
      cc.append(i)

  #준비운동
  pre_result1 = df_aar.columns[aa[0]]
  pre_result2 = df_aar.columns[aa[1]]
  pre_result3 = df_aar.columns[aa[2]]

  #본운동
  main_result1 = df_ar.columns[bb[0]]
  main_result2 = df_ar.columns[bb[1]]
  main_result3 = df_ar.columns[bb[2]]

  #마무리운동
  print(df_aaar.columns[cc[0]])
  print(df_aaar.columns[cc[1]])
  print(df_aaar.columns[cc[2]])
elif AGE_NUM < 60 :
  ree = []
  for i in df_aar1.columns:
    ree.append(xgb_model.fit(df_pre_20, df_aar1[i]).predict(x)[0])

  ree1 = []
  for i in df_ar1.columns:
    ree1.append(xgb_model.fit(df_mai_20, df_ar1[i]).predict(x)[0])

  ree2 = []
  for i in df_aaar1.columns:
    ree2.append(xgb_model.fit(df_las_20, df_aaar1[i]).predict(x)[0])

  pp_ind=[]
  ree_se = sorted(ree)
  ree_se.reverse()
  for i in ree:
    pp_ind.append(ree_se.index(i)+1)

  pp_ind1=[]
  ree_se1 = sorted(ree1)
  ree_se1.reverse()
  for i in ree1:
    pp_ind1.append(ree_se1.index(i)+1)

  pp_ind2=[]
  ree_se2 = sorted(ree2)
  ree_se2.reverse()
  for i in ree2:
    pp_ind2.append(ree_se2.index(i)+1)

  aaa=[]
  for i in range(len(pp_ind)):
    if pp_ind[i] <= 3:
      aaa.append(i)

  bbb=[]
  for i in range(len(pp_ind1)):
    if pp_ind1[i] <= 3:
      bbb.append(i)

  ccc=[]
  for i in range(len(pp_ind2)):
    if pp_ind2[i] <= 3:
      ccc.append(i)

  #준비운동
  pre_result1 = df_aar1.columns[aaa[0]]
  pre_result2 = df_aar1.columns[aaa[1]]
  pre_result3 = df_aar1.columns[aaa[2]]


  #본운동
  main_result1 = df_ar1.columns[bbb[0]]
  main_result2 = df_ar1.columns[bbb[1]]
  main_result3 = df_ar1.columns[bbb[2]]

  #마무리운동
  last_result1 = df_aaar1.columns[ccc[0]]
  last_result2 = df_aaar1.columns[ccc[1]]
  last_result3 = df_aaar1.columns[ccc[2]]

elif AGE_NUM >= 28 :
  reee = []
  for i in df_aar2.columns:
    reee.append(xgb_model.fit(df_pre_60, df_aar2[i]).predict(x)[0])

  reee1 = []
  for i in df_ar2.columns:
    reee1.append(xgb_model.fit(df_mai_60, df_ar2[i]).predict(x)[0])

  reee2 = []
  for i in df_aaar2.columns:
    reee2.append(xgb_model.fit(df_las_60, df_aaar2[i]).predict(x)[0])

  ppp_ind=[]
  reee_se = sorted(reee)
  reee_se.reverse()
  for i in reee:
    ppp_ind.append(reee_se.index(i)+1)

  ppp_ind1=[]
  reee_se1 = sorted(reee1)
  reee_se1.reverse()
  for i in reee1:
    ppp_ind1.append(reee_se1.index(i)+1)

  ppp_ind2=[]
  reee_se2 = sorted(reee2)
  reee_se2.reverse()
  for i in reee2:
    ppp_ind2.append(reee_se2.index(i)+1)

  aaaa=[]
  for i in range(len(ppp_ind)):
    if ppp_ind[i] <= 3:
      aaaa.append(i)

  bbbb=[]
  for i in range(len(ppp_ind1)):
    if ppp_ind1[i] <= 3:
      bbbb.append(i)

  cccc=[]
  for i in range(len(ppp_ind2)):
    if ppp_ind2[i] <= 3:
      cccc.append(i)

  #준비운동
  pre_result1 = df_aar2.columns[aaaa[0]]
  pre_result2 = df_aar2.columns[aaaa[1]]
  pre_result3 = df_aar2.columns[aaaa[2]]


  #본운동
  main_result1 = df_ar2.columns[bbbb[0]]
  main_result2 = df_ar2.columns[bbbb[1]]
  main_result3 = df_ar2.columns[bbbb[2]]


  #마무리운동
  last_result1 = df_aaar2.columns[cccc[0]]
  last_result2 = df_aaar2.columns[cccc[1]]
  last_result3 = df_aaar2.columns[cccc[2]]


pre_result = [pre_result1,pre_result2,pre_result3]

main_result = [main_result1,main_result2,main_result3]

last_result = [last_result1,last_result2,last_result3]

all_result = [pre_result1,pre_result2,pre_result3, main_result1,main_result2,main_result3, last_result1,last_result2,last_result3]



