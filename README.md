# module_13_project
Script that goes through log file, checks for specific pattern, manipulates the data to export 2 csv reports.
read_logs(): Reads the logs from a syslog.log, using a regex pattern, identifies specific parts of each log line and stores them in two dictionaries. Calls following functions to export to two different reports:
- generate_error_report(): Generate csv report of descending order count of unique errors (not INFO).
- generate_usage_report(): Generate user statistics csv report (INFO/ERROR per user, user in alphanumeric order).
