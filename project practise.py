 #Ride share 
 
'''ridesharing_distance = [6,24,8,17,20,3]  

def calculate_ride_price(distance):
     
     #intially 
     ride_price = 0
     ride_type = "unknown"
     
     
     if distance >= 15:
         ride_price = distance * 25
         ride_type = "big_distance"
         
     else:
         ride_price = distance * 20
         ride_type = "small_distance"
         
     
     return ride_price,ride_type


for km in ridesharing_distance:
    
     total_price ,status = calculate_ride_price(km)
    
     print(f"Distance: {km} km ") 
     print(f"Total_price:{total_price} taka")
     print (f"Ride_type: {status}")   '''
     
     
     
     
     
     ####   object && class  #####
     

'''class Robot:
    def __init__(self,name):
        self.name = name
        self.battery = 100
        
        
        
    def hello(self):
        print(f"Hello! I am {self.name} ")
        
    def dance(self):
        print(f"{self.name}  is dancing ")
        self.battery = self.battery-10
        
    def battery_status(self):
        print(f"BATTERY : {self.battery}%")
        
        
        
robot_name = input("ENTER ROBOT NAME :")

robot = Robot(robot_name) 

robot.hello()   
robot.dance()  
robot.battery_status() '''


'''
class Music_player:
    def play(self):
        print("music is playing")
        
    
    def pause(self):
        print("music paused")
        
    def stop(self):
        print("music stoped")
        
        
player = Music_player()

player.play()
player.pause()
player.stop()'''



'''class Coffee_making():
    
    def make_coffee (self):
        print("Coffee ready!!")
        
    def add_milk(self):
        print("milk added")
        
    def clean (self):
        print("Machine cleaned!!!!!!")
        
        

coffee = Coffee_making() 

coffee.make_coffee()
coffee.add_milk()
coffee.clean()
    '''
    
''' 
### Movie Ticket  ####

        
booking = {} 

while  True:
    
    print("\n_____Movie Ticket Booking_____") 
    print("1.Book ticket")
    print("2.View booking")    
    print("3.Exit")
    
    
    option = input("Choose your option:")
    
    if option == "1":
        customer_name = input("Enter your name :")
        ticket_count = int(input("How many tickets???:"))
        
        
        booking["Name"] =  customer_name
        booking["tickets"] = ticket_count
        
        print("\n BOOKING SUCCESSFUL !!")
        
        
    elif option == "2" :
        if booking:
            print("\n Booking Details") 
            print(f"Customer :{booking["Name"]}") 
            print(f"Tickets : {booking["tickets"]}") 
            
            
        else:
            print("\n NO BOOKING IS FOUND //// ")
            
            
    elif option == "3" :
        print("\n Thank You ,,visit again !!")
        break 
    
    else :
        print("\n INVALID OPTION !!!")'''
        
      
      
        
        
        
#### json  process ######


'''import json 

student = {
    'name': input("enter your name : "),
    
    'roll' : int(input("enter your roll: ")) ,
    
    'department': input("department name : ") 
       
}

print ("\n----student dictionary----")
print (student)


json_data = json.dumps(student)

print (json_data)


student_again = json.loads(json_data)

print("\n Back to dictionary")
print(student_again)


with open("data.txt","w") as file :
    
    save = json.dump(student_again,file,indent=4)
    
    
print("\n save  file")
print(save)


with open("data.txt","r") as file :
    read = json.load(file)
    
    
print("\n read json file")
print(read)'''
    
    
    
    
  ##### WEATHER app  #####
  
'''  
import requests  

city = input("enter city name :")

url = f"https://wttr.in/{city}?format=j1"


report = requests.get(url)

print(report.status_code)

weather_info = report.json()

print (weather_info)

current_weather = weather_info["current_condition"][0]

temperature = current_weather["temp_C"]
humidity = current_weather["humidity"]



print("\n______WEATHER INFO______")
print(f"CITY: {city}")
print(f"TEMPERATURE: {temperature} degree calcius")
print(f"HUMIDITY: {humidity}") '''





####   banking system    #####

'''class Bank_Account():
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
account.check_balance() 

    
'''

    
    
    
    
        
    




 
 
 
 
 
 
 
 
 
 
 
 
     
     
     
     
       