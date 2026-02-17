def numbers():
    org_list = input("Enter a list of numbers separated by commas: ")
    # Convert input string into a list of integers
    org_list = [int(x.strip()) for x in org_list.split(",")]
    
    # Filter only even numbers
    even_list = [num for num in org_list if num % 2 == 0]
    
    if even_list:
        even_list.sort()
        print("\nFinal sorted list:", even_list)
    else:
        print("No even numbers found!")

numbers()
