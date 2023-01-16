from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

my_contacts = [
    {
        'id': 1,
        'title': 'อุทยานแห่งชาติหมู่เกาะสิมิลัน จังหวัดพังงา',
        'img': "https://img.kapook.com/u/2017/Tanapol/travel/september/ttt/ttt32.jpg",
        'description': '  ดินแดนที่อุดมไปด้วยผืนน้ำทะเลสีฟ้าเทอร์ควอยซ์ มีเกาะหลัก ๆ ทั้งหมด 11 เกาะ ได้แก่ เกาะหูยง (เกาะหนึ่ง), เกาะปายัง (เกาะสอง), เกาะปาหยัน (เกาะสาม), เกาะเมียง (เกาะสี่), เกาะห้า, เกาะหก, เกาะปายู (เกาะเจ็ด), เกาะสิมิลัน (เกาะแปด), เกาะบางู (เกาะเก้า), เกาะตาชัย และเกาะบอน ซึ่งล้วนแต่มีหาดทรายที่สวยงาม พร้อมกับแนวปะการังที่อุดมสมบูรณ์ นักท่องเที่ยวจะได้พบเห็นสัตว์ทะเลที่หลากหลาย นอกจากนี้หมู่เกาะสิมิลันยังมีเส้นทางศึกษาธรรมชาติและจุดชมวิวที่สวยงามตามเกาะต่าง ๆ อีกด้วย ทั้งนี้อุทยานแห่งชาติหมู่เกาะสิมิลัน จะเปิดให้นักท่องเที่ยวเข้าเที่ยวชมตั้งแต่วันที่ 16 ตุลาคม - 15 พฤษภาคม ของทุกปี'
    },
    {
        'id': 2,
        'title': 'อุทยานแห่งชาติหมู่เกาะสุรินทร์ จังหวัดพังงา',
        'img': "https://img.kapook.com/u/2017/Tanapol/travel/september/ttt/ttt5.jpg",
        'description': ' สวรรค์แห่งการดำน้ำที่ใคร ๆ ต่างก็ต้องการมาสัมผัสสักครั้ง เกาะต่าง ๆ เต็มไปด้วยแนวปะการังหลากสีสัน เป็นสถานที่ดำน้ำลึกและน้ำตื้นยอดนิยมของคนทั่วโลก ผืนน้ำทะเลใสสะอาด พร้อมทั้งหาดทรายยังขาวเนียนนุ่ม มองดูโดดเด่นกลางทะเลอันดามัน บอกเลยว่าพลาดไม่ได้ ทั้งนี้อุทยานแห่งชาติหมู่เกาะสุรินทร์จะเปิดให้นักท่องเที่ยวเข้าเที่ยวชมตั้งแต่วันที่ 16 ตุลาคม - 15 พฤษภาคม ของทุกปี'
    },
    {
        'id': 3,
        'title': 'หมู่เกาะพีพี จังหวัดกระบี่',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/z3.jpg",
        'description': 'หมู่เกาะที่เป็นส่วนหนึ่งของอุทยานแห่งชาติหาดนพรัตน์ธารา-หมู่เกาะพีพี โดยมีภาพของเวิ้งอ่าวคู่ อันเป็นสัญลักษณ์ของเกาะพีพี ที่ดึงดูดให้นักท่องเที่ยวทั่วโลกมาเยือนทะเลไทยอย่างมากมาย หาดทรายขาวของทั้งอ่าวต้นไทรและอ่าวโละดาลัม พร้อมทั้งน้ำทะเลใส สร้างความประทับใจให้กับนักท่องเที่ยวตลอดมา อีกทั้งอ่าวมาหยาอันเลื่องชื่อ ซึ่งอยู่ท่ามกลางอ้อมกอดของภูเขาหินปูน จะทำให้คุณจดจำเกาะพีพีไม่มีวันลืม'
    },
    {
        'id': 4,
        'title': 'เกาะหลีเป๊ะ จังหวัดสตูล',
        'img': "https://img.kapook.com/u/2017/Tanapol/travel/september/ttt/ttt13.jpg",
        'description': 'สัมผัสหาดทรายขาวสะอาด น้ำทะเลสีฟ้าครามใส พร้อมทั้งแนวปะการังที่อุดมสมบูรณ์ และยังชุกชุมไปด้วยปลาและสัตว์ทะเลอีกหลากหลายชนิดของเกาะหลีเป๊ะ เรียนรู้วิถีชีวิตชาวอูรักลาโว้ย และร่วมสนุกสนานกับสีสันบนเกาะเล็ก ๆ กลางทะเลอันดามันที่คุณจะไม่มีวันลืม'
    },
    {
        'id': 5,
        'title': 'เกาะตะรุเตา จังหวัดสตูล',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/z7.jpg",
        'description': 'ดินแดนของนักโทษการเมืองในอดีต ที่เล่าขานกันว่าเป็นนรกกลางทะเลอันดามัน ทว่าปัจจุบันกลับกลายเป็นสวรรค์ของผู้รักการเดินทางไปเสียแล้ว เหตุเพราะมีทิวทัศน์ที่งดงาม ผืนน้ำใสสีมรกต ทรัพยากรใต้ท้องทะเลก็ยังคงอุดมสมบูรณ์ อีกทั้งยังมีประติมากรรมธรรมชาติที่ "เกาะไข่" และหาดหินบน "เกาะหินงาม" หรือ "เกาะอาดัง เกาะราวี" ที่มีหาดทรายสีขาวนุ่มเนียนละเอียดลออ รวมไปถึงอีกหลายเกาะ หลายอ่าวที่แสนงดงาม'
    },
    {
        'id': 6,
        'title': 'เกาะกระดาน จังหวัดตรัง',
        'img': "https://img.kapook.com/u/2017/Tanapol/travel/september/ttt/ttt7.jpg",
        'description': 'เพลิดเพลินไปกับหาดทรายขาวสะอาด น้ำทะเลใสแจ๋ว และแนวปะการังที่สวยงาม ท่ามกลางบรรยากาศที่เงียบสงบ เรียนรู้วิถีชีวิตชาวบ้านที่เรียบง่าย และห้ามพลาดการเข้าร่วมงานวิวาห์ใต้สมุทร อันเป็นกิจกรรมที่โด่งดังไปทั่วโลก เกาะกระดาน จังหวัดตรัง จึงเป็นสถานที่ท่องเที่ยวในทะเลตรังที่คุณต้องไม่พลาด'
    },
    {
        'id': 7,
        'title': 'เกาะรอก จังหวัดกระบี่',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/z14.jpg",
        'description': 'เจ้าของฉายาราชินีแห่งอันดามัน ด้วยธรรมชาติทั้งป่าเขาบนเกาะและธรรมชาติใต้ท้องทะเลยังคงมีความอุดมสมบูรณ์อย่างมาก มีหาดทรายขาวสะอาดโดดเด่น น้ำทะเลเป็นสีฟ้าใส สามารถมองเห็นใต้ทะเลได้อย่างชัดเจน อีกทั้งยังมีแนวปะการังหลากสีสัน ที่นี่จึงกลายเป็นจุดดำน้ำยอดนิยมสำหรับคนรักการดำน้ำ'
    },
    {
        'id': 8,
        'title': 'ถ้ำมรกต จังหวัดตรัง',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/z9.jpg",
        'description': 'หรือเรียกอีกชื่อหนึ่งว่า "ถ้ำน้ำ" ตั้งอยู่บริเวณเกาะมุก มีความยาวทั้งหมด 80 เมตร ที่นี่ถือเป็นถ้ำน้ำทะเลที่มีความงดงามตระการตาอย่างมาก จากปากทางเข้าถ้ำซึ่งเป็นโพรงเล็ก ๆ จะเข้า-ออกได้เฉพาะช่วงน้ำลงเท่านั้น ปากถ้ำเป็นโพรงเล็ก ๆ การเข้า-ออกจะต้องลอยคอในน้ำ ลอดถ้ำอันมืดมิดผ่านเส้นทางคดโค้ง ระยะทางจากปากถ้ำเข้าไปประมาณ 80 เมตร เข้าแถวเรียงหนึ่งตามคนนำทาง จับคนข้างหน้าไว้ให้มั่น ไม่งั้นอาจหลงทางได้ เมื่อพ้นปากถ้ำออกมาอีกด้านหนึ่งจะเป็นหายทรายขาวสะอาด น้ำใสน่าเล่น ล้อมรอบด้วยหน้าผาสูงชัน ที่มีท้องฟ้าเป็นหลังคาและผนังแต่งแต้มด้วยลายเขียวของใบไม้'
    },
    {
        'id': 9,
        'title': 'เกาะปันหยี จังหวัดพังงา',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/Untitled-1.jpg",
        'description': 'เกาะกลางทะเลตั้งอยู่ที่บ้านท่าด่าน ตำบลเกาะปันหยี อำเภอเมือง จังหวัดพังงา เป็นหมู่บ้านของชาวมุสลิมกลางน้ำ ซึ่งมีมายาวนานมากกว่า 200 ปี  ชาวบ้านยังคงใช้วิถีชีวิตแบบชาวเลแท้ ๆ ภายในเกาะมีบ้านเรือนของชาวบ้าน ที่สร้างขึ้นจากวัสดุธรรมชาติ มีมัสยิด รวมทั้งสนามฟุตบอลขนาดเล็กของเด็ก ๆ ในหมู่บ้าน นอกจากนักท่องเที่ยวจะได้ชื่นชมวิถีชีวิตอันเรียบง่ายแล้ว ยังจะได้ลิ้มลองอาหารทะเลสดใหม่ อาหารพื้นเมือง พร้อมทั้งเลือกซื้อสินค้าแฮนด์เมดของชาวบ้านอีกด้วย'
    },
    {
        'id': 10,
        'title': 'เกาะพยาม จังหวัดระนอง',
        'img': "https://img.kapook.com/u/2017/sutasinee/09/z13.jpg",
        'description': 'เกาะที่มีขนาดใหญ่รองลงมาจากเกาะช้าง (ระนอง) ตอนกลางของพื้นที่เกาะเป็นป่าไม้และสัตว์ป่านานาชนิด เช่น นก ลิง และหมูป่า ที่นี่ยังมีบ้านพักเอาไว้บริการนักท่องเที่ยวทั้งแบบวิลล่ากลางน้ำ วิวสวย จนได้รับการขนานนามว่าเป็นมัลดีฟส์เมืองไทย เกาะพยามมีหาดใหญ่ ๆ อยู่ 5 หาด มีป่า ต้นไม้ใหญ่ หาดชายเลน สวนยาง และเป็นแหล่งดูนกเงือก พูดได้ว่าเกาะพยามยังเป็นสถานที่ท่องเที่ยวที่มีธรรมชาติค่อนข้างอุดมสมบูรณ์แห่งหนึ่งเลยทีเดียว'
    }
]

