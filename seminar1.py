def is_prime(number):
    if number < 2:
        return False
    if number > 2 and number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True



def test_is_prime():
    test_data = [
        [0, False],
        [1, False],
        [2, True],
        [3, True],
        [4, False],
        [7, True],
        [10, False]
    ]
    for test_entry in test_data:
        num, expected_result = test_entry
        assert is_prime(num) == expected_result

