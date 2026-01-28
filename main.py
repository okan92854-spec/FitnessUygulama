import flet as ft

def main(page: ft.Page):
    # --- 1. AYARLAR ---
    page.title = "Fitness AI - Yeşil Doğa Teması"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"
    page.window_width = 390
    page.window_height = 844
    
    # --- 2. BEYİN KISMI ---
    def program_olustur(kullanici_hedefi, kullanici_adi):
        if kullanici_hedefi == "Kilo Vermek":
            return [
                f"🌿 {kullanici_adi} için Detox & Kilo Verme:",
                "--------------------------------",
                "🥒 SABAH: Maydanoz kürü + 2 Yumurta Beyazı",
                "🍵 ARA: Yeşil Çay + 2 Ceviz",
                "🥗 ÖĞLE: Bol yeşillikli Ton Balıklı Salata",
                "🏃 ANTRENMAN: 40 dk Doğa Yürüyüşü",
                "🥦 AKŞAM: Brokoli Çorbası + Yoğurt"
            ]
        elif kullanici_hedefi == "Kas Yapmak":
            return [
                f"💪 {kullanici_adi} için Güç & Hacim:",
                "--------------------------------",
                "🍳 SABAH: 3 Yumurta + Avokado + Yulaf",
                "🍌 ARA: Muz + Fıstık Ezmesi",
                "🍗 ÖĞLE: Tavuk Göğsü + Yeşil Mercimek",
                "🏋️ ANTRENMAN: Ağırlık Antrenmanı (Sırt/Bacak)",
                "🥬 AKŞAM: Ispanaklı Kırmızı Et + Bulgur"
            ]
        else: 
            return [
                f"🧘 {kullanici_adi} için Denge Programı:",
                "--------------------------------",
                "🥑 Tüm öğünlerde sağlıklı yağlar tüket.",
                "🧘 Haftada 2 gün Yoga/Pilates yap.",
                "🥦 İşlenmiş gıdayı kes, yeşilliği artır."
            ]

    # --- 3. BUTON İŞLEMİ ---
    def hesapla(e):
        if not isim.value or not kilo.value:
            sonuc_alani.controls.clear()
            sonuc_alani.controls.append(ft.Text("⚠️ Lütfen bilgileri eksiksiz girin!", color="red"))
        else:
            buton.content = ft.Text("Analiz Yapılıyor...")
            page.update()
            
            gelen_program = program_olustur(hedef.value, isim.value)
            
            sonuc_alani.controls.clear()
            for satir in gelen_program:
                sonuc_alani.controls.append(ft.Text(satir, size=16, color="green", weight="bold"))
            
            reklam_alani.visible = True
            buton.content = ft.Text("YENİ PROGRAM OLUŞTUR")
            
        page.update()

    # --- 4. TASARIM ---
    
    baslik = ft.Text("DOĞAL YAŞAM KOÇU", size=28, weight="bold", color="green")
    
    # İsim Kutusu (İkonlu)
    isim = ft.TextField(
        label="Adınız", 
        border_color="green", 
        color="black",
        prefix_icon="person" 
    )
    
    # Kilo Kutusu (İkonlu)
    kilo = ft.TextField(
        label="Kilonuz (kg)", 
        keyboard_type=ft.KeyboardType.NUMBER, 
        border_color="green",
        color="black",
        prefix_icon="monitor_weight"
    )
    
    # Hedef Menüsü (İKONSUZ - Hata Çözüldü)
    hedef = ft.Dropdown(
        label="Hedefiniz",
        options=[
            ft.dropdown.Option("Kilo Vermek"),
            ft.dropdown.Option("Kas Yapmak"),
            ft.dropdown.Option("Formu Korumak"),
        ],
        value="Kilo Vermek",
        border_color="green",
        color="black"
    )

    buton = ft.ElevatedButton(
        content=ft.Text("HAYATINI DEĞİŞTİR"),
        bgcolor="green", 
        color="white", 
        width=300,
        height=50,
        on_click=hesapla
    )

    sonuc_alani = ft.Column()

    reklam_alani = ft.Container(
        content=ft.Column([
            ft.Text("📢 SPONSORLU ÖNERİ", weight="bold", color="white"),
            ft.Text("Organik Yeşil Çay İndirimi İçin Tıkla!", color="white")
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="green", 
        padding=15,
        border_radius=10,
        visible=False,
        on_click=lambda _: print("Reklam Geliri +1 TL")
    )

    # --- 5. YERLEŞİM ---
    page.add(
        ft.Column(
            [
                ft.Container(height=20),
                baslik,
                ft.Divider(color="green"),
                isim,
                kilo,
                hedef,
                ft.Container(height=20),
                buton,
                ft.Container(height=20),
                sonuc_alani,
                ft.Container(height=20),
                reklam_alani
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)