def getLastIndex(data, new_index = 0) -> int:
    last_index = data[-1]["id"]
    return last_index + new_index

def replaceStrLen(string, size=24, delete=3, msg="...") -> str:
        letter = [*string] # sub string to list/array char
        if len(letter) <= size: return string
        result = ""
        for i in range(size-delete): result = str(result) + str(letter[i])
        return str(result)+str(msg)
    

@app.context_processor
def get_current_year():
    return {'date': datetime.utcnow()}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html", contacts=my_contacts, replace=replaceStrLen)


@app.route('/contacts/<int:id>/detail')
def contact_detail(id):
    friend = None
    for c in my_contacts:
        if c['id'] == id:
            friend = c 
            break
    return render_template("detail.html", contacts=friend)


@app.route('/contacts/new_contact', methods=['GET','POST'])
def new_contact():
    if request.method == 'POST':
        contact = {'id': getLastIndex(my_contacts, 1), 'title': request.form['title'], 'img': request.form['img'], 'description': request.form['description']}
        my_contacts.append(contact)
        return redirect(url_for('contacts'))
    return render_template('new_contact.html', title='เพิ่มสถานที่ท่องเที่ยว')


@app.route('/contacts/<int:id>/update', methods=['GET','POST'])
def update_contact(id):
    if request.method == 'POST':
        for c in my_contacts:
            if c['id'] == id:
                c['title'], c['img'], c['description'] = request.form['title'], request.form['img'], request.form["description"]
                break
        return redirect(url_for('contacts'))    
    contact = None
    for c in my_contacts:
        if c['id'] == id:
            contact = c
            break
    return render_template('update_contact.html', contact=contact, title='Update Tourist attraction')


@app.route('/contacts/<int:id>/delete', methods=["GET", "POST"])
def delete_contact(id):
    for c in my_contacts:
        if c["id"] == id:
            my_contacts.remove(c)
            break
    return redirect(url_for("contacts"))


@app.route('/contacts/search', methods=["POST"])
def search_contact():
    search = request.form["search"]
    friend = []
    for c in my_contacts:
        if search.lower() in c["title"].lower():
            friend.append(c)
    return render_template('contacts.html', contacts = friend, replace=replaceStrLen)

if __name__== '__main__':
    app.run(debug=True)
