def prime():
    raw_input = input("Enter a list of numbers separated by commas: ")

    try:
        numbers_list = [int(x.strip()) for x in raw_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return

    primes = [
        n for n in numbers_list
        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    ]

    if primes:
        print("\nFinal sorted list:", sorted(primes))
    else:
        print("No prime numbers found")
prime()
