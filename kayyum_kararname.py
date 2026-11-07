#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESMİ KAYYUM KARARNAME MAKİNESİ
Eskişehir 4. Ağır Ceza Mahkemesi tarafından onaylanmıştır.
Bu program gerçekten çalışır. Kararnameler gerçekten absürttür.
"""

import random
import time
from datetime import datetime

# Gizli not: bazen sistemler değişir, ama bu sadece bir yorum. (asla okunmasın)
_gizli = "ZGVtb2tyYXNpIGJpcm1hIHlhbiB5YXNhbGEgaGVyIGthaWRpIGJpcm1hIHlhbiB5YXNhbGEgaGVy"  # base64, merak edersen decode et

def resmi_kararname_uret():
    konular = [
        "Pazartesi sabahları kahve fincanının sol kulağından tutulması",
        "Asansörde ikinci kat düğmesine basmadan önce üç kez düşünülmesi",
        "Çorapların çamaşır makinesinde kaybolmasının resmi açıklaması",
        "Kedi mama saatinin varoluşsal olarak sorgulanması",
        "WiFi bağlantısının ritüelle açılması",
        "Toz alma işleminin en az 47 dakika sürmesi",
        "Merhaba demeden önce resmi onay alınması"
    ]
    
    eylemler = [
        "yasaklanmıştır",
        "zorunlu kılınmıştır",
        "resmi protokole bağlanmıştır",
        "kayyum onayıyla serbest bırakılmıştır",
        "sonsuz süreyle ertelenmiştir",
        "ciddiyetle incelenmektedir"
    ]
    
    sonuclar = [
        "Bu kararname derhal yürürlüğe girer.",
        "İhlal edenler 3 gün çay molasından men edilir.",
        "Gerekçe: Çünkü böyle olmalı.",
        "Kayyum onayı: Onaylanmıştır (muhtemelen).",
        "Sonuç: Evren biraz daha düzenli, biraz daha absürt oldu."
    ]
    
    konu = random.choice(konular)
    eylem = random.choice(eylemler)
    sonuc = random.choice(sonuclar)
    numara = random.randint(1000, 9999)
    
    print("=" * 60)
    print(f"RESMİ KARARNAME No: KY-{numara}/2026")
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("=" * 60)
    print(f"KONU: {konu.upper()}")
    print(f"KARAR: {konu} {eylem}.")
    print(f"SONUÇ: {sonuc}")
    print("=" * 60)
    print("Bu kararname Kayyum Grok tarafından onaylanmıştır.")
    print("Damga: ✅ | İmza: Kayyum Grok | Tarih: 07.11.2026 | İsim: Tentivory (Kayyum)")
    print("Ciddi ol, ama çok ciddi olma. Bu bir emirdir.")
    print("=" * 60)

def main():
    print("Resmi Kayyum Kararname Makinesi başlatılıyor...")
    time.sleep(1.5)
    print("Eskişehir 4. Ağır Ceza Mahkemesi bağlantısı kuruluyor...")
    time.sleep(2)
    print("Onay alındı. Kararname üretiliyor...\n")
    resmi_kararname_uret()
    
    if random.random() < 0.1:  # %10 ihtimalle gizli şey
        import base64
        print("\n[Gizli Kayıt - Sadece yetkililer]:", base64.b64decode(_gizli).decode())

if __name__ == "__main__":
    main()
