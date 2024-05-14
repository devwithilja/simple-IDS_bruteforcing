# simple-IDS_bruteforcing
Hello, this is a simple IDS (Intrusion Detection System) against directory scanning on a Web-Server. 
It is not preventing directory bruteforcing, it limits it to specific amount of requests per second. So the attacker are slowed down with the reconnaisance.

In this scenario there will be an webserver with python as a Flask Application running and you need a tool, like ffuf, on the attacker host to scan directorys with a simple directory list.

The Goal will be writing a simple IDS that 
1. checks the path of each requests and counts requests per IP.
2. Apply a IP Flag to rate limiting or temporarly blocking it from making further requests.
3. (TO-DO) create a docker Environment to make it more secure, by reducing the attack surface

#Installing the Flask application
1. Decide if you want to run it on your host machine or Virtual machine, or in a docker environment.
2. On a Linux system in this case Debian use a terminal to update, install git and clone the repository `apt-get update && apt-get install git python3-pip python3-full -y`
	`git clone https://github.com/devwithilja/simple-IDS_bruteforcing.git`
3. In the subdirectory "Web_IDS" are several versions of the written IDS, You can see the progress how it was step by step developed.
	Use the last version of it. Before executing it, read what the file should be doing and install the requirements for this project.
	And you need to create a virtual environment with python to use the requirement installation file. `python -m venv /your-directory-for-the-project/`	
	After creating you can see some files inside, we need the file "activate" in the directory "bin". Use `source ./bin/activate`
	if you are in the current directory or else the whole or relative path.
	After entering the python environment , that is indicated in the beginning of the terminal row like "(simple-IDS-bruteforcing)"
	we can install the needed requiremnt, with `pip3 install -r Web_IDS/requirements.txt` if oyu are inside the cloned github repo.
	!Note, the installed requirements Flask and Flask-Limiter, are only accessable inside this python environment. So activate it every time
	if you want to use it "activate /your-path-for-the-project/bin/activate"

	!Note, if you are running already a service on port 80, you can deactivate the service or just change the port in the flask app.
	You would be looking for the  last line or search "app.run(host='0.0.0.0', port=80)", I would search for "port=" to find it.
4. Now you access the application via browser on your machine, where you project is hosted. To perform the attacks read the Readme inside
	of the directory "Hacker_Attack".
