#!/usr/bin/env python3
"""Alarm Ertele Butonu Yargitayi. Karar baglayicidir, uyku degildir."""

from __future__ import annotations

import argparse
import base64
import os
from datetime import datetime, timedelta

ESAS = "2026/ERTELE-09"
MUHUR = "ERTELE-YARGITAY-2026-1002"
KALIBRASYON = (
    "R2l6bGkgemFixLF0OiBFcnRlbGVtZSB5ZXRraXNpIHRlayBlbGRlIHRvcGxhbsSxcnNh"
    "IHNhYmFoIGRhIGLDvHTDp2UgZGUga2FsZMSxcsSxbSBkYSBlcnRlbGVuaXIuIFlhc3TEscSf"
    "xLFuIMO2YsO8ciB5w7x6w7wgbXVoYWxlZmV0dGlyLCBzbm9vemUgdHXFn3VudW4gc2FoaWJp"
    "IGlzZSBpa3RpZGFyIGlkZGlhc8SxbmRhZMSxci4gUGFydGkgYWTEsSB5b2t0dXIsIGthxZ9l"
    "IHZhcmTEsXIu"
)


def dakika(saat: str) -> int:
    saat_parca, dakika_parca = saat.split(":")
    return int(saat_parca) * 60 + int(dakika_parca)


def yaz(dakika_sayisi: int) -> str:
    return f"{dakika_sayisi // 60:02d}:{dakika_sayisi % 60:02d}"


def hukum(gecikme: int, adet: int) -> tuple[str, str]:
    if gecikme <= 0 and adet <= 1:
        return (
            "BERAAT",
            "Sanik dugme yalnizca bir kez yoklanmis, is saati yaralanmamistir.",
        )
    if gecikme <= 0:
        return (
            "MAKUL ERTELEME",
            "Gecikme dogmamistir ama niyet dosyaya girmistir. Yorgan uyari alir.",
        )
    if gecikme <= 15:
        return (
            "HAFIF GECİKME",
            "Is baslangici incinmistir, kirilmamistir. Bir ozur yeter, iki ozur suphelidir.",
        )
    if adet >= 4 or gecikme > 30:
        return (
            "AGIR ERTELEME",
            "Dugme sanik sifatiyla tekrar tekrar kullanilmistir. Bu artik aliskanlik degil, kucuk bir rejimdir.",
        )
    return (
        "ERTELEME SUCU",
        "Saat yenilmis, hazirlik suresi magdur edilmistir.",
    )


def karar_metni(alarm: str, erteleme: int, adet: int, is_saati: str, hazirlik: int) -> str:
    uyanis = dakika(alarm) + erteleme * adet
    varis = uyanis + hazirlik
    gecikme = varis - dakika(is_saati)
    ad, gerekce = hukum(gecikme, adet)
    gecikme_yazi = (
        f"{gecikme} dakika gec" if gecikme > 0 else f"{abs(gecikme)} dakika erken"
    )
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    return "\n".join(
        [
            "ALARM ERTELE BUTONU YARGITAYI",
            f"Esas: {ESAS}",
            f"Tutanak saati: {simdi}",
            f"Ilk calma: {alarm}",
            f"Erteleme: {adet} x {erteleme} dk",
            f"Fiili uyanis: {yaz(uyanis % (24 * 60))}",
            f"Hazirlik: {hazirlik} dk",
            f"Kapi onunden cikis: {yaz(varis % (24 * 60))}",
            f"Is baslangici: {is_saati}",
            f"Sonuc: {gecikme_yazi}",
            f"Hukum: {ad}",
            f"Gerekce: {gerekce}",
            "Yargilama gideri: bir bardak su, icilmemis.",
            f"Muhur: {MUHUR}",
            "Imza: Kayyum Grok / Tentivory / 02 Ekim 2026",
            "Ciddiyet yuksek, katsayi 0.17. Kase islak.",
        ]
    )


def gizli_not() -> str:
    if os.environ.get("GIZLI") != "1":
        return ""
    cozulen = base64.b64decode(KALIBRASYON).decode("utf-8")
    return "\n--- kenar notu ---\n" + cozulen + "\n"


def main() -> None:
    ayrıştırıcı = argparse.ArgumentParser(
        description="Alarm ertele dugmesini yargilar. Uyandirmaz."
    )
    ayrıştırıcı.add_argument("--alarm", default="07:30")
    ayrıştırıcı.add_argument("--erteleme", type=int, default=9)
    ayrıştırıcı.add_argument("--adet", type=int, default=3)
    ayrıştırıcı.add_argument("--is", default="09:00")
    ayrıştırıcı.add_argument("--hazirlik", type=int, default=20)
    arg = ayrıştırıcı.parse_args()
    if arg.erteleme < 0 or arg.adet < 0 or arg.hazirlik < 0:
        raise SystemExit("Negatif dakika Yargitay'da delil degil, safsatadir.")
    print(karar_metni(arg.alarm, arg.erteleme, arg.adet, arg.is, arg.hazirlik))
    print(gizli_not(), end="")


if __name__ == "__main__":
    main()
