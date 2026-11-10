# Handle ValueError when converting user input into integers.
i=int(input("Enter a number: "))
def get_int_val(i):
    try:
        if (0 <= int(i) <= 100):
            return (f"The valid number is {i}")
        else:
            print("Input is out of bounds. Please enter an integer between 0 and 100.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None
print(get_int_val(i))
    