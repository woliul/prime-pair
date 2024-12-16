import sympy
import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    return sympy.isprime(n)

# Function to find prime pairs for even numbers in a specific range
def find_prime_pairs_in_range(start, end):
    prime_pairs = []  # List to store the prime pairs
    formulation = []  # List to store the mathematical formulation

    # Loop through even numbers in the specified range
    for even_number in range(start, end + 1, 2):
        for prime in range(2, even_number):
            if is_prime(prime):  # Check if the number is prime
                second_prime = even_number - prime  # Subtract the prime from the even number
                if is_prime(second_prime):  # Check if the result is prime
                    prime_pairs.append((even_number, prime, second_prime))  # Store the prime pair
                    # Add the formulation to the list
                    formulation.append(f"{even_number} = {prime} + {second_prime}")
                    break  # Once a pair is found, move on to the next even number

    return formulation

# Function to split the range into chunks for parallel processing
def chunk_range(start, end, num_chunks):
    step = (end - start) // num_chunks
    ranges = [(start + i * step, start + (i + 1) * step - 1) for i in range(num_chunks)]
    # Ensure the last chunk goes all the way to 'end'
    ranges[-1] = (ranges[-1][0], end)
    return ranges

def main():
    # Set the limit for even numbers (e.g., 4*10^18)
    limit = 4*pow(10,18)
    num_chunks = 4  # You can adjust the number of chunks based on your system's core count

    # Divide the range into smaller chunks
    ranges = chunk_range(4, limit, num_chunks)

    # Use multiprocessing Pool to process each chunk in parallel
    with multiprocessing.Pool(processes=num_chunks) as pool:
        results = pool.starmap(find_prime_pairs_in_range, ranges)

    # Combine results from all processes
    formulations = [item for sublist in results for item in sublist]

    # Print the mathematical formulations (you can limit the output for large numbers)
    for formula in formulations[:10]:  # Limiting output for example purposes
        print(formula)

    # Optionally, save to a file
    with open("goldbach_conjecture_proof.txt", "w") as f:
        for formula in formulations:
            f.write(formula + "\n")

# Ensures the multiprocessing code runs only when executed directly
if __name__ == '__main__':
    main()
