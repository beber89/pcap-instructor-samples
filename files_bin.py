from os import strerror

srcname = input("Source file name?: ")

src = open(srcname, 'rb')
	
dstname = input("Destination file name?: ")

dst = open(dstname, 'wb')
	

buffer = bytearray(65536)

readin = src.readinto(buffer)
while readin > 0:
    written = dst.write(buffer[:readin])
    readin = src.readinto(buffer)
	
    
src.close()
dst.close()
