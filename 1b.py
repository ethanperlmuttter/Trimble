
import pandas as pd

#intitialize nam_table for testing
d = {'StudentID': ['V001', 'V002', 'V003', 'V004'] , 'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos']}

name_table = pd.DataFrame(data= d)


def to_upper_or_lower (table = name_table):
    table['Name']  = table['Name'].apply(lambda x : x.upper() if 'e' in x.lower() else x.lower())
        




to_upper_or_lower(name_table)
print(name_table)