# CSE2102-Fall2024-Team25
Allen Tran, alt20009 
Shanique Rock, SHR22001 
Ethan Skinner, EJS22007
Nichole Samaniego, NSS21006

# trello Board Link 
#https://trello.com/b/Vcp5LOtz/cse2102-fall24-team25

# Figma link
#https://www.figma.com/design/AGrF35lCrJMg0wAdWKu6Sy/Desktop_Prototype?node-id=0-1&t=KcT1WMbt0azHYRQC-1


# How to build docker image (backend and frontend)
docker build --tag team25_backend .
docker build --tag team25_frontend .

# How to run docker image 
docker run -p 5001:5000 team25_backend
docker run -p 5173:5173 team25_frontend

# How to run docker image (detached mode)
docker run -d -p 5001:5000 team25_backend
docker run -d -p 5173:5173 team25_frontend

# How to intialize database
Start backend/sqllite.py by using python sqllite.py or your editor

### Then,
Start backend/sqlite_stubs.py to intialize test stubs or
If you want to restart delete the database.db file

# Pet Quiz feature not implemented 
The reason for this is because we need to have user logged in order to do the pet quiz.
This requires Auth0 which is extra credit. For now the website has full functionality with the
dogs button in the homepage and settings which uses steel threads to connect to the api and requests from and to database.


# Pet-Adoption-Website
# Pet-Adoption-Website
# Pet-Adoption-Website
# Pet-Adoption-Website
# Pet-Adoption-Website
