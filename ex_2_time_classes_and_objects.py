
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if hours <= Time.max_hours:
            self.hours = hours
        if minutes <= Time.max_minutes:
            self.minutes = minutes

        if seconds <= Time.max_seconds:
            self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):

        if self.seconds == 59:
            self.seconds = 00
            if self.minutes == 59:
                self.minutes = 00
                if self.hours == 23:
                    self.hours = 00
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())


