import json
import mechanize
import asyncio
import sys
from bs4 import BeautifulSoup

SCHOOL_ID = "U2Nob29sLTg4MA=="

async def ProfessorSearch(professor):
    profList = []
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]

    try:
        response = br.open(
            f'https://www.ratemyprofessors.com/search/teachers?query={professor}&sid={SCHOOL_ID}')
        page = BeautifulSoup(response.read(), 'html.parser')
    except Exception as e:
        print(e)

    prof_cards = page.body.find_all(
        'a', class_="TeacherCard__StyledTeacherCard-syjs0d-0")

    for card in prof_cards:
        wrapper = card.div
        rating_div = wrapper.div.contents[0]
        info_div = wrapper.contents[1]
        university_div = info_div.contents[1]
        feedback_div = info_div.contents[2]

        profList.append({
            "name": info_div.contents[0].text,
            "university": university_div.contents[1].text,
            "department": university_div.contents[0].text,
            "rating": rating_div.contents[1].text,
            "rating_count": rating_div.contents[2].text.split()[0],
            "wouldtakeagain": feedback_div.contents[0].text.split()[0],
            "difficulty": feedback_div.contents[3].text.split()[0]
        })
    
    return json.dumps(profList[:10])


async def main():
    professors = await ProfessorSearch(sys.argv[1])
    print(professors)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
