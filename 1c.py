import pandas as pd
pt_b = __import__('1b')

d = {'StudentID': ['V001', 'V002', 'V003', 'V004'] , 'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos']}

name_table = pd.DataFrame(data= d)

d1 = {'StudentID': ['V001', 'V002', 'V003', 'V004'] , 'Total_marks': [95, 80, 74, 81]}

marks_table = pd.DataFrame(data= d1)

name_table_UL = pt_b.to_upper_or_lower(name_table)

#print(name_table_UL)
def summarize_upper_lower(nt = name_table_UL, mt = marks_table):
    name_marks_table = pd.merge(nt.copy(deep = True), mt.copy(deep = True), on = 'StudentID')
    name_marks_lower = name_marks_table[name_marks_table['Name'].str.islower()]
    name_marks_upper = name_marks_table[name_marks_table['Name'].str.isupper()]

    lower_mean = name_marks_lower['Total_marks'].mean()
    upper_mean = name_marks_upper['Total_marks'].mean()

    ds = {'Name Type':['UPPERCASE', 'LOWERCASE'], 'Average Marks': [lower_mean, upper_mean]}
    return pd.DataFrame(data = ds)
    #print(name_marks_table)


print(summarize_upper_lower(name_table_UL, marks_table))




#print( marks_table)