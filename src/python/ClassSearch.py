import json
import mechanize
import asyncio
import sys
from bs4 import BeautifulSoup

async def quickSearch(searchString):
    """
    :param searchString: the class to seach for, the database expects a classnumber

    :returns: dicts with the following schema
        [   
            {
                coursenumber: "CSC210[1]"
                type: "LEC" # Either LEC or LAB I belive
                title: "Introduction to Computer Programming"  
                units: "3"
                classnumber: "1908"
                days: "Tu Th"
                time: "12:30PM - 1:45PM"
                date: "23-AUG-2021 - 10-DEC-2021"
                location: "Online Synchronous" # This field is blank if the class does not have a room assigned yet
                instructor: "Arno Puder"
                seats: "0"
                waitlist: "5"
            }
        ]
    """
    url = "https://webapps.sfsu.edu/public/classservices/classsearch"
    formName = "classScheduleQuick"
    searchFieldName = "classScheduleQuick[searchFor]"
    jsonResultsUrl = "https://webapps.sfsu.edu/public/classservices/searchresultsjson"

    # Create a virtual browswer instance
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]

    # Navagate to the page with the form and select the form
    br.open(url)
    br.select_form(formName)

    # Fill out the form, we are only using 1 field at the moment but the form also has fields to select a semester.
    br.form.find_control(searchFieldName).value = searchString
    br.submit()
    result = br.open(jsonResultsUrl)

    # TODO: Test if this always works.
    if result == "":
        raise Exception("Class not Found")

    #
    data = json.loads(result.read())
    classList = []

    # for some reason all the data is nested inside of a field named aaData
    for entity in data["aaData"]:
        courseNumber = entity[0].split('>')[1].split('<')[0]
        type = entity[1]
        title = entity[2]
        units = entity[3]
        classNumber = entity[4]

        # Need to do some string parsing to get information out of line 7
        dateLine = BeautifulSoup(entity[7], 'html.parser').div.contents
        if len(dateLine) == 2:
            days = dateLine[0].text
            time = "TBD or ONLINE"
            dates = dateLine[1].text
            location = "TBD"
        elif len(dateLine) == 3:
            days = dateLine[0].text
            time = "TBD or ONLINE"
            dates = dateLine[1].text
            location = dateLine[2].text
        elif len(dateLine) == 4:
            days = dateLine[0].text
            time = dateLine[1].text
            dates = dateLine[2].text
            location = dateLine[3].text
        else:
            days = ""
            time = "TBD or ONLINE"
            dates = ""
            location = "TBD"
        

        # Need to strip the HTML out of the line storing the professors name as well
        professor = entity[8].split('>')[1].split('<')[0].strip()
        seats = entity[9]
        waitlist = entity[10]

        classList.append({
            "coursenumber":courseNumber,                         
            "type":type,
            "title":title,
            "units":units,
            "classnumber":classNumber,
            "days":days,
            "time":time,
            "dates":dates,
            "location":location,
            "instructor":professor,
            "seats":seats,
            "waitlist":waitlist,
        })

    print(json.dumps(classList[:10]))


async def main():
    classes = await quickSearch(sys.argv[1])



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
