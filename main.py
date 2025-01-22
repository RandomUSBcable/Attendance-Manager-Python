#this is my todo list kinda
#get if the user uses "hours" or "periods" in timeTable
#get the number of days in the week to be included
#get the number of perionds in the week
#get the days of the week to be included
#add q as the character to quit from any menu


def getSubjects():
    subjects = []
    while True:
        subject: str = input("Enter a subject (or 'q' to quit): ")
        if (subject.lower() == 'q'):
            break
        elif(subject.lower() in subjects):
            print("Subject already exists. Please enter a different subject.")
        else:
            subjects.append(subject.lower())
    return subjects


def getAttendance(subjects):
    attendance = {} 
    for i in subjects:
        while True:
            temp = input("Enter current attendance percentage for " + i + " (in %): ")
            if (temp.isdigit()) and (int(temp)<=100):
                attendance[i] = int(temp)
                break
            else:
                print("Enter a valid number mate")
    return attendance


def getTimeTable(subjectList):
    #   print("I need some basic info first")
    #   this is to get the number of days and such; i'll do that later, i just want MVP for this commit
    timeTable = [[],[]]
    #   timeTable = [[],[],[],[],[]]
    for day in timeTable:
        for period in range(1, 7+1):
            while True:
                temp =(input("period "+ str(period) +" on day "+" ?"))
                if temp.lower() in subjectList:
                    day.append(temp)
                    break
                else:
                    print("this subject was not in the list you know...")
    return timeTable

def showTimeTable(timeTableObj):
    for i in timeTableObj:
        print(i, sep="   ")
        '''
        for j in i:
            print(j, end = "\t")
        print()
        '''



subjectList = getSubjects()

currentAttendancePerSubject = getAttendance(subjectList)

timeTable = getTimeTable(subjectList)

showTimeTable(timeTable)

