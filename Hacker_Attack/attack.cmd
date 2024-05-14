ffuf -w common_extra.txt -rate 200 -recursion -u http://192.168.178.31:80/FUZZ -o ffuf_recursion_IDS.csv -of csv
ffuf -ac -mc 429,200 -w common_extra.txt -rate 1 -p 1 -recursion -u http://127.0.0.1:80/files/FUZZ -o ffuf_recursion_IDS.csv -of csv
#with -rate 1(1 request per second) and -p 2(2 second pause after request) and -t 1(using only 1 thread), we get a 1 request every 2 seconds
