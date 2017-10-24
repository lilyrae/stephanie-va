import datetime as dt
from Stephanie.Modules.base_module import BaseModule


class SystemModule(BaseModule):
    def __init__(self, *args):
        super(SystemModule, self).__init__(*args)
        self.name = self.get_configuration(section="USER", key="name")
        self.gender = self.get_configuration(section="USER", key="gender")

    def default(self):
        return _("Repeat back your command!.")

    def meaning_of_life(self):
        return _("42 is the meaning of life.")

    def time_right_now(self):
        t = dt.datetime.now()
        return self.time_teller(t)

    def date_today(self):
        t = dt.datetime.now()
        return self.date_teller(t)

    def wake_up(self):
        t = dt.datetime.now()
        if self.gender:
            gender = self.gender.lower()
            if gender == "male":
                return _("{0}, sir!").format(self.phase_of_the_day(t))
            elif gender == "female":
                return _("{0}, mam!").format(self.phase_of_the_day(t))
            else:
                return _("{0}, dear!").format(self.phase_of_the_day(t))
        elif self.name:
            return "{0}, {1}!".format(self.phase_of_the_day(t), self.name)
        else:
            return "{0}!".format(self.phase_of_the_day(t))
    # Example to access assistant instance
    # def wake_up(self):
    #     self.assistant.say("What time is it again?")
    #     text = self.assistant.listen().decipher()
    #     return "Good %s, sir!" % text

    def go_to_sleep(self):
        self.assistant.events.add("sleep").trigger("sleep")
        return _("Sleep for the weak!")

    def quit(self):
        self.assistant.events.add("quit").trigger("quit")
        return _("I will come back stronger!")

    def tell_system_status(self):
        import psutil
        import platform
        import datetime

        os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = _("I am currently running on {0} version {1}.  ").format(os, version)
        response += _("This system is named {0} and has {1} CPU cores.  ").format(name, cores)
        response += _("Current disk_percent is {0} percent.  ").format(disk_percent)
        response += _("Current CPU utilization is {0} percent.  ").format(cpu_percent)
        response += _("Current memory utilization is {0} percent. ").format(memory_percent)
        response += _("it's running since {0}.").format(running_since)
        return response

    @staticmethod
    def time_teller(time):
        # t = time.strftime('%I %M %H')
        # phase = time.strftime("%p")
        t = time.strftime("%I:%M:%p")

        d = {0: "oh",
             1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine",
             10: "ten",
             11: "eleven",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen",
             20: "twenty",
             30: "thirty",
             40: "forty",
             50: "fifty",
             60: "sixty"}

        time_array = t.split(":")
        hour, minute, phase = int(time_array[0]), int(time_array[1]), time_array[2]
        # hour = d[hour]
        # minute = d[minute]

        return _("The time is {0} {1} {2}").format(hour, minute, phase)
        #
        # hour = d[int(t[0:2])] if t[0:2] != "00" else d[12]
        # # suffix = 'a.m.' if d[int(t[7:9])] == hour else 'p.m.'
        # suffix = phase
        #
        # if t[3] == "0":
        #     if t[4] == "0":
        #         minute = ""
        #     else:
        #         minute = d[0] + " " + d[int(t[4])]
        # else:
        #     minute = d[int(t[3]) * 10] + '-' + d[int(t[4])]
        # return 'The time is %s %s %s.' % (hour, minute, suffix)

    @staticmethod
    def date_teller(date):
        return date.strftime("It's %A, %d %B %Y today!")

    @staticmethod
    def phase_of_the_day(time):
        hour = time.hour
        if hour < 12:
            return _('Good Morning')
        elif 12 <= hour < 18:
            return _('Good Afternoon')
        if hour > 6:
            return _('Good Evening')
