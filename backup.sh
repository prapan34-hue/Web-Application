#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/home/ubuntu/backups"
SOURCE_DIR="/home/ubuntu/my-web-app" # หรือโฟลเดอร์ไฟล์เว็บ/ฐานข้อมูลที่ต้องการสำรอง
S3_BUCKET="s3://my-webapp-backup-bucket-6501234567"

mkdir -p $BACKUP_DIR
ZIP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# อัดไฟล์เว็บ
tar -czf $ZIP_FILE $SOURCE_DIR

# อัปโหลดขึ้น S3
aws s3 cp $ZIP_FILE $S3_BUCKET/

# ลบไฟล์สำรองบนเครื่อง local ที่เก่ากว่า 7 วันเพื่อประหยัดดิสก์
find $BACKUP_DIR -type f -mtime +7 -exec rm {} \;
