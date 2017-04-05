from urllib.request import urlopen as uReq

import null as null
from bs4 import BeautifulSoup as soup
from bs4 import Comment

gmitUrl = 'file:///C:/Users/Conor/PycharmProjects/gmitimetable/departments.html'

# connect to gmit and parse the timetables html
gmitTimetable = uReq(gmitUrl)
page_html = gmitTimetable.read()
gmitTimetable.close()

filename="dept.csv"
file = open(filename,"w")

headers = "Courses, Days\n"
file.write(headers)

# html parse
page_soup = soup(page_html, "html.parser")

depts = page_soup.findAll("div", {"id":"pObject"})
days = page_soup.findAll("div", {"id": "pDays"})

for dept in depts:
    dept_res = dept.findAll("select",{"id":"dlObject"})
    dept_res = dept_res[0].text
    print(dept_res)
    file.write(dept_res )

for day in days:
    day_res = day.findAll("select", {"id": "lbDays"})
    day_res = day_res[0].text
    print(day_res)
    file.write(day_res )
