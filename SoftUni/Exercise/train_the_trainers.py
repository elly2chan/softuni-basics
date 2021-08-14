judges_count = int(input())
presentation_name = input()
final_assessment = 0
grades_count = 0

while presentation_name != "Finish":
    current_presentation_grade = 0
    for grade in range(judges_count):
        judge_grade = float(input())
        current_presentation_grade += judge_grade
        final_assessment += judge_grade
        grades_count += 1

    print(f'{presentation_name} - {(current_presentation_grade / judges_count):.2f}')

    presentation_name = input()

print(f"Student's final assessment is {(final_assessment / grades_count):.2f}")