## UTS Database Principles Tutorial 2, for 32606 &31061. Lecturer: Sri Madhisetty.

Do not type the answers, to see the result. Use your own knowledge of SQL to produce answers at least 
try. You will learn nothing if you finish the tutorial by typing the answers given. If you finish the tutorial without looking at the answers even once, you can leave. Try the sql discussed in the lecture. 

Single SQL SELECT statements:

1) Select the project name (projectName) and the mission number (missionNo) of all missions that landed on the moon ( missionType = 'LL'). 

Select projectName, missionNo from NASA2_Mission where missionType = 'LL';

2) Select mission missionNo and craftname of all lunar modules.

 Select missionno, craftname from NASA2_Spacecraft where crafttype ='LM';

3) List all astronaut names, year of birth, and year of death who were born before 1930 and who have died. Order by year of birth.

Select astroname, birth, death from NASA2_astronaut  where birth<1930 and death is not null order by birth;
 
4) Select missions of all projects (projectname, mission no) that lasted less than an hour. Show the hours and minutes of those missions.

Select projectname, missionNo, hours, minutes from NASA2_Mission where days <1 and hours <1;

5) Select all missions (Projectname, Missionno) launched in 1969.

Select missionno, craftname from NASA2_Spacecraft where projectname = 'Mercury'; 
OR
Select projectname, missionno from NASA2_mission where launchyear = 1969;









