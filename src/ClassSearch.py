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

        class ClassServicesResultsPageURL(Enum):
            CLASS_SEARCH_JSON_RESULTS_URL = "https://webapps.sfsu.edu/public/classservices/searchresultsjson"

        class ClassSearchPageURL(Enum):
            CLASS_SEARCH_URL = "https://webapps.sfsu.edu/public/classservices/classsearch"

        class ClassSearchPageForms(Enum):
            CLASS_SCHEDULE_QUICK_FORM = "classScheduleQuick"
            CLASS_SCHEDULE_QUICK_FORM_SEARCH_FOR = "classScheduleQuick[searchFor]"

        def __init__(self) -> None:
            pass

class MechanizeWebBrowser:
    class Headers(Enum):
        USER_AGENT = "User-agent"
        FIREFOX = "Firefox"
    
    browser: mechanize.Browser
    def __init__(self) -> None:
        self.browser = mechanize.Browser()

    def set_handle_robots(self, enabled: bool):
        self.browser.set_handle_robots(enabled)

    def set_handle_refresh(self, enabled: bool):
        self.browser.set_handle_refresh(enabled)

    def set_headers_user_agent_and_firefox(self):
        self.browser.addheaders = [(self.Headers.USER_AGENT, self.Headers.FIREFOX)]

    def open_url(self, url: str):
        self.browser.open(url)
    
    def select_html_form(self, form: str):
        self.browser.select_form(form)
    
    def find_html_form_control(self, form: str):
        self.browser.form.find_control(form)

class ClassSearch:
    page: ClassSearchPage
    browser: MechanizeWebBrowser

    def __init__(self):
        self.page = ClassSearchPage()
        self.browser = MechanizeWebBrowser().browser
        
    def classSearch(self, searchString):
        self.browser = MechanizeWebBrowser()
        self.browser.set_handle_robots(enabled=False) # ignore robots
        self.browser.set_handle_refresh(enabled=False) # can sometimes hang without this

        self.browser.set_headers_user_agent_and_firefox()

        self.browser.open_url(self.page.ClassSearchPageURL.CLASS_SEARCH_URL)

        self.browser.select_html_form(self.page.ClassSearchPageForms.CLASS_SCHEDULE_QUICK_FORM)

        self.browser.form.find_control(self.page.ClassSearchPageForms.CLASS_SCHEDULE_QUICK_FORM_SEARCH_FOR).value = searchString

        self.browser.submit()

        result = self.browser.open(self.page.ClassServicesResultsPageURL.CLASS_SEARCH_JSON_RESULTS_URL)
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
                
