import unittest
from password_checker import validate_password, validate_password_and_raise_reason

class TestPasswordValidator(unittest.TestCase):
    
    def test_valid_password(self):
        """Test that valid passwords return True."""
        valid_passwords = [
            "Password1!",
            "Abcdefg1!",
            "aB3!efghi",
            "1aB!2345678",
            "p@Ssw0rd",
            "A1b2C3d4!",
            "Test12345!"
        ]
        for password in valid_passwords:
            with self.subTest(password=password):
                self.assertTrue(validate_password(password), f"Password '{password}' should be valid")
    
    def test_password_too_short(self):
        """Test that passwords shorter than 8 characters return False."""
        short_passwords = [
            "Abc1!",
            "A1b!",
            "1aB!",
            "aB3!",
            "Ab1!"
        ]
        for password in short_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (too short)")
    
    def test_password_too_long(self):
        """Test that passwords longer than 16 characters return False."""
        long_passwords = [
            "Abcdefg1!Abcdefg1!",
            "ThisPasswordIs17Ch!",
            "VeryLongPassword123!",
            "1234567890AbCdEf!+"
        ]
        for password in long_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (too long)")
    
    def test_password_no_digits(self):
        """Test that passwords without digits return False."""
        no_digit_passwords = [
            "Password!",
            "AbcdefgH!",
            "NoDigitsHere!",
            "OnlyLetters!"
        ]
        for password in no_digit_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (no digits)")
    
    def test_password_no_uppercase(self):
        """Test that passwords without uppercase letters return False."""
        no_uppercase_passwords = [
            "password1!",
            "allsmall123!",
            "nouppercases1!",
            "only2lower!"
        ]
        for password in no_uppercase_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (no uppercase)")
    
    def test_password_no_lowercase(self):
        """Test that passwords without lowercase letters return False."""
        no_lowercase_passwords = [
            "PASSWORD1!",
            "ALLCAPS123!",
            "NOLOWERCASE1!",
            "ONLY2UPPER!"
        ]
        for password in no_lowercase_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (no lowercase)")
    
    def test_password_no_special_chars(self):
        """Test that passwords without special characters return False."""
        no_special_passwords = [
            "Password123",
            "Abcdefg123",
            "NoSpecialChars1",
            "JustAlphaNum2"
        ]
        for password in no_special_passwords:
            with self.subTest(password=password):
                self.assertFalse(validate_password(password), f"Password '{password}' should be invalid (no special chars)")
    
    def test_edge_cases(self):
        """Test edge cases."""
        edge_cases = [
            ("", False),  # Empty string
            ("A1b3d!g", False),  # 7 chars (too short)
            ("A1b2C3d4!678901234", False),  # 17 chars (too long)
            ("A1b2C3d4!6789012", True),  # 16 chars (max length)
            ("A1b2C3d!", True),  # 8 chars (min length)
        ]
        for password, expected in edge_cases:
            with self.subTest(password=password):
                self.assertEqual(validate_password(password), expected, 
                                f"Password '{password}' validation result should be {expected}")


class TestPasswordValidatorWithReason(unittest.TestCase):
    
    def test_valid_password_no_exception(self):
        """Test that valid passwords don't raise exceptions."""
        valid_passwords = [
            "Password1!",
            "Abcdefg1!",
            "aB3!efghi",
            "1aB!2345678"
        ]
        for password in valid_passwords:
            with self.subTest(password=password):
                try:
                    result = validate_password_and_raise_reason(password)
                    self.assertTrue(result, f"Password '{password}' should be valid")
                except ValueError:
                    self.fail(f"Password '{password}' raised ValueError unexpectedly")
    
    def test_password_too_short_exception(self):
        """Test that passwords shorter than 8 characters raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("Abc1!")
        self.assertIn("at least 8 characters", str(context.exception))
    
    def test_password_too_long_exception(self):
        """Test that passwords longer than 16 characters raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("ThisPasswordIs17Ch!")
        self.assertIn("at most 16 characters", str(context.exception))
    
    def test_password_no_digits_exception(self):
        """Test that passwords without digits raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("Password!")
        self.assertIn("digit", str(context.exception))
    
    def test_password_no_uppercase_exception(self):
        """Test that passwords without uppercase letters raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("password1!")
        self.assertIn("uppercase", str(context.exception))
    
    def test_password_no_lowercase_exception(self):
        """Test that passwords without lowercase letters raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("PASSWORD1!")
        self.assertIn("lowercase", str(context.exception))
    
    def test_password_no_special_chars_exception(self):
        """Test that passwords without special characters raise appropriate exception."""
        with self.assertRaises(ValueError) as context:
            validate_password_and_raise_reason("Password123")
        self.assertIn("special character", str(context.exception))


if __name__ == '__main__':
    unittest.main()