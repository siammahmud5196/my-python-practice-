'''dict1 = { 'a':1, 'b':2 , 'c':5}
dict2 = { 'f':1, 'b':4 , 'c':9}

for key in dict1:
    if key in dict2:
        print (key)
print (len(dict1)) ''' 


'''dict1 = { 'a':1, 'b':2 , 'c':5}
dict2 = { 'f':1, 'b':4 , 'c':9}

keys = 'a','b','c','f'

common = dict1.keys() & dict2.keys ()


print (common)'''



'''m1 = [2,3,4,5,8]
item2 = [2,5,8,7]


common = set(item1) & set (item2)

print (common) '''


## input sytems 

'''name = input ("what is  your name:")
age =  input ("what is your age :")


print ("Hello "+   name  +  "How old are you ?")
print ("I am "+ age  +" years old") '''

 



'''name = "Siam mahmud hadi"
age = 20 

print ("name : ",name )
print ("age : ",age )'''


'''def joy(name):
    

 print("How are you?",name )


joy("siam")'''  



# file read 

'''file = open("me.text","r")
 
content = file.read()
 
print(content)

file.close() '''




#SCOPE PRACTISE 

'''x = 500
def test():
    x = 50 
    print(x)
    
test()

print(x) '''



### REGEX TOPIC ###

'''import re  

text = "python_112 refe_234"


print (re.findall(r"\w",text))'''



'''import re 

number = "my number is 01322425196"

print(re.findall(r"\d",number))'''


'''import re

email = "my email is siam1233@gmail.com"


##print (re.search(r"@gmail\.com",email))


print (re.findall(r"\w+@gmail\.com",email)) '''





## lambda function ##


#lambda parameter:  expression 



'''marks = [35,49,50,20,80,93]

bonus = list(map(lambda x:x+5,marks))

passed  = list(filter(lambda x:x>=40,bonus ))


print ("origianl marks:",marks)
print("bonus marks:",bonus)
print("passed marks:",passed)
'''


'''even = lambda x : x%2==0 

print(even(4))'''


'''maximum = lambda a,b : a if a>b  else b


print (maximum(10,20))'''


'''result = lambda marks: "pass"if marks>=33 else "fail"

print (result(32)) 

print (result(70))'''

##### list comprehension  #######


'''square = [i*i for i in range(1,6)]

print (square)



even_number = [num for num in range(1,20) if num%2==0]

print(even_number) '''


'''numbers = [2,4,6]

result = [i*2 for i in numbers]

print (result)'''


'''result = [i for i in range(1,10) if i%3==0]

print (result) '''





##  decorator  function / wrapper function  


'''def decorator (func):
    def wrapper ():
        print ("brfore")
        
        func ()                #### structure 
        
        print ("after")
        
    return wrapper  

'''

'''def decorator(func):
    def wrapper():
        print ("starting....")
        
        
        func()
        
        
        print("finished")
        
    return wrapper 



@decorator 
def study():
    print("python study")
    
study()
'''

'''def login_check (func):
    
    def wrapper():
        print("LOGIN SUCCESS")
        
        func()
        
        print("LOGOUT")
        
    return  wrapper  

@login_check
def login():
   print("Dashbosrd opened ") 
   
login()
'''


'''def login_check(my_login):
    def wrapper():
        is_logged_in = "true" 
        
        if ("true"):
            print("Logged in successfully")
        else :
            print("Please login first")
            
        my_login() 
        
        print("login done")
        
    return wrapper


@login_check
def login_verification():
    print ("Dashboard opened")
    
    
login_verification()

'''



####  enumerate $$$$

###names = ['siam','hadi','rafi','sazid']

'''index = 0

for name in names :
    print(index,name)
    
    
    index = index + 1 '''
    
    
## with enumerate 

'''for index,name in enumerate (names):
    print (index,name) '''
    
    
    
    ## datetime 
    
    
'''from datetime import datetime 
now = datetime.now()

print(now.time())
print(now.date())
'''
    
    
    
### collections

'''
items = ['rice','oil','suagr','salt','milk']

from collections import Counter
print (Counter(items)) '''



'''names = ['siam','rafi','hadi','sazid','siam','rafi'] 

from collections import Counter

count = Counter(names)

print (count)
print(count.most_common())'''




## iterators 
'''
items = ['banana','milk','yogert','juice','water']


 

itr = iter(items)



print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))'''


## generator 


'''def offdays():
    yield"firday"
    yield"saturday "
    yield"tuesday" 
    

off_day = offdays() 
    
    
print (next(off_day))
print (next(off_day))
print (next(off_day))'''
'''

def levels ():
    yield 1
    yield 2
    yield 3
    yield 4
    
level = levels()

for games_level in level:
    print(games_level)'''
    
    
    
    
### zip file 

