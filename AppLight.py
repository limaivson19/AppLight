from tkinter import *
import serial
import threading
import requests
from bs4 import BeautifulSoup

ser = serial.Serial('COM9', 9600, timeout=1)


def home_page():
    def luz():
        home.destroy()
        luz_func()

    def fan():
        home.destroy()
        fan_func()

    def rgb():
        home.destroy()
        rgb_func()

    def info():
        home.destroy()
        info_func()

    def ajustes():
        home.destroy()
        ajustes_func()

    def sair():
        home.destroy()

    home = Tk()
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.82)
    home.geometry(f'600x524+{int(x)}+{int(y)}')
    home.title("Light App")
    home.iconbitmap('imgs/icon/favicon.ico')
    home.configure(bg="#240b35")
    canvas = Canvas(
        home,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"imgs/hp_img/background.png")
    canvas.create_image(
        48.5, 262.0,
        image=background_img)

    img0 = PhotoImage(file=f"imgs/hp_img/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        bg="#a91333",
        activebackground="#a91333",
        highlightthickness=0,
        relief="flat")

    b0.place(
        x=0, y=7,
        width=121,
        height=60)

    img1 = PhotoImage(file=f"imgs/hp_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#a01232",
        command=luz,
        relief="flat")

    b1.place(
        x=0, y=81,
        width=121,
        height=60)

    img2 = PhotoImage(file=f"imgs/hp_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#911133",
        command=fan,
        relief="flat")

    b2.place(
        x=0, y=153,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/hp_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#821033",
        command=rgb,
        relief="flat")

    b3.place(
        x=0, y=229,
        width=121,
        height=60)

    img4 = PhotoImage(file=f"imgs/hp_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#720f34",
        command=info,
        relief="flat")

    b4.place(
        x=0, y=303,
        width=121,
        height=62)

    img5 = PhotoImage(file=f"imgs/hp_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#660e34",
        command=ajustes,
        relief="flat")

    b5.place(
        x=0, y=379,
        width=121,
        height=60)

    img6 = PhotoImage(file=f"imgs/hp_img/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        bg="#a91333",
        activebackground="#570e34",
        command=sair,
        relief="flat")

    b6.place(
        x=0, y=453,
        width=121,
        height=60)

    home.resizable(False, False)
    home.mainloop()


