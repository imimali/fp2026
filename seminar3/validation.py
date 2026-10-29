class EmptyStringError(Exception):
    pass

def validate_string(raw_string: str):
    if raw_string.strip() == "":
        raise EmptyStringError("Non-empty string expected")
