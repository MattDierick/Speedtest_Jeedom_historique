This python script is used on Jeedom to generate speedtest traffic and populate the Database.

Install process :

	- Copy script in /var/www/html/plugins/script/core/ressources/bw_hist.py
	- Go to Plugins Script and create 2 new script
		- Script Start Test
			- Add a new command with Action
			- Select the script

		- Script Read Results
			- Add 3 new commands (Download, Upload, Ping)
			- For each, select JSON, type Info, numerique
			- In Request write (download, upload or ping)
			- In options : http://<Jeedom_IP_Address>/bw.json

Run it :

	- Create a new scenario
		- Progammed, select your crontab choice (every hour for instance)
		- Create a new action that starts both scripts

