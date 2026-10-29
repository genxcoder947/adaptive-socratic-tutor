SOLUTIONS = {
    "sum": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(sum(data[1:1 + n]))""",
    "maximum": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(max(data[1:1 + n]))""",
    "palindrome": """text = input().casefold()
print(str(text == text[::-1]).lower())""",
    "factorial": """n = int(input())
result = 1
for value in range(1, n + 1):
    result *= value
print(result)""",
    "prime": """n = int(input())
is_prime = n >= 2
divisor = 2
while is_prime and divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
    divisor += 1
print(str(is_prime).lower())""",
    "fibonacci": """n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)""",
    "reverse": """text = input()
print(text[::-1])""",
    "vowels": """text = input().casefold()
print(sum(character in 'aeiou' for character in text))""",
    "evens": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(sum(value % 2 == 0 for value in data[1:1 + n]))""",
    "second_max": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
values = set(data[1:1 + n])
print(sorted(values)[-2])""",
    "power": """base, exponent = map(int, input().split())
result = 1
for _ in range(exponent):
    result *= base
print(result)""",
    "word_count": """print(len(input().split()))""",
    "unique": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(len(set(data[1:1 + n])))""",    "min_value": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(min(data[1:1 + n]))""",
    "average": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
values = data[1:1 + n]
print(format(sum(values) / n, 'g'))""",
    "is_even": """n = int(input())
print('even' if n % 2 == 0 else 'odd')""",
    "sum_digits": """n = abs(int(input()))
total = 0
while n:
    total += n % 10
    n //= 10
print(total)""",
    "gcd": """import math
a, b = map(int, input().split())
print(math.gcd(a, b))""",
    "leap_year": """year = int(input())
is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print(str(is_leap).lower())""",
    "fizzbuzz": """n = int(input())
for value in range(1, n + 1):
    if value % 15 == 0:
        print('FizzBuzz')
    elif value % 3 == 0:
        print('Fizz')
    elif value % 5 == 0:
        print('Buzz')
    else:
        print(value)""",
    "anagram": """import sys
lines = sys.stdin.read().splitlines()
first = ''.join(lines[0].split()).casefold() if lines else ''
second = ''.join(lines[1].split()).casefold() if len(lines) > 1 else ''
print(str(sorted(first) == sorted(second)).lower())""",
    "numeric_palindrome": """n = int(input())
text = str(n)
print(str(text == text[::-1]).lower())""",
    "binary_search": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
values = data[1:1 + n]
target = data[1 + n]
left, right = 0, n
while left < right:
    middle = (left + right) // 2
    if values[middle] < target:
        left = middle + 1
    else:
        right = middle
print(left if left < n and values[left] == target else -1)""",
    "rotate_right": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
values = data[1:1 + n]
k = data[1 + n] % n
rotated = values[-k:] + values[:-k] if k else values
print(*rotated)""",
    "valid_parentheses": """text = input()
balance = 0
valid = True
for character in text:
    balance += 1 if character == '(' else -1
    if balance < 0:
        valid = False
        break
print(str(valid and balance == 0).lower())""",
    "deduplicate": """import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
seen = set()
result = []
for value in data[1:1 + n]:
    if value not in seen:
        seen.add(value)
        result.append(value)
print(*result)""",
    "longest_word": """words = input().split()
print(max(words, key=len) if words else '')""",
    "char_count": """import sys
lines = sys.stdin.read().splitlines()
text = lines[0] if lines else ''
target = lines[1] if len(lines) > 1 else ''
print(text.count(target[0]) if target else 0)""",
    "table": """n = int(input())
for multiplier in range(1, 11):
    print(n * multiplier)""",
}


def offline_solution(problem, language):
    if language != "python":
        return None
    return SOLUTIONS.get(problem)

