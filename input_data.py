import pandas as pd
import numpy as np

# """This part we are gonna see the code to load the data from buckets, in this case the Data we will load is the sentiment"""


class Input_Data:
    def __init__(self, Route):

        self.Route = Route

    def Data_Sent(self):

        df = pd.read_excel(self.Route)
        Data = df.loc[:, ["Id_Model", "Message"]]
        return Data
