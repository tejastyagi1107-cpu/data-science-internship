def calculate_grade(marks):
    if marks >= 90:
        return "A", "Outstanding! Keep it up! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! 😊"
    elif marks >= 60:
        return "D", "Keep Improving! 💪"
    else:
        return "F", "Don't Give Up! Practice More! ❤️"


print("===== Student Grade Calculator =====")

student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks should be between 0 and 100.")

    except ValueError:
        print("❌ Please enter a valid number.")


grade, message = calculate_grade(marks)

print("\n========== RESULT ==========")
print(f"Student Name : {student_name}")
print(f"Marks        : {marks}")
print(f"Grade        : {grade}")
print(f"Message      : {message}")
print("============================")