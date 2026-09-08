import re

text = "Call me at 01712345678 or 01898765432. My email is noman@example.com"

numbers = re.findall(r"\d+", text)
print(numbers)

word_to_find = "email"
pattern = r"\b" + word_to_find + r"\b" 
match = re.search(pattern, text)
if match:
    print(f"Found! The matched word is {match.group(0)}")
else:
    print("Email word not found!")

hidden_number_text = re.sub(r"\d+", "[HIDDEN]", text)
print(hidden_number_text)