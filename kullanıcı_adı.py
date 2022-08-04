print(""""**********************Kullanıcı adı ve parola sistemi
********************************""")
sys_kullanici = "mmustafa"
sys_parola = "123456"

giris_hakki = 3

while True:
    kullanici_adi = input("lütfen kullanici adı giriniz")
    parola = input("lütfen kullanıcı parolası giriniz")
    if (sys_kullanici!= kullanici_adi and sys_parola == parola):
        print("kullanıcı adı hatalı")
        giris_hakki -= 1
    elif (sys_kullanici == kullanici_adi and sys_parola != parola):
        print("hatalı parola")
        giris_hakki -= 1
    elif(sys_kullanici!=parola and sys_parola != parola):
        print("kullanıcı adı ve parola yanlış")
        giris_hakki-=1
    else:
        print("kullanıcı adı ve parola dogru")
        break
    if(giris_hakki==0):
        print("kullancı giriş hakkkınız bitti")
        break

