#ให้ทำโปรแกรมป้อนจำนวนเงิน และจำนวนคนทางแป้นพิมพ์ และแสดงผลออกมาว่า
#จำนวนเงิน ??? บาท จำนวนคน ??? คน ต้องหารกันคนละ ??? บาท
#ให้แสดงผลโดยใช้ print ทั้ง 5 แบบ
money = input('ป้อนจำนวนเงิน : ')
person = input('ป้อนจำนวนคน : ')
print('---------------------------------')
print(f'จำนวนเงิน {float(money):.2f} บาท จำนวนคน {person} คน ต้องหารกันคนละ {(float(money)/int(person)):.2f} บาท')
print() #,
print(f'จำนวนเงิน',f'{float(money):,.2f}','บาท','จำนวนคน',person, 'คน','ต้องหารกันคนละ',f'{float(money)/int(person):,.2f}','บาท')
print() #+
print(f'จำนวนเงิน ' +f'{float(money):,.2f}'+ ' บาท ' 'จำนวนคน ' +person+ ' คน' ' ต้องหารกันคนละ ' +f'{float(money)/int(person):,.2f}'+ ' บาท')
print() #.format
print('จำนวนเงิน {:.2f} บาท จำนวนคน {} คน ต้องหารกันคนละ {:.2f} บาท'.format(float(money),person,(float(money)/int(person))))
print() #%
print('จำนวนเงิน %.2f บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f บาท'%(float(money),person,float(money)/int(person)))