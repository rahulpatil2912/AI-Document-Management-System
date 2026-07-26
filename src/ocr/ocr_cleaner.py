import re


def remove_duplicate_lines(lines):
    """
    Remove duplicate lines while preserving order.
    """

    seen = set()
    cleaned = []

    for line in lines:
        line = line.strip()

        if line and line not in seen:
            seen.add(line)
            cleaned.append(line)

    return cleaned


def remove_noise_lines(lines):
    """
    Remove OCR noise such as lines containing only symbols.
    """

    cleaned = []

    for line in lines:

        # Keep lines that contain at least one letter or digit
        if re.search(r"[A-Za-z0-9]", line):
            cleaned.append(line)

    return cleaned


def normalize_spacing(text):
    """
    Normalize multiple spaces and blank lines.
    """

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n\s*\n+", "\n", text)

    return text.strip()

def clean_ocr_text(text):
    """
    Clean OCR-generated text.
    """

    lines = text.splitlines()

    lines = remove_duplicate_lines(lines)

    lines = remove_noise_lines(lines)

    cleaned_text = "\n".join(lines)

    cleaned_text = normalize_spacing(cleaned_text)

    return cleaned_text