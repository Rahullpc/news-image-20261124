"""Salin poster berita hari ini ke folder keluaran.

Ini entrypoint untuk bounty news-image-20261124: program menyalin
berkas entry.png yang sudah ada di repositori (satu folder dengan
berkas ini) ke /output/entry.png, tempat grader membacanya. Posternya
sendiri sudah final dan disetujui, jadi tidak ada gambar yang digambar
ulang di sini — tugas program hanyalah menyalin byte demi byte, secara
deterministik, tanpa jaringan dan tanpa acak.
"""

import hashlib
import os
import shutil
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    size = source.stat().st_size
    if size > 1_048_576:
        raise SystemExit(f"entry.png {size} byte melebihi batas 1 MiB")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if _sha256(source) != _sha256(target):
        raise SystemExit("salinan entry.png tidak identik dengan aslinya")
    print(f"entry.png disalin: {size} byte -> {target}")


if __name__ == "__main__":
    main()
