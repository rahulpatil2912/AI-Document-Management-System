import re


def clean_text(text):
    """
    Clean extracted text without changing its meaning.
    """

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove extra spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove trailing spaces from each line
    text = "\n".join(line.strip() for line in text.splitlines())

    # Remove leading/trailing whitespace
    text = text.strip()

    return text