def luz_func():
    luz_page = Tk()
    # ==================================================
    screen_width = luz_page.winfo_screenwidth()
    screen_height = luz_page.winfo_screenheight()
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.85)
    luz_page.geometry(f'600x524+{int(x)}+{int(y)}')
    luz_page.title("Light App")
    luz_page.iconbitmap('imgs/icon/favicon.ico')
    luz_page.configure(bg="#240b35")
    canvas = Canvas(
        luz_page,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    def btn_sair():
        luz_page.destroy()

    def btn_ajustes():
        luz_page.destroy()
        ajustes_func()

    def btn_info():
        luz_page.destroy()
        info_func()

    def btn_rbg():
        luz_page.destroy()
        rgb_func()

    def btn_fan():
        luz_page.destroy()
        fan_func()

    def btn_voltar():
        luz_page.destroy()
        home_page()

    def btn_100():
        ser.write(b'b')
        ser.write(b'1')

    def btn_50():
        ser.write(b'b')
        ser.write(b'5')

    def btn_25():
        ser.write(b'b')
        ser.write(b'2')

    def btn_0():
        ser.write(b'0')

    def btn_desligar():
        pass

    def btn_ligar():
        pass

    background_img = PhotoImage(file=f"imgs/luz_img/background.png")
    canvas.create_image(
        218.0, 262.0,
        image=background_img)

    img0 = PhotoImage(file=f"imgs/luz_img/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        bg="#ad1332",
        activebackground="#ad1332",
        command=btn_voltar,
        relief="flat")

    b0.place(
        x=0, y=11,
        width=121,
        height=60)

    img1 = PhotoImage(file=f"imgs/luz_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#901133",
        command=btn_fan,
        relief="flat")

    b1.place(
        x=-1, y=155,
        width=119,
        height=60)

    img2 = PhotoImage(file=f"imgs/luz_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#831033",
        command=btn_rbg,
        relief="flat")

    b2.place(
        x=0, y=229,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/luz_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#720f34",
        command=btn_info,
        relief="flat")

    b3.place(
        x=0, y=303,
        width=121,
        height=62)

    img4 = PhotoImage(file=f"imgs/luz_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#650e34",
        command=btn_ajustes,
        relief="flat")

    b4.place(
        x=0, y=379,
        width=121,
        height=60)

    img5 = PhotoImage(file=f"imgs/luz_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#570e34",
        command=btn_sair,
        relief="flat")

    b5.place(
        x=-2, y=453,
        width=121,
        height=60)

    img6 = PhotoImage(file=f"imgs/luz_img/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_100,
        relief="flat")

    b6.place(
        x=432, y=174,
        width=97,
        height=41)

    img7 = PhotoImage(file=f"imgs/luz_img/img7.png")
    b7 = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_50,
        relief="flat")

    b7.place(
        x=344, y=174,
        width=78,
        height=41)

    img8 = PhotoImage(file=f"imgs/luz_img/img8.png")
    b8 = Button(
        image=img8,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_25,
        relief="flat")

    b8.place(
        x=260, y=174,
        width=77,
        height=41)

    img9 = PhotoImage(file=f"imgs/luz_img/img9.png")
    b9 = Button(
        image=img9,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_0,
        relief="flat")

    b9.place(
        x=192, y=174,
        width=60,
        height=41)

    img10 = PhotoImage(file=f"imgs/luz_img/img10.png")
    b10 = Button(
        image=img10,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_desligar,
        relief="flat")

    b10.place(
        x=192, y=420,
        width=149,
        height=41)

    img11 = PhotoImage(file=f"imgs/luz_img/img11.png")
    b11 = Button(
        image=img11,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_ligar,
        relief="flat")

    b11.place(
        x=432, y=420,
        width=97,
        height=41)

    luz_page.resizable(False, False)
    luz_page.mainloop()


