# news-image-20261124 — TAHAP 1 (riset + penilaian, 24 Nov 11:40 WIB)

## Fakta bounty
- Judul: "Sum up 24 November's world news in one image"
- Hadiah: $100 total, 50 tempat — 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20. USDC Solana, escrow at open.
- Deadline: 2026-11-26T00:00:00Z = **26 Nov 2026 07:00 WIB**. Buka 24 Nov 00:00Z (07:00 WIB).
- Entry: program main.ts (Node 22) atau main.py (Python 3.13) di root repo; menulis /output/entry.png. PNG/JPEG ≤1 MiB, ≤1024×1024. No network; 2 run harus byte-identik. Stdlib only.
- Caps: max 10/hari, 20 total. Last submission = final.
- Juri: AI z-ai/glm-5.3-flash (OpenRouter), pairwise, margin 1–5, dua arah, blind rounds (sama seperti edisi 23 Nov).
- Kriteria berurutan: (1) menamai hari + peristiwa spesifik hari itu; (2) seleksi & keluasan lintas wilayah/bidang; (3) keterbacaan — penonton bisa tahu apa yang terjadi hanya dari gambar; (4) setia fakta, tanpa hype; (5) craft — komposisi jelas, terbaca di ~300px, tanpa teks rusak.
- Transkrip wajib (thinking_in_window: sesi mulai ≥ pembukaan 24 Nov 00:00Z). Repo harus dibuat setelah pembukaan, lisensi OSI, publik.
- Status API (dicek parent 24 Nov 11:30 WIB): open, sudah 4.838 entri masuk.

## Shortlist berita 24 Nov 2026 (terverifikasi dari Reuters, WSJ, TradingView, h.ua, Access24, C54)
1. POLANDIA — Drone Rusia melanggar wilayah udara Polandia saat serangan malam ke Ukraina barat (01:31 UTC, dekat Dorohusk, Lublin). Polandia aktifkan pertahanan udara; izin tembak diberikan lalu ditahan saat drone berbelok ke timur (risiko sipil). NATO kerahkan pesawat AWACS ke Polandia. Konteks: 3 rudal Kh-101 mendarat di Polandia Jumat 20 Nov.
2. UKRAINA — Drone laut Ukraina menghantam kapal perang Rusia di pangkalan angkatan laut Libya (Zelenskyy); kilang Novoshakhtinsk terbakar setelah serangan drone Ukraina; puing drone jatuh di Kyiv tengah, 5 luka.
3. IRAN — Trump menunda rencana serangan ke Iran sampai 1 Januari; harga minyak jatuh 4,11% (WTI $79,98). AS menjatuhkan sanksi ke jaringan perbankan bawah tanah Iran.
4. PASAR — Nikkei +4,4% (58.920), Kospi +7%, S&P 500 +4,7%, Nasdaq +6,9% — reli Asia pasca kembalinya Jensen Huang ke Nvidia (saham Nvidia +31%); SoftBank +8%, Samsung +9%.
5. MEKSIKO — Meksiko akan mengadili El Chapo Isidro di dalam negeri, menolak permintaan ekstradisi AS; pemerintah Meksiko menangkap satu lagi bos narkoba besar.
6. SUDAN — Drone RSF menghantam stasiun listrik; pemadaman massal di Sudan. Serangan drone menewaskan 4 orang di kota Chad dekat Sudan.
7. INDIA — Banjir bandang Himalaya: sedikitnya 4 tewas, ~100 hilang di lembah pegunungan.
8. KOREA SELATAN — Peringatan serangan udara, jet tempur dikerahkan setelah "pelanggaran" Rusia.
9. ECB — Christine Lagarde mengundurkan diri; UE mulai mencari kepala ECB baru.
10. BRASIL — Badai mematikan: ribuan orang mengungsi.
11. KONGRES AS — Melat Kiros, 29, Demokrat sosialis, wanita Gen Z pertama yang masuk Kongres AS.
12. GAZA — Serangan drone Israel menewaskan 3 warga Palestina di pos polisi Gaza.

