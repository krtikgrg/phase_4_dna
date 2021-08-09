import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate


def addSupply():
    global cur
    row = {}
    print("Enter the details of new supply from a factory to a shop: ")
    row["F_Email"] = input("Enter email of the factory: ")
    row["Name_of_Com"] = input("Enter the name of commodity which is supplied: ")
    row["S_Location"] = input("Enter the complete address of the shop: ")

    try:
        query = "INSERT INTO SUPPLY(F_Email, Name_of_Com, S_Location) VALUES('%s', '%s', '%s')" % \
                (row["F_Email"], row["Name_of_Com"], row["S_Location"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return


def addperson():
    global cur
    row = {}
    print("Enter the details of new person: ")
    row["Aadhar_No"] = input("Aadhar no: ")
    check = 0
    if len(row["Aadhar_No"]) != 12:
        check = 1
    for i in row["Aadhar_No"]:
        if i >= '0' and i <= '9':
            pass
        else:
            check = 1
            break
    if check == 1:
        print("\n\nError: INVALID AADHAR NO! TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return
    row["Name"] = input("Name: ")
    row["Address"] = input("Address: ")
    try:
        query = "INSERT INTO PERSON(Aadhar_No, Name, Address) VALUES('%s', '%s', '%s')" % \
                (row["Aadhar_No"], row["Name"], row["Address"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: Try again using different data\n")
        return


def addSemployee():
    global cur
    row = {}
    row["Fk_Aad_No"] = input("Aadhar card no: ")
    row["Fk_S"] = input("Shop address: ")

    print("1. if employee has a supervisor\n2. Otherwise")
    n = int(input("your choice: "))
    if n == 1:
        row["Sup_Aad"] = input("Supervisor's aadhar card no: ")
        try:
            query = "INSERT INTO S_EMPLOYEE(Fk_Aad_No, Fk_S, Sup_Aad) VALUES('%s', '%s', '%s')" % \
                    (row["Fk_Aad_No"], row["Fk_S"], row["Sup_Aad"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again using same data\n")
            return
    else:
        try:
            query = "INSERT INTO S_EMPLOYEE(Fk_Aad_No, Fk_S) VALUES('%s', '%s')" % \
                    (row["Fk_Aad_No"], row["Fk_S"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again using same data\n")
            return


def addInsurance():
    global cur
    row = {}
    row["Name"] = input("Name: ")
    row["Cost"] = int(input("Cost of insurance: "))
    try:
        query = "INSERT INTO INSURANCE_COMPANY(Name, Cost) VALUES('%s', '%d')" % \
                (row["Name"], row["Cost"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again using different data\n")
        return


def addCustomers():
    global cur
    row = {}
    row["Fk_Aad_No"] = input("Aadhar card no: ")
    print("1. IF CUSTOMER HAS A LIFE INSURANCE\n2. OTHERWISE")
    n = int(input("your choice: "))
    if n == 1:
        row["Fk_Insur"] = input("Name of insurance company: ")
        try:
            query = "INSERT INTO CUSTOMERS(Fk_Aad_No, Fk_Insur) VALUES('%s', '%s')" % \
                    (row["Fk_Aad_No"], row["Fk_Insur"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again with different data\n")
            return
    else:
        try:
            query = "INSERT INTO CUSTOMERS(Fk_Aad_No) VALUES('%s')" % \
                    row["Fk_Aad_No"]
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again with different data\n")
            return


def addFemployee():
    global cur
    row = {}
    row["Fk_Aad_No"] = input("Aadhar card no: ")
    row["Fk_F"] = input("Factory Email: ")
    print("1. if employee has a supervisor\n2. Otherwise")
    n = int(input("your choice: "))
    if n == 1:
        row["Sup_Aad"] = input("Supervisor's aadhar card no: ")
        try:
            query = "INSERT INTO F_EMPLOYEE(Fk_Aad_No, Fk_F, Sup_Aad) VALUES('%s', '%s', '%s')" % \
                    (row["Fk_Aad_No"], row["Fk_F"], row["Sup_Aad"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again using different data\n")
            return
    else:
        try:
            query = "INSERT INTO F_EMPLOYEE(Fk_Aad_No, Fk_F) VALUES('%s', '%s')" % \
                    (row["Fk_Aad_No"], row["Fk_F"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: try again using different data\n")
            return


def addInsuredvia():
    global cur
    row = {}
    row["E_Aad"] = input("Aadhar no of employee: ")
    row["F_Email"] = input("Email of factory: ")
    row["I_Name"] = input("Insurance company name: ")
    try:
        query = "INSERT INTO INSURED_VIA(E_Aad, F_Email, I_Name) VALUES('%s', '%s', '%s')" % \
                (row["E_Aad"], row["F_Email"], row["I_Name"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again with some different data\n")
        return


def updatecost():
    global cur
    x = input("Name of insurance company: ")
    y = input("New cost of insurance: ")
    try:
        query = "UPDATE INSURANCE_COMPANY SET Cost='%d' WHERE Name='%s'" % \
                (y, x)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nTry again with some different data!\n")


def addWorkson():
    global cur
    row = {}
    row["Id"] = input("Project id of consignment: ")
    row["Fk_Email"] = input("Email of factory: ")
    try:
        query = "INSERT INTO WORKS_ON(Id, Fk_Email) VALUES('%s', '%s')" % \
                (row["Id"], row["Fk_Email"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again with some different data\n")
        return


def addTracksinfo():
    global cur
    row = {}
    row["CAAD"] = input("aadhar no of customer: ")
    row["Name_of_Com"] = input("name of commodity: ")
    row["S_Location"] = input("Address of shop: ")
    row["F_Email"] = input("Email of factory: ")
    try:
        query = "INSERT INTO TRACKS_INFO(CAAD, Name_of_Com, S_Location, F_Email) VALUES('%s', '%s', '%s', '%s')" % \
                (row["CAAD"], row["Name_of_Com"], row["S_Location"],row["F_Email"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again with some different data\n")
        return


def addConsignment():
    global cur
    row = {}
    row["Fk_Works_Id"] = input("Project id of consignment: ")
    row["Year"] = int(input("Year of consignment: "))
    row["Quantity"] = int(input("Quantity of goods produced: "))
    try:
        query = "INSERT INTO CONSIGNMENT(Fk_Works_Id, Year, Quantity) VALUES('%s', '%d', '%d')" % \
                (row["Fk_Works_Id"], row["Year"], row["Quantity"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again with some different data\n")
        return


def addCommodity():
    global cur
    row = {}
    print("Enter the details of new commodity: ")
    row["Name"] = input("Enter name of the commodity ")

    try:
        query = "INSERT INTO COMMODITY(Name) VALUES('%s')" % (row["Name"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return


def addFactory():
    global cur
    row = {}
    print("Enter the details of factory: ")
    row["E_Mail"] = input("E-mail: ")
    row["Location"] = input("Address Of Factory: ")
    row["Fk_Own_Aad_No"] = input("Aadhar no of owner: ")
    check = 0
    if len(row["Fk_Own_Aad_No"]) != 12:
        check = 1
    for i in row["Fk_Own_Aad_No"]:
        if i >= '0' and i <= '9':
            pass
        else:
            check = 1
            break
    if check == 1:
        print("\n\nError: INVALID AADHAR NO! TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return
    try:
        query = "INSERT INTO FACTORY(E_Mail, Location, Fk_Own_Aad_No) VALUES('%s', '%s', '%s')" % (
            row["E_Mail"], row["Location"], row["Fk_Own_Aad_No"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return


def addShop():
    global cur
    row = {}
    print("Enter the details of of shop")
    row["State_Code"] = int(input("State code of gst no: "))
    row["Pan_Card_No"] = input("Pan card no of gst no: ")
    row["Random_No"] = input("Random no of gst no: ")
    row["Name"] = input("Full name of shop: ")
    row["Location"] = input("Address of shop: ")
    if row["State_Code"] > 37 or row["State_Code"] < 0:
        print("\n\nError:Invalid state code! TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return
    if len(row["Pan_Card_No"]) != 10:
        print("\n\nError:Invalid pan card no! TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return
    try:
        query = "INSERT INTO SHOP(State_Code, Pan_Card_No, Random_No, Name, Location) VALUES('%d', '%s', '%s', '%s', '%s')" % (
            row["State_Code"], row["Pan_Card_No"], row["Random_No"], row["Name"], row["Location"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return


def getOption():
    global cur
    print("Choose an option for insertion: \n\n")
    print("1. SHOP\n2. COMMODITY\n3. FACTORY\n4. SUPPPLY\n5. TRACKING INFORMATION OF A COMMODITY BOUGHT BY A USER")
    print("6. PERSON")
    print("7. CUSTOMERS")
    print("8. SHOP EMPLOYEE")
    print("9. FACTORY EMPLOYEE")
    print("10. CONSIGNMENT")
    print("11. INSURANCE COMPANY")
    print("12. INSURED_VIA")
    print("13. CONSIGNMENTS ON WHICH FACTORY HAS WORKED OR IS WORKING")
    n = int(input("your option: "))
    if n == 1:
       # addShop()
        query = "SELECT * FROM SHOP"
    elif n == 2:
       # addCommodity()
        query = "SELECT * FROM COMMODITY"
    elif n == 3:
       # addFactory()
       query = "SELECT * FROM FACTORY"
    elif n == 4:
       # addSupply()
       query = "SELECT * FROM SUPPLY"
    elif n == 5:
       # addTracksinfo()
       query = "SELECT * FROM TRACKS_INFO"
    elif n == 6:
       # addperson()
       query = "SELECT * FROM PERSON"
    elif n == 7:
       # addCustomers()
       query = "SELECT * FROM CUSTOMERS"
    elif n == 8:
       # addSemployee()
       query = "SELECT * FROM S_EMPLOYEE"
    elif n == 9:
       # addFemployee()
       query = "SELECT * FROM F_EMPLOYEE"
    elif n == 10:
       # addConsignment()
       query = "SELECT * FROM CONSIGNMENT"
    elif n == 11:
       # addInsurance()
       query = "SELECT * FROM INSURANCE_COMPANY"
    elif n == 12:
       # addInsuredvia()
       query = "SELECT * FROM INSURED_VIA"
    elif n == 13:
       # addWorkson()
       query = "SELECT * FROM WORKS_ON"
    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()
    return


def getShops():
    global cur
    name = input("Name of the commodity: ")
    try:
        query = "SELECT Name FROM SHOP INNER JOIN SUPPLY ON SHOP.Location=SUPPLY.S_Location WHERE Name_of_Com='%s'" % name
        cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: TRY AGAIN WITH SOME DIFFERENT DATA!\n")
        return
    rows = cur.fetchall()
    viewTable(rows)
    con.commit()


def delete():
    print("choose an option for deletion !\n\n")
    print("1. SHOP\n2. PERSON\n3. INSURANCE_COMPANY\n4. FACTORY\n5. COMMODITY\n6. CONSIGNMENT")
    n = int(input("option: "))
    global cur
    if n == 1:
        x = input("Enter shop's location: ")
        query = "DELETE FROM SHOP WHERE Location='%s'" % x
    elif n == 2:
        x = input("Enter person's Aadhar card no: ")
        query = "DELETE FROM PERSON WHERE Aadhar_No='%s'" % x
    elif n == 3:
        x = input("Enter Name of Insurance company: ")
        query = "DELETE FROM INSURANCE_COMPANY WHERE Name='%s'" % x
    elif n == 4:
        x = input("Enter E_Mail of Factory: ")
        query = "DELETE FROM  FACTORY WHERE E_Mail='%s'" % x
    elif n == 5:
        x = input("Enter Commodity name: ")
        query = "DELETE FROM COMMODITY WHERE Name='%s'" % x
    elif n == 6:
        x1 = input("factory email: ")
        x2 = input("consignment id: ")
        query = "DELETE FROM WORKS_ON WHERE Id='%s' AND Fk_Email='%s'" % (x2, x1)

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: Please try again with different data!\n")
        return


def findProduction():
    global cur
    x1 = input("Email of factory: ")
    x2 = int(input("Year of production: "))
    try:
        query = "SELECT SUM(Quantity) PRODUCTION FROM CONSIGNMENT INNER JOIN WORKS_ON " \
                "ON CONSIGNMENT.Fk_Works_Id=WORKS_ON.Id WHERE Fk_Email='%s' AND Year='%d'" %\
                (x1, x2)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: Please try again with different data!\n")
        return
    rows = cur.fetchall()
    viewTable(rows)
    con.commit()


def leavJob():
    global cur
    x = input("Employee Aadhar card no: ")
    try:
        query = "SELECT Sup_Aad FROM F_EMPLOYEE WHERE Fk_Aad_No='%s'" % x
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again using different data!\n")
        return
    y = cur.fetchall()
    try:
        query = "UPDATE F_EMPLOYEE SET Sup_Aad='%s' WHERE Sup_Aad='%s'" % (y[0]['Sup_Aad'], x)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again using different data1!\n")
        return
    try:
        query = "DELETE FROM F_EMPLOYEE WHERE Fk_Aad_No='%s'" % x
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again using different data2!\n")
        return


def findMail():
    global cur
    x = input("Customer aadhar card no: ")
    y = input("Name of commodity: ")
    z = input("Location of shop from where it was bought: ")
    try:
        query = "SELECT F_Email FROM TRACKS_INFO WHERE CAAD='%s' AND Name_of_Com='%s' AND S_Location='%s'" % \
                (x, y, z)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: try again using different data!\n")
        return
    rows = cur.fetchall()
    viewTable(rows)


def viewTable(rows):
    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return


def addOption():
    print("Choose an option for insertion: \n\n")
    print("1. SHOP\n2. COMMODITY\n3. FACTORY\n4. SUPPPLY\n5. TRACKS_INFO")
    print("6. PERSON")
    print("7. CUSTOMERS")
    print("8. SHOP EMPLOYEE")
    print("9. FACTORY EMPLOYEE")
    print("10. CONSIGNMENT")
    print("11. INSURANCE COMPANY")
    print("12. INSURED_VIA")
    print("13. WORKS ON (FACTORY ON NEW CONSIGNMENT)")
    n = int(input("your option: "))
    if n == 1:
        addShop()
    elif n == 2:
        addCommodity()
    elif n == 3:
        addFactory()
    elif n == 4:
        addSupply()
    elif n == 5:
        addTracksinfo()
    elif n == 6:
        addperson()
    elif n == 7:
        addCustomers()
    elif n == 8:
        addSemployee()
    elif n == 9:
        addFemployee()
    elif n == 10:
        addConsignment()
    elif n == 11:
        addInsurance()
    elif n == 12:
        addInsuredvia()
    elif n == 13:
        addWorkson()


while 1:
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    try:
        con = pymysql.connect(host="127.0.0.1",
                              user=username,
                              password=password,
                              port=5005,
                              db='trade_network',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print("Connection refused : Either username or Password is incorrect or user does not access to database")
        tmp = input("Enter any key to continue")
        continue

    cur = con.cursor()
    exitflag = 0
    while 1:
        tmp = sp.call('clear', shell=True)
        print("CHOOSE AN OPTION\n")
        print("1. INSERT NEW DATA INTO DATABASE TABLES")
        print("2. RETRIEVE COMPLETE DATA TUPLES")
        print("3. FIND TOTAL PRODUCTION OF A FACTORY IN A GIVEN YEAR")
        print("4. UPDATING DATABASE IF AN EMPLOYEE OF A FACTORY LEAVES THE JOB")
        print("5. DELETE DATA FROM DATABASE")
        print("6. FIND EMAIL OF FACTORY FOR GIVING REVIEWS OF YOUR BOUGHT PRODUCT")
        print("7. NAME OF ALL SHOPS WHICH SUPPLIES GIVEN COMMODITY IN THE AREA")
        print("8. UPDATE COST OF INSURANCE OF THE GIVEN INSURANCE COMPANY")
        print("9. QUIT")
        n = int(input("\nYour choice: "))
        if n == 1:
            addOption()
        elif n == 2:
            getOption()
        elif n == 3:
            findProduction()
        elif n == 4:
           leavJob()
        elif n == 5:
            delete()
        elif n == 6:
            findMail()
        elif n == 7:
            getShops()
        elif n == 8:
            updatecost()
        elif n == 9:
            exitflag = 1
            print("BYE!!")
            break

        print("Press enter to continue ...")
        x = input()

    if exitflag == 1:
        break
