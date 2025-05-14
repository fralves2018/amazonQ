def validate_password(password):
    if len(password) < 8:
        return False
    
    if len(password) > 16:
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    # check for special chars (put special chars in a separeted var):
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(char in special_chars for char in password):
        return False
    
    return True


def validate_password_and_raise_reason(password):
    """
    Validates a password and raises a ValueError with the specific reason if invalid.
    Uses regular expressions for validation.
    
    Args:
        password: The password string to validate
        
    Returns:
        True if the password is valid
        
    Raises:
        ValueError: With a message explaining why the password is invalid
    """
    import re
    
    # Check length
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    if len(password) > 16:
        raise ValueError("Password must be at most 16 characters long")
    
    # Check for at least one digit
    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit")
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    
    # Check for at least one special character
    special_chars = r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]"
    if not re.search(special_chars, password):
        raise ValueError("Password must contain at least one special character")
    
    return True