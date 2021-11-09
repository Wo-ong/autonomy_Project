import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('C:/Users/jeonghun7898/PycharmProjects/webservice/webservice/DATA_P.csv', encoding='utf-8')
df_1 = df.drop(['TEST_CNT','AGE_GBN','CENTER_NM','TEST_GBN','INPUT_GBN','CERT_GBN','TEST_YMD','PRES_NOTE','ITEM_F011','ITEM_F029','ITEM_F038','ITEM_F039'],axis=1)


df_10 = df_1[df_1['TEST_AGE'] < 20]
df_20_30 = df_1[(df_1['TEST_AGE'] >= 20) & (df_1['TEST_AGE'] < 60)]
df_60 = df_1[df_1['TEST_AGE'] >= 60]


df_10 = df_10.drop(['ITEM_F003','ITEM_F007','ITEM_F009','ITEM_F013','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F018','ITEM_F020','ITEM_F021','ITEM_F023','ITEM_F024','ITEM_F025','ITEM_F026','ITEM_F027','ITEM_F028','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037','ITEM_F040','ITEM_F041'],axis=1)

df_20_30 = df_20_30.drop(['ITEM_F003','ITEM_F007','ITEM_F009','ITEM_F010','ITEM_F013','ITEM_F014','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F018','ITEM_F020','ITEM_F021','ITEM_F023','ITEM_F024','ITEM_F025','ITEM_F026','ITEM_F027','ITEM_F028','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037','ITEM_F040','ITEM_F041'],axis=1)

df_60 = df_60.drop(['ITEM_F003','ITEM_F007','ITEM_F009','ITEM_F010','ITEM_F013','ITEM_F014','ITEM_F015','ITEM_F016','ITEM_F017','ITEM_F018','ITEM_F020','ITEM_F021','ITEM_F024','ITEM_F025','ITEM_F026','ITEM_F027','ITEM_F028','ITEM_F030','ITEM_F031','ITEM_F032','ITEM_F033','ITEM_F034','ITEM_F035','ITEM_F036','ITEM_F037','ITEM_F040','ITEM_F041'],axis=1)


df_10['ITEM_F010'] = df_10['ITEM_F010'].fillna(df_10['ITEM_F010'].mean())
df_10['ITEM_F014'] = df_10['ITEM_F014'].fillna(df_10['ITEM_F014'].mean())
df_10['ITEM_F019'] = df_10['ITEM_F019'].fillna(df_10['ITEM_F019'].mean())
df_10['ITEM_F022'] = df_10['ITEM_F022'].fillna(df_10['ITEM_F022'].mean())

df_20_30['ITEM_F008'] = df_20_30['ITEM_F008'].fillna(df_20_30['ITEM_F008'].mean())
df_20_30['ITEM_F012'] = df_20_30['ITEM_F012'].fillna(df_20_30['ITEM_F012'].mean())
df_20_30['ITEM_F019'] = df_20_30['ITEM_F019'].fillna(df_20_30['ITEM_F019'].mean())
df_20_30['ITEM_F022'] = df_20_30['ITEM_F022'].fillna(df_20_30['ITEM_F022'].mean())


df_60['ITEM_F019'] = df_60['ITEM_F019'].fillna(df_60['ITEM_F019'].mean())
df_60['ITEM_F022'] = df_60['ITEM_F022'].fillna(df_60['ITEM_F022'].mean())
df_60['ITEM_F023'] = df_60['ITEM_F023'].fillna(df_60['ITEM_F023'].mean())


df_10 = pd.get_dummies(df_10, columns = ['TEST_SEX'])
X_10 = df_10

df_20_30 = pd.get_dummies(df_20_30, columns = ['TEST_SEX'])
X_20_30 = df_20_30

df_60 = pd.get_dummies(df_60, columns = ['TEST_SEX'])
X_60 = df_60

for i in range(len(df)):
  if df['PRES_NOTE'][i][:3] == '본운동':
    df['PRES_NOTE'][i] = ' / '+ df['PRES_NOTE'][i]

df['준비운동'] = df.PRES_NOTE.str.split(' / ').str[0]
df['본운동'] = df.PRES_NOTE.str.split(' / ').str[1]
df['마무리운동'] = df.PRES_NOTE.str.split(' / ').str[2]

