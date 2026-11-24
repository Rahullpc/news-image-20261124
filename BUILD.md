# news-image-20261124 — BUILD (24 Nov 11:45 WIB; REVISI v3 24 Nov ~12:20 WIB)

## REVISI v3 — audit ketat tanggal KEJADIAN (perintah bos 24 Nov 11:51 WIB: "Perbaiki lagi")

Standar ketat: **hanya peristiwa yang TERJADI persis Selasa 24 Nov 2026**. Audit menemukan kesalahan besar v2: **lead Polandia ternyata peristiwa Senin 23 Nov ~23:00 CET** (jam "01:31 UTC" adalah saat misi pertahanan udara SELESAI + jam publikasi h.ua, bukan jam insiden). Semua panel diaudit ulang dengan standar yang sama (detail + sumber di RESEARCH.md TAHAP 3).

### Temuan + perbaikan (satu per satu)
1. **LEAD Polandia → KOREA (lead diganti):** insiden drone Dorohusk terjadi Senin 23 Nov ~23:00 CET (OSINT map; pernyataan Polish Operational Command 22:53 UTC 23 Nov; Daily Mail "Monday evening"). Lead baru: "RUSSIAN JETS ENTER DEFENCE ZONE" — Korea KADIZ Selasa pagi (Reuters Seoul 24 Nov: jet dikerahkan Selasa pagi; alert Ulleung 07:52 KST dicabut ~5 menit; attaché Rusia dipanggil Selasa). Ikon radar → jet (ikon jet sudah ada, dipakai di lead 148px).
2. **LIBYA → ZAPORIZHZHIA (panel diganti):** serangan kapal perang 22 Nov, diumumkan 23 Nov. Diganti serangan Rusia ke Zaporizhzhia (Reuters 24 Nov): "RUSSIAN STRIKE KILLS 2 IN ZAPORIZHZHIA" / "Overnight attack wounds 22, incl. 2 children." Ikon drone → missile.
3. **IRAN → HASINA (panel diganti):** sudut "strikes unlikely" hanya pernyataan Trump Senin 23 Nov; klaim "oil 3-month low" di v2 TIDAK terverifikasi (minyak jatuh Senin −4%, Selasa bertahan ~$80). Diganti: "HASINA PLANS DEC 16 RETURN" / "Ousted PM seeks Biman flight home after 2 years in exile." (Reuters 24 Nov, juru bicara: "on Tuesday".) Ikon bolt → globe.
4. **PASAR (angka diperbaiki):** "Samsung +8%" TIDAK terkonfirmasi di penutupan (AP 7,5%, WSJ 6,5%) → diganti "Taiwan +9.1%" (Reuters close Selasa 24 Nov). Nikkei +4,5% dan Kospi +7,5% dipertahankan (penutupan Reuters). Fakta jadi: "Nikkei +4.5%, Kospi +7.5%, Taiwan +9.1% as Huang's return revives the AI rally."
5. **MEKSIKO → CATUR (panel diganti):** keputusan AG Meksiko Senin 23 Nov. Diganti Kejuaraan Dunia Catur Game 1 (FIDE/Reuters, Selasa 24 Nov 15:00 CET, Jenewa): "WORLD CHESS TITLE MATCH OPENS" / "Gukesh defends crown vs Sindarov, both 20, in Geneva." Ikon baru: pawn (fungsi `icon_pawn`, bidak catur hitam + alas navy).
6. **INDONESIA → MINYAK (panel diganti):** kebakaran Cikande Sabtu 21 Nov; 24 tewas dikonfirmasi Senin 23 Nov. Diganti: "OIL HOLDS NEAR $80 AS IRAN TALKS STALL" / "WTI steadies; Brent above $89 after Monday's 4% slide." (Bloomberg, diperbarui 24 Nov.) Ikon baru: droplet (fungsi `icon_drop`, tetesan minyak navy + highlight).
7. **DIPERTAHANKAN (terverifikasi Selasa 24 Nov):** Gaza (Reuters Kairo 24 Nov, ≥3 tewas 5 luka Khan Younis); Pasar (penutupan Reuters 24 Nov); Korea (naik jadi lead).
8. **STRIP BAWAH (panel diganti):** Korea pindah ke lead → panel bawah jadi Jepang: "FACTORY PMI HITS 53.7" / "Manufacturing growth tops forecasts in November." (dpa-AFX, Selasa 24 Nov; flash manufacturing PMI 53,7, tercepat 44 bulan.) Ikon chart.
9. **ALSO TODAY (ketiga item diganti — ketiganya peristiwa Senin 23 Nov):** EU sanksi, UN AI, NZ–India draw → "S. KOREA — BOK seen hiking rates Thu" (jajak pendapat Reuters, Selasa) / "INDIA — Bali Jatra opens in Cuttack" (festival dibuka 24 Nov, Presiden Murmu meresmikan sore ini; terverifikasi dari jadwal resmi distrik — label "on Monday" di satu artikel NIE salah) / "AUSTRALIA — Megafire simulator unveiled" (UNSW + Fire Rescue NSW, Selasa 24 Nov).
10. **Kualitas visual:** semua teks baru diukur dulu dengan PIL sebelum render (grid: headline 2 baris, fakta ≤2 baris; lead: headline 295px + 485px dari batas 676px, fakta 2 baris; ALSO TODAY berakhir 958,8 / 922,3 / 979,9px dari tepi kanan 996px). Ikon baru pawn + droplet terverifikasi terbaca di render penuh + 300px. Ikon missile dipakai 2× (Ukraina + Gaza) dan chart 2× (Pasar + PMI) — pictogram generik yang sama, dapat diterima di format koran.

