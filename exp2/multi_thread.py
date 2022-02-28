import threading
from datetime import datetime
import os
threads = []
results = []
def client(i):
    print("client %d start",i)
    command = "wget --post-file=hello3.json --header='Content-Type: application/json' http://localhost:"+str(i+8080)+"/run"
    r = os.popen(command)  
    text = r.read()  
    results.append(text)
    print("client %d finished" %i)


def many_thread():

    clientNum = 3
    for i in range(clientNum):
        t = threading.Thread(target=client,args=(i,))
        threads.append(t)
    # start the clients
    for i in range(clientNum):
        print("OK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        threads[i].start()
        

    for i in range(clientNum):
        threads[i].join()
    print(results)
if __name__ == '__main__':
    many_thread()
        
