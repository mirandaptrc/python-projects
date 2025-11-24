title = ("Number Guessing!")
print(f"{title}")

text1 = "Rules you have to pay attention for!,"
text2 = "1) You can only input numbers in between 1-10,"
text3 = "2) Only positive integers detected by the system,"
text4 = "3) No letters (a,b,c,...) included in your response"
print(text1)
print(text2)
print(text3)
print(text4)

while True:
    try:
    	num = int(input("Choose one number: "))
    except ValueError:
        print("You have to respond just in number!")
        continue  

    if not 1 <= num <= 10:
    	print("The number must be in range of 1 to 10!")
    	continue
    if num > 8:
        print("Your suggestion is greater than the target number.")
        print(num)
    elif num == 8:
        print("You're correct!")
        break
    elif num < 8:
        print("Your suggestion is less than the target number.")
        print(num)
