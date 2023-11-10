from django.core.exceptions import ValidationError


def validate_customer_name(value):
    for ch in value:
        if not (ch.isalpha() or ch.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def validate_customer_age(value):
    if value < 18:
        raise ValidationError("Age must be greater than 18")


def validate_customer_phone_number(value):
    if value[:4] != '+359' or not value[5:].isdigit():
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")