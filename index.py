import datetime
file=open("index.txt","a+")
file.write("\n"+str(datetime.datetime.now()))