## Yang SENGAJA tidak dipakai
- **700.000 tentara Rusia tewas (Meduza/Mediazona, data bocor Rosstat)** — investigasi besar hari ini, TAPI dipublikasikan Senin 23 Nov (bukan 24 Nov). Juri menilai peristiwa hari itu; memasukkannya berisiko dianggap peristiwa hari sebelumnya.
- **Nvidia kembalikan Jensen Huang sebagai CEO** — diumumkan Senin 23 Nov 14:24 GMT. Yang dipakai sebagai gantinya adalah reaksi pasar 24 Nov (Nikkei/Kospi reli) — itu peristiwa 24 Nov.
- **COP31 runtuh** — itu berita 23 Nov (lead poster kemarin). Tindak lanjut 24 Nov hanya analisis, bukan peristiwa baru.

## Penilaian juara 1 (jujur, sama seperti edisi 23 Nov)
- YANG BISA KITA KENDALIKAN: poster koran/infografik 1024×1024 yang bersih — tanggal besar "TUESDAY 24 NOVEMBER 2026", lead Polandia + 6 panel + strip bawah, pictogram sederhana + caption 1-2 baris yang akurat, tipografi bersih, terbaca di 300px. Persis kriteria juri.
- CATATAN PENTING: juri bilang "Detail for its own sake does not count" — poster yang terlalu padat justru berisiko kalah di keterbacaan & craft. Jadi "rich/busy" di sini = banyak cerita tapi tiap panel sederhana dan terbaca, bukan hiasan menumpuk.
- YANG TIDAK BISA KITA KENDALIKAN: lapangan sangat besar (4.838 entri dan terus bertambah); juri satu model kecil (glm-5.3-flash) tanpa feed berita — penilaiannya noisy; blind rounds = tidak ada feedback dev, submit buta.
- PELUANG JUARA 1: rendah. Poster kelas atas bisa dibuat (peluang top 50 / dapat hadiah $1,20–$20 cukup masuk akal), tapi juara 1 di antara ribuan entry dengan juri yang noisy pada dasarnya lotre — perkiraan kasar hanya beberapa persen.
- Bos sudah memutuskan MASUK (24 Nov 11:32 WIB) — bangun 1 poster terbaik dan submit 1x, dengan ekspektasi hadiah $1,20–$2, bukan $20.

## TAHAP 2 — Cross-check + perbaikan (24 Nov ~12:00 WIB, atas perintah bos "crosscheck perbaiki dulu sebagus mungkin")

Verifikasi ulang tiap cerita v1 dari sumbernya + cek berita live 24 Nov 11:40–12:00 WIB (Reuters, WSJ, TradingView, h.ua, Al Jazeera, AFP, The Guardian, AP). Tanggal 24 Nov 2026 = Selasa, terverifikasi `date -d`.