def fan_func():
    def btn_voltar():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()
        home_page()

    def btn_luz():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()
        luz_func()

    def btn_rgb():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()
        rgb_func()

    def btn_ajustes():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()
        ajustes_func()

    def btn_info():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()
        info_func()

    def btn_sair():
        ser.write(b'0')
        ser.readlines()
        fan_page.destroy()

    def btn_ligar():
        print("ligar")

    def btn_desligar():
        print("desligar")

    fan_page = Tk()
    screen_width = fan_page.winfo_screenwidth()
    screen_height = fan_page.winfo_screenheight()

    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.85)

    fan_page.geometry(f'600x524+{int(x)}+{int(y)}')
    fan_page.title("Light App")
    fan_page.iconbitmap('imgs/icon/favicon.ico')
    fan_page.configure(bg="#240b35")
    canvas = Canvas(
        fan_page,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"imgs/fan_img/background.png")
    canvas.create_image(
        225.0, 262.0,
        image=background_img)

    img0 = PhotoImage(file=f"imgs/fan_img/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#ad1332",
        command=btn_voltar,
        relief="flat")

    b0.place(
        x=0, y=11,
        width=121,
        height=60)

    img1 = PhotoImage(file=f"imgs/fan_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#9f1132",
        command=btn_luz,
        relief="flat")

    b1.place(
        x=0, y=81,
        width=121,
        height=60)

    img2 = PhotoImage(file=f"imgs/fan_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#861133",
        command=btn_rgb,
        relief="flat")

    b2.place(
        x=0, y=229,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/fan_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        bg="#670f34",
        activebackground="#670f34",
        command=btn_ajustes,
        relief="flat")

    b3.place(
        x=0, y=371,
        width=121,
        height=60)

    img4 = PhotoImage(file=f"imgs/fan_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#540e34",
        command=btn_sair,
        relief="flat")

    b4.place(
        x=0, y=441,
        width=121,
        height=60)

    img5 = PhotoImage(file=f"imgs/fan_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_ligar,
        relief="flat")

    b5.place(
        x=390, y=120,
        width=97,
        height=39)

    img6 = PhotoImage(file=f"imgs/fan_img/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_desligar,
        relief="flat")

    b6.place(
        x=230, y=119,
        width=100,
        height=39)
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/1606/jaboataodosguararapes-pe'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }

    site = requests.get(url, headers=headers)

    soup = BeautifulSoup(site.content, 'html.parser')

    temperatura = soup.find('span', class_='-bold -gray-dark-2 -font-55 _margin-l-20 _center').get_text()

    soup.find('div',
              class_='no-gutters -gray _flex _justify-center _margin-t-20 _padding-b-20 _border-b-light-1').get_text()

    temp = int(temperatura[0:3])

    def dados():
        if temp >= 30:
            ser.write(b'q')
            ser.readlines()

        elif 20 < temp < 30:
            ser.write(b'm')
            ser.readlines()

        elif temp < 20:
            ser.write(b'f')
            ser.readlines()

    threading.Thread(target=dados).start()

    entry0_img = PhotoImage(file=f"imgs/fan_img/img_textBox0.png")
    canvas.create_image(
        360.0, 290.5,
        image=entry0_img)

    entry0 = Label(text=temperatura,
                   font=('Gill Sans MT', 15),
                   bd=0,
                   bg="#e5e5e5",
                   highlightthickness=0)

    entry0.place(
        x=320.0, y=275,
        width=80.0,
        height=30)

    entry1_img = PhotoImage(file=f"imgs/fan_img/img_textBox1.png")
    canvas.create_image(
        360.0, 443.5,
        image=entry1_img)

    entry1 = Entry(
        bd=0,
        bg="#e5e5e5",
        highlightthickness=0)

    entry1.place(
        x=320.0, y=428,
        width=80.0,
        height=30)

    img7 = PhotoImage(file=f"imgs/fan_img/img7.png")
    b7 = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#740f34",
        command=btn_info,
        relief="flat")

    b7.place(
        x=0, y=299,
        width=121,
        height=62)
    fan_page.resizable(False, False)
    fan_page.mainloop()


