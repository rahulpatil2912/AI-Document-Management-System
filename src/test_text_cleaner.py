from nlp.text_cleaner import clean_text


sample_text = """

RESUME


Ritesh     Dagadu


Kuwar


Python,      Django

Machine      Learning

Git



"""

print("Before Cleaning:\n")
print(sample_text)

cleaned = clean_text(sample_text)

print("\n" + "=" * 50)

print("\nAfter Cleaning:\n")
print(cleaned)