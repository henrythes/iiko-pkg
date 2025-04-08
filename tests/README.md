# iiko-pkg Tests

This directory contains tests for the iiko-pkg library.

## Running Tests

To run the tests, use the following command:

```bash
python run_tests.py
```

Or you can use unittest directly:

```bash
python -m unittest discover tests
```

Or using tox:

```bash
tox
```

## Test Files

- [test_client.py](test_client.py) - Tests for the IikoClient class.
- [test_models.py](test_models.py) - Tests for the models.
- [test_utils.py](test_utils.py) - Tests for the utility functions.
- [test_exceptions.py](test_exceptions.py) - Tests for the exceptions.
- [test_constants.py](test_constants.py) - Tests for the constants.

## Adding Tests

To add a new test, create a new file in the tests directory with the following naming convention:

```
test_<module_name>.py
```

For example, if you want to test the `models` module, create a file called `test_models.py`.

The test file should contain a class that inherits from `unittest.TestCase` and contains methods that start with `test_`.

Example:

```python
import unittest
from iiko_pkg.models import Organization

class TestModels(unittest.TestCase):
    def test_organization(self):
        org = Organization(
            id="test_id",
            name="Test Organization",
            country="Test Country",
            restaurant_address="Test Address",
            latitude=1.0,
            longitude=2.0
        )

        self.assertEqual(org.id, "test_id")
        self.assertEqual(org.name, "Test Organization")
        self.assertEqual(org.country, "Test Country")
        self.assertEqual(org.restaurant_address, "Test Address")
        self.assertEqual(org.latitude, 1.0)
        self.assertEqual(org.longitude, 2.0)

if __name__ == "__main__":
    unittest.main()
```
