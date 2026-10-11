# Exhale — Complete Mobile-Friendly Website

The latest website source, original artwork, JPG copy, standalone audio exports,
and an optional asset export script. No API keys or backend required.

## Start
Extract the ZIP. Open index.html in a modern browser.
For development, use VS Code Live Server, or run this command in this folder:

    python3 -m http.server 8000

On Windows: py -m http.server 8000
Then open http://localhost:8000 .

Melodies default to ON at 50%. Rain defaults to ON at 20%.
If the browser blocks autoplay, tap the page to start both.
You can mute or change each volume. The site includes mobile and tablet layouts,
large touch targets, safe-area spacing, an animated cat and plant, window rain,
reduced-motion controls and a rest mode.

## Included files
- index.html — page structure and controls
- style.css — responsive appearance and layout
- app.js — interaction logic, audio synthesis, volume defaults and particles
- scene.js — scene animation, cat/plant touch areas and rain rendering
- room.png — original artwork used by the website
- room.jpg — JPG copy of that artwork
- audio/soft-melodies.wav — standalone export of the four-chord melody (28.8 sec)
- audio/window-rain.wav — standalone filtered rain ambience (12 sec)
- audio/cat-purr.wav — standalone synthesized purr (1.7 sec)
- tools/export_assets.py — regenerates the JPG and WAV assets
- tools/requirements.txt — dependencies only for regenerating assets

## About the audio
The website synthesizes its sounds live with the Web Audio API; there were no
external audio recordings to download. The WAV files are standalone rendered
versions based on that sound design, provided for editing or reuse. They are
not required for the website to play audio. The rain and purr exports may differ
slightly from live playback due to random noise and browser audio processing.
The WAV exports use source levels; the site's 50% / 20% defaults are applied
by app.js during live playback.

## Editing
Change labels and content in index.html; styles in style.css.
Change audio and controls in app.js; object movement and rain in scene.js.
Scene coordinates use a 1672 x 941 reference space, mapped onto the artwork.
If you replace the image, adjust the cat, plant and window coordinates too.
To use room.jpg instead, replace room.png in style.css and scene.js.

To regenerate the exported assets, install the optional tools requirements:

    python3 -m pip install -r tools/requirements.txt
    python3 tools/export_assets.py

## Hosting
Upload index.html, style.css, app.js, scene.js and room.png together to a static
website host. Keep all relative paths intact. No build command is necessary.
The downloadable copy has no login system; hosting access controls are separate.

Exported 2026-10-11 from the latest mobile-friendly version.
