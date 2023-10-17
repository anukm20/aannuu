time=str(input("Enter the time: "))
if time>="5" and time<="11:59":
    print("Good morning!")
elif time>="12" and time<="16:59":
    print("Good afternoon")
elif time>="17" and time<="20:59":
    print("Good evening")
elif time>="21" and time<="4:59":
    print("Good night!")
else:
    print("Invalid input")