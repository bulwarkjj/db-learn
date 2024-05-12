import pandas as df
import os


path = ""

for dir in os.listdir(os.getcwd()):
    if dir == "data-store":
        path = f"/home/adam/git/db-learn/data-store/iris/iris.data"
        break


data_frame = df.read_csv(path)

#print(data_frame.loc[[0, 1, 2, 3], "5.1"])


print(data_frame.iloc[:3, :3])



