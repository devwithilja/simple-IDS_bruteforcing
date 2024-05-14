# simple-IDS_bruteforcing
Hello, this is a simple IDS (Intrusion Detection System) against directory scanning on a Web-Server. 
It is not preventing directory bruteforcing, it limits it to specific amount of requests per second. So the attacker are slowed down with the reconnaisance.

In this scenario there will be an webserver with python as a Flask Application running and you need a tool, like ffuf, on the attacker host to scan directorys with a simple directory list.

The Goal will be writing a simple IDS that 
1. checks the path of each requests and counts requests per IP.
2. Apply a IP Flag to rate limiting or temporarly blocking it from making further requests.
3. create a docker Environment to make it more secure, by reducing the attack surface
