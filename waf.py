import re
import os

# Simple threat patterns for demonstration
patterns = [
    r"(?i)<script.*?>.*?</script.*?>",  # XSS
    r"(?i)union\s+select",              # SQLi
    r"(?i)drop\s+table",                # SQLi
    r"(?i);.*?--",                      # SQLi
    r"(?i)(\|\||&&)",                   # Command injection
]

def waf_filter(input_data):
    if not isinstance(input_data, str):
        return True  # Block non-string input
    for pattern in patterns:
        if re.search(pattern, input_data):
            # Log blocked input robustly
            log_path = os.path.join(os.path.dirname(__file__), "blocked.log")
            with open(log_path, "a", encoding="utf-8") as log:
                log.write(f"Blocked input: {input_data}\n")
            return True
    return False
