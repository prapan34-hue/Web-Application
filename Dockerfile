FROM python:3.10-slim

WORKDIR /app

# คัดลอกไฟล์ทั้งหมด
COPY . .

# ติดตั้ง Flask
RUN pip install --no-cache-dir flask

# เปิดพอร์ต 80
EXPOSE 80

# รันแอป Python
CMD ["python", "app.py"]
