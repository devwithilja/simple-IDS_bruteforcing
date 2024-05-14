As the Attacker you can use ffuf with a wordlist.

After installing ffuf (Fuzz Faster U Fool) you can use the delivered wordlist "common_extra.txt"

There are some files included from this project, so you should be able to get some hits. Make sure while performing the scan attack,
adding the /files/ as a directory after the ip:port, because this is how the flask app is written to deliver content from the 
flask apps root directory.

Some examples oyu can find in "attack.cmd" there you have maybe to change your ip address to your local network, depending on 
which ip address the flask application is running. 

!warning 
Don't forget how the network works if you setting this in a VM, cause you need a bridge network device, to access your VM from
your host machine.
