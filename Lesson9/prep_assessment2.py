from unittest import TestCase, main
from Lesson9.ATM_program import verify_pin

class TestPinVerification(TestCase):

    def test_correct_pin(self):
        pin_input = '1234'
        result = verify_pin(pin_input)
        self.assertTrue(result)

if __name__ == '__main__':
    main()

# from unittest import mock
# from unittest import TestCase, main
# from Lesson9.ATM_program import verify_pin, log_in, run_atm
#
# class TestAtm(TestCase):
#
#     # test 1: GIVEN pin equal 1234 THEN pin successfully verified
#     def test_correct_pin(self):
#         pin_input = '1234'
#         result = verify_pin(pin_input)
#         self.assertTrue(result)
#
# if __name__ == '__main__':
#     main()

