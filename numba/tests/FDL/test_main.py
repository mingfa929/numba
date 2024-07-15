import unittest
from numba.tests.test_typeinfer import TestArgRetCasting


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestArgRetCasting("test_arg_ret_casting"))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print(result)