'''names = ['siam',"rafi",'sady','sazid']
rolls = [20,49,34,36,32]
'''
'''result = list(zip(names,rolls))
print(result)
'''

'''itr = iter(zip(names,rolls))

print(next(itr))            ## 2/4/more .......lists connection 
print(next(itr))
print(next(itr))
print(next(itr))

 '''
 
 
'''for name,roll in zip(names,rolls):
    print(name,roll) '''
    
    
    
   ###  json module  ###
   
###### java script object notation --> plain text 
'''
import json 

student_info = {
    "name" : 'siam',
    "age" : 23,
    'roll': 232
}

json_data = json.dumps(student_info)

print(type(json_data))
print(json_data)'''


## reverse work #####

'''import json 

json_data = '{"brand":"bmw",  "years": 1823 }'

car_brand = json.loads(json_data)


print(type(car_brand))
print (car_brand)'''

''''import json 

student ={
   'name': 'siam',
    'age' : 22
      
}                                       ##### save into file 

with open("data.txt","w") as file :
    json.dump(student,file)
    
print("saved successfully")


'''


##### read json from file 
'''
import json 

with open("data.txt","r") as file :
    
    print(json.load(file)) '''
    
    

    
   ### request module 
   
   
'''pip install request '''

'''import requests 


response = requests.get("https://www.google.com/maps/@23.8685226,90.3228985,15z?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D")

print (response.status_code)
print (response.text)'''



'''import requests 


records = requests.get("https://www.google.com/")

data = records.json()

print(data)

print (data["current_user_url"])
print (data["current_user_authorization_html_url"])
    
    '''
    
    
'''import requests

name = input("Enter Name: ")

url = f"https://api.dicebear.com/7.x/adventurer/png?seed={name}"

response = requests.get(url)

open("avatar.png", "wb").write(response.content)

print("Avatar Created!")'''



#### csv ####

''' 
import csv

name = input("enter a name :")
age = int(input("enter an age :"))
department = input("enter a department name :")


with open("mine.csv","w",newline="") as file :
    
    
    
 write = csv.writer(file)
 
 write.writerow(["Name","Age","Department"])
 
 write.writerow([name ,age , department])
 
 print("DATA SAVED SUCCESSFULLY!!!!")
 
 
 #### read the CSV file 
 
with open("mine.csv","r") as file:
     read = csv.reader(file)
     
     for my_name in read:
         print (my_name)


print(read)'''





#### logging ###


'''import logging 

logging.basicConfig(filename="login.log",
                    level= logging.INFO
                    
                    )



username = input("enter your name:")
password = input("enter your password:")
                                                      
                                                             ###### basic logging 
                                                

if username == "hadi" and password == "1234":
    logging.info("LOGIN SUCCESSFUL")
    print("welcome !" , username)
    
    
else:
    logging.warning("LOGIN FAILED")
    print("OPPS!! try again ")'''
    
    
    
   
'''import logging 

logging.basicConfig(
    filename="app.logg",
    level=logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s "     #### custom format #####date time 
       
)                                                                           ### file save

logging.info("login successful")
logging.warning("login failed")
logging.error("something went wrong")'''


### exception logging ///// error handling


'''import logging 

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s " 
) 

try:
    number = 10 / 0
    
    
except ZeroDivisionError:
    logging.error("cannot divide by zero")


try:
    number = 10/0
    
except Exception:
    logging.exception("an error occurred")
    
'''
'''import logging

my_log = logging.getLogger("1st")
my_log.setLevel(logging.INFO)  


terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.logger")

my_format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

terminal_handler.setFormatter(my_format)
file_handler.setFormatter(my_format)



my_log.addHandler(terminal_handler)
my_log.addHandler(file_handler)


my_log.info("app successsfully run ")'''



#### oop practise #####
'''

class Bank_Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.original_balance = balance 
        
        
    def show_info(self):
        print(f"OWNER: {self.owner}")
        print(f"BALANCE OF YOUR ACCOUNT: {self.original_balance}")



    def deposite(self,amount):
        if amount > 0:
            self.balance += amount 
        
        
        
    def withdraw(self,amount):
        if self.balance >= amount > 0 :
           self.balance = self.balance - amount
        
     
    def check_balance(self):
        print(f"CURRENT_BALANCE:  {self.balance}")
        
        
account= Bank_Account("siam",2000) 


account.deposite(1000) 
account.withdraw(500)

account.show_info()

print("\nAFTER CHANGING BALANCE")
account.check_balance() '''



###  threading ####

import threading
import time 


def download_file():
    print("file download started")
    time.sleep(4)
    print("file downloaded")
    
    
    
def send_email():
    print("mail sending started")
    time.sleep(3)
    print("mail sending  done")
    
    
thread_a = threading.Thread(target=download_file)
thread_b = threading.Thread(target=send_email)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print("All tasks completed ")










    
    



























 
 























































































































