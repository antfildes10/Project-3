"""Flight analytics and calculations.

This module provides functions for calculating statistics and filtering
flight data for analysis and reporting.
"""

from datetime import datetime


def calculate_total_hours(flights):
    """Calculate total flight hours.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        float: Total hours flown, rounded to 2 decimal places.
    """
    if not flights:
        return 0.0

    total = sum(flight.get('duration_hours', 0) for flight in flights)
    return round(total, 2)


def calculate_hours_by_type(flights):
    """Calculate hours flown per aircraft type.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        dict: Dictionary mapping aircraft type to total hours.
              Sorted by hours (descending).
    """
    if not flights:
        return {}

    hours_by_type = {}

    for flight in flights:
        aircraft_type = flight.get('aircraft_type', 'Unknown')
        duration = flight.get('duration_hours', 0)
        hours_by_type[aircraft_type] = (
            hours_by_type.get(aircraft_type, 0) + duration
        )

    sorted_types = dict(
        sorted(
            hours_by_type.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    return {k: round(v, 2) for k, v in sorted_types.items()}


def find_longest_flight(flights):
    """Find the flight with the longest duration.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        dict: Flight dictionary with longest duration, or None if empty.
    """
    if not flights:
        return None

    return max(flights, key=lambda x: x.get('duration_hours', 0))


def find_shortest_flight(flights):
    """Find the flight with the shortest duration.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        dict: Flight dictionary with shortest duration, or None if empty.
    """
    if not flights:
        return None

    return min(flights, key=lambda x: x.get('duration_hours', 0))


def filter_by_date_range(flights, start_date, end_date):
    """Filter flights by date range (inclusive).

    Args:
        flights (list): List of flight dictionaries.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        list: Filtered list of flights within date range.

    Raises:
        ValueError: If date format is invalid.
    """
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {str(e)}")

    if start > end:
        raise ValueError("Start date must be before or equal to end date.")

    filtered = []
    for flight in flights:
        flight_date_str = flight.get('date', '')
        try:
            flight_date = datetime.strptime(
                flight_date_str,
                '%Y-%m-%d'
            ).date()
            if start <= flight_date <= end:
                filtered.append(flight)
        except ValueError:
            continue

    return filtered


def filter_by_aircraft_type(flights, aircraft_type):
    """Filter flights by aircraft type.

    Args:
        flights (list): List of flight dictionaries.
        aircraft_type (str): Aircraft type to filter by (case-insensitive).

    Returns:
        list: Filtered list of flights matching aircraft type.
    """
    if not aircraft_type:
        return flights

    aircraft_type_upper = aircraft_type.strip().upper()

    return [
        flight for flight in flights
        if flight.get('aircraft_type', '').upper() == aircraft_type_upper
    ]


def get_flight_count(flights):
    """Get total number of flights.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        int: Number of flights.
    """
    return len(flights) if flights else 0


def calculate_average_duration(flights):
    """Calculate average flight duration.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        float: Average duration in hours, or 0 if no flights.
    """
    if not flights:
        return 0.0

    total = calculate_total_hours(flights)
    count = get_flight_count(flights)

    return round(total / count, 2) if count > 0 else 0.0
