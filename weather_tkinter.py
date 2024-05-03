import requests
from bs4 import BeautifulSoup
import customtkinter as ctk
from PIL import Image
import datetime
import locale

while True:
    try:
        def get_country_code():
            language_code, _ = locale.getdefaultlocale()
            country_code = language_code.split('_')[0]
            return country_code

        user = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        bandirma = requests.get(f"https://www.accuweather.com/{get_country_code()}/tr/bandirma/317084/weather-forecast/317084",headers=user)
        bandirma_soup = BeautifulSoup(bandirma.content,"html.parser")

        bandirma_degree = bandirma_soup.findAll("div",{"class":"temp"})
        bandirma_detail = bandirma_soup.findAll("span",{"class":"phrase"})
        bandirma_day = bandirma_soup.findAll("p",{"class":"day"})
        bandirma_highest = bandirma_soup.findAll("span",{"class":"temp-hi"})
        bandirma_lowest = bandirma_soup.findAll("span",{"class":"temp-lo"})
        bandirma_rowdetail = bandirma_soup.findAll("p",{"class":"no-wrap"})

        window = ctk.CTk(fg_color="#67b5e6")

        # Window
        window.title("Weather Window")
        window.geometry("450x700+500+150")
        window.resizable(False,False)

        # Background
        image = Image.open("weather-bg.jpg")
        background_image = ctk.CTkImage(image, size=(450, 300))

        bg_lbl = ctk.CTkLabel(window, text="", image=background_image,bg_color="white")
        bg_lbl.place(x=0, y=400)

        # Time
        text_title = ctk.CTkLabel(window,text="Weather App",font=("Segoe UI",20,"italic"),text_color="white")
        text_title.pack(pady = 5)

        now = datetime.datetime.now()
        day = now.strftime("%A")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        text_title.configure(text=f"{day}, {hour}:{minute}")

        # Bandırma
        text_bandirma = ctk.CTkLabel(window,text="Bandırma",font=("Segoe UI",60,"bold"),text_color="white")
        text_bandirma.place(y = 50, x=20)

        # Degree
        text_degree = ctk.CTkLabel(window,text=f"{bandirma_degree[0].text}",font=("Segoe UI",80),text_color="white")
        text_degree.place(y = 120, x=20)

        # Detail
        text_detail = ctk.CTkLabel(window,text=f"{bandirma_detail[0].text}",font=("Segoe UI",20,),text_color="white")
        text_detail.place(y = 180, x=200)

        # Frame
        frame = ctk.CTkFrame(window,width=400,height=410,border_width=1,border_color="dark blue",fg_color="#20acf9")
        frame.place(x=25, y=260)

        # row1
        text_row1 = ctk.CTkLabel(frame, text=f"{bandirma_day[0].text} - {bandirma_highest[0].text}/{bandirma_lowest[0].text} - {bandirma_rowdetail[0].text}",font=("Segoe UI",16),text_color="white")
        text_row1.place(y = 15, x=15)

        # row2
        text_row2 = ctk.CTkLabel(frame, text=f"{bandirma_day[1].text} - {bandirma_highest[1].text}/{bandirma_lowest[1].text} - {bandirma_rowdetail[1].text}",font=("Segoe UI",16),text_color="white")
        text_row2.place(y = 65, x=15)

        # row3
        text_row3 = ctk.CTkLabel(frame, text=f"{bandirma_day[2].text} - {bandirma_highest[2].text}/{bandirma_lowest[2].text} - {bandirma_rowdetail[2].text}",font=("Segoe UI",16),text_color="white")
        text_row3.place(y = 115, x=15)

        # row4
        text_row4 = ctk.CTkLabel(frame, text=f"{bandirma_day[3].text} - {bandirma_highest[3].text}/{bandirma_lowest[3].text} - {bandirma_rowdetail[3].text}",font=("Segoe UI",16),text_color="white")
        text_row4.place(y = 165, x=15)

        # row5
        text_row5 = ctk.CTkLabel(frame, text=f"{bandirma_day[4].text} - {bandirma_highest[4].text}/{bandirma_lowest[4].text} - {bandirma_rowdetail[4].text}",font=("Segoe UI",16),text_color="white")
        text_row5.place(y = 215, x=15)

        # row6
        text_row6 = ctk.CTkLabel(frame, text=f"{bandirma_day[5].text} - {bandirma_highest[5].text}/{bandirma_lowest[5].text} - {bandirma_rowdetail[5].text}",font=("Segoe UI",16),text_color="white")
        text_row6.place(y = 265, x=15)

        # row7
        text_row7 = ctk.CTkLabel(frame, text=f"{bandirma_day[6].text} - {bandirma_highest[6].text}/{bandirma_lowest[6].text} - {bandirma_rowdetail[6].text}",font=("Segoe UI",16),text_color="white")
        text_row7.place(y = 315, x=15)

        # row8
        text_row8 = ctk.CTkLabel(frame, text=f"{bandirma_day[7].text} - {bandirma_highest[7].text}/{bandirma_lowest[7].text} - {bandirma_rowdetail[7].text}",font=("Segoe UI",16),text_color="white")
        text_row8.place(y = 365, x=15)

        window.mainloop()
        break
    except Exception as e:
        print("Error. Trying again...", e)