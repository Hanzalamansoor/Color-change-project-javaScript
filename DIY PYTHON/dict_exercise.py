# dic = {
#     "chadar" : "sheet",
#     "pankha" : "fan",
#     "gari"   : "car",
#     "chabi"  : "key"
# }

# input = input("Enter the urdu word to get the meaning in english : ")
# word = dic[input]
# print(word)



# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
# keys = ['Ten', 'Twenty', 'Thirty']  #list 1
# values = [10, 20, 30]  #list 2

# dict_sol = dict(zip(keys, values)) # zip function will create the  key value dictionary from both of the different list
# print(dict_sol)


#Exercise 2: Merge two Python dictionaries into one

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = dict1.copy() # first copy the dictionary 1 into dictionary 3 
# dict3.update(dict2)  # Then update it to add dictionary 2 
# print(dict3)








# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]['history'])  
# So the question was to retrive the marks of the historyclass from the dict
# first we see that the parent element in this case is the class so we invoke the class
#string first and  then we saw student string as a parent class storing the student name
# in the last one we saw that the marks parent class was storing the history marks
# so we followed the process first to get to the marks of the history



#Exercise 4: Initialize dictionary with default values
#In Python, we can initialize the keys with the same values.

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res = dict.fromkeys(employees,defaults) #fromkeys takes an input of the key and assign the default value to both the keys 
# print(res['Kelly'])



#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }

# keys = ["name", "salary"]

# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)


# Exercise 6: Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]


# del sample_dict['name']
# del sample_dict["salary"]
# print(sample_dict)






# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# sample_dict = {'a': 100, 'b': 200, 'c': 300}


# if 200 in sample_dict.values() :
#     print("200 is present in a dict ")
# else :
#     print("200 is not present in a dict")






# Write a program to rename a key city to a location in the following dictionary.

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict.pop('city')
# sample_dict["location"] = "New york" # or you can do like this : sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

identification = {

 "name" : "harry",
  "id" : 44525-758-999,
  "address" : "25,palm-street-florida",
  "age" : 25,
  "D.O.B" : 25-5-1995
}

identification.update({"mm":"ss"})

print(identification)