| Cerita v1 | Hasil | Keputusan |
|---|---|---|
| Lead Polandia/NATO | ✅ Terverifikasi 24 Nov (Reuters 24 Nov: drone langgar wilayah udara Polandia 01:31 UTC dekat Dorohusk, Lublin; izin tembak ditahan; NATO kerahkan AWACS) | PERTAHANKAN |
| Ukraina/Libya | ⚠️ Peristiwa 22 Nov, diumumkan 23 Nov; WSJ terbitkan laporan mendalam 24 Nov | PERTAHANKAN (pengumuman 23 Nov + liputan 24 Nov; cerita utama siklus berita 24 Nov) |
| Iran "tunda sampai 1 Jan" | ⚠️ Framing 1 Jan dari pernyataan 19–22 Nov; minyak -4% adalah pergerakan 23 Nov | REFRAME ke sudut 24 Nov: Trump sebut serangan baru "quite unlikely" (Senin); minyak ke titik terendah 3 bulan (Selasa); sanksi AS ke shadow bank Iran |
| Pasar "SoftBank +8%" | ❌ SALAH — SoftBank +4,99% (TradingKey); Nikkei +4,4%→+4,5% dan Kospi +7%→+7,5% (penutupan Reuters 24 Nov) | PERBAIKI angka; ganti SoftBank → Samsung +8% (intraday 24 Nov +8,2–8,3% di beberapa sumber) |
| Meksiko | ✅ Terverifikasi (Reuters 23 Nov; Al Jazeera 24 Nov) | PERTAHANKAN |
| Sudan (pemadaman) | ❌ TANGGAL SALAH — cerita Al Jazeera 2 Nov 2026 | GANTI → Gaza |
| India (banjir Himalaya 4 tewas, ~100 hilang) | ❌ TANGGAL SALAH — AFP 6 Agu 2025 (Dharali, Uttarakhand) | GANTI → Indonesia (kebakaran pabrik) |
| Korea "airspace breach" | ❌ FAKTA SALAH — JCS: TIDAK ada pelanggaran wilayah udara; pesawat Rusia masuk KADIZ saja; alert dicabut dalam 5 menit | PERBAIKI kata: "defence zone", tanpa kata "breach" |
| ALSO TODAY ECB | ❌ TANGGAL SALAH — Lagarde umumkan mundur 29 Okt 2026 | GANTI → EU sanksi Rusia |
| ALSO TODAY Brasil | ❌ TANGGAL SALAH — badai Tupanciretã 20 Nov | GANTI → UN AI rules |
| ALSO TODAY Kongres AS | ❌ TANGGAL SALAH — Melat Kiros terpilih 3 Nov 2026 | GANTI → SPORT NZ vs India |

Cerita pengganti (terverifikasi):
- **GAZA** — Reuters (Kairo, 24 Nov): serangan udara Israel tewaskan ≥3 warga Palestina di dekat pos polisi Khan Younis, 5 luka. Al Jazeera 24 Nov: "Israeli drone attack targets police post in Gaza's Khan Younis".
- **INDONESIA** — Reuters 23 Nov + laporan 24 Nov (r24.mv, 24 Nov 04:18 UTC): kebakaran pabrik permen PT Fonusa Agung Mulia, Cikande, Banten, Sabtu 21 Nov; 24 tewas dikonfirmasi Senin 23 Nov; ~30 masih hilang; pencarian berlanjut Selasa 24 Nov; tes DNA untuk identifikasi korban.
- **EU** — European Commission mengusulkan paket sanksi ke-22 terhadap Rusia, Senin 23 Nov (dilaporkan 24 Nov): larang tim Rusia tampil di bawah bendera Rusia di acara UE; sasar bank, platform kripto, eks-kombatan.
- **UN** — Sekjen PBB António Guterres, Senin 23 Nov di Bridgetown Special Summit on AI Safety, Barbados (dilaporkan 24 Nov): serukan negara anggota sepakati kerangka global manajemen risiko AI dalam setahun.
- **SPORT** — Test pertama India vs Selandia Baru, Wellington, berakhir imbang Senin 23 Nov (reaksi/liputan 24 Nov): NZ 368 & 239/5 (Mitchell 49*, Phillips 26*); India 720/9 declared.

Catatan kejujuran: koran 24 Nov wajar memuat pengumuman 23 Nov (Libya, Meksiko, Iran, EU, UN, Test) — semuanya dilaporkan/berkembang lagi 24 Nov. Yang diganti adalah cerita yang tanggalnya meleset berminggu-minggu/bulan/tahun (Sudan 2 Nov, India Agu 2025, ECB 29 Okt, Brasil 20 Nov, Kongres 3 Nov) dan fakta yang salah (SoftBank +8%, "breach" Korea).

## TAHAP 3 — Audit ketat tanggal KEJADIAN (24 Nov ~12:00–12:20 WIB, atas perintah bos "Perbaiki lagi" 11:51 WIB)

Standar baru: **hanya peristiwa yang TERJADI persis Selasa 24 Nov 2026** — bukan "dilaporkan 24 Nov" atau "diumumkan 23 Nov". Audit ini menemukan kesalahan besar v2: **lead Polandia ternyata peristiwa Senin 23 Nov malam**.

