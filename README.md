# Suriyon Python

สวัสดีเพื่อนโหลดโปรเจคของเราและทำตาม SetUp ด้านล้างได้เลย

SETUP
-----
```shell
py -pythonversion -m venv myenv
myenv\Scripts\activate
```
เพื่อสร้างและเรียกใช้ที่เก็บสภาพแวดล้อมของโปรเจค
และใช้คำสั่ง
```shell
pip install -r requirements.txt
```
เพื่อติดตั้ง lib, module ต่างๆแ ของโปรเจค  

HOW TO
------
function สำหรับหาค่า ID ล่าสุดสำหรับทำ Generate ID
```python
def getLastIndex(data, new_index = 0) -> int:
    last_index = data[-1]["id"]
    return last_index + new_index
```
