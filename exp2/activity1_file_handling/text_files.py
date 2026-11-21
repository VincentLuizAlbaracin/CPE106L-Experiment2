''' Activity 1, Task 1: text file operations (students.txt).'''

FILENAME = "students.txt"

def create_and_write():
    with open(FILENAME, "w") as f:                 # "w" creates / overwrites
        f.write("ID,Name,Course\n")
        f.write("2021001,Juan Dela Cruz,BSCpE\n")
        f.write("2021002,Maria Santos,BSCpE\n")
        f.write("2021003,Jose Reyes,BSEE\n")
    print(f"[Created] {FILENAME} and wrote 3 student records.")

def read_file():
    with open(FILENAME, "r") as f:                 # "r" reads
        content = f.read()
    print("[Read] Contents of", FILENAME)
    print(content)

def append_records():
    with open(FILENAME, "a") as f:                 # "a" adds to the end
        f.write("2021004,Ana Garcia,BSCpE\n")
        f.write("2021005,Pedro Bautista,BSECE\n")
    print("[Appended] 2 more records.")

if __name__ == "__main__":
    create_and_write()
    read_file()
    append_records()
    read_file()
