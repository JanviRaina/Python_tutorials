# JSON JAVASCRIPT NOTATION
import json
data='{"var1":"harry","var2":56}'
# print(data['var1'])   This is a syntax error that why we use json loads
parsed=json.loads(data)
print(parsed['var1'])

data2={
    "channel name":"hellyblog",
    "cars":["ferrari","bmw","audi a8"],
    "food":("idli",540)
}

# if we want dictionary in javascript

jscomp=json.dumps(data2)
print(jscomp)


# sort_keys