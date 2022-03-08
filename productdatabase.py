import sqlite3 as s
connection = s.connect("Products.db")
# connection.execute(''' CREATE TABLE PRODUCTDATA(
#                        PRODUCT_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
#                        PRODUCT_NAME TEXT,
#                        PRICE INTEGER,
#                        DISTRIBUTOR_NAME TEXT,
#                        MANUFACTURE_NAME TEXT
#
#
#
# ) ''')
#
# print("Table created Successfully")

getPDname = input("Enter Product name: ")
getPrice = input("Enter Price: ")
getDistributorname = input("Enter Distributor Name: ")
getManufacturename = input("Enter Manufacture Name: ")



connection.execute(" INSERT INTO PRODUCTDATA(PRODUCT_NAME, PRICE, DISTRIBUTOR_NAME, MANUFACTURE_NAME) \
 VALUES('"+getPDname+"',"+getPrice+",'"+getDistributorname+"','"+getManufacturename+"')")
connection.commit()
connection.close()
print("Inserted Successfully")
