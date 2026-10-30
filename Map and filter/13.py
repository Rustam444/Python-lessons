def talabalar(grades:list[int], passingGrade:int)->int:
    count=0
    for i in grades:
        if i>=passingGrade:
            count+=1
    return count
grades=[45,60,75,30,90]
passingGrade=60
natija=talabalar(grades, passingGrade)
print(natija)