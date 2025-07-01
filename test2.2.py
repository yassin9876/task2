students=[{"name":"yassin","grades":[90,80,100]},
          {"name":"ahmed","grades":[75,100,90]},
          {"name":"omar","grades":[80,90,100]}]
for student in students:
    average=sum(student["grades"])/len(student["grades"])
    print(student['name'],[average])