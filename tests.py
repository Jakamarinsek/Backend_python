from Counting import check_guess

def testing_check_guess():
    dict = {"Slovenia": "Ljubljana"}
    assert check_guess("Ljubljana", "Slovenia", dict) == True
    return "testing_check_guess() passed OK"

print testing_check_guess()