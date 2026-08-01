




# 📒 Contact Book Pro

A Python contact management system with CSV storage — add, search, update, and delete contacts, with data automatically saved between runs.

## Features

- ➕ Add contacts (with duplicate detection — warns before overwriting an existing name)
- 👁️ Show all contacts
- 🔍 Case-insensitive search (e.g. searching "john" finds "John")
- ✏️ Update a contact's number (case-insensitive lookup)
- 🗑️ Delete a contact, with a confirmation prompt before deleting
- 📇 View total contact count
- ✅ Phone number validation — must be digits only, at least 7 digits
- 💾 Auto save & load from CSV — phone numbers are stored as text, so leading zeros are never lost
- ⚠️ Handles a missing, empty, or malformed `contacts.csv` gracefully

## Requirements

- Python 3.x
- pandas (`pip install pandas`)

## How to Run

```bash
python contact_book_pro.py
```

## How to Use

1. Run the program — if a `contacts.csv` already exists, your saved contacts load automatically.
2. Choose an option from the menu (1-7).
3. Names are matched case-insensitively for search, update, and delete — you don't need to type the exact casing.
4. Deleting a contact asks for confirmation first, so nothing is removed by accident.
5. Every change (add, update, delete) is saved to `contacts.csv` immediately.

## CSV Format

Contacts are automatically saved to `contacts.csv` in this format:

```
Name,Number
John,9876543210
Amit,0912345678
```

- The `Number` column is always stored as text, so numbers starting with `0` keep their leading zero.
- You don't need to create this file yourself — it's created automatically the first time you add a contact.

## Technologies Used

- Python
- Pandas
- CSV

## Author

Charan Aade | Python Developer







