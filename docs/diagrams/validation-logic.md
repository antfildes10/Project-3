# FlightLog Validation Logic

This diagram shows the detailed validation sequence for adding or editing a flight record. Every input field undergoes comprehensive validation before being accepted.

```mermaid
flowchart TD
    Start([User Selects Add/Edit Flight]) --> DateInput[Request Date Input]

    DateInput --> DateCheck{Date Valid?}
    DateCheck -->|Empty| Cancel1([Cancel Operation])
    DateCheck -->|Invalid Format| DateError1[Error: Invalid date format<br/>Use YYYY-MM-DD]
    DateCheck -->|Future Date| DateError2[Error: Date cannot<br/>be in the future]
    DateCheck -->|Valid| RegInput[Request Aircraft Registration]
    DateError1 --> DateInput
    DateError2 --> DateInput

    RegInput --> RegCheck{Registration Valid?}
    RegCheck -->|Empty| Cancel2([Cancel Operation])
    RegCheck -->|Invalid Format| RegError[Error: 2-10 characters<br/>Letters, numbers, hyphens only]
    RegCheck -->|Valid| DupCheck{Duplicate Flight?}
    RegError --> RegInput

    DupCheck -->|Yes| DupWarn[Warning: Flight exists<br/>Continue anyway?]
    DupWarn --> DupConfirm{User Confirms?}
    DupConfirm -->|No| Cancel3([Cancel Operation])
    DupConfirm -->|Yes| TypeInput
    DupCheck -->|No| TypeInput[Request Aircraft Type]

    TypeInput --> TypeCheck{Type Valid?}
    TypeCheck -->|Empty| Cancel4([Cancel Operation])
    TypeCheck -->|Valid| DepInput[Request Departure Airport]

    DepInput --> DepCheck{Departure Valid?}
    DepCheck -->|Empty| Cancel5([Cancel Operation])
    DepCheck -->|Invalid Length| DepError[Error: Must be<br/>3-4 characters]
    DepCheck -->|Invalid Format| DepError
    DepCheck -->|Valid| DestInput[Request Destination Airport]
    DepError --> DepInput

    DestInput --> DestCheck{Destination Valid?}
    DestCheck -->|Empty| Cancel6([Cancel Operation])
    DestCheck -->|Invalid Length| DestError[Error: Must be<br/>3-4 characters]
    DestCheck -->|Invalid Format| DestError
    DestCheck -->|Valid| DurInput[Request Flight Duration]
    DestError --> DestInput

    DurInput --> DurCheck{Duration Valid?}
    DurCheck -->|Empty| Cancel7([Cancel Operation])
    DurCheck -->|Not a Number| DurError1[Error: Must be<br/>a number]
    DurCheck -->|Negative/Zero| DurError2[Error: Duration must<br/>be greater than 0]
    DurCheck -->|Too Large| DurError3[Error: Duration must<br/>be ≤ 12 hours]
    DurCheck -->|Valid| RemarkInput[Request Remarks Optional]
    DurError1 --> DurInput
    DurError2 --> DurInput
    DurError3 --> DurInput

    RemarkInput --> RemarkCheck{Remarks Valid?}
    RemarkCheck -->|Too Long| RemarkError[Error: Max 200 characters]
    RemarkCheck -->|Valid/Empty| CreateFlight[Create Flight Record]
    RemarkError --> RemarkInput

    CreateFlight --> GenerateID[Generate UUID]
    GenerateID --> AssembleData[Assemble Flight Data]
    AssembleData --> SaveData[Save to flights.json]
    SaveData --> ShowConfirm[Display Confirmation<br/>with Flight Details]
    ShowConfirm --> Success([Return to Main Menu])

    style Start fill:#90EE90
    style Success fill:#90EE90
    style Cancel1 fill:#FFB6C1
    style Cancel2 fill:#FFB6C1
    style Cancel3 fill:#FFB6C1
    style Cancel4 fill:#FFB6C1
    style Cancel5 fill:#FFB6C1
    style Cancel6 fill:#FFB6C1
    style Cancel7 fill:#FFB6C1
    style DateError1 fill:#FFD700
    style DateError2 fill:#FFD700
    style RegError fill:#FFD700
    style DepError fill:#FFD700
    style DestError fill:#FFD700
    style DurError1 fill:#FFD700
    style DurError2 fill:#FFD700
    style DurError3 fill:#FFD700
    style RemarkError fill:#FFD700
    style DupWarn fill:#FFA500
```

