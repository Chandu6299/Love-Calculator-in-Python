print("Welcome to the love calculator")
name1=input("Enter your Name ")
name2=input("Enter their Name ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

a = t + r + u + e
b = l + o + v + e

c=str(a)+str(b)
cf = int(c)
if cf < 10 or cf >90 :
    print(f"your love percentage is {c}%, you go together like coke and mentos")
elif cf <= 50 and cf >= 40:
         print(f"your love percentage is {c}%, you are alright together")
else:
    print(f"your love percentage is {c}%")
