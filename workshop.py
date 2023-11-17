import os
def inputdata():
    stuname = input('ป้อนชื่อ-นามสกุลนักเรียน:')
    mid = input('ป้อนคะแนนกลางภาค:')
    final = input('ป้อนคะแนนปลายภาค:')
    score = input('ป้อนคะแนนรวม:')
    return stuname,mid,final,score

def checkpassinggrad(mid,final,score):
    result = int(mid) + int(final) + int(score)
    return result

def cresubject():
    print('สร้างไฟล์วิชาใหม่')
    subjectname = input('ป้อนชื่อวิชาเพื่อเก็บข้อมูล(ez.txt):').strip()
    if not '.txt' in subjectname :
        print('ไม่ใช่ .txt โปรดลองใหม่')
    elif '.txt' in subjectname:
        filename = open(subjectname,'w',encoding='utf-8')
        stuname,mid,final,score = inputdata()
        result = checkpassinggrad(mid,final,score)
        if result >= 50:
            filename.write(f'กรุณาใส่ชื่อ{stuname}\nกรุณาใส่คะแนนกลางภาค{mid}\nกรุณาใส่คะแนนปลายภาค{final}\n{result}คุณผ่าน')
            filename.close()
        else:
            filename.write(f'กรุณาใส่ชื่อ{stuname}\nกรุณาใส่คะแนนกลางภาค{mid}\nกรุณาใส่คะแนนปลายภาค{final}\n{result}คุณไม่ผ่าน')
            filename.close()
    
def search():
    fileexplorer = os.listdir
    if not fileexplorer:
        print('ไม่พบไฟล์')
    else:
        for showfile in fileexplorer:
            if showfile.endswith('.txt'):
                print(showfile)
        selcectfile = input('เลือกไฟล์')
        if selcectfile not in fileexplorer:
            print('พิมพ์ชื่อไฟล์ผิด')
        else:
            filename = open(selcectfile,'a',encoding='utf-8')
            stuname,mid,final,score = inputdata()
            result = checkpassinggrad(mid,final,score)
            if result >= 50:
                filename.write(f'กรุณาใส่ชื่อ{stuname}\nกรุณาใส่คะแนนกลางภาค{mid}\nกรุณาใส่คะแนนปลายภาค{final}\n{result}คุณผ่าน')
                filename.close()
            else:
                filename.write(f'กรุณาใส่ชื่อ{stuname}\nกรุณาใส่คะแนนกลางภาค{mid}\nกรุณาใส่คะแนนปลายภาค{final}\n{result}คุณไม่ผ่าน')
                filename.close()

def read():
    fileexplorer = os.listdir()
    if not fileexplorer:
        print('ไม่พบไฟล์')
    else:
        for showfile in fileexplorer:
            if showfile.endswith('.txt'):
                print(showfile)
        selectfile = input('เลือกไฟล์')
        if selectfile not in fileexplorer:
            print('พิมพ์ชื่อไฟล์ผิด')
        else:
            data = open(selectfile,'r',encoding='utf-8')
            readdata = data.read()
            print(readdata)

def remove():
    fileexplorer = os.listdir()
    if not fileexplorer:
        print('ไม่พบไฟล์')
    else:
        for showfile in fileexplorer:
            if showfile.endswith('.txt'):
                print(showfile)
        selectfile = input('เลือกไฟล์')
        if selectfile not in fileexplorer:
            print('พิมพ์ชื่อไฟล์ผิด')
        elif selectfile in fileexplorer:
            os.remove(selectfile)
            print('ลบไฟล์เรียบร้อย')

def mainmenu():
    while True:
        print("**********************************************************************")
        print('SCHOOL')
        print("**********************************************************************")
        print('1.สร้างไฟล์วิชา')
        print("**********************************************************************")
        print('2.เลือกวิชาและเพิ่มข้อมูลต่อท้าย')
        print("**********************************************************************")
        print('3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล')
        print("**********************************************************************")
        print('4.เลือกวิชาและลบไฟล์')
        print("**********************************************************************")
        print('0. จบการทํางาน')
        print("**********************************************************************")
        userinput = input('เลือกเมนู')
        if userinput == '1':
            cresubject()
            break
        elif userinput == '2':
            search()
            break
        elif userinput == '3':
            read()
            break
        elif userinput == '4':
            remove()
            break
        elif userinput == '0':
            print('จบ')
            break
        else:
            print('กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0')
            break
mainmenu()