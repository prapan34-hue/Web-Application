# My Web App

เว็บแอปพลิเคชันแบบง่ายที่แสดงข้อมูลส่วนตัวและงานวิจัยผ่าน 3 หน้า:

- หน้าแรก: แสดงชื่อและ ID
- About: แสดงข้อมูลเกี่ยวกับตัวเอง
- My Research: แสดงรายละเอียดงานวิจัยที่สนใจ

## โครงสร้างโปรเจกต์

```text
my-web-app/
├── public/
│   └── css/
│       └── style.css
├── views/
│   ├── index.ejs
│   ├── about.ejs
│   └── myresearch.ejs
├── app.js
├── package.json
├── Dockerfile
└── docker-compose.yml
```

## ข้อกำหนดเบื้องต้น

- Node.js
- npm
- Docker และ Docker Compose (ถ้าต้องการรันด้วยคอนเทนเนอร์)

## การติดตั้ง

```bash
npm install
```

## วิธีรันโปรเจกต์

### รันด้วย Node.js

```bash
node app.js
```

เปิดเบราว์เซอร์ที่:

```text
http://localhost:3000
```

### รันด้วย Docker Compose

```bash
docker-compose up --build
```

เปิดเบราว์เซอร์ที่:

```text
http://localhost:3000
```

## ข้อมูลเพิ่มเติม

โปรเจกต์นี้ถูกออกแบบให้เป็นตัวอย่างเว็บแอปที่มีหน้าเว็บหลายหน้าและสามารถขยายฟีเจอร์ได้ในอนาคต
