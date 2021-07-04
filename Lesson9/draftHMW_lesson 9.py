# Use Simple ATM program (previous homework) to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

from unittest import mock
from unittest import TestCase, main
from Lesson9.ATM_program import verify_pin, log_in, run_atm

#test 1: expected result: pin successfully verified, pin equal to 1234
#test 2: expected result: unsuccessful login, pin not equal to 1234
#test 3: expected result: unsuccessful login & close program, if user tries to insert the pin 4 times incorrectly, the 5th should close the program
#test 4: expected result: new balance message, pre condition: successful login, balance should subtract from original balance
#test 5: expected result: error message, pre condition: successful login, Insufficient fund for withdrawals higher than balance

class TestAtm(TestCase):

    def test_correct_pin(self):
        pin_input = '1234'
        result = verify_pin(pin_input)
        self.assertTrue(result)

if __name__ == '__main__':
    main()