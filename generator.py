import pandas as pd
import numpy as np



#"""This part we will found the code will  convert the sentiment 
#    data in a generator to meke the reuest to the model """    

class Generator:
    def __init__(self, Sentiment,Path):
        
        self.Sentiment = Sentiment
        self.Path = Path
        
    def Iterator(self):
        
        df = self.Sentiment
        
        Sentiment_df = df['Message']
        
        General_list = Sentiment_df.to_numpy().tolist()
        
        New_df = pd.DataFrame (General_list, columns = ['Sentiment'])
        
        for i in range(len(New_df)):
            
            df_fn = (New_df.loc[i, 'Sentiment'])
            
            new_list = [df_fn]
            
            df_second = pd.DataFrame(new_list, columns = [''])
            
            df_second.to_csv(f"{self.Path}{i}.txt",index=False,header=False)
        
        return New_df 