import math
arrival_rate = float(input("Enter arrival rate per hour: "))
if arrival_rate <= 0:
    while arrival_rate <= 0:
        print("arrival rate can't be 0")
        arrival_rate = float(input("Enter arrival rate  per hour: "))

service_rate = float(input("Enter service rate per hour: "))
if service_rate <= 0:
    while service_rate <= 0:
        print("service rate can't be 0")
        service_rate = float(input("Enter service rate per hour: "))

print(f"The arrival rate is {arrival_rate}")
print(f"The service rate is {service_rate}")

pho = arrival_rate/service_rate

print("Probablity that there are n number of people in the system")
print("How many number of people do you want to determine: ")

n = int(input("Input the number of people: "))

p = 1-pho

ans = math.pow(p,n) * (p)
#if type(n) != int:
#    while type(n) is not int:
#        print("n is supposed to be an enter an integer")
#        n = int(input("Input the number of people: "))

print(f"For {n} number of people, the answer is {ans}")

len_of_system = pho / (1-pho)
len_of_queue = len_of_system - pho
wait_of_system = len_of_system / arrival_rate
wait_of_queue = len_of_queue / arrival_rate

print(f"The length of the system is {len_of_system}, the length of the queue is {len_of_queue}, waiting time of the system is {wait_of_system}, and the waiting time of the queue is {wait_of_queue}")