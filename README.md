# Simple Pytest Example

This is Simple project on how to test python code with Pytest.

* [YouTube - Pytest Unit Testing Tutorial • How to test your Python code](https://www.youtube.com/watch?v=YbpKMIUjvK8&list=PLZJBfja3V3RvxooZ5SNOr7CMFzURr4NBs&index=2)
* [YouTube - PyTest • REST API Integration Testing with Python](https://www.youtube.com/watch?v=7dgQRVqF1N0&list=PLZJBfja3V3RvxooZ5SNOr7CMFzURr4NBs&index=3)
* [Pytest Documentation](https://docs.pytest.org/en/6.2.x/getting-started.html#getstarted)
* [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)

### Install Pytest

```bash
pip install pytest
```

### Run the tests

```bash
pytest
```

### Run a specific file

```bash
pytest test_shopping_cart.py
```

### Run a specific test

```bash
pytest test_shopping_cart.py::test_can_get_total_price
```