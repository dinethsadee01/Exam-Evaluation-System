#Declaring Variables
listNo1=[]
outcome_Count=0
progress_Count=0
trailer_Count=0
retriever_Count=0
exclude_Count=0

#Validating Inputs
while True:
    try:
        pass_Mark = int(input("Please enter your credits at pass: "))
        if pass_Mark not in range(0,121,20):
                print("Out Of Range")
                continue
    except ValueError:
        print("Integer required")
        continue
    try:
        defer_Mark = int(input("Please enter your credits at defer: "))
        if defer_Mark not in range(0,121,20):
                print("Out Of Range")
                continue
    except ValueError:
        print("Integer required")
        continue
    try:
        fail_Mark = int(input("Please enter your credits at fail: "))
        if fail_Mark not in range(0,121,20):
                print("Out Of Range")
                continue
    except ValueError:
        print("Integer required")
        continue
    total= pass_Mark + defer_Mark + fail_Mark
    if total != 120:
        print("Total Incorrect")
        continue
    
#Displaying Grades
    if pass_Mark == 120:    
        outcome_Count+=1
        progress_Count+=1
        grade="Progress"
    elif pass_Mark ==100:
        outcome_Count+=1
        trailer_Count+=1
        grade="Progress(module trailer)"
    elif fail_Mark in range(80,121,20):
        outcome_Count+=1
        exclude_Count+=1
        grade="Exclude"
    else: 
        outcome_Count+=1
        retriever_Count+=1
        grade="Module retriever"
    print("Progression Outcome: ",grade)
    
#Adding Gradings to List 
    grade_List = grade +" : " +str (pass_Mark) + ", " + str (defer_Mark) + ", " + str (fail_Mark)
    listNo1.append(grade_List)
    
#Saving Grades to a Text
    text=open("My Outcomes.txt","a")
    text.write(grade_List+"\n")
    text.close()
    
#Asking User Continue or Break
    user_Input= input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if user_Input=="y":
        print("\n")
        cond=False
        continue
    elif user_Input=="q":
        print("""
        1 - Show Horizontal Histogram
        2 - Show Vertical Histogram
        3 - Show Outcomes as a List
        4 - Show Outcomes from Text File
        """)
        user_Choice= input("Enter the method number(1/2/3/4): ")
    else:
        print('Enter valid letter.')
        continue
        
#1) Showing Horizontal Histogram       
    if user_Choice== "1":
        print("\n---------------------------------------------------------------------------")
        print("Horizontal Histogram")
        print("  progress  " , progress_Count ,"          :" , progress_Count*"*")
        print("  trailer   " , trailer_Count  ,"          :" , trailer_Count*"*")
        print("  retriever " , retriever_Count,"          :" , retriever_Count*"*")
        print("  exclude   " , exclude_Count  ,"          :" , exclude_Count*"*")
        print("")
        print(outcome_Count ," outcomes in total.")
        print("---------------------------------------------------------------------------")
        break
         
#2) Showing Vertical Histogram        
    elif user_Choice== "2":
        print("\n---------------------------------------------------------------------------")
        print("Vertical Histogram")
        gradeslist = [' Progress ', ' Trailer ', ' Retriever ', ' Exclude ']
        print('|'.join(gradeslist))
        for x in range(max(progress_Count, trailer_Count, retriever_Count, exclude_Count)):
            print("     {0}        {1}         {2}         {3}".format(
            '*' if x < progress_Count else ' ',
            '*' if x < trailer_Count else ' ',
            '*' if x < retriever_Count else ' ',
            '*' if x < exclude_Count else ' '
            ))
        print("")
        print(outcome_Count ," outcomes in total.")
        print("---------------------------------------------------------------------------")
        break
             
#3) Showing as a List     
    elif user_Choice== "3":
        for item in listNo1:
            print(item)
            break
            
#4) Listing & Showing Informations as a Txt       
    elif user_Choice=="4":
        text=open("My Outcomes.txt","r")
        lines = text.readlines()
        for line in lines:
            print(line)
        text.close()
         
    break
