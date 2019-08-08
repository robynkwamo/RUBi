
from sqlite_database import *

# ####################********* Check data in the table total available power generated ************######################
# x = input("At what time do you want to check the power generated? ")
# t = convert_to_integer_get_hourly_power_by_daytime_from_db(x)
# print('The power generated at ', x, ' am is: ', t)
#
# ####################********* Check data in the table hourly power cost ************####################################
# x = input("At what time do you want to check the power cost? ")
# t = convert_to_integer_get_hourly_power_cost_by_daytime_week_from_db(x)
# print('The power cost at ', x, ' am is: ', t, '$')
#
#
# ####################********* Check data in the table hourly power cost ************####################################
# x = input("At what time do you want to check the power cost of the weekend? ")
# t = convert_to_integer_get_hourly_power_cost_by_daytime_weekend_from_db(x)
# print('The power cost at ', x, ' am is: ', t, '$')


# ####################********* Check data in the table when the customer is home during the week ************###########
# x = input("At what time do you want to check if the customer is home? ")
# t = convert_to_int_get_hourly_isHomeweek_from_db(x)
# if t == 1:
#     z = 'Home'
# else:
#     z = 'Not Home'
# print('At ', x, ' the customer is: ', z)
#
#
# ####################********* Check data in the table when the customer is sleeping during the week ************########
# x = input("At what time do you want to check if the customer is home? ")
# t = convert_to_int_get_hourly_isSleepingWeek_from_db(x)
# if t == 1:
#     z = 'Sleeping'
# else:
#     z = 'Not Sleeping'
# print('At ', x, ' the customer is: ', z)


# ####################********* Check data in the table when the customer is home during the weekend ************#######
# x = input("At what time do you want to check if the customer is home during the weekend? ")
# t = convert_to_int_get_hourly_isHomeweekend_from_db(x)
# if t == 1:
#     z = 'Home'
# else:
#     z = 'Not Home'
# print('At ', x, ' the customer is: ', z)
#
#
# ####################********* Check data in the table when the customer is sleeping during the weekend ************###
# x = input("At what time do you want to check if the customer is sleeping during the weekend? ")
# t = convert_to_int_get_hourly_isSleepingWeekend_from_db(x)
# if t == 1:
#     z = 'Sleeping'
# else:
#     z = 'Not Sleeping'
# print('At ', x, ' the customer is: ', z)


# ####################********* Check data in the table when the lights are on during the week ************###############
# x = input("At what time do you want to check if the light is on during the week? ")
# t = convert_to_int_get_hourly_isLightWeek_from_db(x)
# if t == 1:
#     z = 'ON'
# else:
#     z = 'OFF'
# print('At ', x, ' the lights are: ', z)
#
#
# ####################********* Check data in the table when the lights are on during the weekend ************###############
# x = input("At what time do you want to check if the light is on during the weekend? ")
# t = convert_to_int_get_hourly_isLightWeekend_from_db(x)
# if t == 1:
#     z = 'ON'
# else:
#     z = 'OFF'
# print('At ', x, ' the lights are: ', z)
#
#
# ####################********* Check data in the table of the lights power consumption during the week ********###############
# x = input("At what time do you want to check if the light power consumption during the week? ")
# t = convert_to_int_get_hourly_LightPowerWeek_from_db(x)
# print('The light power consumption during the week at ', x, ' am is: ', t, '')
#
#
# ####################********* Check data in the table of the lights power consumption during the weekend ********###############
# x = input("At what time do you want to check if the light power consumption during the weekend? ")
# t = convert_to_int_get_hourly_LightPowerWeekend_from_db(x)
# print('The light power consumption during the weekend at ', x, ' am is: ', t, '')
#
#
# ####################********* Check data in the table of total static power consumption during the week ********###############
# x = input("At what time do you want to check the total static power consumption during the week? ")
# t = convert_to_int_get_hourly_totalStaticPowerUsedWeek_from_db(x)
# print('The total power consume by waterheater, fridge and lights during the weekend at ', x, ' am is: ', t, '')
#
#
# ####################********* Check data in the table of the total static power consumption during the weekend ********###############
# x = input("At what time do you want to check the total static power consumption during the weekend? ")
# t = convert_to_int_get_hourly_totalStaticPowerUsedWeekend_from_db(x)
# print('The total power consume by waterheater, fridge and lights during the weekend at ', x, ' am is: ', t, '')
#
#
# ####################********* Check data in the table of the preferred temperature during the week ********###############
# x = input("At what time do you want to check the prefered tempareture during the week? ")
# t = convert_to_int_get_hourly_tempPrefWeek1_from_db(x)
# print('The prefered temperature during the week at ', x, ' am is: ', t, '')

####################********* Check data in the table of the preferred temperature during the weekend ********###############
# x = input("At what time do you want to check the prefered temperature during the weekend? ")
# t = convert_to_int_get_hourly_tempPrefWeekend1_from_db(x)
# print('The prefered temperature during the weekend at ', x, ' am is: ', t, '')
#
# ####################********* Check data in the table that has all the variables ***************########################
# x = input("Which variable value do you want to check ")
# t = freeVariable_from_db(x)
# print(' The variable values at ', x, ' is: ', t, '')

# ####################********* Check data in the table of ac Power consumption during the week ********##################
# x = input("At what time do you want to check the AC power consumption during the week? ")
# t = convert_to_int_get_hourly_acPowerWeek_from_db(x)
# print('The AC power consumption during the week at ', x, ' am is: ', t, '')
#
# ####################********* Check data in the table of ac Power consumption during the weekend ********###############
# x = input("At what time do you want to check the AC power consumption during the weekend? ")
# t = convert_to_int_get_hourly_acPowerWeekend_from_db(x)
# print('The AC power consumption during the weekend at ', x, ' am is: ', t, '')
#
# ####################********* Check data in the table of car charger Power consumption during the weekend ********###############
# x = input("At what time do you want to check the car charger power consumption during the week? ")
# t = convert_to_int_get_hourly_carChargerPowerWeek_from_db(x)
# print('The car charger power consumption during the week at ', x, ' am is: ', t, '')
#
# ####################********* Check data in the table of car charger Power consumption during the week ********###############
# x = input("At what time do you want to check the car charger power consumption during the weekend? ")
# t = convert_to_int_get_hourly_carChargerPowerWeekend_from_db(x)
# print('The car charger power consumption during the weekend at ', x, ' am is: ', t, '')

####################********* Check data in the table of credit Generated during the week ********###############
x = input("At what time do you want to check the credit generated during the week? ")
t = convert_to_int_get_hourly_creditGeneratedWeek_from_db(x)
print("The credit generated during the week at ", x, " am is: ", t, ".")

####################********* Check data in the table of credit Generated during the weekend ********###############
x = input("At what time do you want to check the credit generated during the weekend? ")
t = convert_to_int_get_hourly_carChargerPowerWeekend_from_db(x)
print("The credit generated during the weekend at ", x, " am is: ", t, ".")

####################********* Check data in the table of cost of energy to by during the week ********###############
x = input("At what time do you want to check the cost of energy to buy during the week? ")
t = convert_to_int_get_hourly_energyToBuyWeek_from_db(x)
print("The debited energy to buy during the week at ", x, " am is: ", t, ".")

####################********* Check data in the table of cost of energy to by during the weekend ********###############
x = input("At what time do you want to check  the cost of energy to buy during the weekend? ")
t = convert_to_int_get_hourly_energyToBuyWeekend_from_db(x)
print("The debited energy to buy during the weekend at ", x, " am is: ", t, ".")