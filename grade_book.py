import mysql.connecter as sql
mycon = sql.connect(host = "local host",user = "root", password ="dudedivishere", database = "School")#sql object
a = 0
mycur = mycon.cursor()#cursor object()

def adds():
  n = input("Enter Name: ")
  r = input("Enter Roll Number: ")
  m = input("Math Marks: ")
  e = input("English Marks: ")
  p = input("Physics Marks: ")
  b = input("Biology Marks: ")
  c = input("Chemistry Marks: ")
  percent = (m + p + b + c + e)/5
  s = "Insert into students(name, roll, math, english, physics, biology, chemistry, percent) VALUES (%s, %d, %d, %d, %d, %d, %d, %f)"#add coloumn syntax
  val = (name, roll, math, english, physics, biology, chemistry, percent)#assigning value to above syntax
  mycur.execute(s,val)#executes sql code
  mycon.commit()#commits the changes

def dels():
  a = int(input("Roll Number: "))
  s = "DELETE FROM students WHERE Rol_ Number = {}"#dlete a row syntax
  mycur.execute(s,a)#execute sql code
  mycon.commit()#commits changes

def finds():
  a = float(input("Disqualifying Percentage: "))
  s = "select * from student where Roll_Number >= {}"#sql syntax to find rows with specified condition
  mycur.execute(s,a)#execute the sql code
  myresult = mycur.fetchall()#fetchsall the data in sql file

  for x in myresult:#to print the data in sql file
    print(x)
  mycon.commit()#commits the sql code

def updates():
  r=int(input("Roll Number:"))
  print("Enter 1.Maths\n2.English\n3.Physics\n4.Biology\n5.Chemistry")#offer menu option
  a = int(input("Choice:"))
#below are sql codes 
  if a==1:
    s="Updates students set Maths={} where Roll_Number={}"
  elif a==2:
    s="Updates students set English={} where Roll_Number={}"
  elif a==3:
    s="Updates students set Physics={} where Roll_Number={}"
  elif a==4:
    s="Updates students set Biology={} where Roll_Number={}"
  elif a==5:
    s="Updates students set Chemistry={} where Roll_Number={}"
  
  c = int(input("Changed marks:"))
  v = (s,r)
  mycur.execute(s,v)#execute sql code
  mycon.commit()#commit sql code
#main()
while a != 5: #menu option
  print("press 1 to add")
  print("press 2 to delete")
  print("press 3 to find")
  print("press 4 to update")
  print("press 5 to exit")

  a = int(input("Choice: "))
  if a == 1:
    adds()
  elif a == 2:
    dels()
  elif a == 3:
    finds()
  elif a == 4:
    updates()
  elif a==5:
    break
