import pandas as pd
import numpy as np

#Data 
raw_data=pd.read_csv('SPX.csv')



#Add shift for analysis
raw_data['Yesterday']=raw_data['Close'].shift(1)

#Pruning columns
raw_data=raw_data[['Close', 'Yesterday']]


raw_data['Move']=raw_data['Yesterday']-raw_data['Close']


#Log=returns of SP500
raw_data['Return']=np.log((raw_data['Close']/raw_data['Yesterday']))



raw_data=raw_data.drop([0]) #Drop non-valid return
print(raw_data.head())

#Hyperparameter
magnitude=0.01

#Filter function for market letters

def token_market(x):
    
    if (((x>0) & (np.abs(x)>=magnitude))):
        return 1
    if (((x>0) & (np.abs(x)<magnitude))):
        return 2
    if (((x<=0) & (np.abs(x)>=magnitude))):
        return 3
    if (((x<=0) & (np.abs(x)<magnitude))):
        return 4


#Use function elementwise
# raw_data['M_Letter']=raw_data.apply(lambda x: token_market(x['Return']), axis=1)
# print(raw_data['M_Letter'].head())

#Mapping alternativly 
return_arr=raw_data['Return'].to_numpy()

tokens=[]
for item in return_arr:
    tokens.append(token_market(item))


print(tokens[:10])

#Prepare data for saving
with open('market_tokens.txt', 'w+') as f:
    
    # write elements of list
    for items in tokens:
        f.write('%s\n' %items)
    
    print("File written successfully")

f.close()
