# FlightLog Application Flow

This diagram shows the main navigation flow and user interaction paths through the FlightLog application.

```mermaid
flowchart TD
    Start([Start Application]) --> Load[Load Flight Data<br/>from flights.json]
    Load --> Menu{Main Menu<br/>Display Options 1-7}

    Menu -->|1| Add[Add Flight]
    Menu -->|2| View[View Flights]
    Menu -->|3| Edit[Edit Flight]
    Menu -->|4| Delete[Delete Flight]
    Menu -->|5| Summary[View Summary]
    Menu -->|6| Export[Export Data]
    Menu -->|7| Exit([Exit Application])

    Add --> ValidateAdd{Validate All<br/>Input Fields}
    ValidateAdd -->|Valid| SaveAdd[Save to JSON]
    ValidateAdd -->|Invalid| ErrorAdd[Show Error Message]
    ErrorAdd --> Add
    SaveAdd --> Confirm1[Show Confirmation]
    Confirm1 --> Menu

    View --> Filter{Filter Options}
    Filter -->|All| DisplayAll[Display All Flights]
    Filter -->|Date Range| DisplayDate[Display Filtered by Date]
    Filter -->|Aircraft Type| DisplayType[Display Filtered by Type]
    Filter -->|Back| Menu
    DisplayAll --> Menu
    DisplayDate --> Menu
    DisplayType --> Menu

    Edit --> SelectEdit[Select Flight to Edit]
    SelectEdit --> PrefillEdit[Prefill Current Values]
    PrefillEdit --> ValidateEdit{Validate Changes}
    ValidateEdit -->|Valid| SaveEdit[Update JSON]
    ValidateEdit -->|Invalid| ErrorEdit[Show Error Message]
    ErrorEdit --> PrefillEdit
    SaveEdit --> Confirm2[Show Confirmation]
    Confirm2 --> Menu

    Delete --> SelectDel[Select Flight to Delete]
    SelectDel --> ConfirmDel{Confirm Deletion?<br/>yes/no}
    ConfirmDel -->|Yes| SaveDel[Remove from JSON]
    ConfirmDel -->|No| CancelDel[Cancel Deletion]
    SaveDel --> Confirm3[Show Confirmation]
    CancelDel --> Menu
    Confirm3 --> Menu

    Summary --> CalcStats[Calculate Statistics]
    CalcStats --> DisplayStats[Display Analytics]
    DisplayStats --> Menu

    Export --> ExportChoice{Export Format}
    ExportChoice -->|CSV| ExportCSV[Export to CSV]
    ExportChoice -->|Text| ExportTxt[Export Summary to Text]
    ExportChoice -->|Both| ExportBoth[Export Both Formats]
    ExportChoice -->|Cancel| Menu
    ExportCSV --> Confirm4[Show Success Message]
    ExportTxt --> Confirm4
    ExportBoth --> Confirm4
    Confirm4 --> Menu

    Exit --> Save[Save Flight Data]
    Save --> End([End Application])

    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Menu fill:#87CEEB
    style ValidateAdd fill:#FFD700
    style ValidateEdit fill:#FFD700
    style ConfirmDel fill:#FFD700
```

## Key Navigation Paths

1. **Add Flight Path**: Input validation → Save → Confirmation → Return to menu
2. **View Flight Path**: Select filter → Display results → Return to menu
3. **Edit Flight Path**: Select flight → Prefill values → Validate → Save → Return to menu
4. **Delete Flight Path**: Select flight → Confirm deletion → Delete/Cancel → Return to menu
5. **Summary Path**: Calculate statistics → Display → Return to menu
6. **Export Path**: Select format → Export → Confirmation → Return to menu
7. **Exit Path**: Save data → Exit application

## User Control Features

- All operations return to main menu after completion
- Invalid input prompts user to retry (never crashes)
- Confirmation required for destructive actions (delete)
- Clear error messages guide user to correct input
- User can cancel operations at any point
