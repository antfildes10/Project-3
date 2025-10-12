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
from tabulate import tabulate
from utils import storage, validation, calculations, export


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
    choice = input("\nEnter your choice (1-7): \n").strip()
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
        date_input = input("Date (YYYY-MM-DD): \n").strip()
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
        reg_input = input("Aircraft Registration: \n").strip()
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
        confirm = input("Continue anyway? (yes/no): \n").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return None

    # Aircraft type validation
    while True:
        type_input = input("Aircraft Type: \n").strip()
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
        dep_input = input("Departure (ICAO/IATA): \n").strip()
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
        dest_input = input("Destination (ICAO/IATA): \n").strip()
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
        dur_input = input("Duration (hours): \n").strip()
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
    remarks_input = input("Remarks (optional): \n").strip()
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


def view_flights(flights):
    """Display flights with optional filtering.

    Args:
        flights (list): List of flight dictionaries to display.
    """
    print("\n" + "=" * 60)
    print("VIEW FLIGHTS".center(60))
    print("=" * 60)

    if not flights:
        print("\nNo flights recorded yet.")
        print("Use option 1 from the main menu to add your first flight.")
        return

    print("\nFilter Options:")
    print("1. View All Flights")
    print("2. Filter by Date Range")
    print("3. Filter by Aircraft Type")
    print("4. Back to Main Menu")

    filter_choice = input("\nEnter your choice (1-4): \n").strip()

    flights_to_display = flights

    if filter_choice == '2':
        print("\n" + "-" * 60)
        print("Filter by Date Range")
        print("-" * 60)

        start_date = input("Start date (YYYY-MM-DD): \n").strip()
        is_valid, error = validation.validate_date(start_date)
        if not is_valid:
            print(f"Error: {error}")
            return

        end_date = input("End date (YYYY-MM-DD): \n").strip()
        is_valid, error = validation.validate_date(end_date)
        if not is_valid:
            print(f"Error: {error}")
            return

        try:
            flights_to_display = calculations.filter_by_date_range(
                flights,
                start_date,
                end_date
            )
            print(f"\nShowing flights from {start_date} to {end_date}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            return

    elif filter_choice == '3':
        print("\n" + "-" * 60)
        print("Filter by Aircraft Type")
        print("-" * 60)

        aircraft_type = input("Aircraft type: \n").strip().upper()
        if aircraft_type:
            flights_to_display = calculations.filter_by_aircraft_type(
                flights,
                aircraft_type
            )
            print(f"\nShowing flights for aircraft type: {aircraft_type}")

    elif filter_choice == '4':
        return

    elif filter_choice != '1':
        print("Error: Invalid choice.")
        return

    if not flights_to_display:
        print("\nNo flights match the specified criteria.")
        return

    # Prepare table data
    table_data = []
    for flight in flights_to_display:
        table_data.append([
            flight.get('date', ''),
            flight.get('aircraft_reg', ''),
            flight.get('aircraft_type', ''),
            flight.get('departure', ''),
            flight.get('destination', ''),
            flight.get('duration_hours', 0),
            flight.get('remarks', '')[:30] + '...'
            if len(flight.get('remarks', '')) > 30
            else flight.get('remarks', '')
        ])

    # Display table
    headers = [
        'Date',
        'Registration',
        'Type',
        'From',
        'To',
        'Hours',
        'Remarks'
    ]

    print("\n" + "=" * 60)
    print(tabulate(table_data, headers=headers, tablefmt='grid'))
    print("=" * 60)
    print(f"\nTotal flights shown: {len(flights_to_display)}")
    total_hours = calculations.calculate_total_hours(flights_to_display)
    print(f"Total hours: {total_hours}")


def select_flight(flights, action_name):
    """Display flights and let user select one.

    Args:
        flights (list): List of flight dictionaries.
        action_name (str): Name of action for display (e.g., "edit", "delete").

    Returns:
        tuple: (index, flight_dict) or (None, None) if cancelled.
    """
    if not flights:
        print(f"\nNo flights available to {action_name}.")
        return None, None

    print("\n" + "=" * 60)
    print(f"SELECT FLIGHT TO {action_name.upper()}".center(60))
    print("=" * 60)

    # Display numbered list of flights
    for idx, flight in enumerate(flights, 1):
        print(f"\n{idx}. {flight.get('date')} - "
              f"{flight.get('aircraft_reg')} "
              f"({flight.get('aircraft_type')}) - "
              f"{flight.get('departure')} to {flight.get('destination')} - "
              f"{flight.get('duration_hours')}h")

    print(f"\n{len(flights) + 1}. Cancel")

    while True:
        prompt = f"\nSelect flight number (1-{len(flights) + 1}): \n"
        choice = input(prompt).strip()

        if not choice:
            return None, None

        try:
            selection = int(choice)
            if selection == len(flights) + 1:
                return None, None
            if 1 <= selection <= len(flights):
                return selection - 1, flights[selection - 1]
            else:
                max_num = len(flights) + 1
                print(f"Error: Please enter a number between 1 and "
                      f"{max_num}.")
        except ValueError:
            print("Error: Please enter a valid number.")


def edit_flight(flights):
    """Edit an existing flight with prefilled values.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        bool: True if flight was edited, False otherwise.
    """
    idx, flight = select_flight(flights, "edit")

    if flight is None:
        print("Operation cancelled.")
        return False

    print("\n" + "=" * 60)
    print("EDIT FLIGHT".center(60))
    print("=" * 60)
    print("\nPress Enter to keep current value, or enter new value.")

    # Date
    while True:
        current = flight.get('date', '')
        new_date = input(f"Date [{current}]: \n").strip()

        if not new_date:
            flight_date = current
            break

        is_valid, error = validation.validate_date(new_date)
        if is_valid:
            flight_date = new_date
            break
        else:
            print(f"Error: {error}")

    # Aircraft registration
    while True:
        current = flight.get('aircraft_reg', '')
        new_reg = input(f"Aircraft Registration [{current}]: \n").strip()

        if not new_reg:
            aircraft_reg = current
            break

        is_valid, error, reg = validation.validate_aircraft_reg(new_reg)
        if is_valid:
            aircraft_reg = reg
            break
        else:
            print(f"Error: {error}")

    # Check for duplicate (excluding current flight)
    is_dup, dup_flight = validation.check_duplicate_flight(
        flights,
        flight_date,
        aircraft_reg,
        exclude_id=flight.get('id')
    )
    if is_dup:
        print(f"\nWarning: A flight already exists for {flight_date} "
              f"with registration {aircraft_reg}.")
        confirm = input("Continue anyway? (yes/no): \n").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return False

    # Aircraft type
    while True:
        current = flight.get('aircraft_type', '')
        new_type = input(f"Aircraft Type [{current}]: \n").strip()

        if not new_type:
            aircraft_type = current
            break

        is_valid, error, warning = validation.validate_aircraft_type(new_type)
        if is_valid:
            aircraft_type = new_type.strip().upper()
            if warning:
                print(warning)
            break
        else:
            print(f"Error: {error}")

    # Departure
    while True:
        current = flight.get('departure', '')
        new_dep = input(f"Departure [{current}]: \n").strip()

        if not new_dep:
            departure = current
            break

        is_valid, error, dep = validation.validate_airport_code(
            new_dep,
            "Departure"
        )
        if is_valid:
            departure = dep
            break
        else:
            print(f"Error: {error}")

    # Destination
    while True:
        current = flight.get('destination', '')
        new_dest = input(f"Destination [{current}]: \n").strip()

        if not new_dest:
            destination = current
            break

        is_valid, error, dest = validation.validate_airport_code(
            new_dest,
            "Destination"
        )
        if is_valid:
            destination = dest
            break
        else:
            print(f"Error: {error}")

    # Duration
    while True:
        current = flight.get('duration_hours', 0)
        new_dur = input(f"Duration (hours) [{current}]: \n").strip()

        if not new_dur:
            duration_hours = current
            break

        is_valid, error, duration = validation.validate_duration(new_dur)
        if is_valid:
            duration_hours = duration
            break
        else:
            print(f"Error: {error}")

    # Remarks
    current = flight.get('remarks', '')
    new_remarks = input(f"Remarks [{current}]: \n").strip()

    if not new_remarks:
        remarks = current
    else:
        is_valid, error, remarks = validation.validate_remarks(new_remarks)
        if not is_valid:
            print(f"Error: {error}")
            remarks = current

    # Update flight
    flights[idx]['date'] = flight_date
    flights[idx]['aircraft_reg'] = aircraft_reg
    flights[idx]['aircraft_type'] = aircraft_type
    flights[idx]['departure'] = departure
    flights[idx]['destination'] = destination
    flights[idx]['duration_hours'] = duration_hours
    flights[idx]['remarks'] = remarks

    print("\n" + "-" * 60)
    print("Flight updated successfully!")
    print("-" * 60)

    return True


def delete_flight(flights):
    """Delete a flight with confirmation.

    Args:
        flights (list): List of flight dictionaries.

    Returns:
        bool: True if flight was deleted, False otherwise.
    """
    idx, flight = select_flight(flights, "delete")

    if flight is None:
        print("Operation cancelled.")
        return False

    print("\n" + "=" * 60)
    print("CONFIRM DELETION".center(60))
    print("=" * 60)
    print("\nYou are about to delete the following flight:")
    print("-" * 60)
    print(f"Date:         {flight.get('date')}")
    print(f"Aircraft:     {flight.get('aircraft_reg')} "
          f"({flight.get('aircraft_type')})")
    print(f"Route:        {flight.get('departure')} -> "
          f"{flight.get('destination')}")
    print(f"Duration:     {flight.get('duration_hours')} hours")
    if flight.get('remarks'):
        print(f"Remarks:      {flight.get('remarks')}")
    print("-" * 60)

    prompt = "\nAre you sure you want to delete this flight? (yes/no): \n"
    confirm = input(prompt).strip().lower()

    if confirm in ['yes', 'y']:
        flights.pop(idx)
        print("\nFlight has been deleted successfully.")
        return True
    else:
        print("\nDeletion cancelled.")
        return False


def display_summary(flights):
    """Display flight statistics and analytics.

    Args:
        flights (list): List of flight dictionaries.
    """
    print("\n" + "=" * 60)
    print("FLIGHT SUMMARY & ANALYTICS".center(60))
    print("=" * 60)

    if not flights:
        print("\nNo flights recorded yet.")
        print("Use option 1 from the main menu to add your first flight.")
        return

    # Calculate statistics
    total_hours = calculations.calculate_total_hours(flights)
    flight_count = calculations.get_flight_count(flights)
    avg_duration = calculations.calculate_average_duration(flights)
    hours_by_type = calculations.calculate_hours_by_type(flights)
    longest = calculations.find_longest_flight(flights)
    shortest = calculations.find_shortest_flight(flights)

    # Overall statistics
    print("\n" + "-" * 60)
    print("OVERALL STATISTICS")
    print("-" * 60)
    print(f"Total Flights:        {flight_count}")
    print(f"Total Hours:          {total_hours}")
    print(f"Average Duration:     {avg_duration} hours")

    # Hours by aircraft type
    print("\n" + "-" * 60)
    print("HOURS BY AIRCRAFT TYPE")
    print("-" * 60)

    type_table = []
    for aircraft_type, hours in hours_by_type.items():
        type_count = len(calculations.filter_by_aircraft_type(
            flights,
            aircraft_type
        ))
        type_table.append([aircraft_type, type_count, hours])

    print(tabulate(
        type_table,
        headers=['Aircraft Type', 'Flights', 'Total Hours'],
        tablefmt='grid'
    ))

    # Longest flight
    if longest:
        print("\n" + "-" * 60)
        print("LONGEST FLIGHT")
        print("-" * 60)
        print(f"Date:        {longest.get('date')}")
        print(f"Aircraft:    {longest.get('aircraft_reg')} "
              f"({longest.get('aircraft_type')})")
        print(f"Route:       {longest.get('departure')} -> "
              f"{longest.get('destination')}")
        print(f"Duration:    {longest.get('duration_hours')} hours")

    # Shortest flight
    if shortest:
        print("\n" + "-" * 60)
        print("SHORTEST FLIGHT")
        print("-" * 60)
        print(f"Date:        {shortest.get('date')}")
        print(f"Aircraft:    {shortest.get('aircraft_reg')} "
              f"({shortest.get('aircraft_type')})")
        print(f"Route:       {shortest.get('departure')} -> "
              f"{shortest.get('destination')}")
        print(f"Duration:    {shortest.get('duration_hours')} hours")

    print("\n" + "=" * 60)


def export_data(flights):
    """Export flight data to file.

    Args:
        flights (list): List of flight dictionaries to export.
    """
    print("\n" + "=" * 60)
    print("EXPORT DATA".center(60))
    print("=" * 60)

    if not flights:
        print("\nNo flights to export.")
        print("Use option 1 from the main menu to add your first flight.")
        return

    print("\nExport Options:")
    print("1. Export to CSV")
    print("2. Export Summary to Text")
    print("3. Export Both")
    print("4. Cancel")

    choice = input("\nEnter your choice (1-4): \n").strip()

    if choice == '1':
        success, result = export.export_to_csv(flights)
        if success:
            print(f"\nSuccess! CSV file created: {result}")
        else:
            print(f"\nError: {result}")

    elif choice == '2':
        success, result = export.export_summary_text(flights)
        if success:
            print(f"\nSuccess! Summary file created: {result}")
        else:
            print(f"\nError: {result}")

    elif choice == '3':
        csv_success, csv_result = export.export_to_csv(flights)
        txt_success, txt_result = export.export_summary_text(flights)

        print("\n" + "-" * 60)
        if csv_success:
            print(f"CSV file created: {csv_result}")
        else:
            print(f"CSV export failed: {csv_result}")

        if txt_success:
            print(f"Summary file created: {txt_result}")
        else:
            print(f"Summary export failed: {txt_result}")
        print("-" * 60)

    elif choice == '4':
        print("\nExport cancelled.")
    else:
        print("\nError: Invalid choice.")


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
            view_flights(flights)
        elif choice == '3':
            if edit_flight(flights):
                storage.save_flights(flights)
                print("Changes have been saved.")
        elif choice == '4':
            if delete_flight(flights):
                storage.save_flights(flights)
                print("Changes have been saved.")
        elif choice == '5':
            display_summary(flights)
        elif choice == '6':
            export_data(flights)
        elif choice == '7':
            print("\nSaving flight data...")
            storage.save_flights(flights)
            print("Thank you for using FlightLog. Goodbye!")
            sys.exit(0)
        else:
            print("\nError: Invalid choice. Please enter a number 1-7.")

        input("\nPress Enter to continue...\n")


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
