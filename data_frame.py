import pandas as pd
import numpy as np


# """This part we will found the code that is in charge to convert
#        and clean the data from the buckets"""


class Data_Frame:
    def __init__(self, Data):
        self.Data = Data

    def Transform(self):

        All_Clean = self.Data
        Sentimentnot = All_Clean[All_Clean.Message.notnull()]
        return Sentimentnot
