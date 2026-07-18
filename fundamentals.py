# Diagonal Stripe Check

matrix = [
    [42, 7, 13, 99],
    [6, 42, 7, 13],
    [1, 6, 42, 7]
]

# prints: 0,1,2
# for i in range(len(matrix)):
#     print(i)

# prints [42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]
# for i in matrix:
#     print(i)

# prints: 1,2, range excludes last value
# for i in range(1,len(matrix)):
#     print(i)

# loop backwards
# prints: 2,1
# for i in reversed(range(1,len(matrix))):
#     print(i) 

# 3rd parameter is step
# for i in reversed(range(1,len(matrix), 1)):
#     print(i) 

credit_card = "1234-567-8910"

# for in range(leng(credit_card)) prints index from 0 to end
# for i in credit_card prints actaul string value from 1 to end
# for i in range(1,len(credit_card),2):
#     print(i)

# string = "hello"

# print(len(string))


# SET FUNCTION

# x = set(('apple', 'banana', 'cherry', 'apple'))
# y = set('hello')
# print(y)

# DICTIONARIES
s = "listen"
num = 756
t = "silent"
s_dict = {}
t_dict = {}

#for letter in range(num):
    #print(letter)

for i in range(len(s)):
    if s[i] not in s_dict:
        s_dict[s[i]] = 1
    else:
        s_dict[s[i]] + 1

for j in range(len(t)):
    if t[j] not in t_dict:
        t_dict[t[j]] = 1
    else:
        t_dict[t[j]] + 1

#if s_dict == t_dict:
    #print("True")
#else:
    #print("False")


# PASCALS TRIANGLE:


# trim / strip
#phrase = "Taco cat"
# phrase = "abccba"
# phrase = phrase.lower().replace(" ", "")

# middle = len(phrase) // 2

# half_word = phrase[middle:]
# print(half_word)


txt = "Hello World" [::-1]
# print(txt)

# BASE 13 CONVERSION

num = 4735
base = 13
digits = "0123456789ABC"

base13_conversion = ""

while num > 0:
    remainder = num % base
    base13_conversion = digits[remainder] + base13_conversion
    num //= base

#print(base13_conversion)  # 2203
  
# loop through a number?

def is_looping_number(noom):
    seen = set()

    while noom != 1 and noom not in seen:
        seen.add(noom)

        digits = []

        for i in range(len(str(noom))):
            digits.append(noom % 10)
            noom //= 10

        digits.reverse()

        for i in range(len(digits)):
            digits[i] *= digits[i]

        noom = sum(digits)

    # Reaching 1 means it is not looping.
    # Reaching an already-seen number means there is a cycle.
    return noom != 1


print(is_looping_number(4))   # True
print(is_looping_number(19))  # False
#print(*reversed(digits)) # reversed(digits) prints the object not the contents of the object, use *
