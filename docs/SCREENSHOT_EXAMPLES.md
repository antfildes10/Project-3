# FlightLog Screenshot Examples - What You Should See

This document shows EXACTLY what each screenshot should look like (in text form).

---

## Screenshot #1: PEP8 Validation

**File**: `docs/screenshots/testing/pep8-validation.png`

**What your terminal should show:**

```
anthony@Anthonys-MacBook-Pro Project-3 % flake8 flightlog.py utils/*.py --max-line-length=79
anthony@Anthonys-MacBook-Pro Project-3 %
```

**Key points:**
- Command runs
- NO output = SUCCESS (0 errors)
- You see your prompt again immediately
- ✅ This proves PEP8 compliance

---

## Screenshot #2: Main Menu

**File**: `docs/screenshots/features/main-menu.png`

**What your terminal should show:**

```
============================================================
          FlightLog - Pilot Flight Hour Management
============================================================

Welcome to FlightLog!
Loading flight data...
Loaded 1 flight(s).

Main Menu:
----------------------------------------
1. Add Flight
2. View Flights
3. Edit Flight
4. Delete Flight
5. View Summary & Analytics
6. Export Data
7. Exit
----------------------------------------

Enter your choice (1-7): _
```

**Key points:**
- Shows application header
- Shows number of flights loaded
- Shows all 7 menu options clearly
- Cursor waiting for input
- ✅ This proves app launches successfully

---

## Screenshot #3: Add Flight Success

**File**: `docs/screenshots/features/add-flight.png`

**What your terminal should show:**

```
============================================================
                      ADD NEW FLIGHT
============================================================

Date (YYYY-MM-DD): 2025-10-12
Aircraft Registration: EI-XYZ
Aircraft Type: C172
Departure (ICAO/IATA): EICK
Destination (ICAO/IATA): EIDW
Duration (hours): 1.5
Remarks (optional): Training flight

------------------------------------------------------------
Flight added successfully!
------------------------------------------------------------
Date:         2025-10-12
Aircraft:     EI-XYZ (C172)
Route:        EICK -> EIDW
Duration:     1.5 hours
Remarks:      Training flight
------------------------------------------------------------

Flight has been saved to database.

Press Enter to continue...
```

**Key points:**
- Shows all input fields
- Shows confirmation with all details
- Shows success message
- ✅ This proves add functionality works with validation

---

## Screenshot #4: View Flights Table

**File**: `docs/screenshots/features/view-flights.png`

**What your terminal should show:**

```
============================================================
                       VIEW FLIGHTS
============================================================

Filter Options:
1. View All Flights
2. Filter by Date Range
3. Filter by Aircraft Type
4. Back to Main Menu

Enter your choice (1-4): 1

============================================================
+-----------+--------------+-------+------+------+-------+------------------+
| Date      | Registration | Type  | From | To   | Hours | Remarks          |
+===========+==============+=======+======+======+=======+==================+
| 2025-05-04| EI-HOX       | VIPER | EIDW | EIWT | 0.2   | Weather clear    |
| 2025-10-12| EI-XYZ       | C172  | EICK | EIDW | 1.5   | Training flight  |
+-----------+--------------+-------+------+------+-------+------------------+
============================================================

Total flights shown: 2
Total hours: 1.7

Press Enter to continue...
```

**Key points:**
- Shows formatted table with borders
- Shows all flight fields
- Shows totals at bottom
- ✅ This proves view and tabulate library working

---

## Screenshot #5: Edit Flight (Prefilled)

**File**: `docs/screenshots/features/edit-prefilled.png`

**What your terminal should show:**

```
============================================================
                  SELECT FLIGHT TO EDIT
============================================================

1. 2025-05-04 - EI-HOX (VIPER) - EIDW to EIWT - 0.2h
2. 2025-10-12 - EI-XYZ (C172) - EICK to EIDW - 1.5h

3. Cancel

Select flight number (1-3): 2

============================================================
                       EDIT FLIGHT
============================================================

Press Enter to keep current value, or enter new value.
Date [2025-10-12]:
Aircraft Registration [EI-XYZ]:
Aircraft Type [C172]:
Departure [EICK]:
Destination [EIDW]:
Duration (hours) [1.5]:
Remarks [Training flight]: _
```

