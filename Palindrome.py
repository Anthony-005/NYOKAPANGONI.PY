def check_palindrome():
    text = input("Enter a word or phrase: ").strip().lower()
    text = text.replace(" ", "")
    
    if text == text[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
check_palindrome()
