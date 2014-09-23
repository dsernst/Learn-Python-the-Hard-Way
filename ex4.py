# define var cars as an integer = 100
cars = 100
# define var space_in_a_car as a floating point
# number = 4.0 (1 decimal place)
space_in_a_car = 4.0
# define var drivers as an integer = 30
drivers = 30
# define var passengers as an integer = 90
passengers = 90
# define var cars_not_driven as the difference
# of var cars minus var drivers
cars_not_driven = cars - drivers
# define var cars driven to be eqivalent to var drivers
cars_driven = drivers
# define var capool capicity as the product
# of var cars_driven times var space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# define var average_passengers_per_car as the quotient
# of var passengers divided by var car_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."