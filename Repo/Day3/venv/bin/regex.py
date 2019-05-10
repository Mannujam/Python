'''
1) Connect DB
2) Create DB
3) Create Table
4) Read from url
5) Read content using regular expressions
6) insert data in DB

'''

import sqlite3

# Database access
con = sqlite3.connect('mydb.sqlite3')
# con = anyotherDB (user='', password='', host='', port='',database='')

cur = con.cursor()
query = "create table if not exists logdata (" \
        "IP varchar(100)," \
        "date varchar(100)," \
        "pics varchar(100)," \
        "url varchar(100)," \
        "browsername varchar(30)," \
        "browserversion varchar(10))"
con.execute(query)

# Web scraping
import urllib.request as u

myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'
F = u.urlopen(myurl)

# Reading data from url in form of regular expression
import re

for line in F:
    #print(line)
    #print(type(line))      # check the type. Type should always be string to process regular expression
    line = line.decode()    # convert the type to string.
    #print(type(line))       # check the type again

    #m = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*GET\s+(/pics/(\w+\.\w+))?.*(http[s]?://[a-zA-Z0-9.]+).*', line)
    m = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*GET\s+(/pics/(\w+\.\w+))?.*(http[s]?://[a-zA-Z0-9.]+)?.*"([a-zA-Z]+).*/([0-9.]+).*', line)
                                                                    # '\d' is identifier for digits
                                                                    # '.' --> for all chars including special
                                                                    # '\.' --> only '.'
                                                                    # '{3}' --> repeat 3 times
                                                                    # '{1,3}' --> repeat 1 to 3 times
                                                                    # '[0-9]' --> only numbers from 0 to 9
                                                                    # '[a-zA-Z]' --> any char case insensitive
                                                                    # '?' --> allows right of '*' to take max limit else min limit
                                                                    # '\s+' --> Including one or more space
                                                                    # '\w' --> Including [a-zA-Z0-9]
                                                                    # '\W' --> Excluding [a-zA-Z0-9]
                                                                    # '\W' --> Excluding [0-9]
                                                                    # '\S+' --> Excluding one or more space

    if m != None:
        ip = m.group(1)
        print('IP = ',ip)

        dt = m.group(2)
        print('Date = ',dt)

        img = m.group(4)
        if img != None:
            print('Image = ',img)
        else:
            print('No Image.')

        url = m.group(5)
        print('URL = ',url)

        b = m.group(6)
        print('Browser Name = ',b)

        bv = m.group(7)
        print('Browser Version = ',bv)

        #inserting into data
        query = f"INSERT INTO logdata values ('{ip}','{dt}','{img}','{url}','{b}','{bv}')"
        cur.execute(query)
        con.commit()

# Fetch all data from DB and put it into csv file
cur.execute('select * from logdata')
result = cur.fetchall()
print('Result = ', result)

# write db data into csv
F1 = open ('dbdata.csv','w',newline='')

import csv
import openpyxl         #install openpyxl module

wt = csv.writer(F1)
wt.writerow(['IP Address','Date','Pics','Website','browser','version','id'])

for row in result:
    wt.writerow(row)

F1.close()

#check pandas example
import pandas as pd
L = [[10,20,30],[40,50,60]]

df1 = pd.DataFrame (L,index=['row1','row2'],columns=['c1','c2','c3'])
print(df1)
df2 = pd.DataFrame (result)
df2.to_csv('out4.csv')
df2.to_excel('out5.xlsx')
df2.to_json('out6.json')
print(df2)
