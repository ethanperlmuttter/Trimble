
import pandas as pd

#intitialize nam_table for testing
d = {'StudentID': ['V001', 'V002', 'V003', 'V004'] , 'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos']}

name_table = pd.DataFrame(data= d)

#print(name_table)
def to_upper_or_lower (table = name_table):
    t = table.copy(deep = True)
    t['Name']  = t['Name'].apply(lambda x : x.upper() if 'e' in x.lower() else x.lower())
    return t
        




print(to_upper_or_lower(name_table))
print(name_table)