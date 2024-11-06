import ecommerce_plataform.user as user
import pytest
def test_validate_email_with_valid_emails():
    # Arrange
    valid_emails = [
        "test@test.com",
        "test@test.com.ar",
        "test@test.com.ar.ar"
    ]

    # Act & Assert
    for email in valid_emails:
        assert user.User.validate_email(email) == email

def test_validate_email_with_invalid_email():
    # Arrange
    invalid_email = "test@test.com.ar.ar.ar"

    # Act & Assert
    with pytest.raises(ValueError):
        user.User.validate_email(invalid_email)
