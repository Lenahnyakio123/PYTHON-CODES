import logging

logging.basicConfig(
    filename='bank_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds account balance."""
    pass

def withdraw(balance, amount_input):
    try:
        amount = float(amount_input)

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")

        if amount > balance:
            raise InsufficientFundsError(
                f"Insufficient funds: Requested {amount}, Available {balance}"
            )

        balance -= amount
        print(f"Withdrawal successful. New balance: {balance}")
        return balance

    except ValueError as e:
        print(f"Error: Invalid input - {e}")
        # 5. Log any errors that occur
        logging.error(f"ValueError: {e} | Input was: {amount_input}")

    except InsufficientFundsError as e:
        print(f"Error: {e}")
        logging.error(f"InsufficientFundsError: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected Error: {e}")

    else:
        print("Transaction completed successfully. Thank you!")

    finally:
        print("Thank you for banking with us. Goodbye!")
        print("-" * 40)

    return balance

account_balance = 5000

print("--- Test 1: Valid Withdrawal ---")
account_balance = withdraw(account_balance, "1000")

print("--- Test 2: Invalid Input (ValueError) ---")
account_balance = withdraw(account_balance, "abc")

print("--- Test 3: Insufficient Funds ---")
account_balance = withdraw(account_balance, "10000")