y_10_1 = df[df['TEST_AGE'] < 20]['준비운동']
y_10_2 = df[df['TEST_AGE'] < 20]['본운동']
y_10_3 = df[df['TEST_AGE'] < 20]['마무리운동']

y_20_30_1 = df[(df['TEST_AGE'] >= 20) & (df['TEST_AGE'] < 60)]['준비운동']
y_20_30_2 = df[(df['TEST_AGE'] >= 20) & (df['TEST_AGE'] < 60)]['본운동']
y_20_30_3 = df[(df['TEST_AGE'] >= 20) & (df['TEST_AGE'] < 60)]['마무리운동']

y_60_1 = df[df['TEST_AGE'] >= 60]['준비운동']
y_60_2 = df[df['TEST_AGE'] >= 60]['본운동']
y_60_3 = df[df['TEST_AGE'] >= 60]['마무리운동']

y_10_1[y_10_1 == ''] = '준비운동:깍지 끼고 상체 숙이기,양팔 벌려 전신 비틀기'
y_10_2 = y_10_2.fillna('본운동:누워서 엉덩이 들어올리기, 네발기기 자세로 팔 다리 들기,배스트레칭,엉덩이 스트레칭,넙다리 뒤쪽 스트레칭,넙다리 안쪽 스트레칭,트레드밀에서 걷기,실내 자전거타기,수영,계단 올라갔다 내려오기')
y_10_3 = y_10_3.fillna('마무리운동:마무리운동:내전근 스트레칭,대퇴사두근 스트레칭')

y_20_30_1[y_20_30_1 == '']= '준비운동:하지 루틴 스트레칭1,상지 루틴 스트레칭,하지 루틴 스트레칭2,전신 루틴 스트레칭'
y_20_30_2 = y_20_30_2.fillna('본운동:누워서 엉덩이 들어올리기,네발기기 자세로 팔 다리 들기,배스트레칭,엉덩이 스트레칭,넙다리 뒤쪽 스트레칭,넙다리 안쪽 스트레칭,트레드밀에서 걷기,실내 자전거타기,수영,계단 올라갔다 내려오기')
y_20_30_3 = y_20_30_3.fillna('마무리운동:자가근막이완술 루틴 스트레칭')

y_60_1[y_60_1 == '']= '준비운동:실내 자전거타기,트레드밀에서 걷기,전신 루틴 스트레칭,목 스트레칭,가슴/어깨 앞쪽 스트레칭'
y_60_2 = y_60_2.fillna('본운동:줄넘기,수영,엉덩관절 회전하기,무릎 높이 들어 뛰기,스텝퍼 뛰어서 오르내리기')
y_60_3 = y_60_3.fillna('마무리운동:자가근막이완술 루틴 스트레칭')





model_10_warmup = LogisticRegression(C=10, max_iter=100).fit(X_10,y_10_1)
model_10_main = LogisticRegression(C=10, max_iter=100).fit(X_10,y_10_2)
model_10_finish = LogisticRegression(C=10, max_iter=100).fit(X_10,y_10_3)

model_20_warmup = LogisticRegression(C=10, max_iter=100).fit(X_20_30,y_20_30_1)
model_20_main = LogisticRegression(C=10, max_iter=100).fit(X_20_30,y_20_30_2)
model_20_finish = LogisticRegression(C=10, max_iter=100).fit(X_20_30,y_20_30_3)


model_60_warmup = LogisticRegression(C=10, max_iter=100).fit(X_60,y_60_1)
model_60_main = LogisticRegression(C=10, max_iter=100).fit(X_60,y_60_2)
model_60_finish = LogisticRegression(C=10, max_iter=100).fit(X_60,y_60_3)


pickle.dump(model_10_warmup, open('10_warmup.pkl', 'wb'))
pickle.dump(model_10_main, open('10_main.pkl', 'wb'))
pickle.dump(model_10_finish, open('10_finish.pkl', 'wb'))

pickle.dump(model_20_warmup, open('20_warmup.pkl', 'wb'))
pickle.dump(model_20_main, open('20_main.pkl', 'wb'))
pickle.dump(model_20_finish, open('20_finish.pkl', 'wb'))

pickle.dump(model_60_warmup, open('60_warmup.pkl', 'wb'))
pickle.dump(model_60_main, open('60_main.pkl', 'wb'))
pickle.dump(model_60_finish, open('60_finish.pkl', 'wb'))