**Key points:**
- Shows list of flights to choose from
- Shows current values in square brackets [like this]
- Message says "Press Enter to keep current value"
- ✅ This proves DISTINCTION criterion: never asks for known information

---

## Screenshot #6: Delete Confirmation

**File**: `docs/screenshots/features/delete-confirmation.png`

**What your terminal should show:**

```
============================================================
                 SELECT FLIGHT TO DELETE
============================================================

1. 2025-05-04 - EI-HOX (VIPER) - EIDW to EIWT - 0.2h
2. 2025-10-12 - EI-XYZ (C172) - EICK to EIDW - 1.5h

3. Cancel

Select flight number (1-3): 2

============================================================
                    CONFIRM DELETION
============================================================

You are about to delete the following flight:
------------------------------------------------------------
Date:         2025-10-12
Aircraft:     EI-XYZ (C172)
Route:        EICK -> EIDW
Duration:     1.5 hours
Remarks:      Training flight
------------------------------------------------------------

Are you sure you want to delete this flight? (yes/no): no

Deletion cancelled.

Press Enter to continue...
```

**Key points:**
- Shows flight details before deletion
- Asks for explicit confirmation
- Respects "no" answer
- ✅ This proves DISTINCTION criterion: confirmation on destructive actions

---

## Screenshot #7: Summary and Analytics

**File**: `docs/screenshots/features/summary.png`

**What your terminal should show:**

```
============================================================
                FLIGHT SUMMARY & ANALYTICS
============================================================

------------------------------------------------------------
OVERALL STATISTICS
------------------------------------------------------------
Total Flights:        2
Total Hours:          1.7
Average Duration:     0.85 hours

------------------------------------------------------------
HOURS BY AIRCRAFT TYPE
------------------------------------------------------------
+---------------+---------+-------------+
| Aircraft Type | Flights | Total Hours |
+===============+=========+=============+
| C172          | 1       | 1.5         |
| VIPER         | 1       | 0.2         |
+---------------+---------+-------------+

------------------------------------------------------------
LONGEST FLIGHT
------------------------------------------------------------
Date:        2025-10-12
Aircraft:    EI-XYZ (C172)
Route:       EICK -> EIDW
Duration:    1.5 hours

------------------------------------------------------------
SHORTEST FLIGHT
------------------------------------------------------------
Date:        2025-05-04
Aircraft:    EI-HOX (VIPER)
Route:       EIDW -> EIWT
Duration:    0.2 hours

============================================================

Press Enter to continue...
```

**Key points:**
- Shows total statistics
- Shows table of hours by type
- Shows longest and shortest flights
- ✅ This proves analytics algorithms working

---

## Screenshot #8: Export Success

**File**: `docs/screenshots/features/export-csv.png`

**What your terminal should show:**

```
============================================================
                       EXPORT DATA
============================================================

Export Options:
1. Export to CSV
2. Export Summary to Text
3. Export Both
4. Cancel

Enter your choice (1-4): 1

Success! CSV file created: exports/flights_export_20251012_091523.csv

Press Enter to continue...
```

**Key points:**
- Shows export menu
- Shows success message
- Shows timestamped filename
- ✅ This proves export functionality working

---

## Screenshot #9: Invalid Date Format Error

**File**: `docs/screenshots/testing/invalid-date-format.png`

**What your terminal should show:**

```
============================================================
                      ADD NEW FLIGHT
============================================================

Date (YYYY-MM-DD): 11/10/2025
Error: Invalid date format. Use YYYY-MM-DD.
Date (YYYY-MM-DD): _
```

**Key points:**
- User enters wrong format (slashes instead of dashes)
- Clear error message
- Prompts user to try again
- ✅ This proves input validation working

---

## Screenshot #10: Future Date Error

**File**: `docs/screenshots/testing/future-date.png`

**What your terminal should show:**

```
============================================================
                      ADD NEW FLIGHT
============================================================

Date (YYYY-MM-DD): 2026-12-31
Error: Date cannot be in the future.
Date (YYYY-MM-DD): _
```

