'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
#Loop though dictionary
'''
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict.keys():
    print(key,':',a_dict[key])
'''
#sort dictionary
'''
a_dict = {2:3, 1:89, 4:5, 3:0}

c = {k:a_dict[k] for k in sorted(a_dict.keys())}
print(type(c))
'''
#Datetime
import datetime    
currdate = datetime.date(2021,5,5)
prevdate = datetime.date(2020,6,10)
diff = currdate - prevdate
print(diff.days)
tomorrow = currdate + datetime.timedelta(days = 4)
print(tomorrow)
#loop though dates
for day in range((currdate-prevdate).days):
    #print(day)
    pass
