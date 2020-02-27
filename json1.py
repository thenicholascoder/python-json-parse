#import the json library
import json

#use the triple quoted string to put json in there
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
  "email" : {
     "hide" : "yes"
   }
}'''

#json will turn data into dictionary kvp with nested dictionary kvp
#loads means loads means load from string
#then  parse the data into a structured object or dom
info = json.loads(data)

#info["name"] = it means get the info value of the key name
print('Name:', info["name"])

#info["email"] = if means get the info value of hide inside the email
print('Hide:', info["email"]["hide"])
