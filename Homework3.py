
##TASK1
#create the function called count_letter to extract the number of the letters from a sentence from python and output it as a dictionary

def count_letter(input):

    # check input type
    if type(input) is str:
        #import all lowercase letters
        from string import ascii_lowercase as letters
        
        #transform input to lowercase
        input = input.lower()
        
        # define empty dictionary
        output = {}

        # loop through every letter of the alphabet
        for letter in letters:
            # count amount of occurances
            amount = input.count(letter)
            # store letter and its amount in dictonary
            output.update({letter: amount})

    else:
        output = "ERROR: That was not a string, please try again"

    # print output
    print(output)


#test a few different sentences
def task1():
    #Every letter of the english alphabet at least once
    a= "The quick brown fox jumps over the lazy dog"
    print(a)
    count_letter(a)
    
    #Every letter of the english alphabet EXACTLY once
    b= "Mr Jock, TV quiz PhD, bags few lynx"
    print(b)
    count_letter(b)
    
    #Not a string
    print("Test - Not a string:")
    count_letter(9)


##TASK 2
#Explain: [::-1] get [5,4,3,2,1] and why numbers[4:2:-1] get [5,4]

numbers= [1,2,3,4,5]

def task2():
    print(numbers[::-1])
    #Explanation: Outputs all numbers but in reverse order
    print(numbers[4:2:-1])
    #Explanation: Outputs all numbers between index 4 (included) and index 2 (not included) but in reverse order



##TASK 3
#How to use list slice and index to get [2,4,1] from the list: number = [1,2,3,4,5],
def task3():
    a = [numbers[1]]
    b = [numbers[3]]
    c = [numbers[0]]
    result = a+ b + c
    print(result)
    count_letter("input")


task1()
task2()
task3()