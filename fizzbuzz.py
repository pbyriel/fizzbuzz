#python3
#FizzBuzz exercise for Thinkful Python course

import sys

get_number = True

print('#'*17)
print("This is Fizz Buzz")
print('#'*17)

# checks to see if CLI arg given and if integer, 
# else asks for number (and checks)
while get_number:
    try:
        n = int(sys.argv[1])
        get_number = False
    except:
        try:
            print("You did not provide a whole number yet")
            n = int(input("What number do you want to count to: "))
            get_number = False
        except: 
            continue

print("Fizz buzz counting up to {}".format(n))

for i in range(1,n+1):
  if (i % 3 == 0) and (i % 5 == 0):
    print("fizz buzz")
  elif (i % 3 == 0):
    print("fizz")
  elif (i % 5 == 0):
    print("buzz")
  else:
    print(i)