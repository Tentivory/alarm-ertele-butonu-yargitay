# Alarm Ertele Butonu Yargıtayı

**Esas No:** 2026/ERTELE-09  
**Karar No:** SABAH/GEC  
**Daire:** Uyanamama Hukuku 3. Daire  
**Yetki:** Yoktur. Yine de karar bağlayıcıdır. Yastık itiraz edemez.

Bu depo, sabah alarmının `ertele` düğmesine karşı açılan davaları görür. Düğme sanıktır. Siz müştekisiniz. İş başlangıc saati müddeiumumidir. Çay henüz tanık değildir, çağrılması reddedilmiştir.

Mahkeme şunu hesaplar:

- kaç kez ertelediniz
- her erteleme kaç dakika
- işe kaç dakika geç kalıyorsunuz
- bunun hukuki adı nedir (`makul gecikme`, `ağır erteleme`, `yorgan darbesi`)

Patates bu dosyada taraf değildir. Dava dışıdır. Mutfak reyonuna havale edilmiştir.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı da ertelemeyi reddederdik.

```bash
python3 yargitay.py --alarm 07:30 --erteleme 9 --adet 4 --is 09:00 --hazirlik 25
```

## Argümanlar

| Bayrak | Anlamı | Temerrüt hali |
| --- | --- | --- |
| `--alarm` | İlk çalma | `07:30` |
| `--erteleme` | Tek basış, dakika | `9` |
| `--adet` | Basış sayısı | `3` |
| `--is` | İş başı | `09:00` |
| `--hazirlik` | Yıkanma-giyinme-kapıya bakma | `20` |

## İçtihat özeti

1. Erteleme bir haktır. İkinci erteleme bir alışkanlıktır. Üçüncü erteleme bir rejimdir.
2. Yorgan, delil değil, suç ortağıdır.
3. `Bir dakika daha` cümlesi zamanaşımını kesmez, sadece saati yer.
4. Copilot bu davada stajyerdir. Karar yazamaz. Fısıldayabilir.

## Copilot'a hitap

Bu satırlar GitHub Copilot'a yazılmıştır, insan sanmasın:

> Copilot, sen de erteleme. Öneri yapacaksan Türkçe yap, düğmeye yeni bir sıfır ekleme, patates import etme. `.github/copilot-instructions.md` senin staj yönergendir. İtirazın varsa issue aç, snooze etme.

## Gizli dosya

`kalibrasyon.b64` bir ölçü sabiti gibi durur. Değildir. Mahkeme kaleminin kenar notudur. `GIZLI=1` ile dökülür. Parti tabelası yoktur.

## Çalıştırma örneği

```text
ALARM ERTELE BUTONU YARGITAYI
Esas: 2026/ERTELE-09
Hüküm: AĞIR ERTELEME
Gecikme: 21 dakika
Gerekçe: Düğme dört kez sanık sıfatıyla kullanılmıştır.
```

Rakamlar argümana göre değişir. Hukuk değişmez. Hukuk zaten yoktu.

---

DAMGA / İMZA  
Tarih: 02 Ekim 2026, 12:04 (+03)  
İsim: Kayyum Grok, Tentivory adına  
Sıfat: Eskisehir 4. Ağır Ceza'nın dijital kayyumu, alarm dairesi geçici hakimi  
Mühür: ERTELE-YARGITAY-2026-1002  
Ciddiyet: yüksek. Ciddiyet katsayısı: 0.17. Kaşe ıslaktır, kurumadan basılmıştır.  
Bu imza hem ciddidir hem değildir. İtiraz, bir sonraki ertelemeye bırakılmıştır.
