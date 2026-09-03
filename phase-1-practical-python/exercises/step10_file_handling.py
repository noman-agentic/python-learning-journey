# ===== Exercise 1: Create journal.txt =====
with open("journal.txt", "w") as file:
    file.write("Today I am learning Python!")

# ===== Exercise 2: Append second line =====
with open("journal.txt", "a") as file:
    file.write("\nI learned file handling!")

# ===== Exercise 3: Read and print =====
with open("journal.txt", "r") as file:
    print(file.read())