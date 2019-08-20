# Write a Python program to print the even numbers from a given list. Go to the editor Sample List: [1,2,3,4,5,6,7,8,9] Expected Result: [2,4,6,8]

def even_num(a):   # define a function even_num
    enum = []           # create an empty list for variable enum
    for number in a:       # check each number
        if number % 2 == 0:    # if number is divisible by 2,
            enum.append(number)    # add that number to the empty array enum.
    return enum                               # return the array/list
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))   # call the function and pass it arguments.
