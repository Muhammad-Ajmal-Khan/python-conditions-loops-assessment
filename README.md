# Python Conditions & Loops Assessment

This repository contains two beginner-friendly Python console programs created for the conditional statements and loops assessment.

## Repository Name
`python-conditions-loops-assessment`

## Project Overview

1. **Task 1: Student Scholarship Eligibility System**
   Demonstrates how a program makes decisions using `if`, `elif`, and `else` in a realistic university scholarship scenario. Evaluates a student's data (marks, attendance, income) to decide if they qualify for a full or partial scholarship.

2. **Task 2: Smart Pharmacy Inventory System**
   Demonstrates how a program repeats tasks using `for` loops in a realistic pharmacy inventory scenario. Manages medicine sales, updates remaining stock, calculates total revenue (accumulator), and alerts about low stock (counter).

## Concepts Covered

- `if`, `elif`, and `else` blocks for decision making.
- `for` loops and `range()` to run a block of code a specific number of times.
- **Counters** and **Accumulators** to track low stock items and total daily revenue.
- Input using `input()` and numeric conversion using `int()` and `float()`.
- Input validation to ensure percentages remain within the 0-100 range.
- Basic arithmetic operations and logical operators (`and`, `or`).

## How to Run

1. Install Python 3 on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt in the project folder.
4. To run Task 1, type:
   `python student_scholarship_system.py`
5. To run Task 2, type:
   `python pharmacy_inventory_system.py`

*(Note: On some macOS/Linux systems, use `python3` instead of `python`)*.

## Example Runs

### Task 1: Scholarship System
```text
Enter student name: Ali
Enter marks percentage: 92
Enter attendance percentage: 88
Enter monthly family income: 45000

Scholarship Evaluation Report:
Name: Ali
Status: Eligible
Award: Full Scholarship
```

### Task 2: Pharmacy System
```text
How many different medicines need to be processed? 1

Medicine 1
Enter medicine name: Panadol
Enter available stock: 50
Enter price per unit: 10
Enter quantity sold: 45
Sale successful. Amount: Rs. 450.0
Remaining stock: 5
Warning: Low stock for Panadol

Final Report:
Total medicines processed: 1
Total revenue: Rs. 450.0
Medicines requiring restocking: 1
```

## UI/UX Notes

These are **console-based** programs designed for a clear user experience:
- Direct prompts that tell the user exactly what type of data to enter.
- A clear visual separation between the data entry phase and the final reports.
- Simple step-by-step logic and dynamic warning messages.