**Key points:**
- Future date rejected
- Specific error message
- User can retry
- ✅ This proves business logic validation

---

## Screenshot #11: Negative Duration Error

**File**: `docs/screenshots/testing/negative-duration.png`

**What your terminal should show:**

```
============================================================
                      ADD NEW FLIGHT
============================================================

Date (YYYY-MM-DD): 2025-10-12
Aircraft Registration: EI-ABC
Aircraft Type: C172
Departure (ICAO/IATA): EICK
Destination (ICAO/IATA): EIDW
Duration (hours): -1.5
Error: Duration must be greater than 0.
Duration (hours): _
```

**Key points:**
- Negative value rejected
- Clear error message
- Validation catches invalid data
- ✅ This proves range validation

---

## Screenshot #12: Duplicate Flight Warning

**File**: `docs/screenshots/testing/duplicate-flight.png`

**What your terminal should show:**

```
============================================================
                      ADD NEW FLIGHT
============================================================

Date (YYYY-MM-DD): 2025-10-12
Aircraft Registration: EI-XYZ

Warning: A flight already exists for 2025-10-12 with registration EI-XYZ.
Continue anyway? (yes/no): no
Operation cancelled.

Press Enter to continue...
```

**Key points:**
- System detects duplicate
- Shows warning with details
- Gives user choice to continue or cancel
- ✅ This proves duplicate detection working

---

## Screenshot #13: Filter by Date Range (BONUS)

**File**: `docs/screenshots/features/filter-date.png`

**What your terminal should show:**

```
============================================================
                       VIEW FLIGHTS
============================================================

Filter Options:
1. View All Flights
2. Filter by Date Range
3. Filter by Aircraft Type
4. Back to Main Menu

Enter your choice (1-4): 2

------------------------------------------------------------
Filter by Date Range
------------------------------------------------------------
Start date (YYYY-MM-DD): 2025-10-01
End date (YYYY-MM-DD): 2025-10-31

Showing flights from 2025-10-01 to 2025-10-31

============================================================
+-----------+--------------+-------+------+------+-------+------------------+
| Date      | Registration | Type  | From | To   | Hours | Remarks          |
+===========+==============+=======+======+======+=======+==================+
| 2025-10-12| EI-XYZ       | C172  | EICK | EIDW | 1.5   | Training flight  |
+-----------+--------------+-------+------+------+-------+------------------+
============================================================

Total flights shown: 1
Total hours: 1.5

Press Enter to continue...
```

**Key points:**
- User enters date range
- Only matching flights shown
- Totals reflect filtered data
- ✅ This proves filtering algorithms working

---

## Screenshot #14: Export Text Summary (BONUS)

**File**: `docs/screenshots/features/export-text.png`

**What your terminal should show:**

```
============================================================
                       EXPORT DATA
============================================================

Export Options:
1. Export to CSV
2. Export Summary to Text
3. Export Both
4. Cancel

Enter your choice (1-4): 2

Success! Summary file created: exports/flight_summary_20251012_091545.txt

Press Enter to continue...
```

**Key points:**
- Shows export menu
- Shows success with filename
- Timestamp in filename
- ✅ This proves text export working

---

## 🎯 What Makes a Good Screenshot?

### ✅ Good Screenshot:
- Shows entire relevant section
- Text is readable
- Shows your terminal prompt (proves it's real)
- Shows command or menu choice
- Shows output/result
- No personal info visible

### ❌ Bad Screenshot:
- Cut off text
- Blurry or too small
- Missing the command you typed
- Missing the result
- Shows sensitive information

---

## 💡 Quick Tips

1. **Take slightly more than needed** - you can always crop later
2. **Make terminal bigger** if text is small
3. **Check screenshot before moving on** - easier to retake immediately
4. **Name files correctly** - helps with organization

---

## 📝 Notes

- Don't worry if timestamps/dates differ - that's expected
- Number of flights may vary - that's fine
- Your username will show in prompt - that's okay
- Colors may look different - terminal settings vary

---

**You're ready! Follow the checklist and refer back here if unsure what to capture.** 🚀
