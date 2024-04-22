# simple-IDS_bruteforcing
Hello, this is a simple IDS (Intrusion Detection System) against directory scanning on a Web-Server. 

In this scenario there will be an webserver (NGIX) running and you need a tool on the attacker host to scan directorys with a simple directory list.

The Goal will be writing a simple IDS that 
1. checks the path of each requests and counts requests per IP.
2. Apply a IP Flag to rate limiting or temporarly blocking it from making further requests.
