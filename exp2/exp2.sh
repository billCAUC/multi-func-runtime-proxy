

#docker run -d -p 127.0.0.1:80:8080/tcp --name=bloom_whisker --rm -it --net=host action-python-v3.7:8080
#docker run -d -p 127.0.0.1:80:8081/tcp --name=bloom_whisker2 --rm -it --net=host action-python-v3.7:8081
#docker run -d -p 127.0.0.1:80:8082/tcp --name=bloom_whisker3 --rm -it --net=host action-python-v3.7:8082
#docker run -d -p 127.0.0.1:80:8083/tcp --name=bloom_whisker4 --rm -it --net=host action-python-v3.7:8083
#docker run -d -p 127.0.0.1:80:8084/tcp --name=bloom_whisker5 --rm -it --net=host action-python-v3.7:8084

#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8080/init
#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8081/init
#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8082/init
#wget --post-file=python-fib-init.json --header="Content-Type: application/json" http://localhost:8083/init
#wget --post-file=python-fib-init.json --header="Content-Type: application/json" http://localhost:8084/init


#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8080/run
#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8080/run
#wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8082/run
#wget --post-file=python-fib-run.json --header="Content-Type: application/json" http://localhost:8083/run
#wget --post-file=python-fib-run.json --header="Content-Type: application/json" http://localhost:8084/run


#python3 get_res.py

#rm run*
#rm init*

for((i=1;i<=10;i++));  
do   
wget --post-file=hello3.json --header="Content-Type: application/json" http://localhost:8080/run
done 
python3 get_res.py
