import unittest

# Find the test files in the current directory
tests = unittest.TestLoader().discover('.')

# Specify the level of information provided by the test runner
testRunner = unittest.TextTestRunner(verbosity=2)

result = testRunner.run(tests)

# Check the test results
if result.wasSuccessful():
    print("All tests passed!")
else:
    print("Some tests failed.")
