print("hey, ho, let's go!")
#I have no idea of programming, but lets try this snake
'''Hello
eeverybody'''
def greeting (name:str)->None:
    print ("Hello, "+ name)
#a str can be between "double" or 'single' quotes

greeting("Nero & Taro")

def formal_greeting (name:str)-> None:
    greeting(name)
    print ("Nice to meet you.")

formal_greeting ("Future boss")

#calculates a discount
def discount(price:int,dis:int)->float:
    return price-price*dis/100
print (discount (550,85))

print ("For a text having two lines. \n This is the second one.")
print ("""      If
            we use 3
                        it keeps its
                                        own format""")
text: str = "How many chars does this text has?"
print('This text has: ', len(text),'chars')
#prints a char froma a determinated position
print(text[0])
print(text[33])
print(text[-1])#also prints tha last char


