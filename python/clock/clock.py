class Clock:
    def __init__(self, hour, minute):
        total_minute = ((hour*60 + minute) % 1440)
        self.hour   = total_minute // 60
        self.minute = total_minute % 60
        
    def __repr__(self):
        return str(self.hour).rjust(2,'0')+":"+str(self.minute).rjust(2,'0')        

    def __eq__(self, other):
        return other.hour == self.hour and other.minute == self.minute
        
    def __add__(self, minutes):
        return Clock(self.hour,self.minute+minutes)   

    def __sub__(self, minutes):
        return Clock(self.hour,self.minute-minutes)

