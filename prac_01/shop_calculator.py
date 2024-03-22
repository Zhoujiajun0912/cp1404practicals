
# Shop Calculator Program

# Function to prompt for the number of items with input validation
def get_number_of_items():
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    return num_items

# Main program logic
def main():
    total_price = 0
    num_items = get_number_of_items()

    # Loop to get the price for each item
    for i in range(num_items):
        price = float(input(f"Price of item: "))
        total_price += price

    # Apply discount if applicable
    if total_price > 100:
        total_price *= 0.9  # Apply a 10% discount

    print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()