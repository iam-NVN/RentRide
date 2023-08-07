import mysql.connector as sqlpy
import string
import random
from datetime import datetime, timedelta

def uid_gen(size=12, chars=string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def add_hours_to_utc(hrs):
    return int((datetime.now()+timedelta(hours=hrs)).timestamp())

conn = sqlpy.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = 'rentride'
)

if not conn.is_connected():
    print('DB Connection Failed!')
    
cursor = conn.cursor()


def addUser(uname,pwd,name,location,utype='user'):
    uid = uid_gen(12)
    try:
        cursor.execute(
        'INSERT INTO users VALUES({uid},"{utype}","{uname}","{pwd}","{name}","{location}",0)'
        .format(uid=uid,uname=uname,utype=utype,pwd=pwd,name=name,location=location)
        )
        conn.commit()
        return True
    except:
        return False

def suspendUser(uname,value):
    try:
        cursor.execute(
        'UPDATE users SET suspended = {value} WHERE username = "{uname}"'
        .format(uname=uname,value=value)
        )
        conn.commit()
        return True
    except:
        return False
 
def deleteUser(uname):
    try:
        cursor.execute(
        'DELETE FROM users WHERE username = "{uname}"'
        .format(uname=uname)
        )
        conn.commit()
        return True
    except:
        return False
    
def unameAvailability(username):
    try:
        cursor.execute(
        'SELECT * FROM users WHERE username = "{username}"'
        .format(username=username)
        )
        info = cursor.fetchall()
        if len(info) == 0:
            return True
        else:
            return False
    except:
        return False

def rentCarAdd(carInfo,uid,rentduration,rentbegin,rentend):
    try:
        cursor.execute(
        'INSERT INTO rentstats(UID, CID, OID, Rent_Begin, Rent_End, Rent_Time, Price) VALUES("{uid}","{cid}","{oid}","{rent_begin}","{rent_end}","{rent_time}",{price})'
        .format(uid=uid,cid=carInfo[0],oid=uid_gen(),rent_begin=rentbegin,rent_end=rentend,rent_time=rentduration,price=carInfo[7]*rentduration)
        )
        cursor.execute('update CARS set available = 0 where cid = "{cid}"'.format(cid=carInfo[0]))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getUserInfo(uid):
    try:
        cursor.execute(
        'SELECT * FROM users WHERE UID = "{uid}"'
        .format(uid=uid)
        )
        info = cursor.fetchall()
        return info
    except:
        return False

def getUserInfoUname(uname):
    try:
        cursor.execute(
        'SELECT * FROM users WHERE username = "{uname}"'
        .format(uname=uname)
        )
        info = cursor.fetchall()
        return info
    except:
        return False

def getCarInfo(cid):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE cid = "{cid}"'
        .format(cid=cid)
        )
        info = cursor.fetchall()
        return info
    except:
        return False
   
def getCars(location):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE location_id = "{location}" AND available = 1'
        .format(location=location)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False

