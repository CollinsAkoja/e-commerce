## debugging programming code for an e-commerce application checkout and add a debugging feature,
# first insert a bug in the discount calculation

log = []
def log_message(message):
    log.append(message)
    print(message)

def calculate_total(cart):
    total = sum(cart.values())
    log_message(f"Cart total before discount: {total}")
    return total
def apply_discount(total):
    """
    Intended: 10% discount
    :param total:
    :return:
    """
    discount = total * 0.10  # BUG: should be total * 0.10  
    final_total = total - discount
    log_message(f"Discount applied: {discount}")
    return final_total
def checkout(cart):
    try:
        total = calculate_total(cart)
        final_amount = apply_discount(total)
        log_message(f"Final amount after discount: {final_amount}")
        return final_amount
    except Exception as e:
        log_message(f"Checkout failed: {e}")
        raise
if __name__ == "__main__":
    shopping_cart = {
        "laptop": 350000,
        "mouse": 5000,
        "keyboard": 10000
    }
    amount_due = checkout(shopping_cart)
    print(f"Amount to pay: ${amount_due}")