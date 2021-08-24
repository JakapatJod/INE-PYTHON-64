number = 0
def main():
    global number #เรียกใช้ตัวแปรนอกฟังก์ชันที่ชื่อว่า number ถ้าลบออกไปจะกลาย 0 ทันที
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is',number)

main()