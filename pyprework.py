# Question 1 
def hello_name(user_name):
    """greet a user"""
    print("hello_" + user_name + "!")

hello_name('john69')
hello_name('hunter45')


# Question 2

def first_odds():
    for numbers in range(1,101):
        if numbers % 2 ==0:
            continue
        else:
            print(numbers)
first_odds()


# Question 3

def max_num_in_list(a_list):
    print(max(a_list))

listnumb = [1,2,3,4,5,6,7]
max_num_in_list(listnumb)

# Question 4 

def is_leap_year(year):
    if year % 4 ==0 and year % 100 != 0:
        return True
    elif year % 400 ==0:
        return True
    else:
        return False
    
print(is_leap_year(12))

# Question 5 

def is_consecutive(a_list):
    """determine if a list of numbers is consecutive"""
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

print(is_consecutive([0,1,2,3,5]))
