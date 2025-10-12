# FlightLog Screenshot Checklist

**Print this and check off as you complete each screenshot**

---

## 📋 Pre-Flight Checklist

- [ ] Terminal open
- [ ] Navigate to: `cd /Users/anthony/Downloads/Project-3`
- [ ] Know screenshot shortcut: `Cmd + Shift + 4`
- [ ] Have folders ready: `docs/screenshots/features/` and `docs/screenshots/testing/`

---

## 🔴 ESSENTIAL Screenshots (Required for MERIT)

### Testing Screenshots

- [ ] **1. PEP8 Validation** → `docs/screenshots/testing/pep8-validation.png`
  - Command: `flake8 flightlog.py utils/*.py --max-line-length=79`
  - Should show: No output = 0 errors

---

### Feature Screenshots

- [ ] **2. Main Menu** → `docs/screenshots/features/main-menu.png`
  - Command: `python3 flightlog.py`
  - Should show: Menu with options 1-7

- [ ] **3. Add Flight Success** → `docs/screenshots/features/add-flight.png`
  - Choose: Option 1
  - Enter: Valid data (date: 2025-10-12, reg: EI-XYZ, type: C172, dep: EICK, dest: EIDW, duration: 1.5, remarks: Training)
  - Should show: "Flight added successfully!" with details

- [ ] **4. View Flights Table** → `docs/screenshots/features/view-flights.png`
  - Choose: Option 2, then Option 1
  - Should show: Table with flight data

- [ ] **5. Edit Flight (Prefilled)** → `docs/screenshots/features/edit-prefilled.png`
  - Choose: Option 3, select a flight
  - Should show: Fields with current values in brackets [like this]

- [ ] **6. Delete Confirmation** → `docs/screenshots/features/delete-confirmation.png`
  - Choose: Option 4, select a flight
  - Should show: Flight details + "Are you sure? (yes/no)"
  - Answer: no (don't actually delete)

- [ ] **7. Summary & Analytics** → `docs/screenshots/features/summary.png`
  - Choose: Option 5
  - Should show: Total flights, hours, table by type, longest/shortest

- [ ] **8. Export Success** → `docs/screenshots/features/export-csv.png`
  - Choose: Option 6, then Option 1
  - Should show: "Success! CSV file created: exports/..."

---

## 🟡 VALIDATION Screenshots (Important)

- [ ] **9. Invalid Date Format** → `docs/screenshots/testing/invalid-date-format.png`
  - Choose: Option 1 (Add Flight)
  - Enter date: `11/10/2025` (wrong format)
  - Should show: "Invalid date format. Use YYYY-MM-DD."

- [ ] **10. Future Date Error** → `docs/screenshots/testing/future-date.png`
  - Choose: Option 1 (Add Flight)
  - Enter date: `2026-12-31`
  - Should show: "Date cannot be in the future."

- [ ] **11. Negative Duration** → `docs/screenshots/testing/negative-duration.png`
  - Choose: Option 1, go through until duration
  - Enter duration: `-1.5`
  - Should show: "Duration must be greater than 0."

- [ ] **12. Duplicate Warning** → `docs/screenshots/testing/duplicate-flight.png`
  - Choose: Option 1
  - Enter: Same date + registration as existing flight
  - Should show: "Warning: A flight already exists... Continue anyway? (yes/no)"

---

## 🟢 BONUS Screenshots (Nice to Have)

- [ ] **13. Filter by Date** → `docs/screenshots/features/filter-date.png`
  - Choose: Option 2, then Option 2
  - Enter: Date range
  - Should show: Filtered results

- [ ] **14. Export Text** → `docs/screenshots/features/export-text.png`
  - Choose: Option 6, then Option 2
  - Should show: "Success! Summary file created: exports/..."

---

## ✅ Post-Screenshot Tasks

- [ ] Move all screenshots from Desktop to correct folders
- [ ] Rename files to match checklist names
- [ ] Verify all files saved correctly
- [ ] Check file sizes (should be 50KB-500KB each)

---

## 📝 Quick Reference Commands

**Navigate to project:**
```bash
cd /Users/anthony/Downloads/Project-3
```

**Run PEP8 check:**
```bash
flake8 flightlog.py utils/*.py --max-line-length=79
```

**Run application:**
```bash
python3 flightlog.py
```

**Exit application:**
- Choose Option 7 OR press `Ctrl + C`

---

## 🎯 Estimated Time

- Essential Screenshots (1-8): **15 minutes**
- Validation Screenshots (9-12): **10 minutes**
- Bonus Screenshots (13-14): **5 minutes**
- **Total: 30 minutes**

---

## 💡 Tips

- Take screenshots in order (1-14)
- Don't worry about perfection - just need to show it works
- If you mess up, just try again
- Press Enter without typing to cancel operations
- Save all screenshots before closing terminal

---

**Good luck! You've got this! 🚀**
