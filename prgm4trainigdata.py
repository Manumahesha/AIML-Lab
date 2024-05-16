import pandas as pd
df=pd.read_csv('EnjoySport.csv')
concepts=df.values[:,:-1]
target=df.values[:,-1]
df.head()

def learn(concepts,target):
    specific_h=concepts[0],copy()
    generate_h=[["?"for i in range(len(specific_h))]for i in range(len(specific_h))]
    for i,h in enamurate(concets):
        if target[i]=="yes":
            for x in range(len(specifc_h)):
                if h[x]!=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
                if taget[i]=="no":
                     for x in range(len(specifc_h)):
                        if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]='?'
                    else:
                        general_h[x][x]='?'