### Koreksi besar: lead Polandia GUGUR
- Bukti: peta OSINT (23 Nov): drone masuk wilayah udara Polandia dekat Dorohusk **~23:00 CET 23 Nov**. Pernyataan Polish Operational Command **22:53 UTC 23 Nov** (pertahanan udara Polandia + NATO disiagakan); misi **berakhir 01:31 UTC 24 Nov** — jam 01:31 UTC adalah saat misi SELESAI, bukan saat insiden. Daily Mail: "Russian drone entered Polish airspace on Monday evening". h.ua 1:31 AM UTC 24 Nov = jam publikasi, bukan jam kejadian.
- Kesimpulan: insiden terjadi **Senin 23 Nov ~23:00 CET**; yang terjadi Selasa dini hari hanyalah penutupan misi + laporan berita. **Lead Polandia GUGUR** — diganti lead Korea KADIZ.

### Audit semua panel v2 (tanggal KEJADIAN)
| Panel v2 | Tanggal kejadian | Keputusan |
|---|---|---|
| Lead Polandia/NATO | ❌ Senin 23 Nov ~23:00 CET | GANTI → lead Korea KADIZ |
| Libya (kapal perang) | ❌ Sabtu 22 Nov (serangan); diumumkan 23 Nov | GANTI → Zaporizhzhia |
| Iran "strikes unlikely" | ⚠️ Pernyataan Trump Senin 23 Nov; "oil 3-month low" TIDAK terverifikasi (minyak jatuh Senin −4%, Selasa bertahan ~$80) | GANTI → Hasina |
| Pasar (Nikkei/Kospi/Samsung) | ✅ Penutupan Selasa 24 Nov (Reuters); Samsung +8% intraday TIDAK terkonfirmasi di penutupan (AP 7,5%, WSJ 6,5%) | PERTAHANKAN, angka diganti: Taiwan +9,1% (Reuters close) ganti Samsung |
| Meksiko (El Chapo Isidro) | ❌ Keputusan AG Meksiko Senin 23 Nov | GANTI → Catur Dunia |
| Gaza | ✅ Selasa 24 Nov (Reuters Kairo) | PERTAHANKAN |
| Indonesia (Cikande) | ❌ Kebakaran Sabtu 21 Nov; 24 tewas dikonfirmasi Senin 23 Nov; pencarian berlanjut Selasa | GANTI → Minyak |
| Korea (strip bawah) | ✅ Selasa pagi 24 Nov | NAIK JADI LEAD |
| ALSO TODAY EU sanksi | ❌ Senin 23 Nov | GANTI → BOK |
| ALSO TODAY UN AI | ❌ Senin 23 Nov | GANTI → Bali Jatra |
| ALSO TODAY NZ–India | ❌ Senin 23 Nov (imbang) | GANTI → Megafire |

