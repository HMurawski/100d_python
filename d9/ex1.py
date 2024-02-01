programming_dictionary = {
    "bug" : "an error in a program",
    "function" : "a piece of code to be called over and over again",
    "loop" : "doing something over and over again"
}

print(programming_dictionary["bug"])

programming_dictionary["dot"] = "a dot is a dot"

print(programming_dictionary)

#edit an item in dict
programming_dictionary["bug"] = "a moth in your computer"
print(programming_dictionary["bug"])

#loop through a dict

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



#wiping dict
programming_dictionary = {}
print(programming_dictionary)