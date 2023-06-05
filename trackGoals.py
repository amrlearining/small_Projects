"""
@author: amro almaghraba
Release: 05 JUN 2023
@version: V1.0
This project to track your goals achieving 
"""
from datetime import datetime
"""
cal method to calculate the achieving percent you get
* name = project name
* goal = nummber of lessons
* now = how many lessons do you done
"""
def cal(name, goal, now):
    percent = (now * 100) / goal
    result = name + str(percent) + "%"
    return result
"""
must method calculate how many days still to due date,
and how many percent you must be done now
* t = target day / due date
* f = first day / the day the you began the project in 
"""
def must(f, t):
    # Calculate the number of days remaining
    la_fiday = (t - f).days

    ## still days
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the number of days remaining
    s = (t - current_date).days

    # Display the result
    a2 = (s * 100)/la_fiday
    a3 = 100 - a2
    return "still: ", s, " day", "must be achieved: ", a3, "%"


print (cal("eCommerce: ", 128, 61)) ##
print(must(datetime(2023, 5, 12).date(), datetime(2023, 6, 27).date()))


