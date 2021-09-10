import json
import mechanize
from enum import Enum

class Classes(Enum):
    CSC210 = "CSC210"
    CSC220 = "CSC220"
    CSC256 = "CSC256"
    CSC340 = "CSC340"
    CSC413 = "CSC413"
    CSC415 = "CSC415"
    CSC510 = "CSC510"
    CSC600 = "CSC600"

class ClassSearch:

    def __init__(self):
    
        def classSearch(self,searchString):
            br = mechanize.Browser()
            br.set_handle_robots(False)   # ignore robots
            br.set_handle_refresh(False)  # can sometimes hang without this

            br.addheaders = [('User-agent', 'Firefox')]

            br.open("https://webapps.sfsu.edu/public/classservices/classsearch")
            br.select_form("classScheduleQuick")


            br.form.find_control("classScheduleQuick[searchFor]").value = searchString
            br.submit()
            result = br.open("https://webapps.sfsu.edu/public/classservices/searchresultsjson")
            data = json.loads(result.read())

            print(data["aaData"][0][2])

            for entity in data["aaData"]:
                classID = entity[0].split('>')[1].split('<')[0]
                classType = entity[1]
                classTitle = entity[2]
                classUnits = entity[3]
                classNumber = entity[4]

                # Need to do some string parsing to get information out of line 7
                dateLine = entity[7]
                dateLine = dateLine.split('>')
                classDay = dateLine[2].split('<')[0]
                classTime = dateLine[4].split('<')[0]
                classDate = dateLine[6].split('<')[0]
                classLocation = dateLine[8].split('<')[0]

                # Need to strip the HTML out of the line storing the professors name as well
                classProfessor = entity[8].split('>')[1].split('<')[0].strip()


                classSeats = entity[9]
                classWaitlist = entity[10]

                print(  f"Course: {classID}\n"\
                        f"Type:   {classType}\n"\
                        f"Title:  {classTitle}\n"\
                        f"Units:  {classUnits}\n"\
                        f"Number: {classNumber}\n"\
                        f"Time:   {classDay} {classTime}\n"\
                        f"Date:   {classDate}\n"\
                        f"Room:   {classLocation}\n"\
                        f"Prof:   {classProfessor}\n"\
                        f"Seats:  {classSeats}\tWaitlist: {classWaitlist}"
                    )
                print("-----------------------------------------------------------------------------------------")


classSearch("CSC256")