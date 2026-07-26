from ner.entity_patterns import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    URL_PATTERN,
    DATE_PATTERN,
    PINCODE_PATTERN,
    PAN_PATTERN,
    AADHAAR_PATTERN,
)


def extract_entities(text):
    """
    Extract structured entities from text using regex patterns.
    """

    entities = {
        "emails": sorted(set(EMAIL_PATTERN.findall(text))),
        "phones": sorted(set(PHONE_PATTERN.findall(text))),
        "urls": sorted(set(URL_PATTERN.findall(text))),
        "dates": sorted(set(DATE_PATTERN.findall(text))),
        "pincodes": sorted(set(PINCODE_PATTERN.findall(text))),
        "pan_numbers": sorted(set(PAN_PATTERN.findall(text))),
        "aadhaar_numbers": sorted(set(AADHAAR_PATTERN.findall(text))),
    }

    return entities