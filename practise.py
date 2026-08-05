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
     print (f"Ride_type: {status}")'''   
 
 
 
 
 
 
 
 
 
 
 
 
     
     
     
     
       