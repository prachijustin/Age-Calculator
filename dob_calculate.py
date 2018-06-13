from calendar import monthrange
import datetime
now=datetime.datetime.now()

class Age_calculator:
    def __init__(self,date,month,year,check_year,check_month,check_days,hours,minutes,seconds,ms):
        self.date=date
        self.month=month
        self.year=year
        self.check_year=check_year
        self.check_month=check_month
        self.check_days=check_days
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self.ms=ms
           
    def put(self):
        dob= input("Enter your date of birth(dd-mm-yyyy): ")
        self.date=int(dob[0:2])
        self.month=int(dob[3:5])
        self.year=int(dob[6:10]) 
        return self.date,self.month,self.year  
              
    def years(self):
        if (now.month==self.month):
            if(now.day>=self.date):
                self.check_year= now.year-self.year
            else:
                self.check_year= now.year-self.year-1
                
        elif now.month<self.month:
            self.check_year= now.year-self.year-1
            
        else:
            self.check_year= now.year-self.year
            
        print(self.check_year," years ")
        
    def months(self):
        if(now.month==self.month):
            if(now.day>=self.date):
                self.check_month=0
            else:
                self.check_month= 11
                
        elif(now.month>self.month):
            self.check_month= (now.month-self.month)-1
            
        else:   #todo 
            if now.day>=self.date:
                a=12-self.month
                self.check_month=now.month+a
            else:
                a=12-self.month
                self.check_month=now.month+a-1
            #self.check_month= 12-(self.month-now.month)
            
        print(self.check_month," months ")
        
        
            
    def days(self):
        if(now.month==self.month):
            if(now.day>=self.date):
                self.check_days=now.day-self.date
            else:
                dy=monthrange(now.year, now.month)
                month_day=dy[1]
                chk= self.date-now.day
                self.check_days=month_day-chk +1
                
        elif(now.month>self.month):
            a= monthrange(now.year,now.month-1)
            md=a[1]
            ck= md-self.date
            self.check_days=now.day+ck
            
        else:   
            if self.date<now.day:
                self.check_days=now.day-self.date
            elif self.date==now.day:
                self.check_days=0
            else:
                a= monthrange(now.year,now.month-1)
                md=a[1]
                ck= md-self.date
                self.check_days=now.day+ck
                 
        print(self.check_days," days ")
    
    def total_months(self):
        if(now.month==self.month):
            if(now.day<self.date):
                self.check_month= (self.check_year*12)-1+12
            else:
                self.check_month= self.check_year*12
                
        elif(now.month>self.month):
            self.check_month= (self.check_year*12)+(now.month-self.month)-1
            
        else:    #todo
            if now.day>=self.date:
                a= 12-self.month
                self.check_month= (self.check_year*12)+a+now.month
            else:
                a= 12-self.month
                self.check_month= (self.check_year*12)+a+now.month-1
            
        print("or, ",self.check_month, " months")
        
    def total_weeks(self):
        d1= datetime.date(self.year,self.month,self.date)
        d2= datetime.date(now.year,now.month,now.day)
        delta= d2-d1
        self.mod_dy=delta.days%7
        self.week=delta.days-self.mod_dy
        self.week=int(self.week/7)
        print("or, ",self.week," weeks")
    
    def total_days(self):
        d3= datetime.date(self.year,self.month,self.date)
        d4= datetime.date(now.year,now.month,now.day)
        temp1= d4-d3
        self.check_days= temp1.days
        print("or, " ,self.check_days, " days")
        
    def total_hrs(self):
        self.hours= self.check_days*24
        #print(now.hour)
        hr= now.hour
        self.hours= self.hours+ hr
        print("or, ",self.hours," hours")
        
    def total_mins(self):
        self.minutes= self.hours*60
        mns= now.minute
        self.minutes= self.minutes+ mns
        print("or, ",self.minutes," minutes")
        
    def total_seconds(self):
        self.seconds= self.minutes*60
        sec= now.second
        self.seconds= self.seconds+ sec
        print("or, ",self.seconds," seconds")
        
    def total_ms(self):
        self.ms= self.seconds*60
        print("or, ",self.ms," milli seconds")
        
ag= Age_calculator(0,0,0,0,0,0,0,0,0,0)
a,b,c=ag.put()
d1= datetime.date(c,b,a)
d2= datetime.date(now.year,now.month,now.day)
delta= d2-d1

if delta.days<0:
    print("Wrong DOB! ")
else:
    print("The age is: ")
    ag.years()
    ag.months()
    ag.days()
    ag.total_months()
    ag.total_days()
    ag.total_weeks()
    ag.total_hrs()
    ag.total_mins()
    ag.total_seconds()
    ag.total_ms()

