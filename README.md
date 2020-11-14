<br><img src=/img/mongoscaper.png><br>
# Quick Start
MongoScraper is a powerful interpreter that can manipulate objects and interfere with MongoDB databases
# Functions
**Concretely what can it do ?**
### Database Side
* Create Databases
* Delete Databases
* See Databases
### Collection Side
* Create Collections
* Delete Collections 
* See Collections 
### Document Side
* Create Documents
* See Documents
# Requirements
First install the requirements to not miss the external libraries 
```py
pip3 install -r requirements.txt
```
# Practice
**Here is the client-side VENV**<br>
<br><img src=/img/cli.gif><br>
## Database Handling
<br><img src=/img/db.gif><br>
### Atlas MongoDB Result
* When a database is created MongoDB need to set up a collection so i have referenced it to "defaultcollection"<br>
```py
mycol = dbcreated.create_collection("defaultcollection")
```
<br><img src=/img/dbcreated.png><br>
## Collection Handling
<br><img src=/img/coll.gif><br>
* This function has been called for delete the collection<br>
```py
mydeletecol = str("mydb." + deletecoll + ".drop()")
exec(mydeletecol)
```
<br>
* MongoDB use the JSON format for stock the collections and documents so I developed this function to clear up the display characters of the table<br>
```py
output = str(a).replace('[','').replace(']','').replace(', ', '\n').replace("'",'')
```
