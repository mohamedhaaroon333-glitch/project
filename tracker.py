import json
from datetime import datetime
print("\t ____Student Tracker____ ")
name=input("Enter Your Name:")
department=input("Enter Your Depeartement:")
year=input("Enter Your Year:(1/2/3/4)")
print(f"Name: {name}")
print(f"Departement: {department}")
print(f"year Of Studing: {year}")
print(f"Today's date is {datetime.now().date()}")
with open("task.json","r") as file:
    task=json.load(file)
while True:
    print("\t ___Menu____")
    print("1.Add Task:")
    print("2.View Task")
    print("3.Search Task")
    print("4.Completed Task")
    print("5.Exit")
    choice=int(input("Enter Your Choice"))
    if choice==5:
        print("program completed")
        break
    elif choice==1:
        new_task=input("Enter Your New Task By Comma Sepeerated:")
        new_task=new_task.split(",")
        for t in new_task:
            task.append(t.strip())
        with open("task.json", "w") as file:
            json.dump(task,file,indent=4)
        print("New Task Is Updated Succesfully")
    elif choice==2:
        print("\n Today's Task")
        if len(task)==0:
            print("All Assigned Task Are Complected")
        else:
            for i, tasks in enumerate(task,start=1):
                print(i,":",tasks)
    elif choice==3:
       search_task=input("Enter What Task To Be Searched ")
       if search_task in task:
           print("Task Found")
       else:
           print("Task Not Found ")
    elif choice==4:
        completed_task=input("Enter The Completed Task:")
        if completed_task in task:
            task.remove(completed_task)
            with open("task.json","w") as file:
                json.dump(task,file,indent=4)
            print("Task Complected Succesfully") 
        else:
            print("Task Is not There")   
    else:
        print("Invalid Choice")
