"""
Weighted keywords used for rule-based document classification.
"""

DOCUMENT_RULES = {

    "Resume": {
        "resume": 5,
        "curriculum vitae": 5,
        "education": 3,
        "experience": 4,
        "skills": 4,
        "projects": 3,
        "internship": 3,
        "objective": 2,
        "certifications": 3,
        "github": 4,
        "linkedin": 4,
        "cgpa": 2,
        "university": 2,
    },

    "Invoice": {
        "invoice": 5,
        "invoice no": 4,
        "invoice number": 4,
        "bill": 3,
        "gst": 4,
        "amount": 3,
        "total": 3,
        "subtotal": 2,
        "tax": 2,
        "quantity": 2,
        "price": 2,
        "payment": 3,
    },

    "Aadhaar Card": {
        "aadhaar": 5,
        "uidai": 5,
        "government of india": 3,
        "unique identification authority": 5,
        "vid": 2,
        "dob": 2,
    },

    "PAN Card": {
        "permanent account number": 5,
        "income tax department": 4,
        "pan": 4,
    },

    "Passport": {
        "passport": 5,
        "republic of india": 4,
        "nationality": 3,
        "place of birth": 3,
        "date of issue": 3,
        "date of expiry": 3,
    },

    "Certificate": {
        "certificate": 5,
        "certifies": 4,
        "awarded": 4,
        "successfully completed": 5,
        "issued": 3,
        "completion": 3,
    },
}