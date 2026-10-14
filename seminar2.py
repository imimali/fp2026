"""
feature driven development

1 - read a list of numbers
2 - filter prime numbers - of the read numbers, tell which are prime
3 - delete numbers bigger than a threshold k
0 - exit

- function to read a number
- to verify primeness
- to verify primeness of a list
- a menu function

- delete numbers bigger than k from a list
- edit the menu string
- integrate deletion with the menu

"""
from seminar1 import is_prime


def verify_is_prime_list(numbers: list[int]):
    """
    Compute the primeness of a list of numbers
    :param numbers: list
    :return:
    :raises: -
    """
    result = dict()
    for number in numbers:
        result[number] = is_prime(number)
    return result

def remove_numbers_bigger_than(numbers, k):
    """
    Remove numbers bigger than k from a list
    :param numbers: list of numbers
    :param k: threshold
    :return: numbers less than or equal to k
    """
    result = []
    for number in numbers:
        if number<=k:
            result.append(number)
    return result


def test_remove_numbers_bigger_than():
    assert remove_numbers_bigger_than([],0) == []
    assert remove_numbers_bigger_than([1, 2, 3],0) == []
    assert remove_numbers_bigger_than([1, 2, 3],1) == [1]
    assert remove_numbers_bigger_than([1, 2, 3],10) == [1,2,3]


def test_verify_is_prime_list():
    assert verify_is_prime_list([]) == {}
    assert verify_is_prime_list([1]) == {1: False}
    assert verify_is_prime_list([1, 2]) == {1: False, 2: True}
    assert verify_is_prime_list([0, 3, 6]) == {0: False, 3: True, 6: False}

def end_program():
    print("Byeeee")
    exit()

def read_number_list():
    raw_numbers = input("Enter numbers:")
    numbers_list =  raw_numbers.strip().split(" ")
    return [int(number_str) for number_str in numbers_list]
    # numbers = []
    # for string_nr in numbers_list:
    #     numbers.append(int(string_nr))
    # return numbers


def menu():
    number_list = []
    while True:
        print("""
        1 - read a list of numbers
        2 - filter prime numbers - of the read numbers, tell which are prime
        3 - delete numbers bigger than a threshold
        0 - exit
        """)
        choice = input("Choose: ")
        if choice == "1":
            number_list = read_number_list()
            print("Numbers read successfully")
        elif choice == "2":
            result = verify_is_prime_list(number_list)
            for key,value in result.items():
                print(key,"is prime" if value else "is not prime")
                # if value:
                #     print(key,"is prime")
                # else:
                #     print(key,"is not prime")
        elif choice == "3":
            k = int(input("Enter threshold:"))
            number_list = remove_numbers_bigger_than(number_list,k)
        elif choice == "4":
            print("numbers are",number_list)
        elif choice == "0":
            end_program()
        else:
            print("Invalid choice")








if __name__ == '__main__':
    test_verify_is_prime_list()
    test_remove_numbers_bigger_than()
    menu()
