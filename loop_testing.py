print("Please enter an integer")
try:
    user_in = int(input())
except:
    print("Please ensure you are entering a valid integer")
    exit()

for i in range(1, user_in, 1):
    if user_in % i == 0:
        print(i)
print("These are the factors of", user_in)