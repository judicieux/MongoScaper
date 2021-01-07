import pymongo
import os
import socket
from colorama import Fore, Style, init

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    start()

def logo():
    logo = f"""{Fore.RED}
    ███╗   ███╗ ██████╗ ███╗   ██╗ ██████╗  ██████╗ ███████╗ ██████╗ █████╗ ██████╗ ███████╗██████╗ 
    ████╗ ████║██╔═══██╗████╗  ██║██╔════╝ ██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║   ██║██╔██╗ ██║██║  ███╗██║   ██║███████╗██║     ███████║██████╔╝█████╗  ██████╔╝
    ██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║██║   ██║╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝███████║╚██████╗██║  ██║██║     ███████╗██║  ██║
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

                                [{Fore.BLUE}+{Fore.RED}] By hypostat1c [{Fore.BLUE}+{Fore.RED}]
                     [{Fore.BLUE}+{Fore.RED}] To see manual of commands do "help" [{Fore.BLUE}+{Fore.RED}]   
"""
    print(logo)
logo()

def database():
    databaseactif = True

    while databaseactif == True:
        databaseinput = str(input(f"{Fore.RED}[Database] > "))

        try:
            if databaseinput == "help":
                a = f"""
    Database :
            Create Database > createdb
            Switch Database > switchdb
            See Databases > seedb
                """
                print(f"{Fore.YELLOW}" + a)
                database()
                
            elif databaseinput == "createdb":
                createdatabase = str(input("[+] Name [+] : "))
                dbconnect = pymongo.MongoClient("mongodb+srv://" + myclientuser + ":7vDyWYPW2VfXuihM@cluster1.naysc.mongodb.net/" + createdatabase + "?retryWrites=true&w=majority")
                dbcreated = dbconnect[createdatabase]
                mycol = dbcreated.create_collection("defaultcollection")
                print(f"{Fore.GREEN}Created : " + createdatabase)

            elif databaseinput == "switchdb":
                login()

            elif databaseinput == "seedb":
                a = myclient.list_database_names()
                output = str(a).replace('[', '').replace(']', '').replace(', ', '\n').replace("'", '')
                print(f"\n{Fore.BLUE}[+] Databases [+]\n" + f"{Fore.YELLOW}" + output + "\n")
                database()

            elif databaseinput == "exit":
                start()

            else:
                database()

        except SyntaxError:
            database()

        except ValueError:
            database()

def collection():
    collectionactif = True

    while collectionactif == True:
        collectioninput = str(input(f"{Fore.RED}[Collection] > "))

        try:
            if collectioninput == "help":
                a = """
    Collection :
            Create Collection > createcoll
            Delete Collection > deletecoll
            See Collections > seecoll
                    """
                print(f"{Fore.YELLOW}" + a)
                collection()

            elif collectioninput == "createcoll":
                createcoll = input(f"{Fore.BLUE}[+] Name [+] > ")
                mycol = mydb.create_collection(createcoll)
                print(f"{Fore.GREEN}Added : " + createcoll)

            elif collectioninput == "deletecoll":
                deletecoll = str(input(f"{Fore.BLUE}[+] Name [+] > "))
                mydeletecol = str("mydb." + deletecoll + ".drop()")
                exec(mydeletecol)
                print(f"{Fore.GREEN}Deleted : " + deletecoll)

            elif collectioninput == "seecoll":
                a = mydb.list_collection_names()
                output = str(a).replace('[','').replace(']','').replace(', ', '\n').replace("'",'')
                print(f"\n{Fore.BLUE}[+] Collections [+]\n" + f"{Fore.YELLOW}" + "\n" + output + "\n")
                collection()

            elif collectioninput == "exit":
                start()

            else:
                collection()

        except ValueError:
            collection()

def document():
    documentactif = True
    
    while documentactif == True:
        documentinput = str(input(f"{Fore.RED}[Document] > "))
        
        try:
            if documentinput == "help":
                a = """
    Document :
            Create Document > createdoc
            Delete Document > deletedoc
            See Documents > seedoc
                            """
                print(f"{Fore.YELLOW}" + a)
                document()

            elif documentinput == "createdoc":
                collchoice = str(input("[+] Collection Name [+] > "))
                mycol = mydb[collchoice]
                docid = int(input("[+] id [+] > "))
                docobject = str(input("[+] Object [+] > "))
                docobjectattribut = str(input("[+] Attribute [+] > "))
                doc = {"_id": docid, docobject: docobjectattribut}
                d = mycol.insert_one(doc)
                print(f"\n{Fore.GREEN}Document Added : ")
                print(doc)
                print("")

            elif documentinput == "deletedoc":
                collchoice = str(input("[+] Collection Name [+] > "))
                mycol = mydb[collchoice]
                docid = int(input("[+] id [+] > "))
                docobject = str(input("[+] Object [+] > "))
                docobjectattribut = str(input("[+] Attribute [+] > "))
                doc = {"_id": docid, docobject: docobjectattribut}
                b = mycol.insert_one(doc)
                print(f"{Fore.YELLOW}")
                print(doc)

            elif documentinput == "seedoc":
                collchoice = str(input("[+] Collection Name [+] > "))
                mycol = mydb[collchoice]
                print(f"\n{Fore.BLUE}[+] Documents [+]")
                for x in mycol.find():
                    print(f"{Fore.YELLOW}")
                    print(x)
                    print("")

            elif documentinput == "exit":
                start()

            else:
                document()

        except pymongo.errors.InvalidName:
            print("Collection not found")
            document()

        except TypeError:
            document()

        except ValueError:
            document()

def start():
    hostname = socket.gethostname()
    startinput = input(f"{Fore.RED} MongoScaper" + f"{Fore.BLUE}@" + f"{Fore.RED}" + hostname + f"{Fore.BLUE}~$ ")
    startactif = True

    while startactif == True:
        try:
            if startinput == "help":
                a = """
    Handles :
            Database > db
            Collection > coll
            Document > doc
                """
                print(f"{Fore.YELLOW}" + a)
                start()

            elif startinput == "db":
                database()

            elif startinput == "coll":
                collection()

            elif startinput == "doc":
                document()

            elif startinput == "clear":
                clear()

            elif startinput == "exit":
                exit()

            else:
                start()

        except SyntaxError:
            start()

        except ValueError:
            start()

def login():
    global myclientuser
    myclientuser = str(input(f"{Fore.RED}[Username] > "))
    
    global myclientdatabase
    myclientdatabase = str(input(f"{Fore.RED}[Database] > "))
    
    global myclient
    myclient = pymongo.MongoClient("mongodb+srv://" + myclientuser + ":7vDyWYPW2VfXuihM@cluster1.naysc.mongodb.net/" + myclientdatabase + "?retryWrites=true&w=majority")
    
    global mydb
    mydb = myclient[myclientdatabase]
    clear()
    
    try:
        a = myclient.list_database_names()
        
    except pymongo.errors.OperationFailure:
        print(f"{Fore.RED}[+] User and Database not found [+]")
        exit()
login()
