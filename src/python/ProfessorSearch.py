import asyncio
import mechanize

#pip install RateMyProfessorPyAPI

SCHOOL_ID = "U2Nob29sLTg4MA=="

async def ProfessorSearch(professor):
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]

    try:
        page = br.open(f'https://www.ratemyprofessors.com/filter/professor/?&page={professor}&queryoption=TEACHER&queryBy=schoolId&sid={SCHOOL_ID}')
    except Exception as e:
        print("URL not found")
    print(page)

async def main():
    classes = await advancedSearch("101")
    for c in classes:
        print(c)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


