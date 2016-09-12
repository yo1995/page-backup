cd 'C:/Program Files/Git/usr/yo1995.github.io/photos/page-backup'

git add .
git commit -m "上传照片 $(date +%Y%m%d)"
git push
read -p "部署完毕，任意键退出！" qu