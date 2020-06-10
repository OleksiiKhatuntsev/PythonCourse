# loc = input("Entre a location: ")
# if(loc == "Home"):
#     print("Launch Lol")
# elif(loc == "Work"):
#     print("Go home and launch Lol")
# elif(loc == "Jungle"):
#     print("Eat a postmark")
# else:
#     print("I dont know it")

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if(num % 2 == 0):
        print(num)
    else:
        print(f"Odd numder {num}")

mylist = [(1,2,9), (3,4,10), (5,6,11), (7,8,12)]
for num in mylist:
    print(num)
for (a, b, c) in mylist:
    print(a)