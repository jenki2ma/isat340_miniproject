import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
## data as tuple of tuples

sql1 = "insert into celebs values(?,?,?,?,?,?,?)"

data1 = ((1,"Angelina", "Jolie",40,"angie@hollywood.us",'../static/angie.jpg',"American actress and filmmaker, 3 golden globe awards. Star of malificent."),(2, "Brad","Pitt",51,"brad@hollywood.us",'../static/brad.jpg',"American Acter and Film producer winner of Acadamy award, british academy award and 2 golden globes. Stars in Fight Club"),(3,"Snow", "White",21,"sw@disney.org",'../static/snow.jpg',"Disney princess who lives with 7 dwarves. Just recently met Prince Charming"),(4,"Darth", "Vader",29,"dv@darkside.me",'../static/darth.jpg',"Single, Father of two, real name Anakin Skywalker. Possibly murdered his wife."),
(5,"Taylor", "Swift",25,'ts@1989.us','../static/taylor.jpg',"American singer/songwriter whose music is often inspired by her own personal life"),(6,"Beyonce", "Knowles",34,"beyonce@jayz.me",'../static/beyonce.jpg',"American singer. Married to Jay-Z. Born and Raised in houston Texas"),(7,"Selena", "Gomez",23,"selena@hollywood.us",'../static/selena.jpg',"American singer. Born and raised in texas. Star in tv show Wizards of waverly place"),(8,"Stephen", "Curry",27,"steph@golden.bb",'../static/stephen.jpg',"NBA basket ball player, all time record holder of most 3-pointers ever made. Plays for the Golden state warriors"))
cursor.executemany(sql1, data1)

sql = "insert into members values(?,?,?,?,?,?)"
data = ((1, "Ryan","Buellesbach",21,'buellera@dukes.jmu.edu','Born and raised in Fairfax Virginia. Youngest of 4 and avid Green Bay Packers fan'),(2, "Matt","Jenkins",20,"jenki2ma@dukes.jmu.edu", "Born and raised in Henrico, Virginia. Youngest of 7 and trash talker of the Green bay packers"))
cursor.executemany(sql, data)

sql2= "insert into member_login values(?, ?, ?)"
data2=((1, "rbbach", "potato"),(2,"mattyj","tomato"))
cursor.executemany(sql2,data2)
    

conn.commit()
conn.close()
