# טריטוריה/יות · deck

An HTML presentation of three territories from the Miro board "to boldly go – טריטוריות".

- **Lecturers version:** `index.html`. Slide 2 shows the 3D board snapshot without a link.
- **Classroom version:** `class.html`. Slide 2 links to the live 3D board at https://lukori.github.io/territories/.

`class.html` is generated from `index.html`. To change it, edit `index.html`, then run `python3 make_class.py`.

## Presenting
- Space or → goes forward. ← goes back. `f` toggles full screen.
- Slide 3 is the hub. Space or a click tosses the coin. Saying "עוד פעם" tosses it again; this needs Chrome or Safari and internet.
- The invisible square in the top-right corner of the hub switches between three and two territories.
- The titles on the hub open the territories. Leaving any territory page returns to the hub.
- The invisible area below the hub titles, halfway to the bottom of the page, opens the closing slide.

To present locally, run `python3 serve.py` and open http://localhost:8780/.
Everything works offline except the voice trigger and the YouTube film.
