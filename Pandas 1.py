import pandas as pd

covid_df=pd.read_csv("/content/italy-covid-daywise.csv")

covid_df

covid_df.info()

covid_df.describe()

covid_df.columns

covid_df.shape

covid_data_dict={
    'date':['202-08-30',]
}

type(covid_df)

type(covid_df['new_cases'])

covid_df['new_cases'][246]

covid_df.loc[244]

covid_df['new_cases']

covid_df.head(20)

covid_df.tail(248)

covid_df.at["new_cases",2]

covid_df.sample(28)

total_cases=covid_df.new_cases.sum()
total_death=covid_df.new_deaths.sum()
death_rate=(total_death/total_cases)*100
print("death rate is ",death_rate,"%")

