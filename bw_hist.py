import time
import json
import subprocess

#Run Speedtest-cli and get output in JSON format
time.sleep(30)
process = subprocess.Popen(["speedtest-cli", "--json"], stdout=subprocess.PIPE)
out, err = process.communicate()
print(out)


time.sleep(10)
#Format JSON in Python format
data = json.loads(out)
#Write file
with open('/var/www/html/bw.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()
