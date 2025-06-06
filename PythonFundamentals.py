a = int(42)
b = float(64.5)
c = str("hello")
d = bool(True)
e = [1,2,3,4,5]
f = (5,6,7)
g = {"Student": 5, "Classes": 8}



x = 7
y = 3.5
y = float(y)
z = x + y

result = "Result" + str(z)

mixed = [1, 3.14, "hello", True, None, 2, "world", False]
nums = []
strings = []
others = []
for entry in mixed:
    if type(entry) == int or type(entry) == float:
        nums.append(entry)
    elif type(entry) == str:
        strings.append(entry)
    else:
        others.append(entry)

is_enrolled = bool()
student = {"name": "zaid", "age": 15, "grades": "A*", "major": "No major", is_enrolled: True}



def sum_even(n) -> int:
    cur_sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            cur_sum += i
    return cur_sum

def factorial (n) -> int:
    tracker = n
    answer = 1
    while tracker != 1:
        answer *= tracker 
        tracker -= 1
    return answer

def FizzBuzz (n: int) -> None:
    Fizz_counter = 0 
    Buzz_counter = 0
    FizzBuzz_counter = 0
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            FizzBuzz_counter += 1
            continue
        if number % 3 == 0:
            print("Fizz")
            Fizz_counter += 1
        if number % 5 == 0:
            Buzz_counter += 1
            print("Buzz")
    myTuple = (Fizz_counter,Buzz_counter, FizzBuzz_counter)
    print(myTuple)

def MultiplicationTable(rows: int, cols: int) -> None:
    result = 1
    for row in range(1, rows + 1):
        row_str = ""
        for col in range(1, cols + 1):
            row_str += f"{result:4d}"
            result += 1
        print(row_str)

#MultiplicationTable(3, 3)


def classify_types(mixed_list):
    nums = []
    strings = []
    others = []

    for element in mixed_list:
        if type(element) == int or type(element) == float:
            nums.append(element)
        elif type(element) == str:
            strings.append(element)
        else:
            others.append(element)
    return (nums), (strings), (others)
#print(classify_types([1, "apple", 2.5, False, None]))

def average(grades_list) -> float:
    if grades_list:
        lenList = len(grades_list)
        total = 0
        for num in grades_list:
            total += num
        return (total/lenList)
    return 0.0

def toggle_boolean(value) -> bool:
    return not value

count = 1
def increment_global_counter():
    global count
    count += 1

increment_global_counter()

def apply_to_list(func, stupid_list):
    new_list = []

    for element in stupid_list:
        new_list.append(func(element))
    
    return new_list

def squared(num):
    return num*num

def fib(n: int) -> int:
    history = []
    history.append(n)
    print(history)
    
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(5))

