if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()  # Read student's name
        score = float(input())  # Read student's score
        students.append([name, score])  # Add student's name and score to the list

    # Find the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in students))[1]

    # Find all students with the second lowest grade
    second_lowest_students = sorted([name for name, score in students if score == second_lowest_grade])

    # Print each student's name on a new line
    for student in second_lowest_students:
        print(student)
