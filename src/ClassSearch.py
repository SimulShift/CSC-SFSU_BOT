import mechanize
from time import sleep

br = mechanize.Browser()

br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this

br.addheaders = [('User-agent', 'Firefox')]

br.open("https://webapps.sfsu.edu/public/classservices/classsearch")
br.select_form("classScheduleQuick")


br.form.find_control("classScheduleQuick[searchFor]").value = "CSC210"
br.submit()
result = br.open("https://webapps.sfsu.edu/public/classservices/searchresultsjson")
print(result.read())
