from urllib.request import urlopen as uReq

import null as null
from bs4 import BeautifulSoup as soup
from bs4 import Comment

gmitUrl = 'file:///C:/Users/Conor/PycharmProjects/gmitimetable/SoftwareYear3Semester2.html'

# connect to gmit and parse the timetables html
gmitTimetable = uReq(gmitUrl)
page_html = gmitTimetable.read()
gmitTimetable.close()

filename="G-KSOFGH84 BSc in Software Development L8 Yr 4 Sem 8 Fri.csv"
file = open(filename,"w")

headers = "Room, Module, Group, Capacity, Classes\n"
file.write(headers)

# html parse
page_soup = soup(page_html, "html.parser")

blocks = page_soup.findAll("table", {"class":"object-cell-args"})
i = 0


# Loop through each block on the timetable and extract its data
for block in blocks:
    i = i % 3
    block_res = block.findAll("td", {"align": "left"})
    #print(block_res)
    if i == 0:
        room = block_res
        room = room[0].text
        room = room.replace('[<td align="left">', "")
        room = room.replace('</td>]', "")
        file.write(room.replace(',', "-") + ",")
        print("room", room)
    elif i == 1:
        module = block_res
        module = module[0].text
        module = module.replace('[<td align="left">', "")
        module = module.replace('</td>]', "")
        if "Gr A/P" in module:
            group = "A"
        elif "Gr B" in module:
            group = "B"
        elif "Gr C" in module:
            group = "C"
        elif "Gr D" in module:
            group = "D"
        elif "Gr E" in module:
            group = "E"
        else:
            group = "All Groups"
        print("module", module)
        file.write(module + ",")
        file.write(group + ",")
        print(group)
    elif i == 2:
        classes = block_res
        classes = classes[0].text
        classes = classes.replace('[<td align="left">', "")
        classes = classes.replace('</td>]', "")
        print("classes", classes)
        file.write(classes.replace(',', "-") + ",")
    roomCap = block.findAll("td", {"align": "right"})
    try:
        roomCap = roomCap[0].text
        roomCap = roomCap.replace('[<td align="right">', "")
        roomCap = roomCap.replace('</td>]', "")
        print("cap", roomCap)
        file.write(roomCap + "\n")
    except IndexError:
        print("")
    i += 1
    #file.write(room.replace(',', "-") + "," + module + "," +  classes.replace(',', "-") + roomCap + group)
