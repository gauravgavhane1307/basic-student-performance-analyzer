import numpy as np

# Student records
names = np.array(["Aman", "Chaman", "Chomu", "Khonu", "Ronu"])

marks = np.array([
    [67, 78, 90],
    [88, 87, 96],
    [62, 65, 70],
    [23, 45, 57],
    [90, 91, 94]
])

subjects = ["Subject 1", "Subject 2", "Subject 3"]

# Calculate totals and averages once
total = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)

# Subject-wise statistics
sub_ave = np.mean(marks, axis=0)
high = np.max(marks, axis=0)
low = np.min(marks, axis=0)
topp = np.argmax(marks, axis=0)

# Overall toppers
top_avg = np.argmax(averages)
top_total = np.argmax(total)


# Display all student records
def show_students():
    print("\n" + "-" * 55)
    print(f"{'Name':<12}{'Sub 1':>10}{'Sub 2':>10}{'Sub 3':>10}")
    print("-" * 55)

    for i in range(len(names)):
        print(
            f"{names[i]:<12}"
            f"{marks[i, 0]:>10}"
            f"{marks[i, 1]:>10}"
            f"{marks[i, 2]:>10}"
        )


# Display each student's total and average
def show_performance():
    print("\n" + "-" * 55)
    print(f"{'Name':<12}{'Total':>12}{'Average':>12}")
    print("-" * 55)

    for i in range(len(names)):
        print(f"{names[i]:<12}{total[i]:>12}{averages[i]:>12.2f}")


# Show the overall topper
def show_overall_topper():
    print("\nOVERALL TOPPER")
    print("-" * 35)
    print("Name:", names[top_avg])
    print("Total marks:", total[top_avg])
    print("Average:", round(averages[top_avg], 2))


# Display subject-wise averages
def show_subject_averages():
    print("\nSUBJECT-WISE AVERAGES")
    print("-" * 35)

    for i in range(len(subjects)):
        print(f"{subjects[i]}: {sub_ave[i]:.2f}")


# Display the highest and lowest marks in each subject
def show_subject_stats():
    print("\nSUBJECT STATISTICS")
    print("-" * 45)
    print(f"{'Subject':<15}{'Highest':>12}{'Lowest':>12}")
    print("-" * 45)

    for i in range(len(subjects)):
        print(f"{subjects[i]:<15}{high[i]:>12}{low[i]:>12}")


# Find the topper in each subject
def show_subject_toppers():
    print("\nSUBJECT TOPPERS")
    print("-" * 35)

    for i in range(len(subjects)):
        student = topp[i]
        print(f"{subjects[i]}: {names[student]} ({marks[student, i]})")


# Filter students by average marks
def show_qualifiers():
    print("\nSTUDENTS WITH AVERAGE ABOVE 75")
    print("-" * 40)

    qualified = averages > 75

    if np.any(qualified):
        for i in range(len(names)):
            if qualified[i]:
                print(f"{names[i]}: {averages[i]:.2f}")
    else:
        print("No students found.")


# Show the student with the highest total marks
def show_highest_total():
    print("\nHIGHEST TOTAL MARKS")
    print("-" * 35)
    print("Name:", names[top_total])
    print("Total:", total[top_total])
    print("Average:", round(averages[top_total], 2))


# Main menu
while True:
    print("\n" + "=" * 45)
    print("       STUDENT PERFORMANCE ANALYZER")
    print("=" * 45)

    print("1. View student marks")
    print("2. View totals and averages")
    print("3. View overall topper")
    print("4. View subject-wise averages")
    print("5. View highest and lowest marks")
    print("6. View subject toppers")
    print("7. View students with average above 75")
    print("8. View student with highest total")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ").strip()

    if choice == "1":
        show_students()

    elif choice == "2":
        show_performance()

    elif choice == "3":
        show_overall_topper()

    elif choice == "4":
        show_subject_averages()

    elif choice == "5":
        show_subject_stats()

    elif choice == "6":
        show_subject_toppers()

    elif choice == "7":
        show_qualifiers()

    elif choice == "8":
        show_highest_total()

    elif choice == "9":
        print("\nExiting Student Performance Analyzer. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 9.")