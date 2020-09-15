import pandas as pd 


# Channeling
def get_turnings(data):
    high_convex=pd.DataFrame()
    low_concave=pd.DataFrame()

    # Convexs and concaves
    for i in range(data.shape[0]):
        if i==0: # First day
            if data.High.iloc[i]>data.High.iloc[i+1]:
                high_convex=high_convex.append(data.iloc[i])
            if data.Low.iloc[i]<data.Low.iloc[i+1]:
                low_concave=low_concave.append(data.iloc[i]) 

        elif i==len(data.High)-1: # Last day
            if data.High.iloc[i]>data.High.iloc[i-1]:
                high_convex=high_convex.append(data.iloc[i]) 
            if data.Low.iloc[i]<data.Low.iloc[i-1]:
                low_concave=low_concave.append(data.iloc[i]) 

        else:
            if data.High.iloc[i-1]<data.High.iloc[i] and data.High.iloc[i+1]<data.High.iloc[i]:
                high_convex=high_convex.append(data.iloc[i])
            elif data.High.iloc[i-1]<data.High.iloc[i] and data.High.iloc[i+1]>data.High.iloc[i] and (data.High.iloc[i]-data.High.iloc[i-1])>(data.High.iloc[i+1]-data.High.iloc[i]):
                high_convex=high_convex.append(data.iloc[i])
            elif data.High.iloc[i-1]>data.High.iloc[i] and data.High.iloc[i+1]<data.High.iloc[i] and (data.High.iloc[i-1]-data.High.iloc[i])<(data.High.iloc[i]-data.High.iloc[i+1]):
                high_convex=high_convex.append(data.iloc[i])

            elif data.Low.iloc[i-1]>data.Low.iloc[i] and data.Low.iloc[i+1]>data.Low.iloc[i]:
                low_concave=low_concave.append(data.iloc[i])
            elif data.Low.iloc[i-1]<data.Low.iloc[i] and data.Low.iloc[i+1]>data.Low.iloc[i] and (data.Low.iloc[i]-data.Low.iloc[i-1])<(data.Low.iloc[i+1]-data.Low.iloc[i]):
                low_concave=low_concave.append(data.iloc[i])
            elif data.Low.iloc[i-1]>data.Low.iloc[i] and data.Low.iloc[i+1]<data.Low.iloc[i] and (data.Low.iloc[i-1]-data.Low.iloc[i])>(data.Low.iloc[i]-data.Low.iloc[i+1]):
                low_concave=low_concave.append(data.iloc[i])
    
    return high_convex, low_concave

