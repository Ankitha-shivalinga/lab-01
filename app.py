print("Grade Classifier")
print("----------------")

mark_input = input("Enter your mark out of 100: ")

if mark_input.strip() == "":
    print("Error: Please enter a mark between 0 and 100.")
else:
    try:
        mark = float(mark_input)

        if mark < 0 or mark > 100:
            print(f"Error: {mark} is outside the valid range. Enter a mark from 0 to 100.")
        elif mark >= 80:
            print(f"Your mark is {mark:.1f}/100. Grade: A")
        elif mark >= 70:
            print(f"Your mark is {mark:.1f}/100. Grade: B")
        elif mark >= 60:
            print(f"Your mark is {mark:.1f}/100. Grade: C")
        elif mark >= 50:
            print(f"Your mark is {mark:.1f}/100. Grade: D")
        else:
            print(f"Your mark is {mark:.1f}/100. Grade: F")

    except ValueError:
        print("Error: Please enter a numeric mark between 0 and 100.")