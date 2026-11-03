import json
with open("students.json",encoding="utf-8") as ptr:
    data=json.load(ptr)
    print("BARCHA TALABALAR\n")
    print(f"{data}\n")
    count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,count13,count14,count15=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    
    print("PYTHON KURSIDA O'QIYOTGANLAR\n")
    for i in data:
        if "Python" in i["courses"]:
            count1+=1
            print(i)
        if "Database" in i["courses"]:
            count2+=1
        if "Math" in i["courses"]:
            count3+=1
        if "Java" in i["courses"]:
            count4+=1
        if "Physics" in i["courses"]:
            count5+=1
        if "English" in i["courses"]:
            count6+=1 
        if "C++" in i["courses"]:
            count7+=1
        if "Algorithms" in i["courses"]:
            count8+=1
        if "Web Development" in i["courses"]:
            count9+=1
        if "JavaScript" in i["courses"]:
            count10+=1
        if "AI" in i["courses"]:
            count11+=1
        if "Data Science" in i["courses"]:
            count12+=1
        if "C#" in i["courses"]:
            count13+=1   
        if "Cybersecurity" in i["courses"]:
            count14+=1
        if "Machine Learning" in i["courses"]:
            count15+=1
    print()
    print("PYTHON KURSIDA O'QIYOTGANLAR:", count1 )
    print("Database KURSIDA O'QIYOTGANLAR:", count2)
    print("Math KURSIDA O'QIYOTGANLAR:", count3)
    print("Java KURSIDA O'QIYOTGANLAR:",count4)
    print("Physics KURSIDA O'QIYOTGANLAR:",count5)
    print("English KURSIDA O'QIYOTGANLAR:",count6)
    print("C++ KURSIDA O'QIYOTGANLAR:", count7)
    print("Algorithms KURSIDA O'QIYOTGANLAR:", count8)
    print("Web Development KURSIDA O'QIYOTGANLAR:",count9)
    print("JavaScript KURSIDA O'QIYOTGANLAR:",count10)
    print("AI KURSIDA O'QIYOTGANLAR:",count11)
    print("Data Science KURSIDA O'QIYOTGANLAR:",count12)
    print("C# KURSIDA O'QIYOTGANLAR:", count13)
    print("Cybersecurity KURSIDA O'QIYOTGANLAR:", count14)
    print("Machine Learning KURSIDA O'QIYOTGANLAR:",count15)








