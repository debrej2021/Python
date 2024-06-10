print("This is our first DevOps Class")
name = "Debashis"
print(name)
name = 10
print(name)

def Calculate(noOfcars, noOfbikes):
    collection = noOfcars * 20 + noOfbikes * 10
    if collection > 500:
        print("Thank You")
        print("Good")
    elif collection > 200:
        print("Average")
    else:
        print("Not Good")

Calculate(10, 20)

List1=["Debashis","Mohapatra",1,2,3,3]

print(len(List1))

print(List1[-4])
print(List1[1:4])

print(List1[:4])
List1.append("moha")
#List1.re(0,"Raja")
List1.insert(2,"King")
print(List1)

List2=["Sonu","Krish"]

list3=List1 + List2
print(List1.extend(List2))
print(list3)

#Tuple
tupEnd=("king", "queen", 1, 2,3)
print(tupEnd)
print(tupEnd[1])

myList=list(tupEnd)
myList2=["R1","R2"]
myList.extend(myList2)

my_tuple=tuple(myList)

print(my_tuple)

print(my_tuple.index("R1"))
print(my_tuple.count("R1"))

mytuple1=("R3",)

a=my_tuple + mytuple1

print(a)

fruit={"mango","apple","strawberry", "papaya"}



#fruit.append{"Orange"}


fruit.remove("mango")
print(fruit)

DictStudent={"name":"Debashis",
      "rollno":45,
      "age":39
      }
print(DictStudent)
print(DictStudent.get("rollno"))
DictStudent["rollno"]=46

print(DictStudent)
#DictStudent.update
DictStudent.pop("age")
print(DictStudent)
dictSchool={
    "student1":{"name":"shiva",
                "rollno":56},
    "student2":{"name":"shiva1",
                "rollno":57}
}
print(dictSchool)

student1={"name":"shiva",
                "rollno":56}

student2={"name":"Shri",
                "rollno":67
                }
newDic={
    "student1":student1,
    "student2":student2
}
print(newDic)