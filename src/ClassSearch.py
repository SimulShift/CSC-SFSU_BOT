import json
from logging import exception
import mechanize
import asyncio
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

class ClassSearchResultsKeys(Enum):
    COURSE = "Course"
    TYPE = "Type"
    TITLE = "Title"
    UNITS = "Units"
    NUMBER = "Number"
    DAY = "Day"
    TIME = "Time"
    DATE = "Date"
    LOCATION = "Location"
    PROFESSOR = "Professor"
    SEATS = "Seats"
    WAITLIST = "Waitlist"

class ClassSearchDelimiters(Enum):
    OPEN = '<'
    CLOSE = '>'

class ClassSearchJSONDataKeys(Enum):
    ROOTDATAKEY = "aaData"
def search(searchString):
        
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this

    br.addheaders = [('User-agent', 'Firefox')]

    br.open(ClassSearchPage.ClassSearchPageURL.CLASS_SEARCH_URL.value)
    br.select_form(ClassSearchPage.ClassSearchPageForms.CLASS_SCHEDULE_QUICK_FORM.value)


    br.form.find_control(ClassSearchPage.ClassSearchPageForms.CLASS_SCHEDULE_QUICK_FORM_SEARCH_FOR.value).value = searchString
    br.submit()
    result = br.open(ClassSearchPage.ClassServicesResultsPageURL.CLASS_SEARCH_JSON_RESULTS_URL.value)
    data = json.loads(result.read())
    return data

async def advancedSearch(searchString):
    data = search(searchString=searchString)
    classList = []
    for entity in data[ClassSearchJSONDataKeys.ROOTDATAKEY.value]:
        if entity[0].find(ClassSearchDelimiters.CLOSE.value) or entity[0].find(ClassSearchDelimiters.OPEN.value):
            courseNumber = entity[0].split(ClassSearchDelimiters.CLOSE.value)[1].split(ClassSearchDelimiters.OPEN.value)[0]
            type = entity[1]
            title = entity[2]
            units = entity[3]
            classNumber = entity[4]

        # Need to do some string parsing to get information out of line 7
            try:
                dateLine = entity[7]
                dateLine = dateLine.split(ClassSearchDelimiters.CLOSE.value)
                days = dateLine[2].split(ClassSearchDelimiters.OPEN.value)[0]
                time = dateLine[4].split(ClassSearchDelimiters.OPEN.value)[0]
                dates = dateLine[6].split(ClassSearchDelimiters.OPEN.value)[0]
            except:
                dateLine = ""
                days = ""
                time = ""
                dates = ""
        
        # Not gurenteed to have a location
            try:
                location = dateLine[8].split(ClassSearchDelimiters.OPEN.value)[0]
            except:
                location = ""

        # Need to strip the HTML out of the line storing the professors name as well
            professor = entity[8].split(ClassSearchDelimiters.CLOSE.value)[1].split(ClassSearchDelimiters.OPEN.value)[0].strip()
            seats = entity[9]
            waitlist = entity[10]

            classList.append({
                ClassSearchResultsKeys.COURSE.value:courseNumber,
                ClassSearchResultsKeys.TYPE.value:type,
                ClassSearchResultsKeys.TITLE.value:title,
                ClassSearchResultsKeys.UNITS.value:units,
                ClassSearchResultsKeys.NUMBER.value:classNumber,
                ClassSearchResultsKeys.DAY.value:days,
                ClassSearchResultsKeys.TIME.value:time,
                ClassSearchResultsKeys.DATE.value:dates,
                ClassSearchResultsKeys.LOCATION.value:location,
                ClassSearchResultsKeys.PROFESSOR.value:professor,
                ClassSearchResultsKeys.SEATS.value:seats,
                ClassSearchResultsKeys.WAITLIST.value:waitlist
            })
    return classList

async def quickSearch(searchString):
    """
    :param searchString: the class to seach for, the database expects a classnumber

    :returns: dicts with the following schema
        [   
            {
                CourseNumber: "CSC210[1]"
                Type: "LEC" # Either LEC or LAB I belive
                Title: "Introduction to Computer Programming"  
                Units: "3"
                ClassNumber: "1908"
                Attributes: "Lower Division"
                Days: "Tu Th"
                Time: "12:30PM - 1:45PM"
                Date: "23-AUG-2021 - 10-DEC-2021"
                Location: "Online Synchronous" # This field is blank if the class does not have a room assigned yet
                Instructor: "Arno Puder"
                Seats: "0"
                Waitlist "5"
            }
        ]
    """
    data = search(searchString=searchString)
    classList = []
    for entity in data[ClassSearchJSONDataKeys.ROOTDATAKEY.value]:
        if entity[0].find(ClassSearchDelimiters.CLOSE.value) or entity[0].find(ClassSearchDelimiters.OPEN.value):
            courseNumber = entity[0].split(ClassSearchDelimiters.CLOSE.value)[1].split(ClassSearchDelimiters.OPEN.value)[0]
            type = entity[1]
            title = entity[2]
            units = entity[3]
            classNumber = entity[4]

        # Need to do some string parsing to get information out of line 7
            try:
                dateLine = entity[7]
                dateLine = dateLine.split(ClassSearchDelimiters.CLOSE.value)
                days = dateLine[2].split(ClassSearchDelimiters.OPEN.value)[0]
                time = dateLine[4].split(ClassSearchDelimiters.OPEN.value)[0]
                dates = dateLine[6].split(ClassSearchDelimiters.OPEN.value)[0]
            except:
                dateLine = ""
                days = ""
                time = ""
                dates = ""
        
        # Not gurenteed to have a location
            try:
                location = dateLine[8].split(ClassSearchDelimiters.OPEN.value)[0]
            except:
                location = ""

        # Need to strip the HTML out of the line storing the professors name as well
            professor = entity[8].split(ClassSearchDelimiters.CLOSE.value)[1].split(ClassSearchDelimiters.OPEN.value)[0].strip()
            seats = entity[9]
            waitlist = entity[10]

            classList.append({
                ClassSearchResultsKeys.COURSE.value:courseNumber,
                ClassSearchResultsKeys.TYPE.value:type,
                ClassSearchResultsKeys.TITLE.value:title,
                ClassSearchResultsKeys.UNITS.value:units,
                ClassSearchResultsKeys.NUMBER.value:classNumber,
                ClassSearchResultsKeys.DAY.value:days,
                ClassSearchResultsKeys.TIME.value:time,
                ClassSearchResultsKeys.DATE.value:dates,
                ClassSearchResultsKeys.LOCATION.value:location,
                ClassSearchResultsKeys.PROFESSOR.value:professor,
                ClassSearchResultsKeys.SEATS.value:seats,
                ClassSearchResultsKeys.WAITLIST.value:waitlist
            })
    return classList

class ClassSearchPage:

        class ClassServicesResultsPageURL(Enum):
            CLASS_SEARCH_JSON_RESULTS_URL = "https://webapps.sfsu.edu/public/classservices/searchresultsjson"

        class ClassSearchPageURL(Enum):
            CLASS_SEARCH_URL = "https://webapps.sfsu.edu/public/classservices/classsearch"

        class ClassSearchPageForms(Enum):
            CLASS_SCHEDULE_QUICK_FORM = "classScheduleQuick"
            CLASS_SCHEDULE_QUICK_FORM_SEARCH_FOR = "classScheduleQuick[searchFor]"

async def main():
    classes = await advancedSearch("101")
    for c in classes:
        print(c)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
