def check_sum_equal_50(num_str):
    if not num_str.isdigit():
        print("Invalid input.")
        return
    
    total = sum(int(digit) for digit in num_str)

    if total == 50:
        print("Success!")
    else:
        print(f"The sum is not 50.")

num_str = input("Enter a numeric string: ")
check_sum_equal_50(num_str)