def rgb_func():
    rgb = Tk()
    screen_width = rgb.winfo_screenwidth()
    screen_height = rgb.winfo_screenheight()
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.85)

    rgb.geometry(f'600x524+{int(x)}+{int(y)}')
    rgb.title("Light App")
    rgb.iconbitmap('imgs/icon/favicon.ico')
    rgb.geometry("600x524")
    rgb.configure(bg="#240b35")
    canvas = Canvas(
        rgb,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    def btn_voltar():
        rgb.destroy()
        home_page()

    def btn_luz():
        rgb.destroy()
        luz_func()

    def btn_fan():
        rgb.destroy()
        fan_func()

    def btn_info():
        rgb.destroy()
        info_func()

    def btn_ajustes():
        rgb.destroy()
        ajustes_func()

    def btn_sair():
        rgb.destroy()

    def btn_branco():
        ser.write(b'b')
        ser.readlines()

    def btn_vermelho():
        ser.write(b'V')
        ser.readlines()

    def btn_azul():
        ser.write(b'a')
        ser.readlines()

    def btn_verde():
        ser.write(b'v')
        ser.readlines()

    def btn_laranja():
        ser.write(b'l')
        ser.readlines()

    def btn_roxo():
        ser.write(b'r')
        ser.readlines()

    def btn_0():
        ser.write(b'0')
        ser.readlines()

    def btn_25():
        ser.write(b'2')
        ser.readlines()

    def btn_50():
        ser.write(b'5')
        ser.readlines()

    def btn_75():
        ser.write(b'7')
        ser.readlines()

    def btn_100():
        ser.write(b'1')
        ser.readlines()

    def btn_animacao():
        ser.write(b'8')
        ser.readlines()

    background_img = PhotoImage(file=f"imgs/rgb_img/background.png")
    canvas.create_image(
        174.5, 262.0,
        image=background_img)

    img0 = PhotoImage(file=f"imgs/rgb_img/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        bg="#ad1332",
        activebackground="#ad1332",
        command=btn_voltar,
        relief="flat")

    b0.place(
        x=0, y=11,
        width=121,
        height=60)

    img1 = PhotoImage(file=f"imgs/rgb_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        bg="#9e1232",
        activebackground="#9e1232",
        command=btn_luz,
        relief="flat")

    b1.place(
        x=0, y=81,
        width=121,
        height=60)

    img2 = PhotoImage(file=f"imgs/rgb_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        bg="#921133",
        activebackground="#921133",
        command=btn_fan,
        relief="flat")

    b2.place(
        x=0, y=151,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/rgb_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        bg="#720f34",
        activebackground="#720f34",
        command=btn_info,
        relief="flat")

    b3.place(
        x=0, y=303,
        width=121,
        height=62)

    img4 = PhotoImage(file=f"imgs/rgb_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        bg="#650e34",
        activebackground="#650e34",
        command=btn_ajustes,
        relief="flat")

    b4.place(
        x=0, y=377,
        width=121,
        height=60)

    img5 = PhotoImage(file=f"imgs/rgb_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        bg="#570e34",
        activebackground="#570e34",
        command=btn_sair,
        relief="flat")

    b5.place(
        x=0, y=449,
        width=121,
        height=60)

    img6 = PhotoImage(file=f"imgs/rgb_img/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_branco,
        relief="flat")

    b6.place(
        x=231, y=185,
        width=92,
        height=37)

    img7 = PhotoImage(file=f"imgs/rgb_img/img7.png")
    b7 = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_vermelho,
        relief="flat")

    b7.place(
        x=383, y=185,
        width=118,
        height=35)

    img8 = PhotoImage(file=f"imgs/rgb_img/img8.png")
    b8 = Button(
        image=img8,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_azul,
        relief="flat")

    b8.place(
        x=225, y=301,
        width=98,
        height=37)

    img9 = PhotoImage(file=f"imgs/rgb_img/img9.png")
    b9 = Button(
        image=img9,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_verde,
        relief="flat")

    b9.place(
        x=383, y=243,
        width=112,
        height=35)

    img10 = PhotoImage(file=f"imgs/rgb_img/img10.png")
    b10 = Button(
        image=img10,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_laranja,
        relief="flat")

    b10.place(
        x=218, y=243,
        width=105,
        height=37)

    img11 = PhotoImage(file=f"imgs/rgb_img/img11.png")
    b11 = Button(
        image=img11,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_roxo,
        relief="flat")

    b11.place(
        x=383, y=303,
        width=111,
        height=35)

    img12 = PhotoImage(file=f"imgs/rgb_img/img12.png")
    b12 = Button(
        image=img12,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_0,
        relief="flat")

    b12.place(
        x=140, y=396,
        width=60,
        height=41)

    img13 = PhotoImage(file=f"imgs/rgb_img/img13.png")
    b13 = Button(
        image=img13,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_25,
        relief="flat")

    b13.place(
        x=212, y=396,
        width=77,
        height=41)

    img14 = PhotoImage(file=f"imgs/rgb_img/img14.png")
    b14 = Button(
        image=img14,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_50,
        relief="flat")

    b14.place(
        x=301, y=396,
        width=78,
        height=41)

    img15 = PhotoImage(file=f"imgs/rgb_img/img15.png")
    b15 = Button(
        image=img15,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_75,
        relief="flat")

    b15.place(
        x=391, y=396,
        width=78,
        height=41)

    img16 = PhotoImage(file=f"imgs/rgb_img/img16.png")
    b16 = Button(
        image=img16,
        borderwidth=0,
        highlightthickness=0,
        bg="#240b35",
        activebackground="#240b35",
        command=btn_100,
        relief="flat")

    b16.place(
        x=481, y=396,
        width=97,
        height=41)

    img17 = PhotoImage(file=f"imgs/rgb_img/img17.png")
    b17 = Button(
        image=img17,
        borderwidth=0,
        bg="#240b35",
        activebackground="#240b35",
        highlightthickness=0,
        command=btn_animacao,
        relief="flat")

    b17.place(
        x=288, y=459,
        width=130,
        height=35)
    rgb.resizable(False, False)
    rgb.mainloop()


