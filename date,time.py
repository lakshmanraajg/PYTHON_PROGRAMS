from datetime import date
from datetime import time
from datetime import datetime

def main():
    
    today = date.today()
    print(today)
    
    print(today.weekday()) #0-6
    
    
    today = datetime.now()
    print(today)
    
    t=datetime.time(today)
    print(t)
    
main()