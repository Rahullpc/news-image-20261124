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

## Rencana build
- Layout (sama seperti edisi 23 Nov yang lolos semua cek): header masthead "THE WORLD — TUESDAY 24 NOVEMBER 2026" + lead penuh (Polandia) + grid 2 kolom × 3 baris (Ukraina, Iran, Pasar, Meksiko, Sudan, India) + strip bawah (Korea Selatan + ALSO TODAY: ECB, Brasil, Kongres AS).
- Tiap panel: pictogram sederhana + headline pendek + 1 baris fakta (angka/tempat). Warna: kertas koran terang, aksen merah/biru per kategori.
- Render: program Python stdlib + PIL, 1024×1024, ≤1 MiB, byte-identik di 2 run (main.py menyalin entry.png yang di-commit).
- Repo baru Rahullpc/news-image-20261124, README 3 badge live + About "makefun", bundle transkrip + submit (hanya setelah bos menyetujui poster).
