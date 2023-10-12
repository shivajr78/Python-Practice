myDict = {
    #keys    :  #values
    "Fast"   :   "Quick Manner",
    "Python" :   "CodeWithHarry",
    "Ph.no"  :   "9813682478,9466724305",
    "Marks"  :   "1,2,4,5,0,7",
    'Name'   :   'Shiva',
    'Branch' :   'Computer Science',
    'Roll.no':   '008' 
}
# print(type(myDict.keys()))  #Print the type of myDict
# print(myDict.keys())        #Print all the keys of myDict
# print(myDict.values())      #Print all the values in myDict
#print(myDict.items()) #Print all contant of keys and values in myDict


#print all key and value by using for forloop
for x,y in myDict.items():
    print(x,y)

#Update = Add the a new key and values and update the myDict

# print(myDict)

# updateDict = {

#     'College' : 'Ganga Technical Campus',
#     'Job' :  'SoftWare Engineer in MicroSoft',
#     'Python' : 'Apna College' #it also update already written key values pair in myDict
# }

# myDict.update(updateDict) #Update the myDict by adding key values pair from updateDict 
# print(myDict)

# # get = it used to find the keys also return None if word not present in myDict
# print(myDict.get("Python")) 