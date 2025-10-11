"""Flight data storage operations.

This module handles all JSON file operations for flight data persistence,
including loading, saving, and backup functionality.
"""

import json
import os
from datetime import datetime


FLIGHTS_FILE = 'data/flights.json'


def load_flights():
    """Load flight data from JSON file.

    Returns:
        list: List of flight dictionaries. Returns empty list if file
              doesn't exist or is corrupted.

    Raises:
        None: All exceptions are handled internally with user feedback.
    """
    if not os.path.exists(FLIGHTS_FILE):
        print(f"No flight data found. Creating new file: {FLIGHTS_FILE}")
        save_flights([])
        return []

    try:
        with open(FLIGHTS_FILE, 'r', encoding='utf-8') as file:
            flights = json.load(file)
            if not isinstance(flights, list):
                raise ValueError("Invalid data structure")
            return flights
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error: Corrupted flight data detected.")
        backup_file = backup_corrupted_file()
        print(f"Backup created: {backup_file}")
        print("Creating fresh flight data file.")
        save_flights([])
        return []
    except PermissionError:
        print("Error: Permission denied accessing flight data.")
        return []
    except Exception as e:
        print(f"Error loading flight data: {str(e)}")
        return []


def save_flights(flights):
    """Save flight data to JSON file.

    Args:
        flights (list): List of flight dictionaries to save.

    Returns:
        bool: True if save successful, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(FLIGHTS_FILE), exist_ok=True)
        with open(FLIGHTS_FILE, 'w', encoding='utf-8') as file:
            json.dump(flights, file, indent=2, ensure_ascii=False)
        return True
    except PermissionError:
        print("Error: Permission denied when saving flight data.")
        return False
    except Exception as e:
        print(f"Error saving flight data: {str(e)}")
        return False


def backup_corrupted_file():
    """Create timestamped backup of corrupted JSON file.

    Returns:
        str: Path to backup file, or None if backup failed.
    """
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        backup_path = f"{FLIGHTS_FILE}.bad.{timestamp}"

        if os.path.exists(FLIGHTS_FILE):
            with open(FLIGHTS_FILE, 'r', encoding='utf-8') as source:
                content = source.read()
            with open(backup_path, 'w', encoding='utf-8') as backup:
                backup.write(content)
            return backup_path
    except Exception as e:
        print(f"Warning: Could not create backup: {str(e)}")
        return None


def get_flight_by_id(flights, flight_id):
    """Find a flight by its unique ID.

    Args:
        flights (list): List of flight dictionaries.
        flight_id (str): UUID of the flight to find.

    Returns:
        dict: Flight dictionary if found, None otherwise.
    """
    for flight in flights:
        if flight.get('id') == flight_id:
            return flight
    return None
