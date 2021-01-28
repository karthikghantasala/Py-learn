import pandas as pd
stats = [{'a':1000, 'b':3000, 'c': 100},{'a':15000, 'b':30, 'c': 1000},{'a':10, 'b':3, 'c': 10000}]
list2 = ['p','q','r']
# name of csv file  
filename = "university_records.csv"
lst = []
for x in range(len(stats)):
    max_key = max(stats[x], key=stats[x].get)
    all_values = stats[x].values()
    max_value = max(all_values)
    csv_row = [list2[x],str(max_key),str(max_value)]
    print (csv_row)
    lst.append(csv_row)
print (lst)
city = pd.DataFrame(lst, columns=['City', 'State','Country'])
city.to_csv('city.csv',index=False)
