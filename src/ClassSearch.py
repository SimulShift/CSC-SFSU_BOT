import json
from typing_extensions import TypeAlias
import mechanize
from enum import Enum
import struct
class Classes(Enum):
    CSC210 = "CSC210"
    CSC220 = "CSC220"
    CSC256 = "CSC256"
    CSC340 = "CSC340"
    CSC413 = "CSC413"
    CSC415 = "CSC415"
    CSC510 = "CSC510"
    CSC600 = "CSC600"

class ClassSearchResultsKeys(Enum):
    COURSE = "Course"
    TYPE = "Type"
    TITLE = "Title"
    UNITS = "Units"
    NUMBER = "Number"
    DAY = "Day"
    TIME = "Time"
    DATE = "Date"
    ROOM = "Room"
    PROFESSOR = "Professor"
    SEATS = "Seats"
    WAITLIST = "Waitlist"

class ClassSearchPage:

        class ClassSearchPageURL(Enum):
            CLASS_SEARCH_URL = "https://webapps.sfsu.edu/public/classservices/classsearch"

        class ClassSearchPageForms(Enum):
            CLASS_SCHEDULE_QUICK_FORM = "classScheduleQuick"

        def __init__(self) -> None:
            pass


class ClassSearch:
    page: ClassSearchPage
    def __init__(self):
        self.page = ClassSearchPage()
    def classSearch(self, searchString):
        br = mechanize.Browser()
        br.set_handle_robots(False)   # ignore robots
        br.set_handle_refresh(False)  # can sometimes hang without this

        br.addheaders = [('User-agent', 'Firefox')]

        br.open(self.page.ClassSearchPageURL.CLASS_SEARCH_URL)
        br.select_form(self.page.ClassSearchPageForms.CLASS_SCHEDULE_QUICK_FORM)


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

            return [{ClassSearchResultsKeys.TIME:classID,
                        ClassSearchResultsKeys.TYPE:classType,
                        ClassSearchResultsKeys.TITLE:classTitle,
                        ClassSearchResultsKeys.UNITS:classUnits,
                        ClassSearchResultsKeys.NUMBER:classNumber,
                        ClassSearchResultsKeys.DAY:classDay,
                        ClassSearchResultsKeys.TIME:classTime,
                        ClassSearchResultsKeys.DATE:classDate,
                        ClassSearchResultsKeys.ROOM:classLocation,
                        ClassSearchResultsKeys.PROFESSOR:classProfessor,
                        ClassSearchResultsKeys.SEATS:classSeats,
                        ClassSearchResultsKeys.WAITLIST:classWaitlist}]
                
