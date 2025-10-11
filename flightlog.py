"""FlightLog - Pilot Flight Hour Management System.

A command-line application for pilots to record, manage, and analyze
their flight hours. Provides features for data entry, validation,
analytics, and export functionality.

Author: Anthony Fildes
Course: Diploma in Full Stack Software Development - Python Essentials
Year: 2025
"""

import sys
from utils import storage


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
            print("\n[Add Flight feature - Coming soon]")
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
