import re

def validate_email(email):
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    valid = re.fullmatch(pattern, email)
    if valid:
        return True
    else: 
        return False


def validate_phone(phone):
    phone = re.sub(r"[\s+-]", "", phone)
    if phone.startswith("880"):
        phone = "0" + phone[3:]
    pattern = r"01[3-9]\d{8}$"
    valid = re.fullmatch(pattern, phone)
    if valid:
        return phone
    else:
        return None




def clean_record(record):
    clean_contract = {}
    valid_email = validate_email(record["email"])
    valid_phone = validate_phone(record["phone"])
    if (valid_email == True) and valid_phone:
        clean_contract["name"] = record["name"]
        clean_contract["email"] = record["email"]
        clean_contract["phone"] = valid_phone
    else:
        return None
    return clean_contract
