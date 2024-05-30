def infoGain(P,N):
    import math
    return -P/(P+N)*math.log2(P/(P+N))-N/(P+N)*math.log2(N/(P+N))

def insertNode(tree, addTo,Node):
    for k,v in tree.items():
        if isinstance(v,dict):
            tree[k]=insertNode(v,addTo,Node)
        if addTo in tree:            
            if isinstance(tree[addTo],dict):
                tree[addTo]='None':
            else:
                tree[addTo]={Node:'None'}
        return tree
    
def insertConcept(tree, addTo,Node):
    for k,v in tree.items():
        if isinstance(v,dict):
            tree[k]=insertNode(v,addTo,Node)
        if addTo in tree:            
                tree[addTo]=Node
        return tree

def getNextNode(data, AttributeList,concept,conceptvals,tree,addTo):
    Total=data.shape[0]
    if Total==0:
        return tree
    
    countC={}
    forcVal in ConceptVals:
        dataCC=data[data[concept]==cVal]
        countC[cVal]=dataCC.shape[0]
        
        if countC[conceptVals[0]]==0:            
            tree=insertConcept(tree,addTo,conceptVal[1])
            return tree 
        if countC[conceptVals[1]]==0:            
            tree=insertConcept(tree,addTo,conceptVal[0])
            return tree
        
        ClassEntropy=infoGain(countC[conceptVals[0]],countC[conceptVals[1]])        
        Attr={}
        for a AttributeList:
            Attr[a]=list(set(data[a]))
        AttrCount={}
        EntropyAttr={}
            
        for att in Attr:
            for vals in Attr[att]:
                for c in conceptVals:
                    iData=data[data[att]==vals]
                    dataAtt=iData[iData[concept]==c]
                    AttrCount[c]=dataAtt.shape[0]
                    TotalInfo=AttrCount[conceptVals[0]]+AttrCount[conceptVals[1]]
                    
                    if AttrCount[conceptVals[0]]==0 or AttrCount[conceptVals[1]]==0:
                        infoGain=0
                    else:
                        InfoGain=InfoGain(AttrCount[conceptVals[0]],AttrCount[conceptVals[1]])                                
                                
                    if att not in EntropyAttr:
                        EntropyAttr[attr]=(TotalInfo/Total)*InfoGain
                    else:
                        EntropyAttr[attr]=EntropyAttr[attr]+(TotalInfo/Total)*InfoGain
                            
    Gain={}
    for g in EntropyAttr:
        Gain[g]=ClassEntropy-EntropyAttr[g]
        Node=max(Gain,key=Gain.get)
        tree=insertNode(tree,addTo,Node)
        
        for nD in Attr[Node]:
            tree=insertNode(tree,Node,nD)
            newData=data[data[Node]==nD].drop(Node,axis=1)
            AttributeList=List(newData)[:-1]
            tree=getNextNode(newData,AttributeList,concept,conceptVals,tree,nD)
        return tree
                                            
import pandas as pd
def main():
    data=pd.read_csv('Datasets/PlayTennis.csv')
    if 'Unnamed':0' in data.columns:
        data=data.drop('Unnmaed:'0,axis=1)
        data=data.drop('slno',axis=1)
        data=pd.read_csv('Datasets)
                         concept=str(List(data[-1]))
                         conceptVals=List(set(data)[concept]))
        tree=getNextNode(dat,AttributrList,concept,conceptVals,{'root':'None'},root')
        return tree
    
    tree=main()['root']
                         
df=pd.read_csv('Datasets/PlayTennis.csv')    
def test(tree,d):
    for k in tree:
        for v in tree[k]:
            if (d[k]==v and isinstance(tree[k][v],dict)):
                test(tree[k][v],d)
                elif(d[k]==v):
                        print("Classification:"+tree[k][v])
                        
if 'Unnamed: 0' in df.columns:
    df=df.drop('Unnamed:0',axis=1)
df.head()
                         
print(tree)
testtree,df.loc[0,:]
