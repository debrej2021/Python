class Person:
  #  designation="DevOps Engineer"
    # Salary = 100000
    # yearsOfExperience=5
    def  __init__(self, designation, yearsOfExperience) :
        self.designation=designation
        

    def calculateSalary(self):
        # self is an object
        Salary=0 
        if(self.yearsOfExperience > 5 ):
            Salary=100000
        else :
            Salary=50000
            return self.Salary
        
        laxmi=Person("DevOps Engineer", 10)
        pawan = Person("DevOps Engineer", 5)
        laxmi.calculateSalary()
        pawan.calculateSalary()




laxmi = Person()
print(laxmi.designation)
