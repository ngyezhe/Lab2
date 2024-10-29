print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def funcName(parameter1, parameter2) :
    print ("this is a dummy function")
    return 10

def display_main_menu():
    print ("Enter some numbers separated by commas (e.g 5, 67, 32)")

    x = input()
    num = x.split(',')
    print(num)

def calc_average():
    print("calc_average")

def get_user_input():
    print("get_user_input")

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def calc_average_temperature(num):
    print("calc_average_tempature")
    return sum(num) / len(num)

def calc_min_max_temperature(num):
    print("calc_min_max_temperature")
    return [min(num), max[num]]