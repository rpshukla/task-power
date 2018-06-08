# Task class
# relies on standard datetime module
from datetime import date, timedelta

class Task:

    def __init__(self, task_name, units_name, units_count, starty, startm, startd, endy, endm, endd):

        self.task_name = task_name
        self.units_name = units_name
        self.units_count = units_count
        self.startdate = date(starty, startm, startd) # convert to a datetime.date object
        self.enddate = date(endy, endm, endd)

    def get_duration(self):
        # returns duration in days
        duration_delta = self.enddate - self.startdate # datetime.delta object
        return duration_delta.days

    def get_required_rate(self):
        # returns a number respresenting units per day
        return self.units_count / self.get_duration()

    def generate_text(self):
        # Returns a string containing all attributes of an instance
        # in a human-readable format.
        # This string can be used to save to a file

        string_out = 'Task name:  {}\n'.format(self.task_name) \
                   + 'Units name: {}\n'.format(self.units_name) \
                   + 'Number of units: {}\n'.format(self.units_count) \
                   + 'Start date: {}.{}.{}\n'.format(self.startdate.year, self.startdate.month, self.startdate.day) \
                   + 'End date: {}.{}.{}\n'.format(self.enddate.year, self.enddate.month, self.enddate.day) \

        return string_out

    def save_to_file(self):
        # Takes string generated by generate text and writes to a file called <task_name>.task
        # TODO: if no file called <task_name>.task exists, create new one

        file_name = '{}.task'.format(self.task_name)
        text_to_write = self.generate_text()

        with open(file_name, 'x') as f:
            f.write(text_to_write)
