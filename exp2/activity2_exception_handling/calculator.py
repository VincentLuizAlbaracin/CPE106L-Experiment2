''' Activity 2, Task 3: calculator with multiple exception handlers.'''

OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}

def calculate(a, op, b):
    return OPS[op](a, b)

def main():
    while True:
        text = input("Enter 'num op num' (e.g. 8 / 2) or q to quit: ").strip()
        if text.lower() == "q":
            break
        try:
            a, op, b = text.split()
            result = calculate(float(a), op, float(b))
        except ValueError:
            print("  ValueError: enter two numbers and an operator separated by spaces.")
        except ZeroDivisionError:
            print("  ZeroDivisionError: cannot divide by zero.")
        except Exception as e:                 # anything unexpected
            print(f"  Unexpected {type(e).__name__}: {e}")
        else:
            print(f"  Result = {result}")

if __name__ == "__main__":
    main()
