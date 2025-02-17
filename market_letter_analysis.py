import pandas as pd
import numpy as np

#Data 
df=pd.read_csv('Market_Letters.csv')

#print(df.head())

#Function for comparing

def letter_compare (a, b):
    
    if (a==b):
        return 1
    else:
        return 0

#Check the result
df['check'] = df.apply(lambda x: letter_compare(a = x['forecast'], b = x['true']), axis=1)
#print(df['check'].head())
result=df['check'].sum()/len(df['check'])
print(result) #result=0,3477 higher than 0.25 if prediction was randome 

#Compare with alternative strategy
df['previous']=df['true'].shift(1)
#print(df['previous'].head())

df['alt_strategy']=df.apply(lambda x: letter_compare(a=x['true'], b=x['previous']), axis=1)
#print(df['alt_strategy'].head())
alt_result=df['alt_strategy'].sum()/len(df['alt_strategy'])
print(alt_result) #alt_result=0.3516 almost same as result. Transformer is not better than copying previous movement. But use different logic



#Check different letters

def check_letter(a, b, letter):
    
    if (a==letter) & (a==b):
        return 1
    if (a!=letter):
        return 0
    if (a==letter) &(a!=b):
        return -1


print(df['forecast'].value_counts())
print(df['true'].value_counts())

#Compare forecast for each market letter

df['check_letter_1']=df.apply(lambda x:check_letter(a=x['forecast'], b=x['true'], letter=1), axis=1)

print(df['check_letter_1'].value_counts()[1]/(df['check_letter_1'].value_counts()[1]+df['check_letter_1'].value_counts()[-1]))

df['check_letter_2']=df.apply(lambda x:check_letter(a=x['forecast'], b=x['true'], letter=2), axis=1)

print(df['check_letter_2'].value_counts()[1]/(df['check_letter_2'].value_counts()[1]+df['check_letter_2'].value_counts()[-1]))

df['check_letter_3']=df.apply(lambda x:check_letter(a=x['forecast'], b=x['true'], letter=3), axis=1)
print(df['check_letter_3'].value_counts()[1]/(df['check_letter_3'].value_counts()[1]+df['check_letter_3'].value_counts()[-1]))

df['check_letter_4']=df.apply(lambda x:check_letter(a=x['forecast'], b=x['true'], letter=4), axis=1)
print(df['check_letter_4'].value_counts()[1]/(df['check_letter_4'].value_counts()[1]+df['check_letter_4'].value_counts()[-1]))

# Check failure

def check_failure (a, b, letter, anti_letter):
    
    if (a==letter) & (a==b):
        return 1
    if (a==letter) & (a!=b) & (b==anti_letter):
        return -1
    else:
        return 0

df['check_failure_1']=df.apply( lambda x: check_failure(a=x['forecast'], b=x['true'], letter=1, anti_letter=4), axis=1)
print(df['check_failure_1'].sum())

df['check_failure_2']=df.apply( lambda x: check_failure(a=x['forecast'], b=x['true'], letter=2, anti_letter=4), axis=1)
print(df['check_failure_2'].sum())

df['check_failure_3']=df.apply( lambda x: check_failure(a=x['forecast'], b=x['true'], letter=3, anti_letter=4), axis=1)
print(df['check_failure_3'].sum())

df['check_failure_4']=df.apply( lambda x: check_failure(a=x['forecast'], b=x['true'], letter=4, anti_letter=3), axis=1)
print(df['check_failure_4'].sum())


#Check intersection

def strat_intersection (a,b,c):
    if (a==b)& (a==c):
        return 1
    
    if (a==b)&(a!=c):
        return -1
    
    else:
        return 0

df['strat_inter']=df.apply(lambda x: strat_intersection(a=x['forecast'], b=x['previous'], c=x['true']), axis=1)
print(df['strat_inter'].sum()/len(df['strat_inter']))
print(df['strat_inter'].value_counts())
print(df['strat_inter'].value_counts()[1]/(df['strat_inter'].value_counts()[1]+df['strat_inter'].value_counts()[-1]))