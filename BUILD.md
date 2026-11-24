# news-image-20261124 — BUILD (24 Nov 11:45 WIB)

Satu poster, siap ditunjukkan ke bos. BELUM di-submit — submit hanya atas perintah eksplisit bos setelah ia melihat posternya.

## Poster
- File: [entry.png](sandbox://workspace/makefun/news-image-20261124/entry.png) — 1024×1024, 137.597 byte (≤1 MiB)
- sha256: `bf51716fb6fe1658c5058de7a1a739e6ef74a23b55e33f03350d278ee1df434e`
- Program gambar: [draw_poster.py](sandbox://workspace/makefun/news-image-20261124/draw_poster.py) (ditulis dari nol di sesi ini, PIL; deterministik — tanpa network/jam/random)
- Entrypoint: [main.py](sandbox://workspace/makefun/news-image-20261124/main.py) (stdlib only, menyalin entry.png ke /output/entry.png)

## Layout
Koran satu halaman, kertas koran terang + tinta hitam + aksen merah/navy/hijau (format sama dengan edisi 23 Nov yang lolos semua cek):
- Masthead "THE WORLD" + "TUESDAY, 24 NOVEMBER 2026" + garis merah
- Lead penuh: drone Rusia langgar wilayah udara Polandia (ikon radar) — "RUSSIAN DRONE IN NATO AIRSPACE"
- Grid 2×3: Ukraina, Iran, Pasar, Meksiko, Sudan, India — tiap panel pictogram + kicker + headline + 1 baris fakta
- Strip bawah: Korea Selatan + "ALSO TODAY" (ECB, Brasil, Kongres AS)
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
