#Create a python package, for this Assignment,And each number in a separate module. Create third module to import and use/ call the two functions created in question 1 and two.

#Write a python function that takes a list and returns a new list with unique elements of the first list. Don't use list methods.

def uniqueli(L):  # define a function that takes a list L
  x = []          #initialise an empty list
  for b in L:    #for element'b' in list L;
    if b not in x:   # check if exists in uniqueli;
      x.append(b)  
  return x    # return the list/

print(uniqueli([1,1,7,7,7,8,8,8,8,4,4,4,4,9,9,9,9])) # calling the function and passing it params.