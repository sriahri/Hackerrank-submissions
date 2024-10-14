if __name__ == '__main__':
    n = int(raw_input())
    su=0
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    su=sum(student_marks[query_name])
    ave=float(su/3)
    print('%.2f'%ave)
        
        
        
        
        
        