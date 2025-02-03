#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 12
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours 
  hours = input("Enter hours: ")
  hours = int(hours)
  
  #Ask user for minutes
  minutes = input("Enter minutes: ")
  minutes = int(minutes)
  futureMinute = currentMinute + minutes
  additionalHours = (futureMinute // 60)
  futureMinute = futureMinute % 60
  futureHour = (currentHour + hours + additionalHours)
  futureHour = (futureHour % 12)

  strHour = str(futureHour)
  strMin = str(futureMinute)

  




  if futureMinute < 10:
    strMin = "0" + strMin
  print(strHour + ":" + strMin)



  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
