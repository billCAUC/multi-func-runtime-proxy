import json

container_num  =10
res_list = []
with open("./run",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
print(load_dict["time"])    
res0 = load_dict["time"]
res_list.append(res0)

for i in range(1,container_num):
    file_name = "./run."+str(i)
    with open(file_name,'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    res_list.append(load_dict["time"])
    
    
print(res_list)
mean_res = sum(res_list)/len(res_list)
print(mean_res)
filename='result.json'
with open(filename,'w') as file_obj:
    json.dump(res_list,file_obj)
    json.dump(mean_res,file_obj)
    
