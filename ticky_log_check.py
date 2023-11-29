#!/usr/bin/env python3

import re
import sys
import operator
import csv

errors = {} #dic. for the number of different error messages
error_per_user = {} #dict. to count the number of entries for each user (INFO & ERROR)

def read_logs(): # Add path parameters to make this function work on any input/output file
    """ From log file, using regex pattern, treat data and export error message count into a csv file and a user statistics report in another """
    with open("/home/donsacafq/Module_13_project/syslog.log", "r") as my_file:
        for line in my_file:
            user_error = re.search(r"ticky: ([A-Z]*) ([\w '\[\]#]*) \(([\w.]*)\)", line) # Groups: (error) type, (message) followed by (user)
            if user_error.group(1) == "INFO": # Find messages of type INFO
                if user_error.group(3) in error_per_user:
                    error_line = error_per_user.get(user_error.group(3), 0)
                    temp = error_line[0] + 1
                    temp1 = error_line[1]
                    error_per_user[user_error.group(3)] = [temp,temp1]
                else: 
                    error_per_user[user_error.group(3)] = [1, 0]
            elif user_error.group(1) == "ERROR": # Find messages of type ERROR
                errors[user_error.group(2)] = errors.get(user_error.group(2), 0) + 1 # increment error messages
                if user_error.group(3) in error_per_user:
                    error = error_per_user.get(user_error.group(3))
                    error[1] += 1
                    error_per_user[user_error.group(3)] = error
                else:
                    error_per_user[user_error.group(3)] = [0, 1]
            
        generate_error_report(sorted(errors.items(), key = operator.itemgetter(1), reverse=True)) # errors count
        generate_usage_report(sorted(error_per_user.items(), key = operator.itemgetter(0))) # usage counts

def generate_error_report(errors):
    """ Generate error (not INFO) message report """
    header = ["Error", "Count"]
    with open("/home/donsacafq/Module_13_project/error_message.csv", "w") as my_file:
        writer = csv.DictWriter(my_file, fieldnames=header)
        writer.writeheader()
        for key, value in errors:
            line = ("{},{}".format(key, value))
            my_file.write(line + "\n")
    
def generate_usage_report(error_report):
    """ Generate user statistics report """
    header = ["Username", "INFO", "ERROR"]
    with open("/home/donsacafq/Module_13_project/user_statistics.csv", "w") as my_file:
        writer = csv.DictWriter(my_file, fieldnames=header)
        writer.writeheader()
        for key, value in error_report:
            line = ("{},{},{}".format(key, value[0], value[1]))
            my_file.write(line + "\n")
    
if __name__ == '__main__':
    read_logs()
