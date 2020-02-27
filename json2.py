#import the json library
import json

#use the triple quoted string
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#json will turn data into json list with nested dictionary kvp
#json.loads() = load from strings
info = json.loads(data)

#len() = get the length of the strings inside info
print('User count:', len(info))

#for each item in info, itterate through info:
for item in info:

    #print Name and also the value of name
    print('Name', item['name'])

    #print Id and also the value of id
    print('Id', item['id'])

    #print the Attribute and also the value of x
    print('Attribute', item['x'])