## Validation Rules

### 1. Date Validation
- **Format**: Must be YYYY-MM-DD
- **Range**: Cannot be in the future
- **Required**: Yes (empty cancels operation)
- **Implementation**: `validation.validate_date()`

### 2. Aircraft Registration Validation
- **Length**: 2-10 characters
- **Characters**: Alphanumeric and hyphens only
- **Case**: Converted to uppercase
- **Required**: Yes
- **Implementation**: `validation.validate_aircraft_reg()`

### 3. Duplicate Flight Check
- **Check**: (date + aircraft_reg) combination
- **Action**: Warns user, allows override
- **Purpose**: Prevent accidental duplicate entries
- **Implementation**: `validation.check_duplicate_flight()`

### 4. Aircraft Type Validation
- **Length**: Must not be empty
- **Case**: Converted to uppercase
- **Required**: Yes
- **Implementation**: `validation.validate_aircraft_type()`

### 5. Airport Code Validation (Departure & Destination)
- **Length**: 3-4 characters (ICAO or IATA format)
- **Characters**: Alphanumeric only
- **Case**: Converted to uppercase
- **Required**: Yes
- **Implementation**: `validation.validate_airport_code()`

### 6. Duration Validation
- **Type**: Must be a valid number
- **Range**: > 0 and ≤ 12.0 hours
- **Format**: Decimal allowed (e.g., 1.5)
- **Required**: Yes
- **Implementation**: `validation.validate_duration()`

### 7. Remarks Validation
- **Length**: Maximum 200 characters
- **Required**: No (optional field)
- **Default**: Empty string if not provided
- **Implementation**: `validation.validate_remarks()`

## Edit Flight Special Behavior

When editing an existing flight:
1. **Prefill Values**: All current values displayed in brackets [like this]
2. **Press Enter to Keep**: User presses Enter without typing to keep current value
3. **Type to Change**: User types new value to update field
4. **Same Validation**: All new values undergo same validation as add operation
5. **Exclude Self from Duplicate Check**: When checking duplicates, excludes the flight being edited

## User Experience Features

### Error Handling
- **Clear Messages**: Each error explains exactly what's wrong
- **Immediate Feedback**: Validation happens as soon as input is provided
- **Retry Allowed**: User can immediately retry after error
- **No Data Loss**: Partial input is retained where appropriate

### Cancellation
- **Empty Input**: Pressing Enter without input cancels operation
- **Any Stage**: User can cancel at any validation stage
- **Confirmation**: Cancel message displayed
- **Return to Menu**: Safe return to main menu

### Confirmation
- **Duplicate Warning**: User must explicitly confirm duplicate entry
- **Delete Confirmation**: Explicit yes/no required for deletion
- **Success Message**: Clear confirmation after successful save
- **Details Display**: Full flight details shown after add/edit

## Data Integrity Guarantees

1. **No Invalid Data**: Only validated data reaches storage
2. **Type Safety**: All fields converted to correct types (string, float, etc.)
3. **Format Consistency**: Dates, codes, and registrations normalized to uppercase
4. **Duplicate Prevention**: Warning system prevents accidental duplicates
5. **UUID Uniqueness**: Every flight has guaranteed unique identifier

This validation system ensures **100% data integrity** while maintaining **excellent user experience** through clear feedback and error recovery.
