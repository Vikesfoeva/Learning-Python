user_in = int(input())

for i in range(1, user_in, 1):
    if user_in % i == 0:
        print(i)
print("These are the factors of", user_in)