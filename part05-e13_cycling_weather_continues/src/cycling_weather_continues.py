#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def cycling_weather():
    weather_data=pd.read_csv('kumpula-weather-2017.csv')
    weather_data.rename(columns={'m':'month','d':'day'},inplace=True)
    weather_data['Päivämäärä']=pd.to_datetime(weather_data[['Year','month','day']])
    weather_data = weather_data.set_index('Päivämäärä')
    weather_data = weather_data.drop(columns=['Year','month','day','Time','Time zone'],axis=1)
    cyclist_data=split_date_continues()
   
    cyclist_data['Päivämäärä']=pd.to_datetime(cyclist_data[['Year','Month','Day','Hour']])
    cyclist_data = cyclist_data.set_index('Päivämäärä')
    cyclist_data = cyclist_data.drop(columns=['Year','Month','Day','Weekday','Hour'],axis=1)
    daily_sums= cyclist_data.groupby(pd.Grouper(freq='D')).sum()
    daily_sums=daily_sums['2017-01-01':'2017-12-31']
    #daily_sums=daily_sums.reset_index()
   

    result = pd.merge(daily_sums,weather_data, right_on=['Päivämäärä'],left_on=['Päivämäärä'])
   # result = result.drop(columns=['m','d','Time','Time zone'])
   
    return result

def split_date(data):
    data=data['Päivämäärä'].str.split(expand=True)
    data.columns=['Weekday','Day','Month','Year','Hour']

    data.Month = data.Month.map({'tammi':1,'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7,'elo':8,'syys':9,'loka':10,'marras':11,'joulu':12})
    data.Weekday = data.Weekday.map({'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'})
    data.Hour = data.Hour.str.split(':',expand=True)
    data = data.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return data

def split_date_continues():
    data = pd.read_csv('Helsingin_pyorailijamaarat.csv',sep=';')
    data=data.dropna(how='all')
    data=data.dropna(axis=1,how='all')
    split_data=split_date(data)
    result=pd.concat([split_data,data],axis=1)
    result=result.drop(columns=['Päivämäärä'],axis=1)
    return result


def cycling_weather_continues(station):
    data = cycling_weather()
    data = data.fillna(method='ffill',axis=0)
    X=data[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)']]
    X['koe']=data['Precipitation amount (mm)']**2
    X['koe1']=data['Snow depth (cm)']**2
    X['koe2']=data['Air temperature (degC)']**2
    X['koe3']=data['Precipitation amount (mm)']**3
    X['koe4']=data['Snow depth (cm)']**3
    X['koe5']=data['Air temperature (degC)']**3
    #print(X)
    
    y=data[station]
    model=LinearRegression(fit_intercept=True)
  #  print(data[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)','Merikannontie']])
  #  model.fit(daily_sums[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)']], daily_sums[station])
  #  score =model.score(daily_sums[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)']],daily_sums[station])
    model.fit(X,y)
    score =model.score(X,y)
  #  input = np.array([[50,15,40]])
  #  print(model.predict(input))
    xfit=np.linspace(0,35,365)
    yfit=xfit*model.coef_[0] + model.intercept_
    tfit=xfit*model.coef_[1] + model.intercept_
    zfit=xfit*model.coef_[2] + model.intercept_
   # ffit=xfit*model.coef_[0]+(xfit**2)*(model.coef_[3])+model.intercept_

    plt.plot(data[['Precipitation amount (mm)','Snow depth (cm)','Air temperature (degC)']],y, 'o')
    plt.plot(xfit,yfit,color='red')
    plt.plot(xfit,zfit,color='green')
    plt.plot(xfit,tfit,color='purple')
   # plt.plot(xfit,ffit,color='black')
    #plt.plot(xfit,yf,'x')
  #  plt.show()
    return ((model.coef_[0], model.coef_[1], model.coef_[2]), score)
    
def main():
    station = 'Merikannontie'
    coefs, score = cycling_weather_continues(station)
    variables=['precipitation','snow depth','temperature']
    print(f'Measuring station: {station}')
    for i,j in enumerate(variables):
        print(f'Regression coefficient for variable \'{j}\': {coefs[i]:.1f}')
    print(f'Score: {score:.2f}')
    return

if __name__ == "__main__":
    main()
