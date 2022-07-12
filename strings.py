#strings just pieces of text.
#strings are immutable.
def string ():
    our_string = "Hello World"
    print(our_string)

#how to add them in different times.    
def word (): 
    my_word= "Hello world"  
    me ="I said:" + my_word
    print(me)
    
#how to repeat multiple times
def multiple():
    my_school = "AkiraChix"
    multiply = my_school*3
    print(multiply)

#Slicing- getting part of a string.
#Positive slicing.
def positive_slicing():
    some_string = "Mercy Chirii"
    slicee = some_string[2:5]
    print(slicee)

#negative slicing.
def negative_slicing():
    a_string = "mercy Chirii"
    slicing = a_string[-5:-2]
    print(slicing)

#slice the first character and print the other string.
def slice_one():
    a_string = "mercy Chirii"
    slicing = a_string[1:]
    print(slicing)
    
def negative_one_slice():
    a_string = "mercy Chirii"
    slicing = a_string[:-1]
    print(slicing)
  
#   indexing and starts at 0, the first character is 0.
# indexing in negative start with negative 1
def index():
    a_string = "mercy Chirii"
    slicing = a_string[2]
    print(slicing)
    
#string methods.
#in uppercase,...
def string_method():
    a_string = "mercy Chirii"
    name= a_string.upper()
    print(name)

#in lowercase ....
def string_lower():
    a_string = "MERCY CHIRII"
    name= a_string.lower()
    print(name)
    
#startswith
def start_with():
    a_string = "mercy Chirii"
    name= a_string.startswith("mercy")#python is case sentitive.
    print(name)
    
#endswith
def ends_with():
    a_string = "mercy Chirii"
    name= a_string.endswith("mercy")
    print(name) 
    
#replace a word with another, .replace()
def replace():
    a_string = "mercy Chirii"
    name= a_string.replace("mercy","there")
    print(name)
    
#.count() count the number of characters passed.
def count():
    a_string = "mercy Chirii"
    name= a_string.count('i')
    print(name)