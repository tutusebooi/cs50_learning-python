def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))

    # Convert the time to hours as a float
    return hours + minutes / 60.0

def meal(time):
    breakfast_range = (7.0, 8.0)
    lunch_range = (12.0, 13.0)
    dinner_range = (18.0, 19.0)


    time_in_hours = convert(time)

    # Check if it's breakfast, lunch, or dinner time
    if breakfast_range[0] <= time_in_hours <= breakfast_range[1]:
        print("It's breakfast time!")
    elif lunch_range[0] <= time_in_hours <= lunch_range[1]:
        print("It's lunch time!")
    elif dinner_range[0] <= time_in_hours <= dinner_range[1]:
        print("It's dinner time!")

user_time = input("Enter the time in 24-hour format (e.g., 12:30): ")


meal_time_decision(user_time)

if __name__ == "__main__":
    main()
