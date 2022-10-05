
# practicing loop

def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# Infinite Loops and How to Break Them

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n = n+1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# print_prime_factors function print all the prime factors of a number. 
#print_prime_factors function print all the prime factors of a number. 

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  i = 1
  sum = 0
  while i < n:
    if n % i == 0:
      sum += i
      i +=1
    else:
      i+=1
  return sum
    

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114