def main():
    num_students = 6  # Number of students
    subjects = ["国語", "数学"]  # Subjects

    scores = {subject: [] for subject in subjects}  # Dictionary to store scores

    print(f"{num_students}人分の点数を入力せよ。\n")

    for i in range(1, num_students + 1):
        print(f"{i}番・・・")
        for subject in subjects:
            score = int(input(f"{subject}: "))
            scores[subject].append(score)
        print()  # Blank line for formatting

    # Calculate and display results
    total_all_students = 0
    for subject in subjects:
        total = sum(scores[subject])
        average = total / num_students
        total_all_students += total
        print(f"{subject} 合計 {total} 平均 {average:.1f}")

    # Overall total and average
    average_all_students = total_all_students / num_students
    print(f"学生 合計 {total_all_students} 平均 {average_all_students:.1f}")

'''if __name__ == "__main__":
    main()'''
