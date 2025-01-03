filename = input("Enter file name: ")
try:
    with open(filename, 'r') as file1:
        line = file1.readlines()
    lines = [l.strip() for l in line]  # Fixed variable name to `l` instead of `line`
    print("Lines from the file:", lines)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
