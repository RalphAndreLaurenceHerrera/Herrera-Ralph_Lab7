Name = input("Student's Name: ")
Section = input("Student's Section: ")
PreGrade = float(input("Student's Preliminary Grade: "))
if PreGrade >= 40 and PreGrade <= 100:
    MidGrade = float(input("Student's Midterm Grade: "))
    if MidGrade >= 40 and MidGrade <= 100:
        FinGrade = float(input("Student's Finals Grade: "))
        if FinGrade >= 40 and FinGrade <= 100:
            FinalGrade = (PreGrade + MidGrade + FinGrade)/3
            FinalGrade = round (FinalGrade)
        else:
            print("Error. Please input between the range of 40 and 100 for Finals grades.")
    else:
        print("Error. Please input between the range of 40 and 100 for Midterms grades.")
else:
    print("Error. Please input between the range of 40 and 100 for Preliminary grades.")
    
if FinalGrade >= 99:
    gpa = 1.00
    description = "Excellent"
elif FinalGrade >= 96:
    gpa = 1.25
    description = "Outstanding"
elif FinalGrade >= 93:
    gpa = 1.50
    description = "Superior"
elif FinalGrade >= 90:
    gpa = 1.75
    description = "Very Good"
elif FinalGrade >= 87:
    gpa = 2.00
    description = "Good"
elif FinalGrade >= 84:
    gpa = 2.25
    description = "Satisfactoy"
elif FinalGrade >= 81:
    gpa = 2.50
    description = "Fairly Satisfactory"
elif FinalGrade >= 78:
    gpa = 2.75
    description = "Fair"
elif FinalGrade >= 75:
    gpa = 3.00
    description = "Passed"
elif FinalGrade < 75:
    gpa = 5.00
    description = "Failed"
else:
    gpa = 100.00
    description = "Super Failed"
    print("How is this possible!?")
print(f"Name: {Name}\nSection: {Section}\nPrelim Grade: {PreGrade:.2f}\nMidGrade: {MidGrade:.2f}\nFinals Grade: {FinGrade:.2f}\nFinal Grade(Average): {FinalGrade:.0f}\nGPA: {gpa}\nDescription: {description}")