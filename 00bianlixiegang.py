from PIL import Image
import os
import os.path  
import sys
 
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

# path = os.getcwd()
fname = raw_input("Please input the dir: (example: awards cannot process GIF!)\n")
path = 'C:\Program Files\Git\usr\yo1995.github.io\photos\page-backup\\' +  fname
lcur = len(fname) + 2

small_path = (path[:-1] if path[-1]=='/' else path) + '_m'
print small_path
imgblank = 'templ.jpg'
thumbsize = (600,600)
if not os.path.exists(small_path):  
    os.mkdir(small_path)
for root, dirs, files in os.walk(path):  
    for f in files:  
        fp = os.path.join(root, f)
        img = Image.open(fp)
        imgb = Image.open(imgblank)
        (sizeblankw , sizeblankh)= imgb.size
        savepath = os.path.join(small_path, f)
        if os.path.isfile(savepath + fp[len(savepath)-1:]):
            print u'existing, not writing'
        else :
            img.thumbnail(thumbsize,Image.ANTIALIAS)
            w,h = img.size
            print (w,h)
            wm = (sizeblankw - w) / 2.0 
            hm = (sizeblankh - h) / 2.0 
            box2 = (int(wm) , int(hm) , int(sizeblankw - wm), int(sizeblankh - hm))
            print box2
            imgb.paste(img , box2)
            imgb.save(savepath)
            print 'writing file ' + fp  


reload(sys)  
sys.setdefaultencoding('utf8')
l = len(path)
list = GetFileList(path, [])
with open ('result.txt','wb') as result:
    for e in list:
      e = e[l-lcur+1:]
      e =  '- image_title: ' + e[lcur:-4] \
      + '\r\n  image_path: "https://raw.githubusercontent.com/yo1995/page-backup/master' + e \
      +  '" \r\n  thumb_path: "https://raw.githubusercontent.com/yo1995/page-backup/master' + e[:lcur-1] + '_m/'+ e[lcur:] + '"'
      e = e.replace("\\", '/')
      
      result.write(e + '\r\n')

raw_input('finished ! press any key to exit')
