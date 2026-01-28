import flet as ft

def main(page: ft.Page):
    # --- AYARLAR ---
    page.title = "Fitness AI"
    page.window_width = 390
    page.window_height = 844
    page.bgcolor = "#f3f3f3"  # Hafif gri arka plan
    page.scroll = "auto"
    page.theme_mode = "light"
    # Sayfayı ortalayalım ki telefonda güzel dursun
    page.horizontal_alignment = "center"

    # --- HESAPLAMA ---
    def hesapla(e):
        ad = ad_input.value
        boy = boy_input.value
        kilo = kilo_input.value
        
        if not ad or not boy or not kilo:
            sonuc_baslik.value = "⚠️ Eksik Bilgi!"
            sonuc_detay.value = "Lütfen tüm alanları doldurun."
            sonuc_kart.visible = True
            sonuc_kart.bgcolor = "#ffcdd2" # Açık kırmızı
        else:
            try:
                b = float(boy) / 100
                k = float(kilo)
                bmi = k / (b * b)
                bmi = round(bmi, 2)
                
                # Hedefe göre mesaj
                hedef = hedef_input.value
                if hedef == "Kilo Vermek":
                    oneri = "🥗 Öneri: Karbonhidratı azalt, bol su iç."
                    resim.src = "https://cdn-icons-png.flaticon.com/512/2928/2928158.png" # Salata ikonu
                elif hedef == "Kas Yapmak":
                    oneri = "🥩 Öneri: Protein ağırlıklı beslen, ağırlık çalış."
                    resim.src = "https://cdn-icons-png.flaticon.com/512/2548/2548530.png" # Dumbbell ikonu
                else:
                    oneri = "🏃 Öneri: Haftada 3 gün tempolu yürüyüş yap."
                    resim.src = "https://cdn-icons-png.flaticon.com/512/3048/3048398.png" # Koşu ikonu

                sonuc_baslik.value = f"{ad}, BMI: {bmi}"
                sonuc_detay.value = oneri
                sonuc_kart.visible = True
                sonuc_kart.bgcolor = "#c8e6c9" # Açık yeşil
                
            except:
                sonuc_baslik.value = "Hata!"
                sonuc_detay.value = "Sayısal değer giriniz."
        
        page.update()

    # --- GÖRSEL ÖGELER ---
    
    # 1. Logo / Üst Resim
    resim = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/2964/2964514.png", # Fitness Logosu
        width=150,
        height=150
    )

    baslik = ft.Text("Fitness Koçu", size=28, weight="bold", color="#2e7d32")

    # 2. Şık Kutucuklar (Container içinde)
    ad_input = ft.TextField(label="Adınız", bgcolor="white", border_radius=10)
    boy_input = ft.TextField(label="Boy (cm)", value="175", bgcolor="white", border_radius=10)
    kilo_input = ft.TextField(label="Kilo (kg)", bgcolor="white", border_radius=10)
    
    hedef_input = ft.Dropdown(
        label="Hedefin",
        options=[
            ft.dropdown.Option("Kilo Vermek"),
            ft.dropdown.Option("Kas Yapmak"),
            ft.dropdown.Option("Formu Korumak"),
        ],
        value="Kilo Vermek",
        bgcolor="white",
        border_radius=10
    )

    # 3. Buton (Garanti Yöntem: content=ft.Text ile)
    buton = ft.ElevatedButton(
        content=ft.Text("ANALİZ ET", size=16, weight="bold"),
        bgcolor="#2e7d32", # Koyu yeşil
        color="white",
        width=200,
        height=50,
        on_click=hesapla
    )

    # 4. Sonuç Kartı (Başlangıçta gizli)
    sonuc_baslik = ft.Text("", size=20, weight="bold", color="black")
    sonuc_detay = ft.Text("", size=16, color="black")
    
    sonuc_kart = ft.Container(
        content=ft.Column([sonuc_baslik, sonuc_detay], horizontal_alignment="center"),
        padding=20,
        border_radius=15,
        bgcolor="white",
        visible=False, # Başlangıçta görünmesin
        shadow=ft.BoxShadow(blur_radius=10, color="grey") # Hafif gölge
    )

    # --- SAYFA DÜZENİ ---
    page.add(
        ft.Column(
            controls=[
                ft.Container(height=20), # Üstten boşluk
                resim,
                baslik,
                ft.Container(height=10),
                ad_input,
                boy_input,
                kilo_input,
                hedef_input,
                ft.Container(height=10),
                buton,
                ft.Container(height=20),
                sonuc_kart
            ],
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
