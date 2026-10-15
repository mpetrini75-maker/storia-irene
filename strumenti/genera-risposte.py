r"""Registra a voce le RISPOSTE della prova d'interrogazione (prova-interrogazione.html).
genera-audio.py legge solo le domande (salta le .sol apposta); qui ogni <div class="sol" id="sN">
diventa audio/risposta-sN.mp3, che la pagina suona col tasto "Ascolta la risposta".
Nato il 15/10/2026: per Irene (DSA) leggere la risposta e' faticoso, ascoltarla no.
Uso:  py strumenti\genera-risposte.py
"""
import asyncio, re, sys
from pathlib import Path
from bs4 import BeautifulSoup
import edge_tts

R = Path(__file__).resolve().parent.parent
AUDIO = R / "audio"
VOCE, RATE, PITCH = "it-IT-ElsaNeural", "+0%", "+15Hz"   # la stessa voce di genera-audio.py


async def registra(testo, dest):
    prova = dest.with_suffix(".tmp")
    try:
        for tentativo in range(8):   # il servizio voci a volte risponde 403: si riprova
            try:
                await edge_tts.Communicate(testo, VOCE, rate=RATE, pitch=PITCH).save(str(prova))
                if prova.stat().st_size < 2000:
                    raise RuntimeError(f"{dest.name}: registrazione vuota")
                break
            except Exception:
                if tentativo == 7:
                    raise
                await asyncio.sleep(4 + 4 * tentativo)
        prova.replace(dest)
    finally:
        prova.unlink(missing_ok=True)


async def main():
    soup = BeautifulSoup((R / "prova-interrogazione.html").read_text(encoding="utf-8"), "html.parser")
    sol = soup.select("div.sol[id]")
    for s in sol:
        testo = re.sub(r"\s+", " ", s.get_text(" ")).strip()
        dest = AUDIO / f"risposta-{s['id']}.mp3"
        await registra(testo, dest)
        print(f"  {dest.name}: {len(testo)} caratteri")
    print(f"risposte registrate: {len(sol)}")

asyncio.run(main())
