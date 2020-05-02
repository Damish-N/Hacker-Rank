if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        # print(name,line)
        # To get line of marks
        scores = list(map(float, line))
        # print(scores)
        # print(number)
        student_marks[name] = scores
    # print(student_marks)
    query_name = input()
    # print(student_marks[query_name])
    number=len(student_marks[query_name])
    # print(number)
    sum=0
    i=0
    # print(student_marks[query_name][0])
    for i in range(number) :
         sum=sum+student_marks[query_name][i]
    
    answer=sum/number
    answer = str(round(answer, 2))     
    print(answer)
    print ("%.2f" % float(answer))
    # print("{%.2f}".format(answer))