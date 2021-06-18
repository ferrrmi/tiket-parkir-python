import random, string
import qrcode
from random import randint
from datetime import datetime

print("========== Manless Pos Masuk ===============")
NamaLokasi = str(input("input Nama Lokasi: "))
JenisKendaraan = str(input("Input Jenis Kendaraan: "))
if JenisKendaraan == "MOBIL":
    KodeKendaraan = "C"
elif JenisKendaraan == "MOTOR":
    KodeKendaraan = "M"
else:
    print("Kendaraan tidak terdaftar!")
    exit()
KodeLokasi = str(input("input Kode Lokasi: "))
if len(KodeLokasi) > 2:
    print("Kode Lokasi terlalu panjang")
    exit()
def KodeTiket(n):
    range_awal = 10**(n-1)
    range_akhir = (10**n)-1
    return randint(range_awal, range_akhir)
Nopol = str(KodeTiket(7))
def KodeAcak(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
NopolEnc = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
NopolEncrypt = int(hash(NopolEnc)) % (10 ** 7)
NopolEncrypt = str(KodeKendaraan) + str(NopolEncrypt)
KodeKunci = int(KodeAcak(2))
NoTiket = str(KodeLokasi) + str(NopolEncrypt) + str(KodeKunci)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
PanjangNopol = len(str(NopolEncrypt))

a=("TIKET PARKIR\n")
b=("SELAMAT DATANG DI "+NamaLokasi+"\n")
d=("JAM MASUK   : " + current_time+"\n")
e=("NOMOR TIKET : "+NoTiket+"\n")
f=("KUNCI KENDARAAN ANDA\n")
g=("DAN\n")
h=("JAGALAH BARANG BAWAAAN ANDA\n")
ver=("PM Manless V.1.0")
PrintTextTop = str(d+e)
print("--- log system ---")
print("Nama Lokasi: "+NamaLokasi)
print("Kode Lokasi: "+KodeLokasi)
print("Jenis Kendaraan: "+JenisKendaraan)
print("Jam Masuk: "+current_time)
print("Nomor Tiket: "+NoTiket)
print("--- ticket detail ---")
print("Nopol Encrypt: "+str(NopolEncrypt)+"\nPanjang Encrypt Nopol: "+str(PanjangNopol)+"\nKode Kunci: "+str(KodeKunci))

def QrCode():
    from PIL import Image
    W, H = (250,280)
    background = Image.new('RGBA', (W, H), (255,255,255,255))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(background)
    w = draw.textsize(a)[0]
    x = draw.textsize(b)[0]
    bot_1 = draw.textsize(f)[0]
    bot_2 = draw.textsize(g)[0]
    bot_3 = draw.textsize(h)[0]
    bot_4 = draw.textsize(ver)[0]
    draw.text(((W-w)/2,5), a, (0,0,0))
    draw.text(((W-x)/2,20), b, (0,0,0))
    draw.text((5,50), PrintTextTop, (0,0,0))
    draw.text(((W-bot_1)/2,225), f, (0,0,0))
    draw.text(((W-bot_2)/2,235), g, (0,0,0))
    draw.text(((W-bot_3)/2,245), h, (0,0,0))
    draw.text(((W-bot_4)/2,265), ver, (0,0,0))
    # Link for website
    input_data = NoTiket
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=1)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    center = int(66.5)
    background.paste(img,(center,93))
    background.save("tiket_manless_"+NoTiket+".png")

QrCode()