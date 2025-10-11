"""Input validation for flight data.

This module contains all validation functions for flight entry fields,
ensuring data integrity and proper formatting.
"""

from datetime import datetime


KNOWN_AIRCRAFT_TYPES = [
    'C152', 'C172', 'C182', 'PA28', 'PA44', 'DA40', 'DA42',
    'SR20', 'SR22', 'BE58', 'BE76', 'A320', 'B737', 'B747'
]


def validate_date(date_str):
    """Validate date string in ISO format (YYYY-MM-DD).

    Args:
        date_str (str): Date string to validate.

    Returns:
        tuple: (is_valid, error_message)
               is_valid (bool): True if valid, False otherwise.
               error_message (str): Error description or empty string.
    """
    if not date_str or not date_str.strip():
        return False, "Date is required."

    try:
        flight_date = datetime.strptime(date_str.strip(), '%Y-%m-%d')
        today = datetime.now()

        if flight_date.date() > today.date():
            return False, "Date cannot be in the future."

        return True, ""
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."


def validate_aircraft_reg(registration):
    """Validate aircraft registration.

    Args:
        registration (str): Aircraft registration to validate.

    Returns:
        tuple: (is_valid, error_message, formatted_value)
               formatted_value (str): Uppercase version of registration.
    """
    if not registration or not registration.strip():
        return False, "Aircraft registration is required.", ""

    reg = registration.strip().upper()

    if not reg.replace('-', '').isalnum():
        return False, "Registration must be alphanumeric.", ""

    if len(reg) < 2 or len(reg) > 10:
        return False, "Registration must be 2-10 characters.", ""

    return True, "", reg


def validate_aircraft_type(aircraft_type):
    """Validate aircraft type.

    Args:
        aircraft_type (str): Aircraft type to validate.

    Returns:
        tuple: (is_valid, error_message, warning)
               warning (str): Warning if type not in known list.
    """
    if not aircraft_type or not aircraft_type.strip():
        return False, "Aircraft type is required.", ""

    atype = aircraft_type.strip().upper()

    if atype not in KNOWN_AIRCRAFT_TYPES:
        warning = (
            f"Warning: '{atype}' is not in the known aircraft list. "
            f"Known types: {', '.join(KNOWN_AIRCRAFT_TYPES[:7])}..."
        )
        return True, "", warning

    return True, "", ""


def validate_airport_code(code, field_name="Airport"):
    """Validate ICAO/IATA airport code.

    Args:
        code (str): Airport code to validate.
        field_name (str): Field name for error messages.

    Returns:
        tuple: (is_valid, error_message, formatted_value)
    """
    if not code or not code.strip():
        return False, f"{field_name} code is required.", ""

    code_upper = code.strip().upper()

    if not code_upper.isalpha():
        return False, f"{field_name} code must contain only letters.", ""

    if len(code_upper) < 3 or len(code_upper) > 4:
        return False, f"{field_name} code must be 3-4 characters.", ""

    return True, "", code_upper


def validate_duration(duration_str):
    """Validate flight duration in hours.

    Args:
        duration_str (str): Duration string to validate.

    Returns:
        tuple: (is_valid, error_message, float_value)
    """
    if not duration_str or not str(duration_str).strip():
        return False, "Duration is required.", 0.0

    try:
        duration = float(str(duration_str).strip())

        if duration <= 0:
            return False, "Duration must be greater than 0.", 0.0

        if duration > 12.0:
            return (
                False,
                "Duration cannot exceed 12 hours. "
                "Split long flights into multiple entries.",
                0.0
            )

        return True, "", duration
    except ValueError:
        return False, "Duration must be a valid number.", 0.0


def check_duplicate_flight(flights, date, aircraft_reg, exclude_id=None):
    """Check for duplicate flight entry.

    Args:
        flights (list): List of existing flights.
        date (str): Flight date to check.
        aircraft_reg (str): Aircraft registration to check.
        exclude_id (str): Flight ID to exclude from check (for edits).

    Returns:
        tuple: (is_duplicate, duplicate_flight)
    """
    for flight in flights:
        if exclude_id and flight.get('id') == exclude_id:
            continue

        if (flight.get('date') == date and
                flight.get('aircraft_reg') == aircraft_reg):
            return True, flight

    return False, None


def validate_remarks(remarks):
    """Validate remarks field.

    Args:
        remarks (str): Remarks text to validate.

    Returns:
        tuple: (is_valid, error_message, cleaned_value)
    """
    if not remarks:
        return True, "", ""

    cleaned = remarks.strip()

    if len(cleaned) > 500:
        return False, "Remarks cannot exceed 500 characters.", ""

    return True, "", cleaned
