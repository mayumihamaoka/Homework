# Use Simple ATM program (previous homework) to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

from unittest import mock
from unittest import TestCase, main
from Lesson9.ATM_program import verify_pin, log_in, run_atm

class TestAtm(TestCase):

    # test 1: GIVEN pin equal 1234 THEN pin successfully verified
    def test_correct_pin(self):
        pin_input = '1234'
        result = verify_pin(pin_input)
        self.assertTrue(result)

    @mock.patch('Lesson9.ATM_program.input')
    def test_login_correct_pin(self, mock_input):
        pin_input = '1234'
        mock_input.return_value = pin_input
        result = log_in()
        self.assertTrue(result)

    # test 2: GIVEN pin not equal to 1234 THEN unsuccessful verification
    def test_incorrect_pin(self):
        pin_input2 = '5555'
        result = verify_pin(pin_input2)
        self.assertFalse(result)

    # test 3: GIVEN pin not equal to 1234 four times THEN unsuccessful login & close program on 5th try
    @mock.patch('Lesson9.ATM_program.input')
    def test_login_incorrectPin_multiple_attempts(self, mock_input):
        pin_input = '124'
        mock_input.return_value = pin_input
        result = log_in()
        self.assertFalse(result)

    #test 4: GIVEN pin equal to 1234 AND withdrawal_amount lower than balance THEN successful withdrawal
    @mock.patch('Lesson9.ATM_program.input')
    def test_login_withdrawal(self, mock_input):
        pin_input = '1234'
        mock_input.return_value = pin_input
        withdrawal_amount = 50
        result = run_atm(withdrawal_amount)
        self.assertTrue(result)

    #test 5: GIVEN pin equal to 1234 AND withdrawal_amount lower than balance THEN new balance subtract from original balance
    @mock.patch('Lesson9.ATM_program.input')
    def test_login_newbalance(self, mock_input):
        pin_input = '1234'
        mock_input.return_value = pin_input
        withdrawal_amount = 10
        result = run_atm(withdrawal_amount)
        new_balance = 100 - withdrawal_amount
        self.assertEqual(result,new_balance)

    # #test Don't know how to do: GIVEN pin equal to 1234 AND withdrawal_amount higher than balance THEN Valueerror msg Insufficient fund for withdrawals
    # @mock.patch('Lesson9.ATM_program.input')
    # def test_login_insufficient_funds(self, mock_input):
    #     pin_input = '1234'
    #     mock_input.return_value = pin_input
    #     withdrawal_amount = 9999
    #     result = run_atm(withdrawal_amount)
    #     self.assertRaises(ValueError, result, 'Insufficient funds on your account')
# OR
    # @mock.patch('Lesson9.ATM_program.input')
    # def test_login_insufficient_funds(self, mock_input):
    #     pin_input = '1234'
    #     mock_input.return_value = pin_input
    #     withdrawal_amount = 9999
    #     result = run_atm(withdrawal_amount)
    #     self.assertEqual(type(result),ValueError)

if __name__ == '__main__':
    main()