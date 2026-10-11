"""Export editable JPG and standalone WAV versions of Exhale's generated sounds.
Install numpy and Pillow only if you want to regenerate these assets.
The website itself needs neither Python nor these packages.
"""
from pathlib import Path
import wave
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
SR=44100
(ROOT/'audio').mkdir(exist_ok=True)
def save(name,data):
    samples=np.clip(data,-1,1)
    with wave.open(str(ROOT/'audio'/name),'wb') as f:
        f.setnchannels(1);f.setsampwidth(2);f.setframerate(SR)
        f.writeframes((samples*32767).astype('<i2').tobytes())
Image.open(ROOT/'room.png').convert('RGB').save(ROOT/'room.jpg',quality=95,optimize=True)
# A four-chord loop based on the browser's sine-wave score, including release tails.
length=round(28.8*SR); melody=np.zeros(length)
chords=[[130.81,196,261.63,329.63],[110,164.81,220,329.63],[87.31,174.61,261.63,349.23],[98,196,293.66,392]]
def note(freq,start,duration,volume):
    t=np.arange(round(duration*SR))/SR
    envelope=np.where(t<.09,volume*t/.09,volume*np.exp(np.log(.0001/volume)*(t-.09)/(duration-.09)))
    signal=np.sin(2*np.pi*freq*t)*envelope
    indices=(np.arange(len(t))+round(start*SR))%length
    np.add.at(melody,indices,signal)
for c,chord in enumerate(chords):
    for i,f in enumerate(chord):note(f,c*7.2+i*.12,7,.055)
    for i,n in enumerate([0,2,3,2]):note(chord[n]*2,c*7.2+i*1.5,3.8,.07)
save('soft-melodies.wav',melody)
# Periodic filtered noise with the same smoothing and low-pass character as the app.
n=SR*12;rng=np.random.default_rng(26);white=rng.uniform(-.02,.02,n)
freq=np.fft.rfftfreq(n,1/SR);omega=2*np.pi*freq/SR
transfer=7/(1.02-np.exp(-1j*omega));lowpass=1/(1+1j*freq/1100)
rain=np.fft.irfft(np.fft.rfft(white)*transfer*lowpass,n)
save('window-rain.wav',rain)
t=np.arange(round(1.7*SR))/SR
env=.02*np.exp(np.log(.0001/.02)*np.minimum(t,1.6)/1.6)
purr=np.sin(2*np.pi*65*t)*(env+.012*np.sin(2*np.pi*24*t))
purr*=np.minimum(t/.015,1)*np.minimum((1.7-t)/.08,1)
save('cat-purr.wav',purr)
print('Exported room.jpg and three WAV files.')
