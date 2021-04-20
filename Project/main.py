# This code might throw error when you try to run it because we will delete the VM instance to save credits 
# as per professor's advice.
# Without active VM instace, local queries still can be executed successfully, 
# but for that you need to comment out code related to remote query processing.

import pickle
import re
from datetime import datetime
from pickling import Utilities
from queryparser import Queryparser
from SelectOperation import select_operation
from InsertOperation import insert_operation
from DeleteOperation import delete_operation
from UpdateOperation import update_operation
from read_bucket import getBucket
from read_bucket import readFileFromBucket
from write_bucket import processDataAndWriteFileToBucket
from write_bucket import writeFileToBucket
from prettytable import PrettyTable
import json
import os
import paramiko


class Login:

    def login(self):

        file = "login.pkl"
        fileobj = open(file, 'rb')
        unpickled_tree = pickle.load(fileobj)

        print("Welcome Superuser!\n")
        userName = input("Enter Username: ") 
        password = input("Enter Password: ")

        levelOfUserName = Utilities("").getLevel(unpickled_tree, userName)
        levelOfPassword = Utilities("").getLevel(unpickled_tree, password)


        if(levelOfPassword != 0  or levelOfUserName != 0):
            if(levelOfPassword == levelOfUserName):
                print("Authentication Successful!\n")
                return True , userName
            else:
                return False , userName
        else:
            print("Invalid Credentials!\n")


    def takeInputFromUser(self):
        print("\n")
        query = input("Enter QUERY to Execute (to exit the console enter - 'quit'): ")
        query = query.strip()
        inputOfUser = query
        return inputOfUser       

    def performOperation(self , query , userName):
        file1 = open("log.txt","a")
        attributList, isQueryValid  = Queryparser().queryParser(query)
        now = datetime.now()
        today = now.strftime("%m/%d/%Y, %H:%M:%S")

        list_from_file = []

        if isQueryValid:

            if attributList[0] == "select":
                tablename = attributList[2].strip().lower()
                attribute = attributList[1]
                condition = attributList[4]
                conattributes = attributList[3]
                if attributList[5]:
                    convalue = int(attributList[5])
                else:
                    convalue = attributList[5]


                filename = tablename + ".pkl"

                with open('GDD.json') as f1:
                    data1 = json.load(f1)

                if(tablename in data1["local"]):
                    fileobj = open("data/"+filename, 'rb')
                    list_from_file = pickle.load(fileobj)
                elif(tablename in data1["remote"]):
                    bucket = getBucket()
                    list_from_file = readFileFromBucket(bucket, filename)


                    f = open("query.txt", "a")
                    f.write(query)
                    f.close()

                    # reference taken from
                    # https://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server

                    # Connect to remote host
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect('104.155.168.92', username='falgun', password='1999@falgun')

                    # Setup sftp connection and transmit this script
                    sftp = client.open_sftp()
                    sftp.put(__file__, '/tmp/query.txt')
                    sftp.close()

                    # Run the transmitted script remotely without args and show its output.
                    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
                    list_from_file = client.exec_command('python /data/main.py')[1]
                    
                    saved = list_from_file

                    client.exec_command('rm /tmp/query.txt')[1]
                    
                    client.close()

                    os.remove("query.txt")

                saved = list_from_file

                isTablePresent = False
                file = open("concurrentTransactionFile.txt", "r")
                for line in file:
                    if (line != "\n") :
                        if (line == tablename):
                            isTablePresent = True
                file.close()
                if isTablePresent:
                    print("table is in use try after some time")
                else:
                    file = open("concurrentTransactionFile.txt", "a")
                    file.write("\n")
                    file.write(tablename)
                    file.close()

                select_operation(saved,attribute,condition,conattributes,convalue)

                file = open("concurrentTransactionFile.txt", "r")
                fileLines = file.readlines()
                new_file = open("concurrentTransactionFile.txt", "w+")
                for line in fileLines:
                    if(line.strip("\n") != tablename):
                        new_file.write(line)
                new_file.close()

                file1.write("\n")
                file1.write("query is__" + query + "__by user__" + userName +"__at time__" + today)
                file1.close()
                f1.close()

            elif attributList[0] == "insert":
                
                tablename = attributList[1].strip().lower()
                attributes = attributList[2]
                newvalues = attributList[3]
                tablelocation = ""

                filename2 = tablename + ".pkl"

                with open('GDD.json') as f2:
                    data2 = json.load(f2)
                

                if(tablename in data2["local"]):
                    tablelocation = "local"
                    fileobj2 = open("data/" + filename2, 'rb')
                    list_from_file = pickle.load(fileobj2)
                elif(tablename in data2["remote"]):
                    tablelocation = "remote"
                    bucket = getBucket()
                    list_from_file = readFileFromBucket(bucket, filename2)

                    f = open("query.txt", "a")
                    f.write(query)
                    f.close()

                    # reference taken from
                    # https://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server

                    # Connect to remote host
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect('104.155.168.92', username='falgun', password='1999@falgun')

                    # Setup sftp connection and transmit this script
                    sftp = client.open_sftp()
                    sftp.put(__file__, '/tmp/query.txt')
                    sftp.close()

                    # Run the transmitted script remotely without args and show its output.
                    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
                    list_from_file = client.exec_command('python /data/main.py')[1]
                    
                    saved = list_from_file

                    client.exec_command('rm /tmp/query.txt')[1]
                    
                    client.close()

                    os.remove("query.txt")

                saved = list_from_file
                last = newvalues.pop()
                last = int(last)    
                newvalues.append(last)

                isTablePresent = False
                file = open("concurrentTransactionFile.txt", "r")
                for line in file:
                    if (line != "\n") :
                        if (line == tablename):
                            isTablePresent = True
                file.close()
                
                if isTablePresent:
                    print("table is in use try after some time")
                else:
                    file = open("concurrentTransactionFile.txt", "a")
                    file.write("\n")
                    file.write(tablename)
                    file.close()

                final_list = insert_operation(saved,attributes,newvalues)
                print("1 row inserted!")

                if tablelocation == "local":
                    f2 = open("data/" + filename2, 'wb')
                    pickle.dump(final_list, f2)
                elif tablelocation == "remote":
                    f2 = open(filename2, 'wb')
                    processDataAndWriteFileToBucket(bucket, final_list, f2, filename2)
                    os.remove(filename2)

                file = open("concurrentTransactionFile.txt", "r")
                fileLines = file.readlines()
                new_file = open("concurrentTransactionFile.txt", "w+")
                for line in fileLines:
                    if(line.strip("\n") != tablename):
                        new_file.write(line)
                new_file.close()

                file1.write("\n")
                file1.write("query is__" + query + "__by user__" + userName + "__at time__" + today)
                file1.close()

            elif attributList[0] == "delete":

                tablelocation = ""
                tablename = attributList[1].strip().lower()
                conattribute = attributList[2]
                condition = attributList[3]
                convalue = int(attributList[4])

                filename3 = tablename + ".pkl"

                with open('GDD.json') as f1:
                    data1 = json.load(f1)

                if(tablename in data1["local"]):
                    tablelocation = "local"
                    fileobj = open("data/"+filename3, 'rb')
                    list_from_file = pickle.load(fileobj)
                elif(tablename in data1["remote"]):
                    tablelocation = "remote"
                    bucket = getBucket()
                    list_from_file = readFileFromBucket(bucket, filename3)

                    f = open("query.txt", "a")
                    f.write(query)
                    f.close()

                    # reference taken from
                    # https://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server

                    # Connect to remote host
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect('104.155.168.92', username='falgun', password='1999@falgun')

                    # Setup sftp connection and transmit this script
                    sftp = client.open_sftp()
                    sftp.put(__file__, '/tmp/query.txt')
                    sftp.close()

                    # Run the transmitted script remotely without args and show its output.
                    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
                    list_from_file = client.exec_command('python /data/main.py')[1]
                    
                    saved = list_from_file

                    client.exec_command('rm /tmp/query.txt')[1]
                    
                    client.close()

                    os.remove("query.txt")

                saved = list_from_file

                isTablePresent = False
                file = open("concurrentTransactionFile.txt", "r")
                for line in file:
                    if (line != "\n") :
                        if (line == tablename):
                            isTablePresent = True
                file.close()
                
                if isTablePresent:
                    print("table is in use try after some time")
                else:
                    file = open("concurrentTransactionFile.txt", "a")
                    file.write("\n")
                    file.write(tablename)
                    file.close()

                final_list = delete_operation(saved,conattribute,convalue,condition)

                if tablelocation == "local":
                    f2 = open("data/" + filename3, 'wb')
                    pickle.dump(final_list, f2)
                elif tablelocation == "remote":
                    f2 = open(filename3, 'wb')
                    processDataAndWriteFileToBucket(bucket, final_list, f2, filename3)
                    os.remove(filename3)

                file = open("concurrentTransactionFile.txt", "r")
                fileLines = file.readlines()
                new_file = open("concurrentTransactionFile.txt", "w+")
                for line in fileLines:
                    if(line.strip("\n") != tablename):
                        new_file.write(line)
                new_file.close()


                file1.write("\n")
                file1.write("query is__" + query + "__by user__" + userName + "__at time__" + today)
                file1.close()

            elif attributList[0] == "update":

                attributes = attributList[1]
                tablename = attributList[2].strip().lower()
                updatevalues = attributList[3]
                conattribute = attributList[4]
                condition = attributList[5]
                if attributList[6]:
                    convalue = int(attributList[6])
                else:
                    convalue = attributList[6]

                filename4 = tablename + ".pkl"

                with open('GDD.json') as f1:
                    data1 = json.load(f1)

                if(tablename in data1["local"]):
                    tablelocation = "local"
                    fileobj = open("data/"+filename4, 'rb')
                    list_from_file = pickle.load(fileobj)
                elif(tablename in data1["remote"]):
                    tablelocation = "remote"
                    bucket = getBucket()
                    list_from_file = readFileFromBucket(bucket, filename4)

                    f = open("query.txt", "a")
                    f.write(query)
                    f.close()

                    # reference taken from
                    # https://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server

                    # Connect to remote host
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect('104.155.168.92', username='falgun', password='1999@falgun')

                    # Setup sftp connection and transmit this script
                    sftp = client.open_sftp()
                    sftp.put(__file__, '/tmp/query.txt')
                    sftp.close()

                    # Run the transmitted script remotely without args and show its output.
                    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
                    list_from_file = client.exec_command('python /data/main.py')[1]
                    
                    saved = list_from_file

                    client.exec_command('rm /tmp/query.txt')[1]
                    
                    client.close()

                    os.remove("query.txt")

                saved = list_from_file
                isTablePresent = False
                file = open("concurrentTransactionFile.txt", "r")
                for line in file:
                    if (line != "\n") :
                        if (line == tablename):
                            isTablePresent = True
                file.close()
                
                if isTablePresent:
                    print("table is in use try after some time")
                else:
                    file = open("concurrentTransactionFile.txt", "a")
                    file.write("\n")
                    file.write(tablename)
                    file.close()

                final_list = update_operation(saved,attributes,updatevalues,condition,conattribute,convalue)
                print("1 row Updated!")

                if tablelocation == "local":
                    f2 = open("data/" + filename4, 'wb')
                    pickle.dump(final_list, f2)
                elif tablelocation == "remote":
                    f2 = open(filename4, 'wb')
                    processDataAndWriteFileToBucket(bucket, final_list, f2, filename4)
                    os.remove(filename4)

                file = open("concurrentTransactionFile.txt", "r")
                fileLines = file.readlines()
                new_file = open("concurrentTransactionFile.txt", "w+")
                for line in fileLines:
                    if(line.strip("\n") != tablename):
                        new_file.write(line)
                new_file.close()


                file1.write("\n")
                file1.write("query is__" + query + "__by user__" + userName + "__at time__" + today)
                file1.close()

            elif attributList[0] == "create":

                final_list = []
                gdd_keys = []

                bucket = getBucket()
                z = PrettyTable()

                tablelocation = ""
                columncount = attributList[1]
                columnnames = attributList[2]
                columntypes = attributList[3]
                tablename = attributList[4].strip().lower()
                primarykey = attributList[2][0]

                filename5 = tablename + ".pkl"

                final_list.append(columncount)
                final_list.append(1)
                final_list.append(tablename)

                for i in range(columncount):
                    final_list.append(columnnames[i]+"|"+columntypes[i])

                with open('GDD.json') as f:
                    data = json.load(f)

                for x in data:
                    gdd_keys.append(x)

                if tablename not in x:
                    data[tablename] = []
                    for i in range(columncount):
                        data[tablename].append(columnnames[i]+"|"+columntypes[i])
    
                if tablename[0] >= 'm':
                    if tablename not in data["local"]:
                        data["local"].append(tablename)
                        tablelocation = "local"
                else:
                    if tablename not in data["remote"]:
                        data["remote"].append(tablename)
                        tablelocation = "remote"

                    f = open("query.txt", "a")
                    f.write(query)
                    f.close()

                    # reference taken from
                    # https://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server

                    # Connect to remote host
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect('104.155.168.92', username='falgun', password='1999@falgun')

                    # Setup sftp connection and transmit this script
                    sftp = client.open_sftp()
                    sftp.put(__file__, '/tmp/query.txt')
                    sftp.close()

                    # Run the transmitted script remotely without args and show its output.
                    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
                    list_from_file = client.exec_command('python /data/main.py')[1]
                    
                    saved = list_from_file

                    client.exec_command('rm /tmp/query.txt')[1]
                    
                    client.close()

                    os.remove("query.txt")

                if tablelocation == "local":
                    f5 = open("data/" + filename5, 'wb')
                    pickle.dump(final_list, f5)
                    f5.close()
                elif tablelocation == "remote":
                    f5 = open(filename5, 'wb')
                    processDataAndWriteFileToBucket(bucket, final_list, f5, filename5)
                    f5.close()
                    os.remove(filename5)

                with open('GDD.json', 'w') as f:
                    json.dump(data, f)
                
                print("Empty table created!\n")
                z.field_names = columnnames
                print(z)

                input('')



if __name__ == '__main__':

    isUserLoggedIn , userName = Login().login()
    f = open("logFile.txt","a")

    if isUserLoggedIn:
        userInput = Login().takeInputFromUser()
        while userInput != "quit":
            Login().performOperation(userInput , userName)
            userInput = Login().takeInputFromUser()
              
    else: 
        print("Invalid Credentials!")