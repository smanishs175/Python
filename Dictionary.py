# Dictionary works in pairs , word acts like key, key always has value "key" : value
# mutable 
dict = {
   "sachin" : "mumbai",
   "mahendra" : "delhi",
    "rahul" : [1,2,3]
}

print(dict["sachin"])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("mahendra"))

#print(dict.update(newDict"))

#dict_keys(['sachin', 'mahendra', 'rahul'])
#dict_values(['mumbai', 'delhi', [1, 2, 3]])
#dict_items([('sachin', 'mumbai'), ('mahendra',
#