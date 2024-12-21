from mysql.connector import connect
from flask import request,make_response
# import sqlite3
# sqlite3.connect("SHOPPING.db")


connection_string=connect(host="localhost",user="root",password="",port=5050,database="shopping")
query=connection_string.cursor(dictionary=True)

class Product:
    print("DATABASE Connected Successfully!!")
    def get_all_products(self):
        query.execute("SELECT * FROM PRODUCT")
        return make_response({"success":query.fetchall()})
    def post_products(self):
        data=request.json
        try:
            query.execute("INSERT INTO PRODUCT(PRODUCT_NAME,PRODUCT_PRICE,PRODUCT_MANIFATURED_BY,PRODUCT_AVALABILITY)VALUES(%s,%s,%s,%s)",tuple(data.values()))
            connection_string.commit()
            return make_response({"success":"Product data added successfully"})
        except Exception as e:
            return make_response({"erorr":f"Something error occured as{e}"},400)
    def update_products(self):
        pass
    
    
    def delete_products(self):
        pass
    
    
        










# print("DATABASE CONNECTED SUCCESSFULLY")
# query=connection_string.cursor()
# query.execute("CREATE TABLE SHOPPING")
# print("TABLE SHOPPING CREATED SUCCESSFULLY!!!")
