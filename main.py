import os
import re

ENTRY = "Gave Earth one star because the locals worship glowing rectangles and queue for bean water, but the tacos were so good I'd let them abduct me again."

def validate(text):
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text, "entry must not have leading/trailing whitespace"
    assert not any(ord(c) < 32 or ord(c) == 127 for c in text), "entry must not contain control characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be a single sentence ending with one period"
    assert not re.search(r"[.!?]\s+[A-Z]", text), "entry must not contain a second sentence"

def main():
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
