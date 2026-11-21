''' Activity 2, Task 2: file error handling.'''

def read_file(name):
    try:
        with open(name) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{name}' was not found. Check the name and folder.")
    except PermissionError:
        print(f"You do not have permission to open '{name}'.")
    finally:
        print("(finished attempting to open the file)")
    return None

def main():
    name = input("File to open: ")
    text = read_file(name)
    if text is not None:
        print(text)

if __name__ == "__main__":
    main()
