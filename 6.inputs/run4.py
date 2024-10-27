"""
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
user_input = float(input("Enter temperature: "))
print(type(user_input))
print(weather_condition(user_input))
"""
##################
"""
user_input = input("Enter your username: ")
# message = "Hello %s!" % user_input
# message = "Hello {}!".format(user_input)
message = f"Hello {user_input}!"
print(message)
"""
##################

name = input("Enter your firstname: ")
surname = input("Enter your surname: ")
when = "today"
# message = "Hello %s %s!" % (name, surname)
# message = "Hello {} {}!".format(name, surname)
message = f"Hello {name} {surname}! What's up {when}"
print(message)
