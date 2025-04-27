#time module
#multithreading
from time import sleep,time      #method is yellow color
from threading import Thread      #class is green color
import datetime
import logging

logging.basicConfig(filename='demo.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def sample_func(name,age,address):
    if age<18:
        if address in ['Bengalore','Manglore','Hubli','Tumkur']:
            logging.info(f"Name is {name}")
            logging.info(f"Name is {age}")
            logging.info(f"Name is {address}")
            logging.info(f"User is eligible to vote")
        else:
            logging.error(f"Name is not valid")
    else:
        logging.error('address is not in the list')
sample_func("suchi",20,"Banglore")






# print(datetime.datetime.now().date())
# print(datetime.datetime.today())
# print(datetime.datetime.time)
# # print(datetime.datetime.day)
# # print(datetime.datetime.date('27','9','2021'))
# # print(datetime.datetime.month)
# # print(datetime.datetime.year)
# start=time()
# def func_1():
#     for data in range(5):
#         print(f"Hi I am executing the function 1 for{data} time")
#         sleep(1)

# def func_2(num_1,num_2):
#     for data in range(5):
#         print(f"Hi I am executing the function 1 for{data} time")
#         print(f"Addition of two number is {num_1+num_2}")

#         sleep(1)
# def func_3():
#     for data in range(5):
#         print(f"Hi I am executing the function 1 for{data} time")
#         sleep(1)

# # func_1()
# # func_2()
# # func_3()

# call_func1=Thread(target=func_1)
# call_func2=Thread(target=func_2,args=(10,15))
# call_func3=Thread(target=func_3)
# call_func1.start()
# call_func2.start()
# call_func3.start()
# call_func1.join()
# call_func2.join()
# call_func3.join()
# end=time()
# print(f"start time is{start}")
# print(f"end time is{end}")
# print(f"Time taken to execute the script is {end-start}")