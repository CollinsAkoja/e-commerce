# E-Commerce Checkout System

A Python-based e-commerce application that demonstrates a basic checkout system with discount calculation and logging features.

## Overview

This project implements a simple shopping cart checkout process with the following features:
- **Cart Management**: Add items and their prices to a shopping cart
- **Discount Calculation**: Apply a 10% discount to the total purchase amount
- **Transaction Logging**: Track all checkout operations and calculations
- **Error Handling**: Graceful exception handling during the checkout process

## Features

- **calculate_total(cart)**: Computes the sum of all items in the shopping cart
- **apply_discount(total)**: Applies a 10% discount to the total amount
- **checkout(cart)**: Orchestrates the complete checkout process
- **log_message(message)**: Logs all operations and prints them to the console

## Installation

No external dependencies required. Simply ensure you have Python 3.x installed.

```bash
python --version
```

## Usage

Run the application:

```bash
python e-commerce.py
```

### Example Output

```
Cart total before discount: 365000
Discount applied: 36500
Final amount after discount: 328500
Amount to pay: $328500
```

### Custom Usage

Modify the `shopping_cart` dictionary in the `__main__` block to add your own items:

```python
shopping_cart = {
    "item_name": price,
    "another_item": price,
}
amount_due = checkout(shopping_cart)
```

## Project Structure

```
e-commerce/
├── e-commerce.py    # Main application file
├── README.md        # This file
```

## How It Works

1. **Initialize Cart**: Define items and their prices
2. **Calculate Total**: Sum all item prices
3. **Apply Discount**: Calculate and subtract a 10% discount
4. **Checkout**: Process the transaction and return the final amount
5. **Logging**: All steps are logged for debugging and transaction tracking

## Debugging Features

The application includes comprehensive logging that tracks:
- Cart totals before discounts
- Discount amounts applied
- Final amounts after discounts
- Any errors encountered during checkout

Access logs via the `log` list variable for further analysis.

## Notes

- This is a demonstration project designed for educational purposes
- Prices are in arbitrary currency units
- Error handling ensures the system gracefully manages exceptions