def info_func():
    info = Tk()
    screen_width = info.winfo_screenwidth()
    screen_height = info.winfo_screenheight()

    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.85)

    info.geometry(f'600x524+{int(x)}+{int(y)}')
    info.title("Light App")
    info.iconbitmap('imgs/icon/favicon.ico')
    info.geometry("600x524")
    info.configure(bg="#240b35")
    canvas = Canvas(
        info,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    def btn_voltar():
        info.destroy()
        home_page()

    def btn_luz():
        info.destroy()
        luz_func()

    def btn_fan():
        info.destroy()
        fan_func()

    def btn_rgb():
        info.destroy()
        rgb_func()

    def btn_ajustes():
        info.destroy()
        ajustes_func()

    def btn_sair():
        info.destroy()

    background_img = PhotoImage(file=f"imgs/info_img/background.png")
    canvas.create_image(
        227.0, 262.0,
        image=background_img)

    img0 = PhotoImage(file=f"imgs/info_img/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#ad1332",
        command=btn_voltar,
        relief="flat")

    b0.place(
        x=0, y=7,
        width=121,
        height=60)

    img1 = PhotoImage(file=f"imgs/info_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#9f1132",
        command=btn_luz,
        relief="flat")

    b1.place(
        x=0, y=81,
        width=121,
        height=60)

    img2 = PhotoImage(file=f"imgs/info_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#861133",
        command=btn_fan,
        relief="flat")

    b2.place(
        x=0, y=155,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/info_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#861133",
        command=btn_rgb,
        relief="flat")

    b3.place(
        x=0, y=225,
        width=121,
        height=60)

    img4 = PhotoImage(file=f"imgs/info_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#610e34",
        command=btn_ajustes,
        relief="flat")

    b4.place(
        x=0, y=381,
        width=121,
        height=60)

    img5 = PhotoImage(file=f"imgs/info_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#540e34",
        command=btn_sair,
        relief="flat")

    b5.place(
        x=0, y=455,
        width=121,
        height=60)

    import psutil
    # cpu_usage = StringVar()
    # cpu = int(psutil.cpu_percent(0.5))
    # cpu_usa = format(f'{cpu}%')
    # cpu_usage.set(str(cpu_usa))
    #
    # memory_used = StringVar()
    # memory_used.set(str.format('{:.2f} Gb', psutil.virtual_memory().used / 1000000000))
    #
    # total_memory = StringVar()
    # total_memory.set(str.format('{:.2f} Gb', psutil.virtual_memory().total / 1000000000))
    #
    # free_memory = StringVar()
    # free_memory.set(str.format('{:.2f} Gb', psutil.virtual_memory().free / 1000000000))
    #
    # entry0_img = PhotoImage(file=f"imgs/info_img/img_textBox0.png")
    # canvas.create_image(
    #     400.5, 202.0,
    #     image=entry0_img)
    #
    # entry0 = Label(textvariable=memory_used,
    #                font=('Gill Sans MT', 15),
    #                bd=0,
    #                bg="#ffffff",
    #                highlightthickness=0)
    # entry0.place(
    #     x=356.0, y=183,
    #     width=89.0,
    #     height=36)
    #
    # entry1_img = PhotoImage(file=f"imgs/info_img/img_textBox1.png")
    # canvas.create_image(
    #     400.5, 269.0,
    #     image=entry1_img)
    #
    # entry1 = Label(textvariable=total_memory,
    #                font=('Gill Sans MT', 15),
    #                bd=0,
    #                bg="#ffffff",
    #                highlightthickness=0)
    #
    # entry1.place(
    #     x=356.0, y=250,
    #     width=89.0,
    #     height=36)
    #
    # entry2_img = PhotoImage(file=f"imgs/info_img/img_textBox2.png")
    # canvas.create_image(
    #     400.5, 336.0,
    #     image=entry2_img)
    #
    # entry2 = Label(textvariable=free_memory,
    #                font=('Gill Sans MT', 15),
    #                bd=0,
    #                bg="#ffffff",
    #                highlightthickness=0)
    #
    # entry2.place(
    #     x=356.0, y=317,
    #     width=89.0,
    #     height=36)
    #
    # entry3_img = PhotoImage(file=f"imgs/info_img/img_textBox3.png")
    # canvas.create_image(
    #     400.5, 395.0,
    #     image=entry3_img)
    #
    # entry3 = Label(textvariable=cpu_usage,
    #                font=('Gill Sans MT', 15),
    #                bd=0,
    #                bg="#ffffff",
    #                highlightthickness=0)
    #
    # entry3.place(
    #     x=356.0, y=376,
    #     width=89.0,
    #     height=36)

    def inf():
        while True:
            cpu_usage = StringVar()
            cpu = int(psutil.cpu_percent(0.5))
            cpu_usa = format(f'{cpu}%')
            cpu_usage.set(str(cpu_usa))

            memory_used = StringVar()
            memory_used.set(str.format('{:.2f} Gb', psutil.virtual_memory().used / 1000000000))

            total_memory = StringVar()
            total_memory.set(str.format('{:.2f} Gb', psutil.virtual_memory().total / 1000000000))

            free_memory = StringVar()
            free_memory.set(str.format('{:.2f} Gb', psutil.virtual_memory().free / 1000000000))

            entry0_img = PhotoImage(file=f"imgs/info_img/img_textBox0.png")
            canvas.create_image(
                400.5, 202.0,
                image=entry0_img)

            entry0 = Label(textvariable=memory_used,
                           font=('Gill Sans MT', 15),
                           bd=0,
                           bg="#ffffff",
                           highlightthickness=0)
            entry0.place(
                x=356.0, y=183,
                width=89.0,
                height=36)

            entry1_img = PhotoImage(file=f"imgs/info_img/img_textBox1.png")
            canvas.create_image(
                400.5, 269.0,
                image=entry1_img)

            entry1 = Label(textvariable=total_memory,
                           font=('Gill Sans MT', 15),
                           bd=0,
                           bg="#ffffff",
                           highlightthickness=0)

            entry1.place(
                x=356.0, y=250,
                width=89.0,
                height=36)

            entry2_img = PhotoImage(file=f"imgs/info_img/img_textBox2.png")
            canvas.create_image(
                400.5, 336.0,
                image=entry2_img)

            entry2 = Label(textvariable=free_memory,
                           font=('Gill Sans MT', 15),
                           bd=0,
                           bg="#ffffff",
                           highlightthickness=0)

            entry2.place(
                x=356.0, y=317,
                width=89.0,
                height=36)

            entry3_img = PhotoImage(file=f"imgs/info_img/img_textBox3.png")
            canvas.create_image(
                400.5, 395.0,
                image=entry3_img)

            entry3 = Label(textvariable=cpu_usage,
                           font=('Gill Sans MT', 15),
                           bd=0,
                           bg="#ffffff",
                           highlightthickness=0)

            entry3.place(
                x=356.0, y=376,
                width=89.0,
                height=36)

            if cpu <= 20:
                ser.write(b'f')
                ser.readlines()
                ser.write(b'0')
                ser.readlines()

            elif 20 < cpu <= 60:
                ser.write(b'm')
                ser.readlines()
                ser.write(b'0')
                ser.readlines()

            elif cpu > 60:
                ser.write(b'q')
                ser.readlines()
                ser.write(b'0')
                ser.readlines()

    threading.Thread(target=inf).start()
    info.resizable(False, False)
    info.mainloop()


def ajustes_func():
    def btn_voltar():
        ajuste_.destroy()
        home_page()

    def btn_luz():
        ajuste_.destroy()
        luz_func()

    def btn_fan():
        ajuste_.destroy()
        fan_func()

    def btn_rgb():
        ajuste_.destroy()
        rgb_func()

    def btn_info():
        ajuste_.destroy()
        info_func()

    def btn_sair():
        ajuste_.destroy()

    ajuste_ = Tk()
    screen_width = ajuste_.winfo_screenwidth()
    screen_height = ajuste_.winfo_screenheight()

    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (524 / 1.85)

    ajuste_.geometry(f'600x524+{int(x)}+{int(y)}')
    ajuste_.title("Light App")
    ajuste_.iconbitmap('imgs/icon/favicon.ico')
    ajuste_.configure(bg="#240b35")
    canvas = Canvas(
        ajuste_,
        bg="#240b35",
        height=524,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    if ser.isOpen():
        conectado = "ESP32 conectado"
        porta = ser.port
        velocidade = ser.baudrate
    else:
        conectado = "Desconectado"
        porta = " "
        velocidade = " "

    entry0_img = PhotoImage(file=f"imgs/ajustes_img/img_textBox0.png")
    canvas.create_image(
        285.5, 113.5,
        image=entry0_img)

    entry0 = Label(text=conectado,
                   font=('Gill Sans MT', 15),
                   bd=0,
                   bg="#ffffff",
                   highlightthickness=0)

    entry0.place(
        x=187.0, y=99,
        width=197.0,
        height=30)

    entry1_img = PhotoImage(file=f"imgs/ajustes_img/img_textBox1.png")
    canvas.create_image(
        285.5, 226.5,
        image=entry1_img)

    entry1 = Label(text=velocidade,
                   font=('Gill Sans MT', 15),
                   bd=0,
                   bg="#ffffff",
                   highlightthickness=0)

    entry1.place(
        x=187.0, y=212,
        width=197.0,
        height=30)

    entry2_img = PhotoImage(file=f"imgs/ajustes_img/img_textBox2.png")
    canvas.create_image(
        285.5, 342.5,
        image=entry2_img)

    entry2 = Label(text=porta,
                   font=('Gill Sans MT', 15),
                   bd=0,
                   bg="#ffffff",
                   highlightthickness=0)

    entry2.place(
        x=187.0, y=328,
        width=197.0,
        height=30)

    background_img = PhotoImage(file=f"imgs/ajustes_img/background.png")
    canvas.create_image(
        207.0, 262.0,
        image=background_img)

    # img0 = PhotoImage(file=f"imgs/ajustes_img/img0.png")
    # b0 = Button(
    #     image=img0,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     bg="#240b35",
    #     activebackground="#240b35",
    #     command=atualizar,
    #     relief="flat")
    #
    # b0.place(
    #     x=422, y=445,
    #     width=145,
    #     height=39)

    img1 = PhotoImage(file=f"imgs/ajustes_img/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#ad1332",
        command=btn_voltar,
        relief="flat")

    b1.place(
        x=0, y=12,
        width=121,
        height=60)

    img2 = PhotoImage(file=f"imgs/ajustes_img/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#9f1132",
        command=btn_luz,
        relief="flat")

    b2.place(
        x=0, y=82,
        width=121,
        height=60)

    img3 = PhotoImage(file=f"imgs/ajustes_img/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        bg="#921133",
        activebackground="#921133",
        command=btn_fan,
        relief="flat")

    b3.place(
        x=0, y=152,
        width=121,
        height=60)

    img4 = PhotoImage(file=f"imgs/ajustes_img/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#861133",
        command=btn_rgb,
        relief="flat")

    b4.place(
        x=0, y=227,
        width=121,
        height=58)

    img5 = PhotoImage(file=f"imgs/ajustes_img/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        bg="#720f34",
        activebackground="#720f34",
        command=btn_info,
        relief="flat")

    b5.place(
        x=0, y=304,
        width=121,
        height=62)

    img6 = PhotoImage(file=f"imgs/ajustes_img/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        bg="#4f0d35",
        activebackground="#540e34",
        command=btn_sair,
        relief="flat")

    b6.place(
        x=0, y=450,
        width=121,
        height=59)

    ajuste_.resizable(False, False)
    ajuste_.mainloop()


home_page()
