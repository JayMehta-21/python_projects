def Add_task():
    task=input("Enter your task :")
    with open("task.txt","a") as tf:
        tf.write(task)

def View_task():
    pass
def Remove_task():
    pass
def main():
    print("... Your to do list ...")
    print('''     1) ADD TASK
     2) VIEW TASK
     3) REMOVE TASK''')
    user_choice=int(input("Enter your choice(number only) : "))
    if user_choice==1:
        Add_task()
    elif user_choice==2:
        View_task()
    elif user_choice==3:
        Remove_task()
    else:
        print("Enter a Valid choice ")
main()