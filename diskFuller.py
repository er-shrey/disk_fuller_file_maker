f = open('newfile',"wb") #newFile is the filename
f.seek(1048576) #1 MB of file‬
f.write(b"\0")
f.close()
import os
os.stat("newfile").st_size
