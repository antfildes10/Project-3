"""Flight data export functionality.

This module handles exporting flight data to CSV and text summary formats
for external use and reporting.
"""

import csv
import os
from datetime import datetime
from utils import calculations


EXPORT_DIR = 'exports'


def ensure_export_directory():
    """Create exports directory if it doesn't exist."""
    os.makedirs(EXPORT_DIR, exist_ok=True)


def export_to_csv(flights):
    """Export all flights to CSV file.

    Args:
        flights (list): List of flight dictionaries to export.

    Returns:
        tuple: (success, filepath_or_error_message)
    """
    if not flights:
        return False, "No flights to export."

    try:
        ensure_export_directory()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'flights_export_{timestamp}.csv'
        filepath = os.path.join(EXPORT_DIR, filename)

        fieldnames = [
            'date',
            'aircraft_reg',
            'aircraft_type',
            'departure',
            'destination',
            'duration_hours',
            'remarks'
        ]

        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for flight in flights:
                row = {field: flight.get(field, '') for field in fieldnames}
                writer.writerow(row)

        return True, filepath
    except PermissionError:
        return False, "Permission denied: Cannot write to export directory."
    except Exception as e:
        return False, f"Export failed: {str(e)}"


def export_summary_text(flights):
    """Export flight summary to text file.

    Args:
        flights (list): List of flight dictionaries to summarize.

    Returns:
        tuple: (success, filepath_or_error_message)
    """
    if not flights:
        return False, "No flights to summarize."

    try:
        ensure_export_directory()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'flight_summary_{timestamp}.txt'
        filepath = os.path.join(EXPORT_DIR, filename)

        total_hours = calculations.calculate_total_hours(flights)
        flight_count = calculations.get_flight_count(flights)
        avg_duration = calculations.calculate_average_duration(flights)
        hours_by_type = calculations.calculate_hours_by_type(flights)
        longest = calculations.find_longest_flight(flights)
        shortest = calculations.find_shortest_flight(flights)

        with open(filepath, 'w', encoding='utf-8') as textfile:
            textfile.write("=" * 60 + "\n")
            textfile.write("FLIGHT LOG SUMMARY REPORT\n")
            textfile.write("=" * 60 + "\n\n")

            report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            textfile.write(f"Generated: {report_time}\n\n")

            textfile.write("-" * 60 + "\n")
            textfile.write("OVERALL STATISTICS\n")
            textfile.write("-" * 60 + "\n")
            textfile.write(f"Total Flights:        {flight_count}\n")
            textfile.write(f"Total Hours:          {total_hours}\n")
            textfile.write(f"Average Duration:     {avg_duration} hours\n\n")

            textfile.write("-" * 60 + "\n")
            textfile.write("HOURS BY AIRCRAFT TYPE\n")
            textfile.write("-" * 60 + "\n")
            for aircraft_type, hours in hours_by_type.items():
                textfile.write(f"{aircraft_type:<20} {hours:>10.2f} hours\n")
            textfile.write("\n")

            if longest:
                textfile.write("-" * 60 + "\n")
                textfile.write("LONGEST FLIGHT\n")
                textfile.write("-" * 60 + "\n")
                textfile.write(f"Date:        {longest.get('date')}\n")
                textfile.write(
                    f"Aircraft:    {longest.get('aircraft_reg')} "
                    f"({longest.get('aircraft_type')})\n"
                )
                textfile.write(
                    f"Route:       {longest.get('departure')} -> "
                    f"{longest.get('destination')}\n"
                )
                textfile.write(
                    f"Duration:    {longest.get('duration_hours')} hours\n\n"
                )

            if shortest:
                textfile.write("-" * 60 + "\n")
                textfile.write("SHORTEST FLIGHT\n")
                textfile.write("-" * 60 + "\n")
                textfile.write(f"Date:        {shortest.get('date')}\n")
                textfile.write(
                    f"Aircraft:    {shortest.get('aircraft_reg')} "
                    f"({shortest.get('aircraft_type')})\n"
                )
                textfile.write(
                    f"Route:       {shortest.get('departure')} -> "
                    f"{shortest.get('destination')}\n"
                )
                textfile.write(
                    f"Duration:    {shortest.get('duration_hours')} hours\n\n"
                )

            textfile.write("=" * 60 + "\n")
            textfile.write("END OF REPORT\n")
            textfile.write("=" * 60 + "\n")

        return True, filepath
    except PermissionError:
        return False, "Permission denied: Cannot write to export directory."
    except Exception as e:
        return False, f"Export failed: {str(e)}"
