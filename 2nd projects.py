'''import subprocess 

output = subprocess.check_output(
    "netsh wlan show interfaces",
    shell=True
).decode()


print (output)
'''





### youtube video download 

'''from pytube import YOUTUBE

url = input("enter video url:")
yt = YOUTUBE (url)

stream = yt.streams.filter(
    progressive = True,
    file_extension = "mp4"
    ).order_by("resolution").desc().first()



stream.download(output_path="downloads")

print("Download Complete!!")
'''








































































































