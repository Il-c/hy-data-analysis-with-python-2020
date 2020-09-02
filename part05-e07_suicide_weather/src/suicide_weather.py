#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    top40 = pd.read_csv('src/who_suicide_statistics.csv',sep=',')
    top40=top40.dropna(subset=['suicides_no'])
    top40['suicides_no']=top40.suicides_no/top40.population
    tulos=top40.groupby('country').mean()
    group=tulos.suicides_no
    return group

def suicide_weather():
    weather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html',index_col=0,header=0)
    weather=weather[0]
    weather=weather['Average yearly temperature (1961–1990, degrees Celsius)'].apply(lambda x: float(x.replace("\u2212", "-")))
    suicides=suicide_fractions()
    whole=pd.concat([suicides,weather],axis=1,join='inner')
    result=whole['suicides_no'].corr(whole['Average yearly temperature (1961–1990, degrees Celsius)'],method='spearman')
    return (suicides.shape[0], weather.shape[0], whole.shape[0], result)

def main():
    s,w,wh,c = suicide_weather()
    print(f"Suicide DataFrame has {s} rows \nTemperature DataFrame has {w} rows\nCommon DataFrame has {wh} rows\nSpearman correlation: {c}")
    return

if __name__ == "__main__":
    main()
