def grader(students, answers) :

    score_index = 3
    count = 0
    students_list = []
    score_list = []
    result_list = []

    for sep in students :
        for answer in answers :
            if sep[score_index] == str(answer) :
                count += 10
                score_index += 1
            elif sep[score_index] != str(answer) :
                score_index += 1
        score_list.append(count)
        count = 0
        score_index = 3

    for sep in students :
        students_list.append(sep[:2])

    for i in range(len(students)) :
        result_list.append(str(score_list[i]) + students_list[i])

    result_list.sort()
    result_list.reverse()

    for i in range(len(result_list)) :
        print(f"학생: {result_list[i][2:]} 점수: {result_list[i][:2]}점 {i+1}등")

students = ["김갑,3242524215", "이을,3242524223", "박병,2242554131", "최정,4245242315", "정무,3242524315"] 

answer = [3,2,4,2,5,2,4,3,1,2]

grader(students, answer)