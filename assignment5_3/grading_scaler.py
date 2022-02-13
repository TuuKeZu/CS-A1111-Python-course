def determine_grade_limits(max_points, passing_percentage):
    passing_points = max_points * (passing_percentage / 100)

    gradable_points = max_points - passing_points

    grade_gap = gradable_points / 5;
    
    grading = [0.0] * 5
    current_grade = passing_points;

    for i in range(5):
        grading[i] = current_grade
        current_grade += grade_gap;
    
    return(grading)

def grade_points(exam_points, grade_limits):
    index = 0
    for limit in grade_limits:
        if(exam_points < limit):
            return index

        index += 1
        # tässä vaiheessa koodi on käynyt läpi kaikkien numeroiden minirajat, joten numeron on oltava suurin
    return 5

def main():
    point_array = []

    max_points = float(input("Enter the maximum points of the exam.\n"))
    passing_perc = float(input("Enter the passing percentage of the exam.\n"))
    points = input("Enter the exam points of the students. Stop with empty line.\n")

    while(points != ''):
        point_array.append(float(points));
        points = input()
    else:
        print("Points Grade")

        grading = determine_grade_limits(max_points, passing_perc)

        for points in point_array:
            
            grade = grade_points(points, grading)

            print('{:<6s}{:>3s}'.format(str(points), str(grade)))
        return



main()


        