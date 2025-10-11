"""FlightLog - Pilot Flight Hour Management System.

A command-line application for pilots to record, manage, and analyze
their flight hours. Provides features for data entry, validation,
analytics, and export functionality.

Author: Anthony Fildes
Course: Diploma in Full Stack Software Development - Python Essentials
Year: 2025
"""

import sys
import uuid
from utils import storage, validation


def clear_screen():
    """Clear the terminal screen."""
    print("\033[H\033[J", end="")


def print_header():
    """Display application header."""
    print("\n" + "=" * 60)
    print("FlightLog - Pilot Flight Hour Management".center(60))
    print("=" * 60 + "\n")


def display_menu():
    """Display main menu options."""
    print("\nMain Menu:")
    print("-" * 40)
    print("1. Add Flight")
    print("2. View Flights")
    print("3. Edit Flight")
    print("4. Delete Flight")
    print("5. View Summary & Analytics")
    print("6. Export Data")
    print("7. Exit")
    print("-" * 40)


def get_menu_choice():
    """Get and validate menu choice from user.

    Returns:
        str: User's menu choice.
    """
    choice = input("\nEnter your choice (1-7): ").strip()
    return choice


def add_flight(flights):
    """Add a new flight entry with full validation.

    Args:
        flights (list): List of existing flights to check for duplicates.

    Returns:
        dict: New flight dictionary if successful, None if cancelled.
    """
    print("\n" + "=" * 60)
    print("ADD NEW FLIGHT".center(60))
    print("=" * 60 + "\n")

    # Date validation
    while True:
        date_input = input("Date (YYYY-MM-DD): ").strip()
        if not date_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg = validation.validate_date(date_input)
        if is_valid:
            flight_date = date_input
            break
        else:
            print(f"Error: {error_msg}")

    # Aircraft registration validation
    while True:
        reg_input = input("Aircraft Registration: ").strip()
        if not reg_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg, reg = validation.validate_aircraft_reg(reg_input)
        if is_valid:
            aircraft_reg = reg
            break
        else:
            print(f"Error: {error_msg}")

    # Check for duplicate
    is_duplicate, dup_flight = validation.check_duplicate_flight(
        flights,
        flight_date,
        aircraft_reg
    )
    if is_duplicate:
        print(f"\nWarning: A flight already exists for {flight_date} "
              f"with registration {aircraft_reg}.")
        confirm = input("Continue anyway? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return None

    # Aircraft type validation
    while True:
        type_input = input("Aircraft Type: ").strip()
        if not type_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg, warning = validation.validate_aircraft_type(
            type_input
        )
        if is_valid:
            aircraft_type = type_input.strip().upper()
            if warning:
                print(warning)
            break
        else:
            print(f"Error: {error_msg}")

    # Departure airport validation
    while True:
        dep_input = input("Departure (ICAO/IATA): ").strip()
        if not dep_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg, dep = validation.validate_airport_code(
            dep_input,
            "Departure"
        )
        if is_valid:
            departure = dep
            break
        else:
            print(f"Error: {error_msg}")

    # Destination airport validation
    while True:
        dest_input = input("Destination (ICAO/IATA): ").strip()
        if not dest_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg, dest = validation.validate_airport_code(
            dest_input,
            "Destination"
        )
        if is_valid:
            destination = dest
            break
        else:
            print(f"Error: {error_msg}")

    # Duration validation
    while True:
        dur_input = input("Duration (hours): ").strip()
        if not dur_input:
            print("Operation cancelled.")
            return None

        is_valid, error_msg, duration = validation.validate_duration(dur_input)
        if is_valid:
            duration_hours = duration
            break
        else:
            print(f"Error: {error_msg}")

    # Remarks (optional)
    remarks_input = input("Remarks (optional): ").strip()
    is_valid, error_msg, remarks = validation.validate_remarks(remarks_input)
    if not is_valid:
        print(f"Error: {error_msg}")
        remarks = ""

    # Create flight object
    new_flight = {
        'id': str(uuid.uuid4()),
        'date': flight_date,
        'aircraft_reg': aircraft_reg,
        'aircraft_type': aircraft_type,
        'departure': departure,
        'destination': destination,
        'duration_hours': duration_hours,
        'remarks': remarks
    }

    print("\n" + "-" * 60)
    print("Flight added successfully!")
    print("-" * 60)
    print(f"Date:         {new_flight['date']}")
    print(f"Aircraft:     {new_flight['aircraft_reg']} "
          f"({new_flight['aircraft_type']})")
    print(f"Route:        {new_flight['departure']} -> "
          f"{new_flight['destination']}")
    print(f"Duration:     {new_flight['duration_hours']} hours")
    if new_flight['remarks']:
        print(f"Remarks:      {new_flight['remarks']}")
    print("-" * 60)

    return new_flight


def main():
    """Main application loop."""
    print_header()
    print("Welcome to FlightLog!")
    print("Loading flight data...")

    flights = storage.load_flights()
    print(f"Loaded {len(flights)} flight(s).\n")

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == '1':
            new_flight = add_flight(flights)
            if new_flight:
                flights.append(new_flight)
                storage.save_flights(flights)
                print("\nFlight has been saved to database.")
        elif choice == '2':
            print("\n[View Flights feature - Coming soon]")
        elif choice == '3':
            print("\n[Edit Flight feature - Coming soon]")
        elif choice == '4':
            print("\n[Delete Flight feature - Coming soon]")
        elif choice == '5':
            print("\n[Summary & Analytics feature - Coming soon]")
        elif choice == '6':
            print("\n[Export Data feature - Coming soon]")
        elif choice == '7':
            print("\nSaving flight data...")
            storage.save_flights(flights)
            print("Thank you for using FlightLog. Goodbye!")
            sys.exit(0)
        else:
            print("\nError: Invalid choice. Please enter a number 1-7.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        print("Exiting FlightLog. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        print("Please contact support if this problem persists.")
        sys.exit(1)