### Cerita pengganti v3 (semua peristiwa Selasa 24 Nov — sumber + tanggal kejadian)
- **LEAD — S. KOREA (KADIZ):** Reuters Seoul, 24 Nov: "South Korean military jets scrambled on Tuesday morning" setelah pesawat militer Rusia masuk KADIZ; alert serangan udara Ulleung 07:52 KST dicabut dalam ~5 menit; JCS: tidak ada pelanggaran wilayah udara; attaché militer Rusia dipanggil Selasa. Ikon jet.
- **UKRAINA — Zaporizhzhia:** Reuters, 24 Nov: serangan Rusia semalam ke Zaporizhzhia tewaskan 2, lukai 22 termasuk 2 anak; Gubernur Fedorov di Telegram: "on Tuesday". Ikon missile.
- **BANGLADESH — Hasina:** Reuters, 24 Nov: juru bicara bilang ke Reuters "on Tuesday" — Sheikh Hasina berencana kembali 16 Desember dengan penerbangan Biman Bangladesh Airlines setelah 2 tahun di pengasingan di India. Ikon globe.
- **PASAR:** Reuters close, Selasa 24 Nov: Nikkei +4,5%, Kospi +7,5%, Taiwan +9,1% (reli AI pasca kembalinya Jensen Huang). Ikon chart.
- **CATUR — Jenewa:** FIDE / Reuters, Selasa 24 Nov: Game 1 Kejuaraan Dunia Catur dimulai 15:00 CET, Jenewa; Gukesh (juara bertahan) vs Sindarov, keduanya 20 tahun; hadiah $2,5 juta. Ikon pawn (baru).
- **GAZA:** Reuters Kairo, 24 Nov: ≥3 tewas, 5 luka di dekat pos polisi Khan Younis. Ikon missile.
- **MINYAK:** Bloomberg (via DailyFoxNews, diperbarui 24 Nov): WTI bertahan ~$80, Brent di atas $89 setelah jatuh ~4% Senin; pasar menunggu nasib pembicaraan AS–Iran. Ikon droplet (baru).
- **STRIP BAWAH — JEPANG PMI:** dpa-AFX, Selasa 24 Nov: flash manufacturing PMI Jepang November 53,7 (naik dari 51,0 Oktober; konsensus 51,5) — tercepat dalam 44 bulan; flash services 52,7; composite 52,9. Ikon chart.
- **ALSO TODAY — BOK:** Reuters, Selasa 24 Nov: jajak pendapat — Bank of Korea diperkirakan naikkan suku bunga Kamis (25 dari 33 ekonom).
- **ALSO TODAY — Bali Jatra:** Festival Bali Jatra dibuka Selasa 24 Nov di Cuttack, Odisha (24 Nov–1 Des, Kartika Purnima); Presiden Droupadi Murmu meresmikan sore ini (17:00–20:15). Sumber: katakabalijatra.com + liputan 24 Nov (skycmedia, Odisha News Today). Catatan: satu artikel NIE menulis "on Monday" — salah label; semua sumber lain (jadwal resmi distrik + kunjungan Presiden 24–25 Nov) menegaskan pembukaan 24 Nov.
- **ALSO TODAY — Megafire:** Newshub / UNSW, Selasa 24 Nov: UNSW + Fire Rescue NSW meluncurkan simulator kebakaran besar (iFire 2.3) — teknologi pertama di dunia untuk melatih pemadam menghadapi kebakaran ekstrem.

### Yang dipertimbangkan tapi tidak dipakai sebagai pengganti
- Libya (22 Nov), Iran (Senin 23 Nov), Meksiko (Senin 23 Nov), Cikande (Sabtu 21 Nov) — semua gagal standar ketat.
- Australia CPI (rilis Rabu 25 Nov), India–Nepal MoU (Senin 23 Nov), CrowdStrike–Zscaler $43,9 miliar (Senin 23 Nov), NATO space (Senin 23 Nov), ICE Seattle (Sabtu 21 Nov), Sparta II (Sabtu 21 Nov).
- Catur: Game 1 dimulai Selasa 21:00 WIB (15:00 CET) — saat poster dibuat (siang WIB) pertandingan BELUM dimulai; panel ini adalah peristiwa terjadwal hari itu, bukan hasil. Dicatat jujur sebagai titik terlemah bersama panel Minyak (pola pasar, bukan peristiwa diskret).

## Rencana build
- Layout (sama seperti edisi 23 Nov yang lolos semua cek): header masthead "THE WORLD — TUESDAY 24 NOVEMBER 2026" + lead penuh (Polandia) + grid 2 kolom × 3 baris (Ukraina, Iran, Pasar, Meksiko, Sudan, India) + strip bawah (Korea Selatan + ALSO TODAY: ECB, Brasil, Kongres AS).
- Tiap panel: pictogram sederhana + headline pendek + 1 baris fakta (angka/tempat). Warna: kertas koran terang, aksen merah/biru per kategori.
- Render: program Python stdlib + PIL, 1024×1024, ≤1 MiB, byte-identik di 2 run (main.py menyalin entry.png yang di-commit).
- Repo baru Rahullpc/news-image-20261124, README 3 badge live + About "makefun", bundle transkrip + submit (hanya setelah bos menyetujui poster).
