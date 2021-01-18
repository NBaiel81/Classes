class Student:
    student_id=0
    def __init__(self,name,last_name,group):
        self.name=name
        self.last_name=last_name
        self.group=group
        Student.student_id+=1
student1=Student('Baiel','Nurmatbekov','python')
print(student1.name,student1.group,student1.student_id)#nobody own this id, this is id of last student
student2=Student('Akylbek','Melisov','python')
print(student2.name,student2.group,student2.student_id)


class Car:
    def __init__(self,mark,color,model,year):
        self.mark=mark
        self.color=color
        self.model=model
        self.year=year
        self.run=0
        self.engine=''
        self.boots=0
    def move(self,distance:int):
        if distance>0:
            self.run+=distance
    def set_engine(self,new_engine):
        self.engine=new_engine
        if new_engine=='common':
            self.boots=7
        elif new_engine=='advanced':
            self.boots=5
        elif new_engine=='race':
            self.boots=2
car1=Car('bmw','black','x6','2020')
car2=Car('mercedes','pink','s 600','2021')
car3=Car('tesla','while','S 6','2021')
print(car1.model,car2.model,car1.run,car2.run)
car1.move(240)
car2.move(-12)
print(car1.model,car2.model,car1.run,car2.run)
car1.set_engine('race')
print(car1.engine,car1.boots)



