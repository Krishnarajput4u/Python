"""A car travels a certain distance in a given time. Calculate and give distance 150KM and time is equal too 2.5 Hrs. If the car maintains the same speed, how far it would travel in 5 hours? How long would it take to travel 300 KM at the same speed? Print all the results with appropriate labels also use comments in the codes."""

distance = 150  # in kilometers
time = 2.5      # in hours

speed = distance / time  # speed in km/h
print("Speed of the car:", speed, "km/h")

# Distance traveled in 5 hours
time_5hrs = 5  # in hours
distance_5hrs = speed * time_5hrs
print("Distance traveled in 5 hours:", distance_5hrs, "km")

# Time taken to travel 300 KM
distance_300km = 300  
time_300km = distance_300km / speed
print("Time taken to travel 300 KM:", time_300km, "hours")