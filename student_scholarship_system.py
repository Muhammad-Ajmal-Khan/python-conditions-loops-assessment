name = input("Enter student name: ")
marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = int(input("Enter monthly family income (Rs.): "))

print("\n--- Scholarship Result ---")
print("Student Name:", name)

if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
    print("Invalid input! Marks and attendance must be between 0 and 100.")
else:

    if marks >= 80 and attendance >= 85 and income <= 50000:
        print("Status: ELIGIBLE")
        
        if marks >= 90:
            print("Award: Full Scholarship")
        elif marks >= 80 and marks < 90:
            print("Award: Partial Scholarship")
            
    else:

        print("Status: NOT ELIGIBLE")
        print("Reasons for rejection:")
        
        if marks < 80:
            print("- Marks are below 80%")
        if attendance < 85:
            print("- Attendance is below 85%")
        if income > 50000:
            print("- Family income is more than Rs. 50,000")