# Task class
# relies on standard datetime module
from datetime import date, timedelta

class Task:

    def __init__(self, task_name, units_name, units_count, work_periods):
        # task_name and units_name are strings
        # units_count is an integer
        # work_periods is a nested list of date objects [[start1, end1], [start2, end2], ... ]

        self.task_name = task_name
        self.units_name = units_name
        self.units_count = units_count
        self.work_periods = work_periods

    def get_required_rate(self):
        # returns a number respresenting units per day
        return self.units_count / self.get_duration()

    def generate_text(self):
        # Returns a string containing all attributes of an instance
        # in a human-readable format.
        # This string can be used to save to a file

        string_out = 'Task name: {}\n'.format(self.task_name) \
                   + 'Units name: {}\n'.format(self.units_name) \
                   + 'Number of units: {}\n'.format(self.units_count) \
                   + 'Start date: {}.{}.{}\n'.format(self.start_date.year, self.start_date.month, self.start_date.day) \
                   + 'End date: {}.{}.{}\n'.format(self.end_date.year, self.end_date.month, self.end_date.day)

        return string_out

    def save_to_file(self):
        # Takes string generated by generate text and writes to a file called <task_name>.task
        # If no file called <task_name>.task exists, create new one.
        # Otherwise, overwrite <task_name>.task

        file_name = '{}.task'.format(self.task_name)
        text_to_write = self.generate_text()

        try:
            with open(file_name, 'x') as f:
                f.write(text_to_write)
                print('New file created.')
        except FileExistsError:
            with open(file_name, 'w') as f:
                f.write(text_to_write)
                print('Existing file overwritten.')
