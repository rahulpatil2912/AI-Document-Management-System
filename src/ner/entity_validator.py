from datetime import datetime
import re


def validate_date(date_str):
    """
    Returns True if the date is valid.
    """
    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%d/%m/%y",
        "%d-%m-%y",
    ]

    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue

    return False


def validate_phone(phone):
    """
    Validates Indian phone numbers.
    """
    digits = re.sub(r"\D", "", phone)

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return len(digits) == 10 and digits[0] in "6789"


def validate_pincode(pincode):
    """
    Validates Indian PIN codes.
    """
    return (
        len(pincode) == 6
        and pincode.isdigit()
        and pincode[0] != "0"
    )


def validate_aadhaar(aadhaar):
    """
    Basic Aadhaar validation.
    """
    digits = re.sub(r"\D", "", aadhaar)
    return len(digits) == 12


def normalize_email(email):
    """
    Converts email to lowercase.
    """
    return email.strip().lower()


def validate_entities(entities):
    """
    Returns a new dictionary containing only valid entities.
    """

    validated_entities = {
        "emails": sorted({
            normalize_email(email)
            for email in entities.get("emails", [])
        }),

        "phones": sorted({
            phone
            for phone in entities.get("phones", [])
            if validate_phone(phone)
        }),

        "urls": sorted(set(entities.get("urls", []))),

        "dates": sorted({
            date
            for date in entities.get("dates", [])
            if validate_date(date)
        }),

        "pincodes": sorted({
            pincode
            for pincode in entities.get("pincodes", [])
            if validate_pincode(pincode)
        }),

        "pan_numbers": sorted(set(
            entities.get("pan_numbers", [])
        )),

        "aadhaar_numbers": sorted({
            aadhaar
            for aadhaar in entities.get("aadhaar_numbers", [])
            if validate_aadhaar(aadhaar)
        }),
    }

    return validated_entities