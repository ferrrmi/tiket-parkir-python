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
NopolEnc = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
NopolEncrypt = int(hash(NopolEnc)) % (10 ** 8)
KodeKunci = int(KodeAcak(2))
NoTiket = str(KodeLokasi) + str(KodeKendaraan) + str(NopolEncrypt)[::-1] + str(KodeKunci)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
PanjangNopol = len(str(NopolEncrypt))

a=("          --- Manless TIKET ---\n")
b=("SELAMAT DATANG DI "+NamaLokasi+"\n")
d=("Jam Masuk: " + current_time+"\n")
e=("Nomor Tiket: "+NoTiket+"\n")
f=("          Kunci kendaraan anda\n")
g=("                  dan\n")
h=("       jagalah barang bawaan anda.\n")
PrintTextTop = str(a+b+d+e)
PrintTextBot = str(f+g+h)
print("--- log system ---")
print("Lokasi: "+NamaLokasi)
print("Jenis Kendaraan: "+JenisKendaraan)
print("Jam Masuk: "+current_time)
print("Nomor Tiket: "+NoTiket)
print("--- ticket detail ---")
print("Nopol Encrypt: "+str(NopolEncrypt)+"\nPanjang Encrypt Nopol: "+str(PanjangNopol)+"\nKode Kunci: "+str(KodeKunci))

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
    background.save("tiket_manless_"+NoTiket+".png")

QrCode()