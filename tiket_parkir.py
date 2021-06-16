import hashlib
import qrcode
from random import randint
from datetime import datetime

print("========== Konvensional Pos Masuk ===============")
KodeLokasi = str(input("input Kode Lokasi: "))
if len(KodeLokasi) > 2:
    print("Kode Lokasi terlalu panjang")
    exit()
Nopol = str(input("input Nopol: "))
if len(Nopol) > 8:
    print("Nopol Terlalu Panjang")
    exit()
def KodeAcak(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
NopolEnc = int(hashlib.sha256(Nopol.encode('utf-8')).hexdigest(), 16) % 10**8
KodeKunci = int(KodeAcak(2))
NoTiket = str(KodeLokasi) + str(NopolEnc)[::-1] + str(KodeKunci)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

a=("          === TIKET PARKIR ===\n")
b=("          SELAMAT DATANG DI "+KodeLokasi+"\n")
c=("Nomor Plat: " + Nopol+"\n")
d=("Jam Masuk: " + current_time+"\n")
e=("Nomor Tiket: " + NoTiket+"\n")
f=("          Kunci kendaraan anda\n")
g=("                   dan\n")
h=("       jagalah barang bawaan anda.\n")
PrintTextTop = str(a+b+c+d+e)
PrintTextBot = str(f+g+h)

def QrCode():
    from PIL import Image
    background = Image.new('RGBA', (250, 280), (255,255,255,255))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(background)
    draw.text((5,5), PrintTextTop, (0,0,0))
    draw.text((5,230), PrintTextBot, (0,0,0))
    # Link for website
    input_data = NoTiket
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    background.paste(img,(50,80))
    background.save('tiket.png')

QrCode()