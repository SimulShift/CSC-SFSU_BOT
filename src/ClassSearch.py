import json
import mechanize
import asyncio

async def quickSearch(searchString):
    """
    :param searchString: the class to seach for, the database expects a classnumber

    :yields: dicts with the following schema
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
    classList = []

    for entity in data["aaData"]:
        classes = []
        courseNumber = entity[0].split('>')[1].split('<')[0]
        type = entity[1]
        title = entity[2]
        units = entity[3]
        classNumber = entity[4]

        # Need to do some string parsing to get information out of line 7
        dateLine = entity[7]
        dateLine = dateLine.split('>')
        days = dateLine[2].split('<')[0]
        time = dateLine[4].split('<')[0]
        dates = dateLine[6].split('<')[0]
        
        # Not gurenteed to have a location
        try:
            location = dateLine[8].split('<')[0]
        except:
            location = ""

        # Need to strip the HTML out of the line storing the professors name as well
        professor = entity[8].split('>')[1].split('<')[0].strip()
        seats = entity[9]
        waitlist = entity[10]

        classList.append({
            "CourseNumber":courseNumber,
            "Type":type,
            "Title":title,
            "Units":units,
            "ClassNumber":classNumber,
            "Days":days,
            "Time":time,
            "Dates":dates,
            "Location":location,
            "Professor":professor,
            "Seats":seats,
            "Waitlist":waitlist
        })
        
    return classList

async def main():
    classes = await quickSearch("CSC210")
    for c in classes:
        print(c)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