def getAllCars():
    try:
        cursor.execute(
        'SELECT * FROM cars'
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False

def getUsers():
    try:
        cursor.execute(
        'SELECT * FROM users WHERE type = "user"'
        )
        users = cursor.fetchall()
        usersdb = []
        for x in users:
            totalspent = getUserAmounts(x[0])
            totalrentals = getUserRentals(x[0])
            usersdb.append([x,totalrentals[0]+totalrentals[1],"₹"+str(totalspent[0]+totalspent[1])])
        return usersdb
    except:
        return False
    
def getPartners():
    try:
        cursor.execute(
        'SELECT * FROM users WHERE type = "partner"'
        )
        users = cursor.fetchall()
        usersdb = []
        for x in users:
            stats = getPartnerStats(x[0])
            usersdb.append([x,stats[0],stats[1],"₹"+str(stats[3])])
        return usersdb
    except:
        return False
    
def getPartnerCars(uid):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE PID = "{uid}"'
        .format(uid=uid)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False

def addPartnerCar(brand,model,ctype,fuel,seater,transmission,rate,city,uid):
    cid = uid_gen(12)
    try:
        cursor.execute(
        'INSERT INTO cars VALUES("{cid}","{brand}","{model}","{ctype}","{fuel}",{seating},"{transmission}","{rate}","{pid}","{location}")'
        .format(cid=cid,brand=brand,model=model,seating=seater,ctype=ctype,fuel=fuel,transmission=transmission,rate=rate,pid=uid,location=city)
        )
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False

def editPartnerCar(cid,brand,model,ctype,fuel,seating,transmission,rate,city):
    try:
        cursor.execute(
        'UPDATE cars SET brand = "{brand}", model = "{model}", type = "{ctype}", fuel = "{fuel}",seating = {seating}, transmission = "{transmission}", rate = "{rate}", location_id = "{location}" WHERE cid = "{cid}"'
        .format(cid=cid,brand=brand,model=model,ctype=ctype,fuel=fuel,seating = seating,transmission=transmission,rate=rate,location=city)
        )
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False

def deletePartnerCar(cid):
    try:
        cursor.execute(
        'DELETE FROM cars WHERE cid = "{cid}"'
        .format(cid=cid)
        )
        conn.commit()
        return True
    except:
        return False

def getPartnerStats(uid):
    try:
        cursor.execute(
        'SELECT CID FROM cars WHERE PID = "{uid}"'
        .format(uid=uid)
        )
        ccarids = cursor.fetchall()
        carids = []
        for c in ccarids:
            carids.append(c[0])
            
        totalcars = len(carids)
        if totalcars == 0:
            return [0,0,0,0]
        
        cursor.execute(
        'SELECT COUNT(*),SUM(total) FROM rentstats WHERE CID in {carids}'
        .format(carids=str(carids).replace('[','(').replace(']',')'))
        )
        tt = cursor.fetchone()
        rentalcount = tt[0]
        totalincome = round(float(tt[1])*0.8,2)
        
        cursor.execute(
        'SELECT COUNT(*) FROM rentstats WHERE CID in {carids} AND status ="0"'
        .format(carids=str(carids).replace('[','(').replace(']',')'))
        )
        carsonrent = cursor.fetchone()[0]
        
        return [totalcars,rentalcount,carsonrent,totalincome]
    except:
        return False

def getAdminStats():
    try:
        cursor.execute('SELECT type,COUNT(*) FROM users GROUP BY type ORDER BY type')
        users = cursor.fetchall()
        cursor.execute('SELECT COUNT(*) FROM users WHERE type = "user" AND suspended = 1')
        sususers = cursor.fetchall()[0]
        
        userbase = [users[2][1],sususers[0],users[1][1],users[0][1],users[0][1]+users[2][1]] #User,Suspended,Partner,Admin,Total
        
        
        cursor.execute('SELECT type,COUNT(*) FROM cars GROUP BY type ORDER BY type')
        carstype = cursor.fetchall()
        sedan = hatchback = suv = muv = coupe = sports = 0
        for x in carstype:
            if x[0] == 'Sedan':
                sedan = x[1]
            elif x[0] == 'Hatchback':
                hatchback = x[1]
            elif x[0] == 'SUV':
                suv = x[1]
            elif x[0] == 'MUV':
                muv = x[1]
            elif x[0] == 'Coupe':
                coupe = x[1]
            elif x[0] == 'Sports':
                sports = x[1]
                
        cursor.execute('SELECT fuel,COUNT(*) FROM cars GROUP BY fuel ORDER BY fuel')
        carsfuel = cursor.fetchall()
        diesel = petrol = electric = 0
        for x in carsfuel:
            if x[0] == 'Petrol':
                petrol = x[1]
            elif x[0] == 'Diesel':
                diesel = x[1]
            elif x[0] == 'Electric':
                electric = x[1]
                
        cars = [[sedan,hatchback,suv,muv,coupe,sports],[diesel,petrol,electric]]
        
        cursor.execute('SELECT COUNT(*),SUM(total) FROM rentstats')
        statsrent = cursor.fetchall()
        totalrents = statsrent[0][0]
        amount = statsrent[0][1]
        profit = round(float(amount)*0.2,2)
        transactions = [totalrents,amount,profit]
        
        return userbase,cars,transactions
    except:
        return False
      
def getCarsBrand(brand):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE brand = "{brand}"'
        .format(brand=brand)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False
    
def getPartnerInfo(pid):
    try:
        cursor.execute(
        'SELECT name,location_id FROM users WHERE uid = {pid}'
        .format(pid=pid)
        )
        cars = cursor.fetchall()
        return cars[0]
    except:
        return False
       
def getPartnerCIDS(uid):
    try:
        cursor.execute(
        'select CID FROM cars WHERE pid = {uid}'
        .format(uid=uid)
        )
        cars = cursor.fetchall()
        carslist = []
        for x in cars:
          carslist.append(x[0])
        return carslist
    except:
        return False
   
def getPartnerRecords(pid):
    try:
        cursor.execute(
        'SELECT * FROM rentstats WHERE CID IN {cids} ORDER BY Rent_Begin DESC'.format(cids=tuple(getPartnerCIDS(pid)))
        )
        history = cursor.fetchall()
        return history
    except:
        return False
    
def getPartnerCarStatus(cid):
    try:
        cursor.execute(
        'SELECT * FROM rentstats WHERE CID = {cid} AND Status = 0'
        .format(cid=cid)
        )
        cars = cursor.fetchall()
        if len(cars) > 0:
            return True
        else:
            return False
    except:
        return False
    
def getCarsFuel(fuel):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE fuel = "{fuel}"'
        .format(fuel=fuel)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False

def getCarsType(type):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE type = "{type}"'
        .format(type=type)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False

def getCarsTM(transmission):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE transmission = "{transmission}"'
        .format(transmission=transmission)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False
       
def getCarsSearch(search):
    try:
        cursor.execute(
        'SELECT * FROM cars WHERE Model LIKE "%{Name}%"'
        .format(Name=search)
        )
        cars = cursor.fetchall()
        return cars
    except:
        return False
    
def login(uname,pwd):
    try:
        cursor.execute(
        'SELECT * FROM users WHERE username = "{uname}" AND passwd = "{pwd}"'
        .format(uname=uname,pwd=pwd)
        )
        info = cursor.fetchall()
        return info
    except:
        return False
    
def getUserHistory(uid):
    try:
        cursor.execute(
        'SELECT * FROM rentstats WHERE uid = "{uid}" ORDER BY Rent_Begin DESC'
        .format(uid=uid)
        )
        history = cursor.fetchall()
        return history
    except:
        return False

def getUserAmounts(uid):
    try:
        cursor.execute(
        'SELECT IFNULL(SUM(total),0) FROM rentstats WHERE uid = "{uid}" AND status = "1"'
        .format(uid=uid)
        )
        sumpaid = cursor.fetchone()
        if len(sumpaid) == 0:
            sumpaidx = 'k'
        else:
            print(sumpaid)
            sumpaidx = sumpaid[0]
            
        cursor.execute(
        'SELECT IFNULL(SUM(total),0) FROM rentstats WHERE uid = "{uid}" AND status = "0"'
        .format(uid=uid)
        )
        sumdue = cursor.fetchone()
        if len(sumdue) == 0:
            sumduex = 0
        else:
            sumduex = sumdue[0]
        
        return sumpaidx,sumduex
    except:
        return False
    
def getUserRentals(uid):
    try:
        cursor.execute(
        'SELECT IFNULL(COUNT(*),0) FROM rentstats WHERE uid = "{uid}" AND status = "1"'
        .format(uid=uid)
        )
        carsreturned = cursor.fetchone()
        
        cursor.execute(
        'SELECT IFNULL(COUNT(*),0) FROM rentstats WHERE uid = "{uid}" AND status = "0"'
        .format(uid=uid)
        )
        carsdue = cursor.fetchone()
        
        return carsreturned[0],carsdue[0]
    except:
        return False
    
def getUserNotReturned(uid):
    try:
        cursor.execute(
        'SELECT * FROM rentstats WHERE uid = "{uid}" AND status = "0" ORDER BY Rent_Begin DESC'
        .format(uid=uid)
        )
        history = cursor.fetchall()
        return history
    except:
        return False

def returnCar(cid,uid,oid,price,penalty):
    try:
        cursor.execute(
        'UPDATE rentstats SET status = "1",penalty = {penalty},total = {total} WHERE oid = "{oid}" AND uid = "{uid}"'
        .format(uid=uid,oid=oid,penalty=int(penalty),total=int(price)+int(penalty)))
        cursor.execute('update CARS set available = 1 where cid = "{cid}"'.format(cid=cid))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
 