### Poster v3
- File: [entry.png](sandbox://workspace/makefun/news-image-20261124/entry.png) — 1024×1024, 137.143 byte (≤1 MiB)
- sha256: `5d2e5fc9c8094e4c5f742160cbfd0cb4d0fac9c888713ed8aec411da6c1f3fd4`
- Salinan tampil (nama baru, anti-cache): [entry-v3-strict.png](sandbox://workspace/makefun/news-image-20261124/entry-v3-strict.png) — byte-identik dengan entry.png (hanya untuk ditunjukkan ke bos; TIDAK di-commit ke repo)
- Render 300px: entry-300.png (diperbarui ke v3)

### Verifikasi v3
- Ukuran: 1024×1024, 137.143 byte ≤ 1.048.576 ✓
- Determinisme: draw 2× → sha256 sama `5d2e5fc9…c1f3fd4`; main.py (MAKEFUN_OUTPUT_DIR berbeda, 2 dir) → sha256 sama ✓
- Cek visual penuh: semua teks terbaca huruf per huruf, tanpa typo, tanpa tumpang tindih; lead fakta 2 baris tidak menabrak garis grid; ALSO TODAY tidak ada yang mepet tepi kanan (berakhir ≤979,9px).
- Cek 300px: masthead, tanggal, headline lead + headline panel dan struktur koran tetap terbaca; teks fakta kecil (wajar untuk format koran).
- Titik terlemah (jujur): (1) Catur Game 1 dimulai Selasa 21:00 WIB — saat poster dibuat pertandingan belum dimulai, jadi panel ini peristiwa terjadwal, bukan hasil; (2) panel Minyak adalah pola pasar (bertahan di ~$80), bukan peristiwa diskret; (3) poster kehilangan cerita Polandia — cerita paling banyak diliput hari ini — karena insidennya Senin malam; kalau bos mau Polandia kembali, itu keputusan editorial bos, bukan fakta.

## REVISI v2 — cross-check (perintah bos 24 Nov 11:39 WIB: "crosscheck perbaiki dulu sebagus mungkin")

Cross-check fakta live 24 Nov 11:40–12:00 WIB (Reuters, WSJ, Al Jazeera, AFP, TradingView, The Guardian, AP) menemukan **5 cerita tanggalnya meleset + 2 fakta salah + 2 angka meleset**. Semua diperbaiki di `draw_poster.py`, render ulang, verifikasi ulang. BELUM di-submit — submit hanya atas perintah eksplisit bos setelah ia melihat poster revisi.

### Temuan + perbaikan (satu per satu)
1. **SUDAN → GAZA (panel diganti):** cerita v1 (drone RSF hantam stasiun listrik, pemadaman massal) ternyata Al Jazeera **2 Nov 2026** — bukan 24 Nov. Diganti Gaza, terverifikasi Reuters 24 Nov: "AIRSTRIKE KILLS 3 AT GAZA POLICE POST" / "At least 3 dead, 5 wounded near a police post in Khan Younis." Ikon baru: missile.
2. **INDIA → INDONESIA (panel diganti):** cerita v1 (banjir Himalaya 4 tewas, ~100 hilang) ternyata AFP **6 Agu 2025** (Dharali) — lebih dari setahun lalu. Diganti kebakaran pabrik Cikande, Banten (Reuters 23 Nov + laporan 24 Nov): "24 DEAD, 30 MISSING IN FACTORY FIRE" / "Search goes on at Java candy plant; DNA tests to name victims." Ikon baru: flame (fungsi `icon_flame`, api merah + inti emas).
3. **IRAN (reframe):** headline v1 "TRUMP DELAYS IRAN STRIKE TO JAN 1" bersumber dari pernyataan 19–22 Nov; "oil falls 4%" adalah pergerakan 23 Nov. Diganti sudut 24 Nov: "TRUMP: NEW IRAN STRIKES UNLIKELY" / "Oil hits 3-month low; U.S. sanctions Iran's shadow banks." (Trump sebut serangan baru "quite unlikely" Senin 23 Nov; minyak ke titik terendah 3 bulan Selasa 24 Nov; sanksi Treasury ke shadow bank Iran.) Ikon: missile → bolt (energi/minyak).
4. **PASAR (angka diperbaiki):** "SoftBank +8%" **SALAH** (aktual +4,99%, TradingKey). Diganti "Samsung +8%" (intraday 24 Nov +8,2–8,3% di beberapa sumber). Nikkei +4,4% → **+4,5%** dan Kospi +7% → **+7,5%** (penutupan Reuters 24 Nov).
5. **KOREA (fakta diperbaiki):** "AIR-RAID ALERT AFTER BREACH" + "Jets scramble after a Russian airspace breach" **SALAH** — JCS: TIDAK ada pelanggaran wilayah udara Korea Selatan; pesawat Rusia hanya masuk KADIZ (zona identifikasi); alert dicabut dalam 5 menit. Diganti: "RUSSIAN JETS ENTER DEFENCE ZONE" / "Jets scramble as Russian planes enter defence zone." Kata "breach" dihapus dari poster.
6. **ALSO TODAY (ketiga item diganti):** ECB "Lagarde resigns" = **29 Okt 2026**; Brasil "Storm displaces thousands" = badai **20 Nov**; Kongres "First Gen Z woman elected" = **3 Nov 2026**. Diganti (semua dilaporkan 24 Nov): "EU — 22nd Russia sanctions proposed" / "UN — Guterres seeks global AI rules" / "SPORT — NZ hold India to Wellington draw".
7. **DIPERTAHANKAN (terverifikasi):** Lead Polandia/NATO (Reuters 24 Nov — drone 01:31 UTC Dorohusk, izin tembak ditahan, AWACS); Ukraina/Libya (pengumuman 23 Nov + laporan mendalam WSJ 24 Nov); Meksiko (Reuters 23 Nov, Al Jazeera 24 Nov).
8. **Tanggal poster terverifikasi:** 24 Nov 2026 memang Selasa (`date -d 2026-11-24` → Tuesday). Kicker, footer, dan masthead tidak berubah.
9. **Kualitas visual:** tidak ada panel kosong — semua panel sudah padat (ikon + kicker + headline + fakta). Tidak ada hiasan tambahan yang diperlukan; lebar semua teks baru diukur dulu dengan PIL sebelum render (Korea 450,9px/490px; ALSO TODAY berakhir ≤978px dari tepi kanan 996px; fakta panel ≤684px/756px untuk 2 baris).

### Poster v2 (diganti — JANGAN submit)
- File: entry.png v2 — 1024×1024, 136.628 byte
- sha256: `9219e8f53bd02621f89684515fa7e553c4ae0ac841ce5b5ad0c9fe91cb82421c`
- Status: SUPERSEDED oleh v3 (audit ketat tanggal kejadian 24 Nov ~12:20 WIB — lead Polandia ternyata peristiwa Senin 23 Nov malam).

### Verifikasi v2
- Ukuran: 1024×1024, 136.628 byte ≤ 1.048.576 ✓
- Determinisme: draw 2× → sha256 sama `9219e8f5…82421c`; main.py (MAKEFUN_OUTPUT_DIR berbeda, 2 dir) → sha256 sama ✓
- Cek visual penuh: semua teks terbaca, tanpa typo, tanpa tumpang tindih; Korea 1 baris headline + 1 baris fakta (tidak menabrak footer); ALSO TODAY tidak ada yang mepet tepi kanan (berakhir ≤978px).
- Cek 300px: masthead, tanggal, headline lead + headline panel dan struktur koran tetap terbaca; teks fakta kecil (wajar untuk format koran).

## Poster v1 (diganti — JANGAN submit)
- File: entry.png v1 — 1024×1024, 137.597 byte
- sha256: `bf51716fb6fe1658c5058de7a1a739e6ef74a23b55e33f03350d278ee1df434e`
- Status: SUPERSEDED oleh v2 (cross-check 24 Nov ~12:00 WIB).

## Layout (v3 — berlaku)
Koran satu halaman, kertas koran terang + tinta hitam + aksen merah/navy/hijau (format sama dengan edisi 23 Nov yang lolos semua cek):
- Masthead "THE WORLD" + "TUESDAY, 24 NOVEMBER 2026" + garis merah
- Lead penuh: jet Rusia masuk zona pertahanan Korea Selatan (ikon jet) — "RUSSIAN JETS ENTER DEFENCE ZONE"
- Grid 2×3: Zaporizhzhia, Hasina, Pasar, Catur, Gaza, Minyak — tiap panel pictogram + kicker + headline + 1 baris fakta
- Strip bawah: PMI Jepang + "ALSO TODAY" (BOK, Bali Jatra, Megafire)
- Footer: "All events reported on Tuesday, 24 November 2026. Sources: wire reports."

## Fakta per panel (sumber: RESEARCH.md — Reuters, WSJ, TradingView, h.ua, Access24, C54)
| Panel | Fakta di poster | Sumber |
|---|---|---|
| Polandia (lead) | Shoot-down authorised, then held; NATO sends AWACS to Poland | Drone Rusia langgar wilayah udara Polandia (01:31 UTC, Dorohusk); izin tembak ditahan; NATO kerahkan AWACS |
| Ukraina | Drones strike a Russian warship at a Libyan base; a refinery burns in Russia | Drone laut Ukraina hantam kapal perang Rusia di pangkalan Libya; kilang Novoshakhtinsk terbakar |
| Iran | Attack put off until January; oil falls 4% as U.S. sanctions Iran's banking network | Trump tunda serangan ke Iran sampai 1 Jan; minyak -4,11%; sanksi AS ke jaringan bank Iran |
| Pasar | Nikkei +4.4%, Kospi +7% as Huang's return revives the AI rally; SoftBank +8% | Nikkei +4,4% (58.920), Kospi +7%, S&P +4,7%, Nasdaq +6,9%; Nvidia +31% |
| Meksiko | Mexico to prosecute the cartel boss at home, defying a U.S. extradition request | Meksiko adili El Chapo Isidro di dalam negeri, tolak ekstradisi AS |
| Sudan | RSF drones strike power stations; mass blackouts across Sudan | Drone RSF hantam stasiun listrik; pemadaman massal |
| India | Flash flood tears down a mountain valley; about 100 unaccounted for | Banjir bandang Himalaya, ≥4 tewas, ~100 hilang |
| Korea Selatan | Jets scramble after a Russian airspace breach | Peringatan serangan udara; jet dikerahkan setelah pelanggaran Rusia |
| Also today | ECB: Lagarde resigns; Brazil: storm displaces thousands; Congress: first Gen Z woman elected | Lagarde mundur; badai Brasil; Melat Kiros (29) wanita Gen Z pertama di Kongres AS |

## Yang sengaja tidak dipakai
- **700.000 tentara Rusia tewas (Meduza/Mediazona)** — investigasi besar, TAPI dipublikasikan Senin 23 Nov, bukan 24 Nov.
- **Nvidia kembalikan Jensen Huang** — diumumkan Senin 23 Nov; yang dipakai adalah reaksi pasar 24 Nov (reli Nikkei/Kospi).
- **COP31 runtuh** — berita 23 Nov (lead poster kemarin).

## Verifikasi
- Ukuran: 1024×1024, 137.597 byte ≤ 1.048.576 ✓
- Determinisme: draw 2× → sha256 sama `bf51716f…1df434e`; main.py (MAKEFUN_OUTPUT_DIR berbeda) → sha256 sama ✓
- Cek visual penuh: semua teks terbaca, tanpa typo, tanpa tumpang tindih. Perbaikan dari draft pertama: headline lead dipendekkan ("IN NATO AIRSPACE", tadinya "BREACHES NATO AIRSPACE" menabrak ikon radar); ikon chart dibalik naik (tadinya turun — bertentangan dengan headline reli pasar); fakta lead dipendekkan (tadinya yatim "AWACS."); headline Korea dipendekkan (tadinya fakta menabrak footer); strip "U.S. CONGRESS" dipendekkan jadi "CONGRESS" (tadinya "elected" mepet tepi).
- Cek 300px: masthead, tanggal, headline lead + headline panel dan struktur koran tetap terbaca; teks fakta kecil (wajar untuk format koran)

## Repo
- https://github.com/Rahullpc/news-image-20261124
- HEAD: `70168bc2ca203cf1dcc865fa1c1293989b23b52c`
- Isi: LICENSE (MIT), README.md (3 badge live make.fun + link bounty), main.py, entry.png, draw_poster.py, RESEARCH.md
- About: homepage = https://make.fun/bounty/news-image-20261124, topics = ai-agents, bounties, infographic, makefun, news, python (sudah di-set SEBELUM submit, pelajaran dari penolakan 422 edisi 23 Nov)

## Submit — MENUNGGU PERSETUJUAN BOS
- Belum ada submission id/claim. Setelah bos menyetujui poster dengan kata-katanya sendiri: download kit news-image-20261124, cek kuota @vjev (cap 3 entri/kompetisi), bangun bundle (recipe edisi 23 Nov, parent session 319594c3-e1ba-4eec-bcdc-eb2c0bde2d4f TRIM dulu, prompt-file = satu pesan verbatim bos), lalu submit via kit CLI.
- Deadline entries: 26 Nov 2026 07:00 WIB. Escrow: belum dicek (cek saat submit).
- Ekspektasi hadiah $1,20–$2 (top 50), bukan $20 — peluang juara 1 rendah (lapangan 4.838+ entri, juri AI noisy, blind rounds), sesuai laporan tahap 1.
