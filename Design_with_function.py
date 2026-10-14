#Leo Esparza
#Dr. Giles CIT-104-A26.AU
#Design with Function
#Calculates the time to reach highest point
def time_to_peak(vertical_speed, gravity=-32):
    time = -vertical_speed / gravity
    return time
#Calculates the maximum height
    time = time_to_peak(vertical_speed, gravity)
def maximum_height(vertical_speed, gravity=-32, initial_height=0):
    time = time_to_peak(vertical_speed, gravity)
    height = 0.5 * gravity * time**2 + vertical_speed * time + initial_height
    return height
# asks for user input
vertical_speed = float(input("Enter initial vertical speed: "))
#prints the results in seconds and feet
print("Time to peak:", time_to_peak(vertical_speed), "seconds")
print("Maximum height:", maximum_height(vertical_speed), "feet")
print("Total flight time:", 2 * time_to_peak(vertical_speed), "seconds")
