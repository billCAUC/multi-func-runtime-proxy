import json

exp_num  =10
docker_num = 3
base_num = 3
res_list=[]
for j in range(base_num,exp_num+base_num):
    file_name = "./run."+str(j)
    print(file_name)
    print("\n")
    with open(file_name,'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    res_list.append(load_dict["time"])
    
for j in range(1,docker_num):
    for i in range(base_num,exp_num+base_num):
        file_name = "./run."+str(i)+"."+str(j)
        print(file_name)
        print("\n")    
        with open(file_name,'r') as load_f:
            load_dict = json.load(load_f)
            print(load_dict)
        res_list.append(load_dict["time"])
    
    
print(res_list[0:exp_num])
mean_res = sum(res_list)/len(res_list)
mean_res1 = sum(res_list[0:exp_num])/exp_num
mean_res2 = sum(res_list[exp_num:2*exp_num])/exp_num
mean_res3 = sum(res_list[2*exp_num:3*exp_num])/exp_num
print("~~~~~~~~~~~~~~~~``",exp_num)
print("mean_res1: ", mean_res1)
print("mean_res2: ", mean_res2)
print("mean_res3: ", mean_res3)
print("mean_res: ", mean_res)
filename='result.json'
with open(filename,'w') as file_obj:
    json.dump(res_list,file_obj)
    json.dump(mean_res,file_obj)
    
