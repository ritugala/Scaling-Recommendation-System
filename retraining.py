from movies.model_selection import models_train
from DataCleaning.rate_preprocess import getRatingDf
from DataStreaming.kafkaPipe import getRateData
from subprocess import Popen, PIPE

import os
import timeit

p1 = Popen(['lsof', f'-ti:9092'], stdout=PIPE)
output = p1.communicate()[0]
if not output.decode():
	os.system("sshpass -p seaitunnel ssh -o ServerAliveInterval=60 -L 9092:localhost:9092 tunnel@128.2.204.215 -NTf")
    
print("###########Getting Rate Data...########")
starttime = timeit.default_timer()
getRateData(1)
print("get rate data took: ", timeit.default_timer()-starttime)

print("Cleaning Rate data.....")
starttime = timeit.default_timer()
df = getRatingDf()
print("cleaningn data took: ", timeit.default_timer()-starttime)


print("Training model....")
starttime = timeit.default_timer()
models_train(df)
print("Trainign model took: ", timeit.default_timer()-starttime)
print("Model trained!!")

