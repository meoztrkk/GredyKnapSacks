
import pandas as pd 
import time
dist_bin=pd.read_csv("Dist_yuzbin.csv").columns
kar_bin=pd.read_csv("Kar_yuzbin.csv").columns

dist_bin= list(map(float, dist_bin))[:3000]
kar_bin= list(map(float, kar_bin))[:3000]
 
keep_dist_=0
for index, value in enumerate(dist_bin):
    keep_dist_= keep_dist_ + value 
    dist_bin[index]=keep_dist_
print(dist_bin) 

class find_greedy_solution(object):
    def greedy(self, X, dist_bin, kar_bin): 
        max_kar={'kar': 0, 'istasyonlar':list }
        temp_dist= dist_bin[0]
        for index in range(len(dist_bin)-1): 
            if(temp_dist>=X):
                max_kar['kar']= max_kar['kar']+kar_bin[index] 
                temp_dist= dist_bin[index+1]-dist_bin[index]
            else:
                temp_dist= temp_dist+ dist_bin[index+1]-dist_bin[index]
 
            
ob1 = find_greedy_solution()
print("\n") 
 
print("hadi")
time_list = []
for x in range(1,5):
	start = 0
	end = 0
	dist_dene= dist_bin[:x]
	kar_dene= kar_bin[:x]
	start = time.time()   
	ob1.greedy(1000, dist_bin,kar_bin); 
	end = time.time()
	time_list.append(end-start)
 
print("\n timer: ",time_list)