#
# temp = float(input("Whats the temperature outside?: "))
#
# if 0 <= temp <= 30:
#     print("The temperature is good today")
#     print("Go outside")
# elif temp < 0 or temp > 30:
#     print("The temperature is too cold")
#     print("Stay inside")
import time

# name = input("What is your nassme?: ")
#
# while len(name) < 1:
#     name = input("What is your name?: ")

# for i in range(10):
#     print(i)


for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy Birthday")