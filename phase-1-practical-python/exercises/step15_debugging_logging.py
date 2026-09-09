import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename= "phase-1-practical-python/exercises/app.log"
)


my_city = ["Gopalganj", "Dhaka", "Narayanganj"]

def city_i_know(city_number):
    if (city_number == 1):
        print(f"I was born {my_city[0]}.")
    elif (city_number == 2):
        print(f"My first job in {my_city[1]}.")
    elif (city_number == 3):
        print(f"Currently, I live in {my_city[2]}.")
    else:
        print(my_city[city_number])

try:
    city_i_know(9)
except IndexError:
    logging.error("Please! Enter between 1 to 3.")