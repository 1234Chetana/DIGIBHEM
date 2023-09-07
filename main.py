import datetime

def get_valid_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            year, month, day = map(int, date_str.split('-'))
            date_obj = datetime.date(year, month, day)
            return date_obj
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def select_room_type():
    print("Select Room Type:")
    print("1. Delux Room")
    print("2. Suite Room")
    
    
    while True:
        choice = input("Enter the room type number: ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please select a valid room type.")

def select_amenities():
    amenities = []
    print("Select Amenities (enter numbers, separated by commas):")
    print("1. AC - $1000 per day")
    print("2. Locker - $300 per day")
    
    while True:
        choices = input("Enter amenity numbers (e.g., 1,2): ").split(',')
        valid_choices = ['1', '2']
        if all(choice.strip() in valid_choices for choice in choices):
            return choices
        else:
            print("Invalid choice. Please select valid amenities.")

def calculate_total_cost(room_type, total_days, amenities, total_persons):
    room_rates = {
        'Delux Room': 2500,
        'Suite Room': 4000
    }
    total_cost = room_rates[room_type] * total_days
    
    for amenity in amenities:
        if amenity == '1':
            total_cost += 1000 * total_days  # AC cost
        elif amenity == '2':
            total_cost += 300 * total_days  # Locker cost
    
    extra_person_cost = 1000 * (total_persons - 2) if total_persons > 2 else 0
    
    total_cost += extra_person_cost * total_days
    
    return total_cost

def make_payment(total_cost):
    while True:
        try:
            advance_payment = float(input(f"Enter Advance Payment (Total Cost: ${total_cost}): $"))
            if advance_payment < 0 or advance_payment > total_cost:
                print("Invalid amount. Please enter a valid amount.")
            else:
                return advance_payment
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    print("Hotel Booking Registration Form")
    customer_name = input("Customer Name: ")
    check_in_date = get_valid_date_input("Check-in Date (YYYY-MM-DD): ")
    total_days = get_valid_integer_input("Total No of Days: ")
    total_persons = get_valid_integer_input("Total No of Persons: ")
    room_type_choice = select_room_type()
    amenity_choices = select_amenities()
    
    room_types = ['Delux Room', 'Suite Room']
    selected_room_type = room_types[int(room_type_choice) - 1]
    
    total_cost = calculate_total_cost(selected_room_type, total_days, amenity_choices, total_persons)
    
    print("\nBooking Details:")
    print(f"Customer Name: {customer_name}")
    print(f"Check-in Date: {check_in_date}")
    print(f"Total No of Days: {total_days}")
    print(f"Total No of Persons: {total_persons}")
    print(f"Room Type: {selected_room_type}")
    
    selected_amenities = [amenity for amenity in amenity_choices]
    if '1' in amenity_choices:
        selected_amenities.append('AC')
    if '2' in amenity_choices:
        selected_amenities.append('Locker')
        
    print(f"Selected Amenities: {', '.join(selected_amenities)}")
    print(f"Total Cost: ${total_cost}")
    
    advance_payment = make_payment(total_cost)
    
    balance_amount = total_cost - advance_payment
    
    print(f"Advance Payment: ${advance_payment}")
    print(f"Balance Amount: ${balance_amount}")
    
if __name__ == "__main__":
    main()

