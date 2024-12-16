import sympy


# Function to check if a number is prime
def is_prime(n):
    return sympy.isprime(n)


# Function to find prime pairs for even numbers
def find_prime_pairs(limit):
    prime_pairs = []  # List to store the prime pairs

    # Loop through even numbers
    for even_number in range(10, limit + 1, 2):  # We start from 10 to the limit
        for prime in range(2, even_number):
            if is_prime(prime):  # Check if the number is prime
                second_prime = even_number - prime  # Subtract the prime from the even number
                if is_prime(second_prime):  # Check if the result is prime
                    prime_pairs.append((even_number, prime, second_prime))  # Store the prime pair
                    break  # Once a pair is found, move on to the next even number

    return prime_pairs


# Set the limit for even numbers (e.g., 200)
limit = 2000000

# Get the prime pairs for even numbers up to the limit
pairs = find_prime_pairs(limit)

# Print the results
for pair in pairs:
    print(f"{pair[0]} = {pair[1]} + {pair[2]}")
