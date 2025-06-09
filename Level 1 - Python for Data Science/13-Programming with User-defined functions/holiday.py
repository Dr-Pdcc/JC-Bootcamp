# Function to calculate total accommodation cost based on the number of nights stayed
def hotel_cost(num_nights):
    price_per_night = 75  # Cost per night at the hotel
    return price_per_night * num_nights

# Function to determine flight cost based on the chosen destination
def plane_cost(city_flight):
    if city_flight == "Madrid":
        return 200
    elif city_flight == "New York":
        return 500
    elif city_flight == "Tokyo":
        return 800
    elif city_flight == "Sydney":
        return 900
    
# Function to calculate total car rental cost based on the number of rental days
def car_rental(rental_days):
    daily_rental_cost = 50  # Cost per day for car rental
    return rental_days * daily_rental_cost

# Function to calculate the total cost of the holiday
def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# List of valid cities with predefined flight costs
valid_cities = ["Madrid", "New York", "Tokyo", "Sydney"] # Define list of valid cities

# Loop to repeatedly prompt the user until they enter a valid city
while True:
    city_flight = input("What city are you flying to? (Madrid, New York, Tokyo, Sydney): ")
    if city_flight in valid_cities:
        break
    print("Invalid city. Please enter a city from the list.")

# Get user input for accommodation and car rental details
num_nights = int(input("How many nights are you staying at the hotel?: "))
rental_days = int(input("How many days do you need car rental?: "))

# Calculate individual and total costs
hotel_total = hotel_cost(num_nights)
flight_total = plane_cost(city_flight)
car_rental_total = car_rental(rental_days)
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print a breakdown of the total holiday cost
print("\n---- Holiday cost breakdown ----")
print(f"Destination: {city_flight}")
print(f"Hotel cost: £{hotel_total}")
print(f"Flight cost: £{flight_total}")
print(f"Car rental cost: £{car_rental_total}")
print(f"Total holiday cost: £{total_holiday_cost}")