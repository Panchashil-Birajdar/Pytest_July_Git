from selenium import webdriver


# Configure Interpreter
# Pip Install selenium
# Pip Install Pytest
# Pip Install Pytest-html
# Pip Install Pytest-xdist
# Select pytest as a default runner in python integrated tools setting

class   Test_Credence:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a & b =",sum)
        if  sum == 10:
            assert True
        else:
            assert False

    def test_credence_002(self):
        driver = webdriver.Firefox()
        driver.get("https://credence.in/")
        if  driver.title == "Credence":
            print('You are at Credence.in')
            assert True
        else:
            print("You are at wrong url")
            assert False
        driver.close()

    def test_sub_003(self):
        a = 3
        b = 7
        sub = a - b
        print("Sub of a from b =", sub)
        if sub == -4:
            assert True
        else:
            assert False
































































































































































































































































