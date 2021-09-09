import json
import mechanize
from time import sleep


def classSearch(searchString):
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
        classProfessor = entity[8].split('>')[1].split('<')[0]


        classSeats = entity[9]
        classWaitlist = entity[10]

        print(  f"Title: {classTitle}\n"\
                f"Number: {classNumber}\n"\
                f"ClassTime: {classTime}\n"\
                f"Professor: {classProfessor}"
            )
        print("-----------------------------------------------------------------------------------------")


classSearch("CSC256")
