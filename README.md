<br><img src=/img/mongoscaper.png><br>
# Quick Start
<img src="https://forthebadge.com/images/badges/built-with-love.svg" height="40" length="40">        <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="40" length="40">
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
```py3
pip3 install -r requirements.txt
```
# Practice
**Here is the client-side VENV**<br>
<br><img src=/img/cli.gif><br>
## Database Handler
<br><img src=/img/db.gif><br>
### Atlas MongoDB Result
* When a database is created MongoDB need to set up a collection so i have referenced it to "defaultcollection"<br>
```py3
mycol = dbcreated.create_collection("defaultcollection")
```
<br><img src=/img/dbcreated.png><br>
## Collection Handler
<br><img src=/img/coll.gif><br>
* This function has been called for delete the collection<br>
```py3
mydeletecol = str("mydb." + deletecoll + ".drop()")
exec(mydeletecol)
```
* MongoDB use the JSON format for stock the collections and documents so I developed this function to clear up the display characters of the table<br>
```py3
output = str(a).replace('[','').replace(']','').replace(', ', '\n').replace("'",'')
```
## Document Handler
<br><img src=/img/doc.gif><br>
* This function is used for the creation of the Document<br>
```py3
doc = {"_id": docid, docobject: docobjectattribut}
d = mycol.insert_one(doc)
```
### Atlas MongoDB Result
<br><img src=/img/doccreated.png><br>
* We can see the JSON format
```json
_id:1
tempoobject:"attributerandom"
```
