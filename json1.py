#import the json library
import json

#use the triple quoted string
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

#loads means loads means load from string
info = json.loads(data)

#info["name"] = it means get the info value of the key name
print('Name:', info["name"])

#info["email"] = if means get the info value of hide inside the email
print('Hide:', info["email"]["hide"])
