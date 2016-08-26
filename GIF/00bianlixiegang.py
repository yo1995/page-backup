import os
 
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList

path = os.getcwd()
print path
l = len(path)
list = GetFileList(path, [])
with open ('result.txt','wb') as result:
    for e in list:
      e = e[l-4:]
      e =  '- image_title: ' + e[5:-4] + '\r\n  image_path: "https://raw.githubusercontent.com/yo1995/page-backup/master' + e +  '"'
      e = e.replace("\\", '/')
      result.write(e + '\r\n')
