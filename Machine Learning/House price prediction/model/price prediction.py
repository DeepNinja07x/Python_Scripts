import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["figure.figsize"]=(20,10)


df=pd.read_csv(r"D:\ML\Data sets\project 1 (house price)\house data.csv") #reading data

                                   #DATA PREPROCESSING

df0=df.drop(['area_type','availability','society','balcony'],axis='columns')                      # droping colunms
#print(df0.isnull().sum())                                      #checking for null values before preprocessing data
final_df=df0.dropna()
#print(final_df.isnull().sum())                                       #checking for null values after preprocessing data

#print(final_df['size'].unique())                                         #checking for the unique values in size column

final_df['BHK']=final_df['size'].apply(lambda x:int(x.split(' ')[0]))            #new clm having int values for bedrooms
df1=final_df.drop(['size'],axis='columns')                                                          #droping size column
#print(df1['total_sqft'].unique())                                                        #checking for non uniform data

def isfloat(x):                                                              #function for checking for non uniform data
    try:
        float(x)
    except:
        return False
    return True
#print(df1[~df1['total_sqft'].apply(isfloat)].head(10))                                   #checking for non uniform data


def sqft_to_num(x):                                                          #function for changing diff values in float
    tokens=x.split("-")
    if(len(tokens)==2):
        return(float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

df2=df1.copy()
df2["total_sqft"]=df2["total_sqft"].apply(sqft_to_num)                             #changing diff values in float values
#print(df2['total_sqft'].unique())

                             #FEATURE ENGINEERING

df3=df2.copy()
df3['price_per_sqft']=df3['price']*100000/df3['total_sqft']                                     #creating a new feature

#print(len(df3['location'].unique()))

df3['location']=df3['location'].apply(lambda x: x.strip())                   #removing extra spaces from location values

#removing problem of having so many dummy columns since the unique locations value is 1304 by categorising them in "other"

location_stats=df3.groupby('location')["location"].agg("count").sort_values(ascending=False)
#print(location_stats)
#print(len(location_stats[location_stats<=10]))

location_stats_less_than_10=location_stats[location_stats<=10]
#print(location_stats_less_than_10)

#print(len(df3['location'].unique()))

df3["location"]=df3["location"].apply(lambda x: "other" if x in location_stats_less_than_10 else x)
#print(len(df3['location'].unique()))

                               #FINDING AND REMOVING OUTLIERS

#print(df3[df3.total_sqft/df3.BHK<300].head())
df4=df3[~(df3.total_sqft/df3.BHK<300)]
#print(df4.shape)

#print(df4.price_per_sqft.describe())

def remove_pps_outliers(df):                                                    #removing price_per_sqft column outliers
    df_out=pd.DataFrame()
    for key,subdf in df.groupby("location"):
        m=np.mean(subdf.price_per_sqft)
        st=np.std(subdf.price_per_sqft)
        reduced_df=subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out=pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out

df5=remove_pps_outliers(df4)
#print(df5.shape)

def plot_scatter_chart(df,location):                                     #plottinig chart btw square feet area and price
    bhk2=df[(df.location==location) & (df.BHK==2)]
    bhk3=df[(df.location==location) & (df.BHK==3)]
    matplotlib.rcParams["figure.figsize"]=(15,10)
    plt.scatter(bhk2.total_sqft,bhk2.price,color="blue",label="2 BHK",s=50)
    plt.scatter(bhk3.total_sqft,bhk3.price,marker="+",color="green",label="3 BHK",s=50)
    plt.xlabel("Total square feet area")
    plt.ylabel("price")
    plt.title(location)
    plt.legend()
    plt.show()

#plot_scatter_chart(df5,"Rajaji Nagar")

def remove_bhk_outliers(df):                                                              #removing BHK columns outliers
    exclude_indices=np.array([])
    for location,location_df in df.groupby("location"):
        bhk_stats={}
        for bhk,bhk_df in location_df.groupby("BHK"):
            bhk_stats[bhk]={
                "mean":np.mean(bhk_df.price_per_sqft),
                "std":np.std(bhk_df.price_per_sqft),
                "count":bhk_df.shape[0]
            }
        for bhk,bhk_df in location_df.groupby("BHK"):
            stats=bhk_stats.get(bhk-1)
            if stats and stats["count"]>5:
                exclude_indices=np.append(exclude_indices,bhk_df[bhk_df.price_per_sqft<(stats["mean"])].index.values)
    return df.drop(exclude_indices,axis="index")

df6=remove_bhk_outliers(df5)
#print(df6.shape)

#plot_scatter_chart(df6,"Rajaji Nagar")

import matplotlib                                                           #plotting chart btw price_per_sqft and count
matplotlib.rcParams["figure.figsize"]=(20,10)
plt.hist(df6.price_per_sqft*0.8)
plt.xlabel("price per square feet")
plt.ylabel("count")
#plt.show()

#print(df6.bath.unique())
#print(df6[df6.bath>10])

plt.hist(df6.bath,rwidth=0.8)                                          #plotting chart btw Number of bathrooms and count
plt.xlabel("Number of bathrooms")
plt.ylabel("count")

#plt.show()

#print(df6[df6.bath>df6.BHK+2])

df7=df6[df6.bath<df6.BHK+2]
#print(df7.shape)

                                    #MODEL BUILDING

df8=df7.drop(["price_per_sqft"],axis="columns")

dummies=pd.get_dummies(df8.location)                              #creating dummy columns for categoial column locations
#print(dummies.head(3))

df9=pd.concat([df8,dummies.drop(["other"],axis="columns")],axis="columns")         #making complete numerical data frame
df10=df9.drop(["location"],axis="columns")

x=df10.drop(["price"],axis="columns")                                      # creating dataframe of independent variables
y=df10.price                                                                  # creating dataframe of dependent variable
#print(x.head(3))
#print(y.head(3))

from sklearn.model_selection import train_test_split                    #splitting data into test data and training data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)

from sklearn.model_selection import GridSearchCV        #finding best model,score,parameters for data using GridSearchCV
from sklearn.linear_model import Lasso                                                      # Lasso model for evaluation
from sklearn.tree import DecisionTreeRegressor                                        #Dession Tree model for Evaluation
from sklearn.linear_model import LinearRegression                                 #LinearRegression model for evaluation
from sklearn.model_selection import ShuffleSplit                                                 #for shuffling the data
from sklearn.model_selection import cross_val_score      #K_fold model for finding diff score of model at different data



def find_best_model_using_gridsearchcv(x,y):                           #Applying GridSearchCV method on different models
    algos={
        "linear_regression": {
                "model":LinearRegression(),
                 "params": {
                      "normalize":[True,False]
                 }
        },

        "Lasso": {
                 "model":Lasso(),
                 "params": {
                      "alpha":[1,2],
                      "selection":["random","cyclic"]
                 }
        },

        "decision tree" : {
                 "model":DecisionTreeRegressor(),
                 "params": {
                       "criterion":["mse","friedman_mse"],
                       "splitter":["best","random"]
                 }
        }

    }

    scores=[]
    cv=ShuffleSplit(n_splits=15,test_size=0.2,random_state=0)
    for algo_name,config in algos.items():
        gs=GridSearchCV(config["model"],config["params"],cv=cv,return_train_score=False)
        gs.fit(x,y)
        scores.append({
            "model" : algo_name,
            "best_score" : gs.best_score_,
            "best_params" : gs.best_params_
        })
    return pd.DataFrame(scores,columns=["model","best_score","best_params"])

#print(find_best_model_using_gridsearchcv(x,y))                              #getting the best model,score and parameters
#Linear Regression model has most score among all tested models so we create LinearRegression model
model=LinearRegression()                                                             #creating a linear regression model
model.fit(x_train,y_train)
#print(model.score(x_test,y_test))

cv=ShuffleSplit(n_splits=15,test_size=0.2,random_state=0)     #By k_fold validation checking score of model at diff data
#print(cross_val_score(LinearRegression(),x,y,cv=cv))

def predict_price(location,sqft,bath,BHK):                                                #function for price prediction
    loc_index=np.where(x.columns==location)[0][0]
    X=np.zeros(len(x.columns))
    X[0]=sqft
    X[1]=bath
    X[2]=BHK
    if loc_index>=0:
        X[loc_index]=1
    return model.predict([X])[0]

print(round(predict_price("Indira Nagar",1000,3,3)),2)                                                        # predicting price

                               # TRANSFERRING IN PICKEL FILE AND JSON FILE

import pickle                                                                         #transferring model in pickel file
with open("banglore_home_price_predict_model.pickel","wb") as f:
    pickle.dump(model,f)

import json                                                                      #transferring columns info in json file
columns={
    "data_columns":[col.lower() for col in x.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))





























