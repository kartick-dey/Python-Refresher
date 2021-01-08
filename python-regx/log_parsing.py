import re
import time
import json 




def parse_logs(file):
    PATTERN = r'(?i)^(?P<field>jobId|jobName|createdAt|startedAt|stoppedAt|status|statusReason|jobDefinition|jobQueue|command|exitCode|reason|vcpus|memory|nodes|logStream|log|s3FolderUrl)\s+:\s+(?P<value>.+)'
    

    with open(file, 'r', encoding='utf-8') as fileReader:
        for line in fileReader:
            match = re.search(PATTERN, line)
            if match:
                print("Match ---->   {} : {}".format(match.group('field'), match.group('value')), type(match.group('field')))




if __name__ == '__main__':

	fileName = 'dashboard.txt'

	start_time = time.time()
	parse_logs(fileName)

	end_time = time.time()

	print("Time to parse the logs : {} second".format(end_time - start_time))