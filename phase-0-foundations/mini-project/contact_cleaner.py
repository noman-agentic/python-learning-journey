"""
Phase 0 Mini-Project: Simple Contact Cleaner & Validator
Combines: loops, functions, try/except, dictionaries, sets, f-strings
"""

raw_contacts = [
    "  Noman,noman@example.com,40  ",
    "Rina,rina@example,28",
    "Karim,karim@example.com,abc",
]


def is_valid_email(email):
    return "@" in email and "." in email


processed_contacts = []

for contact in raw_contacts:
    clean_contact = contact.strip()
    parts = clean_contact.split(",")

    name = parts[0]
    email = parts[1]
    age = parts[2]

    try:
        age = int(age)
    except ValueError:
        age = "Invalid"

    processed_contacts.append({
        "name": name,
        "email": email,
        "age": age,
        "email_valid": is_valid_email(email),
    })


valid_emails = set()

for contact in processed_contacts:
    if contact["email_valid"]:
        valid_emails.add(contact["email"])


for contact in processed_contacts:
    print(
        f'{contact["name"]} - '
        f'Email: {contact["email"]} '
        f'({contact["email_valid"]}) - '
        f'Age: {contact["age"]}'
    )

print("\nValid Emails:")
for email in valid_emails:
    print(email)