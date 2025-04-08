#!/usr/bin/env python
"""
Run tests for iiko-pkg
"""

import unittest
import sys

if __name__ == "__main__":
    # Discover and run tests
    test_suite = unittest.defaultTestLoader.discover("tests")
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Exit with non-zero code if tests failed
    sys.exit(not result.wasSuccessful())
