# ex_2_time_classes_and_objects
Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59. You should also create 3 additional instance methods:

- set_time(hours, minutes, seconds) - updates the time with the new values

- get_time() - returns "{hh}:{mm}:{ss}"

- next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method


Test Code
time = Time(9, 30, 59) 

print(time.next_second()) 09:31:00

time = Time(10, 59, 59)

print(time.next_second()) 11:00:00

time = Time(23, 59, 59)

print(time.next_second())

Output

09:31:00

11:00:00

00:00:00
