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

#str has a method to divide its parts with one or more delimiters
print('one/two/three/data_2.txt'.split('/'))
import re
print(re.split('[ ,]', 'I love you, but I hate you'))

# a substr can be replaced by another with replace method
txt = "I love my life, but sometimes I hate my life"
x = txt.replace("life", "boss",1)
print(x)

#operations with dates
from datetime import datetime, date, time

actual:datetime = datetime.now()
hora: int = actual.hour
print (actual)

other: datetime = datetime(2024,12,29)
print(other>actual)

#lists & tuples
cats: list [str] = ["Nero", "Taro", "Pipi", "Mogu"]
print(cats)
print(len(cats))
users: tuple [str,str] = ("Marta","Moreno")
print(users)

cats.append("Momo")
print(cats)
#help(cats)#shows details about method in objects

#sets & dictionary
data: set [float] = \
    {12, 24, 28.5, 33, 40.5, 42.3 }
print(data)
average_temperature: dict[str, float]= {"Almería": 20, \
        "Córdoba": 35, "Sevilla": 33}
print(average_temperature)

#Classes & Objects