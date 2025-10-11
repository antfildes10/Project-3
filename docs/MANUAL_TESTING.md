# FlightLog - Manual Testing Documentation

**Project**: FlightLog - Python Essentials Portfolio Project
**Tester**: Anthony Fildes
**Date**: 2025-10-11
**Version**: 1.0

---

## Table of Contents

1. [Testing Environment](#testing-environment)
2. [PEP8 Validation](#pep8-validation)
3. [Feature Testing](#feature-testing)
4. [Input Validation Testing](#input-validation-testing)
5. [Error Handling Testing](#error-handling-testing)
6. [Data Persistence Testing](#data-persistence-testing)
7. [Cross-Platform Testing](#cross-platform-testing)
8. [Bugs and Fixes](#bugs-and-fixes)
9. [Test Summary](#test-summary)

---

## Testing Environment

### Hardware
- **Device**: MacBook Pro / Desktop PC
- **OS**: macOS 14.0 / Windows 11
- **Terminal**: macOS Terminal / Windows PowerShell

### Software
- **Python Version**: 3.9.6
- **Dependencies**: tabulate 0.9.0
- **Linter**: flake8 6.1.0

---

## PEP8 Validation

### Validation Tool: flake8

**Command Used**:
```bash
flake8 flightlog.py utils/*.py --max-line-length=79 --show-source
```

**Result**: ✅ PASS - No errors or warnings

**Screenshot**: `docs/screenshots/testing/pep8-validation.png`

### Validation Details

| File | Lines Checked | Errors | Warnings | Status |
|------|---------------|--------|----------|--------|
| flightlog.py | 750 | 0 | 0 | ✅ PASS |
| utils/storage.py | 108 | 0 | 0 | ✅ PASS |
| utils/validation.py | 187 | 0 | 0 | ✅ PASS |
| utils/calculations.py | 177 | 0 | 0 | ✅ PASS |
| utils/export.py | 154 | 0 | 0 | ✅ PASS |

**Total**: 1376 lines of code validated with zero issues.

---

## Feature Testing

### Test Case 1: Add Flight Entry

**Test ID**: TC-001
**Feature**: Add Flight
**Priority**: Critical
**Requirement**: LO7.2 - Write code that queries and manipulates data

#### Test Steps:
1. Run application: `python3 flightlog.py`
2. Select option `1` (Add Flight)
3. Enter valid flight data:
   - Date: `2025-10-11`
   - Registration: `EI-ABC`
   - Type: `C172`
   - Departure: `EICK`
   - Destination: `EIDW`
   - Duration: `1.5`
   - Remarks: `Training flight`
4. Verify flight is saved

**Expected Result**:
- All inputs accepted
- Flight details displayed for confirmation
- Success message shown
- Data persisted to JSON file

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/add-flight.png`

**Status**: ✅ PASS

---

### Test Case 2: View All Flights

**Test ID**: TC-002
**Feature**: View Flights
**Priority**: Critical
**Requirement**: LO7.2 - Query and display data

#### Test Steps:
1. Select option `2` (View Flights)
2. Select option `1` (View All Flights)
3. Verify table display

**Expected Result**:
- Flights displayed in formatted table
- All fields visible and correctly formatted
- Total flights and hours shown

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/view-flights.png`

**Status**: ✅ PASS

---

### Test Case 3: Filter by Date Range

**Test ID**: TC-003
**Feature**: Filter Flights by Date Range
**Priority**: High
**Requirement**: LO2.2 - Combine algorithms

#### Test Steps:
1. Select option `2` (View Flights)
2. Select option `2` (Filter by Date Range)
3. Enter start date: `2025-10-01`
4. Enter end date: `2025-10-31`
5. Verify filtered results

**Expected Result**:
- Only flights within date range displayed
- Correct count shown
- Total hours for filtered flights calculated

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/filter-date.png`

**Status**: ✅ PASS

---

### Test Case 4: Filter by Aircraft Type

**Test ID**: TC-004
**Feature**: Filter Flights by Aircraft Type
**Priority**: High
**Requirement**: LO2.2 - Combine algorithms

#### Test Steps:
1. Select option `2` (View Flights)
2. Select option `3` (Filter by Aircraft Type)
3. Enter aircraft type: `C172`
4. Verify filtered results

**Expected Result**:
- Only C172 flights displayed
- Correct count and hours shown
- Case-insensitive matching

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/filter-type.png`

**Status**: ✅ PASS

---

### Test Case 5: Edit Flight (Prefilled Values)

**Test ID**: TC-005
**Feature**: Edit Flight
**Priority**: Critical
**Requirement**: DISTINCTION - Never ask for known information

#### Test Steps:
1. Select option `3` (Edit Flight)
2. Choose a flight from the list
3. Press Enter to keep all current values
4. Verify no changes made

**Expected Result**:
- All fields show current values in brackets
- Pressing Enter keeps existing values
- Update successful message shown

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/edit-prefilled.png`

**Status**: ✅ PASS

---

### Test Case 6: Edit Flight (Change Values)

**Test ID**: TC-006
**Feature**: Edit Flight with Changes
**Priority**: Critical
**Requirement**: LO7.2 - Manipulate data

#### Test Steps:
1. Select option `3` (Edit Flight)
2. Choose a flight
3. Change duration from `1.5` to `2.0`
4. Keep other values by pressing Enter
5. Verify changes saved

**Expected Result**:
- Only changed field updated
- Other fields retained
- Changes persisted to JSON

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/edit-change.png`

**Status**: ✅ PASS

---

### Test Case 7: Delete Flight with Confirmation

**Test ID**: TC-007
**Feature**: Delete Flight
**Priority**: Critical
**Requirement**: DISTINCTION - Confirm destructive actions

#### Test Steps:
1. Select option `4` (Delete Flight)
2. Choose a flight
3. Review flight details
4. Enter `no` when asked for confirmation
5. Verify flight NOT deleted

**Expected Result**:
- Flight details shown for verification
- Cancellation message displayed
- Flight still exists in database

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/delete-cancel.png`

**Status**: ✅ PASS

---

### Test Case 8: Delete Flight Confirmed

**Test ID**: TC-008
**Feature**: Delete Flight (Confirmed)
**Priority**: Critical

#### Test Steps:
1. Select option `4` (Delete Flight)
2. Choose a flight
3. Enter `yes` to confirm
4. Verify flight deleted

**Expected Result**:
- Confirmation prompt shown
- Success message displayed
- Flight removed from database
- Changes persisted

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/delete-confirm.png`

**Status**: ✅ PASS

---

### Test Case 9: View Summary and Analytics

**Test ID**: TC-009
**Feature**: Summary and Analytics
**Priority**: High
**Requirement**: LO1.1 - Implement algorithm

#### Test Steps:
1. Select option `5` (View Summary & Analytics)
2. Verify all statistics displayed

**Expected Result**:
- Total flights count shown
- Total hours calculated correctly
- Average duration calculated
- Hours by aircraft type displayed in table
- Longest flight identified correctly
- Shortest flight identified correctly

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/summary.png`

**Status**: ✅ PASS

---

### Test Case 10: Export to CSV

**Test ID**: TC-010
**Feature**: Export Data to CSV
**Priority**: High
**Requirement**: LO7.2 - Data manipulation

#### Test Steps:
1. Select option `6` (Export Data)
2. Select option `1` (Export to CSV)
3. Verify file created in exports folder
4. Open CSV file to verify contents

**Expected Result**:
- CSV file created with timestamp
- All flight data exported correctly
- File can be opened in Excel/spreadsheet software
- Success message with file path shown

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/export-csv.png`

**Status**: ✅ PASS

---

### Test Case 11: Export to Text Summary

**Test ID**: TC-011
**Feature**: Export Summary Report
**Priority**: High

#### Test Steps:
1. Select option `6` (Export Data)
2. Select option `2` (Export Summary to Text)
3. Verify file created
4. Open text file to verify format

**Expected Result**:
- Text file created with timestamp
- Summary statistics included
- Professional formatting
- Timestamp on report
- Hours by type breakdown
- Longest/shortest flight details

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/export-text.png`

**Status**: ✅ PASS

---

### Test Case 12: Export Both Formats

**Test ID**: TC-012
**Feature**: Export Both CSV and Text
**Priority**: Medium

#### Test Steps:
1. Select option `6` (Export Data)
2. Select option `3` (Export Both)
3. Verify both files created

**Expected Result**:
- Both CSV and text files created
- Success messages for both
- Files have matching timestamps

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/features/export-both.png`

**Status**: ✅ PASS

---

## Input Validation Testing

### Test Case 13: Invalid Date Format

**Test ID**: TC-013
**Feature**: Date Validation
**Priority**: Critical
**Requirement**: LO2.1 - Handle invalid input

#### Test Steps:
1. Start adding a flight
2. Enter invalid date: `11/10/2025`
3. Verify error message

**Expected Result**:
- Error message: "Invalid date format. Use YYYY-MM-DD."
- User prompted to re-enter
- Application does not crash

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/invalid-date-format.png`

**Status**: ✅ PASS

---

### Test Case 14: Future Date

**Test ID**: TC-014
**Feature**: Date Validation (Future Date)
**Priority**: Critical

#### Test Steps:
1. Start adding a flight
2. Enter future date: `2026-12-31`
3. Verify error message

**Expected Result**:
- Error message: "Date cannot be in the future."
- User prompted to re-enter
- Validation prevents future dates

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/future-date.png`

**Status**: ✅ PASS

---

### Test Case 15: Empty Registration

**Test ID**: TC-015
**Feature**: Registration Validation
**Priority**: Critical

#### Test Steps:
1. During flight entry
2. Press Enter without entering registration
3. Verify operation cancelled

**Expected Result**:
- "Operation cancelled." message shown
- Return to main menu
- No partial data saved

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/empty-registration.png`

**Status**: ✅ PASS

---

### Test Case 16: Invalid Registration Format

**Test ID**: TC-016
**Feature**: Registration Validation (Special Characters)
**Priority**: High

#### Test Steps:
1. During flight entry
2. Enter registration with special characters: `EI-ABC!@#`
3. Verify error message

**Expected Result**:
- Error: "Registration must be alphanumeric."
- User prompted to re-enter
- Special characters rejected

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/invalid-registration.png`

**Status**: ✅ PASS

---

### Test Case 17: Unknown Aircraft Type Warning

**Test ID**: TC-017
**Feature**: Aircraft Type Validation
**Priority**: Medium

#### Test Steps:
1. During flight entry
2. Enter unknown type: `CUSTOM123`
3. Verify warning message

**Expected Result**:
- Warning displayed listing known types
- Entry still accepted (allows custom types)
- User informed of unknown type

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/unknown-aircraft-type.png`

**Status**: ✅ PASS

---

### Test Case 18: Invalid Airport Code Length

**Test ID**: TC-018
**Feature**: Airport Code Validation
**Priority**: High

#### Test Steps:
1. During flight entry
2. Enter 2-character code: `EI`
3. Verify error message

**Expected Result**:
- Error: "Airport code must be 3-4 characters."
- User prompted to re-enter
- Length validation enforced

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/invalid-airport-code.png`

**Status**: ✅ PASS

---

### Test Case 19: Negative Duration

**Test ID**: TC-019
**Feature**: Duration Validation (Negative)
**Priority**: Critical

#### Test Steps:
1. During flight entry
2. Enter negative duration: `-1.5`
3. Verify error message

**Expected Result**:
- Error: "Duration must be greater than 0."
- User prompted to re-enter
- Negative values rejected

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/negative-duration.png`

**Status**: ✅ PASS

---

### Test Case 20: Duration Exceeds Maximum

**Test ID**: TC-020
**Feature**: Duration Validation (Maximum)
**Priority**: High

#### Test Steps:
1. During flight entry
2. Enter duration: `15.0`
3. Verify error message

**Expected Result**:
- Error: "Duration cannot exceed 12 hours. Split long flights into multiple entries."
- User prompted to re-enter
- Maximum validation enforced

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/max-duration.png`

**Status**: ✅ PASS

---

### Test Case 21: Non-Numeric Duration

**Test ID**: TC-021
**Feature**: Duration Validation (Type Check)
**Priority**: Critical

#### Test Steps:
1. During flight entry
2. Enter text duration: `abc`
3. Verify error message

**Expected Result**:
- Error: "Duration must be a valid number."
- User prompted to re-enter
- Type validation enforced

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/non-numeric-duration.png`

**Status**: ✅ PASS

---

### Test Case 22: Duplicate Flight Detection

**Test ID**: TC-022
**Feature**: Duplicate Flight Warning
**Priority**: High
**Requirement**: LO2.1 - Data validation

#### Test Steps:
1. Add a flight with date `2025-10-11` and registration `EI-ABC`
2. Attempt to add another flight with same date and registration
3. Verify warning shown
4. Choose to cancel

**Expected Result**:
- Warning: "A flight already exists for 2025-10-11 with registration EI-ABC."
- Prompt: "Continue anyway? (yes/no)"
- User can choose to override or cancel

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/duplicate-flight.png`

**Status**: ✅ PASS

---

### Test Case 23: Remarks Character Limit

**Test ID**: TC-023
**Feature**: Remarks Validation
**Priority**: Low

#### Test Steps:
1. During flight entry
2. Enter remarks with 501 characters
3. Verify error message

**Expected Result**:
- Error: "Remarks cannot exceed 500 characters."
- User prompted to re-enter
- Character limit enforced

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/remarks-limit.png`

**Status**: ✅ PASS

---

## Error Handling Testing

### Test Case 24: Corrupted JSON File

**Test ID**: TC-024
**Feature**: Corrupted Data Recovery
**Priority**: Critical
**Requirement**: LO3.2 - Exception handling

#### Test Steps:
1. Manually corrupt `data/flights.json` (add invalid JSON)
2. Run application
3. Verify graceful handling

**Expected Result**:
- Error message: "Error: Corrupted flight data detected."
- Backup file created with timestamp
- Message: "Backup created: data/flights.json.bad.TIMESTAMP"
- Fresh database created
- Application continues to function

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/corrupted-json.png`

**Status**: ✅ PASS

---

### Test Case 25: Missing Data File

**Test ID**: TC-025
**Feature**: Missing Data File Handling
**Priority**: High

#### Test Steps:
1. Delete `data/flights.json`
2. Run application
3. Verify automatic creation

**Expected Result**:
- Message: "No flight data found. Creating new file: data/flights.json"
- Empty database initialized
- Application functions normally

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/missing-file.png`

**Status**: ✅ PASS

---

### Test Case 26: Keyboard Interrupt (Ctrl+C)

**Test ID**: TC-026
**Feature**: Graceful Shutdown
**Priority**: Medium

#### Test Steps:
1. Run application
2. Press Ctrl+C during menu display
3. Verify clean exit

**Expected Result**:
- Message: "Application interrupted by user."
- Message: "Exiting FlightLog. Goodbye!"
- Clean exit without traceback

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/keyboard-interrupt.png`

**Status**: ✅ PASS

---

## Data Persistence Testing

### Test Case 27: Data Persistence Between Sessions

**Test ID**: TC-027
**Feature**: Data Persistence
**Priority**: Critical
**Requirement**: LO7.1 - Data model

#### Test Steps:
1. Add 3 flights
2. Exit application
3. Restart application
4. Verify all flights still present

**Expected Result**:
- All flights retained
- Data loaded correctly from JSON
- Count matches previous session

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/persistence.png`

**Status**: ✅ PASS

---

### Test Case 28: Auto-Save After Add

**Test ID**: TC-028
**Feature**: Auto-Save
**Priority**: High

#### Test Steps:
1. Add a flight
2. Immediately check `data/flights.json` file
3. Verify new flight is in file

**Expected Result**:
- Flight immediately saved to JSON
- No manual save required
- Data persists even if app crashes

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/auto-save-add.png`

**Status**: ✅ PASS

---

### Test Case 29: Auto-Save After Edit

**Test ID**: TC-029
**Feature**: Auto-Save After Edit
**Priority**: High

#### Test Steps:
1. Edit a flight
2. Immediately check JSON file
3. Verify changes saved

**Expected Result**:
- Changes immediately persisted
- JSON file updated
- No data loss risk

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/auto-save-edit.png`

**Status**: ✅ PASS

---

### Test Case 30: Auto-Save After Delete

**Test ID**: TC-030
**Feature**: Auto-Save After Delete
**Priority**: High

#### Test Steps:
1. Delete a flight
2. Immediately check JSON file
3. Verify deletion persisted

**Expected Result**:
- Flight removed from JSON
- Changes immediate
- File integrity maintained

**Actual Result**: ✅ As expected

**Screenshot**: `docs/screenshots/testing/auto-save-delete.png`

**Status**: ✅ PASS

---

## Cross-Platform Testing

### Test Case 31: macOS Terminal

**Test ID**: TC-031
**Platform**: macOS 14.0
**Terminal**: Terminal.app

**Result**: ✅ All features work correctly

**Notes**:
- Table formatting displays correctly
- Colors not used (cross-platform compatibility)
- All inputs handled properly

**Screenshot**: `docs/screenshots/testing/macos-terminal.png`

---

### Test Case 32: Windows PowerShell

**Test ID**: TC-032
**Platform**: Windows 11
**Terminal**: PowerShell

**Result**: ✅ All features work correctly

**Notes**:
- UTF-8 encoding handled correctly
- Path separators work correctly
- No platform-specific issues

**Screenshot**: `docs/screenshots/testing/windows-powershell.png`

---

## Bugs and Fixes

### Bug #1: Long Lines Exceed PEP8 Limit

**Discovered**: During flake8 validation
**Severity**: Medium
**Status**: ✅ FIXED

**Description**:
Several lines in `flightlog.py` exceeded the 79 character limit required by PEP8.

**Fix Applied**:
- Split long lines into multiple lines
- Extracted long expressions into variables
- Maintained readability while complying with PEP8

**Commit**: `5087887` - "fix: resolve PEP8 violations for code quality"

**Validation**: All code now passes flake8 with zero errors

---

### Bug #2: Unused Exception Variable

**Discovered**: During flake8 validation
**Severity**: Low
**Status**: ✅ FIXED

**Description**:
In `utils/storage.py`, exception variable `e` was captured but never used.

**Fix Applied**:
- Removed exception variable from except clause
- Changed `except (json.JSONDecodeError, ValueError) as e:` to `except (json.JSONDecodeError, ValueError):`

**Commit**: `5087887` - "fix: resolve PEP8 violations for code quality"

**Validation**: flake8 no longer reports F841 error

---

### Bug #3: Unnecessary f-string

**Discovered**: During flake8 validation
**Severity**: Low
**Status**: ✅ FIXED

**Description**:
In `utils/storage.py`, an f-string had no placeholders: `f"Error: Corrupted flight data detected."`

**Fix Applied**:
- Changed f-string to regular string
- Updated to: `"Error: Corrupted flight data detected."`

**Commit**: `5087887` - "fix: resolve PEP8 violations for code quality"

**Validation**: flake8 no longer reports F541 error

---

## Test Summary

### Overall Statistics

| Category | Total Tests | Passed | Failed | Pass Rate |
|----------|-------------|--------|--------|-----------|
| Feature Testing | 12 | 12 | 0 | 100% |
| Input Validation | 11 | 11 | 0 | 100% |
| Error Handling | 3 | 3 | 0 | 100% |
| Data Persistence | 4 | 4 | 0 | 100% |
| Cross-Platform | 2 | 2 | 0 | 100% |
| **TOTAL** | **32** | **32** | **0** | **100%** |

### PEP8 Compliance

✅ **100% Compliant** - 1376 lines validated with zero errors

### Code Quality Metrics

- **Functions**: 15+ (all with docstrings)
- **Lines of Code**: ~1376
- **Modules**: 5 (main + 4 utils)
- **External Libraries**: 1 (tabulate)
- **Test Coverage**: 32 manual test cases
- **Bugs Fixed**: 3 (all resolved)

### Learning Outcomes Coverage

| LO | Requirement | Evidence | Status |
|----|-------------|----------|--------|
| LO1 | Algorithm implementation | Calculations, analytics | ✅ |
| LO2 | Combine algorithms | Filtering, validation | ✅ |
| LO3 | Programming constructs | Loops, functions, exception handling | ✅ |
| LO4 | Explain program | README documentation | ✅ |
| LO5 | Testing and fixes | This document, bug fixes | ✅ |
| LO6 | External libraries | tabulate library | ✅ |
| LO7 | Data model | JSON CRUD operations | ✅ |
| LO8 | Version control | Git commits | ✅ |
| LO9 | Deployment | Pending cloud deployment | ⏳ |

---

## Conclusion

FlightLog has undergone comprehensive manual testing across all features, input validation scenarios, error handling cases, and data persistence operations. All 32 test cases passed successfully with a 100% pass rate.

The application demonstrates robust error handling, comprehensive input validation, and consistent behavior across different platforms. All bugs discovered during testing have been fixed and validated.

The code is fully PEP8 compliant with zero linting errors across 1376 lines of code. All functions include comprehensive docstrings, and the code follows clean code principles throughout.

**Testing Status**: ✅ COMPLETE
**Code Quality**: ✅ EXCELLENT
**Ready for Deployment**: ✅ YES

---

**Tester Signature**: Anthony Fildes
**Date**: 2025-10-11
**Version**: 1.0
