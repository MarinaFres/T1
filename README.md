Primera tasca APA 2023: Anàlisi fitxer de so
============================================

## Nom i cognoms: Marina Fresneda Manzano



## Representació temporal i freqüencial de senyals d'àudio.

### Domini temporal

Per llegir, escriure i representar un fitxer en format `*.wav` en python podem fem servir els següents mòduls:

- Numpy:
```python
import numpy as np
```
- Matplotlib: 
```python
import matplotlib.pyplot as plt
```
- Soundfile:
```python
import soundfile as sf
```

Per **crear** i **guardar** a un fitxer un senyal sinusoidal de freqüència `fx Hz`, digitalitzat a `fm Hz`, de durada `T` segons i amplitud 
`A` fem:

```python
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
```

El resultat és un fitxer guardat al directori de treball i que es pot reproduir amb qualsevol reproductor d'àudio

Per **representar** gràficament 5 períodes de senyal fem:

```python
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
```

El resultat del gràfic és:

<img src="img/sinusoide.png" width="480" align="center">

> Nota: Si es treballa amb ipython, es pot escriure %matplotlib i no cal posar el plt.show() per veure gràfics

El senyal es pot **escoltar (reproduir)** directament des de python important un entorn de treball amb els dispositius de so, com per 
exemple `sounddevice`:

```python
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
```

### Domini transformat

Domini transformat. Els senyals es poden analitzar en freqüència fent servir la Transformada Discreta de Fourier. 

La funció que incorpora el paquet `numpy` al submòdul `fft` és `fft`:

```python
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
```

I podem representar el mòdul i la fase, en funció de la posició de cada valor amb:

```python
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics
```

<img src="img/TF.png" width="480" align="center">

Proves i exercicis a fer i entregar
-----------------------------------

1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera $f_x = 4$ kHz, a banda d'una
    freqüència pròpia en el marge audible. Comenta els resultats.

    ```python
    T= 2.5                               
    fm=8000                              
    fx=4000                              
    A=4                                  
    pi=np.pi                             
    L = int(fm * T)                      
    Tm=1/fm                              
    t=Tm*np.arange(L)                  
    x = A * np.cos(2 * pi * fx * t)      
    sf.write('so_exemple1.wav', x, fm)   


    Tx=1/fx                                  
    Ls=int(fm*5*Tx)                           

    plt.figure(0)                        
    plt.plot(t[0:Ls], x[0:Ls])           
    plt.xlabel('t en segons')            
    plt.title('sinusoide 4K')  
    plt.show() 

    sd.play(x, fm)       
    ```
    <img src="figure_0.png" width="480" align="center">

    ```python           
    N=5000                     
    X=fft(x[0 : Ls], N)        

    k=np.arange(N)             

    plt.figure(1)              
    plt.subplot(211)           
    plt.plot(k,abs(X))         
    plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
    plt.ylabel('|X[k]|')   
    plt.subplot(212)       
    plt.plot(k,np.unwrap(np.angle(X))) 
    plt.xlabel('Index k')               
    plt.ylabel('$\phi_x[k]$')          
    plt.show()     
    ``` 
    <img src="figure_1.png" width="480" align="center">  


    ```python
    T= 2.5                              
    fm=8000                              
    fx=800                              
    A=4                                 
    pi=np.pi                             
    L = int(fm * T)                      
    Tm=1/fm                             
    t=Tm*np.arange(L)                    
    x = A * np.cos(2 * pi * fx * t)      
    sf.write('so_exemple2.wav', x, fm)   


    Tx=1/fx                                  
    Ls=int(fm*5*Tx)                           

    plt.figure(2)                           
    plt.plot(t[0:Ls], x[0:Ls])                
    plt.xlabel('t en segons')               
    plt.title('5 periodes de la sinusoide 800Hz')   
    plt.show()                               


    sd.play(x, fm)              
    ```
    <img src="figure_2.png" width="480" align="center">  


    ```python
    N=5000                     
    X=fft(x[0 : Ls], N)           

    k=np.arange(N)                        

    plt.figure(3)                         
    plt.subplot(211)                      
    plt.plot(k,abs(X))                    
    plt.title(f'Transformada del senyal de 800Hz')   
    plt.ylabel('|X[k]|')                  
    plt.subplot(212)                     
    plt.plot(k,np.unwrap(np.angle(X)))   
    plt.xlabel('Index k')                 
    plt.ylabel('$\phi_x[k]$')             
    plt.show()
    ```                
    <img src="figure_3.png" width="480" align="center"> 

     Com es por observar a la comparació de ambdues gráfiques, a una freqüència de 4kHz, la sinusoide es capaz de realitzar 5 periodes en en un temps de 1.1ms, mentre que a 800Hz triga aproximadament uns 6ms. 
     Ambdues tenen una amplitud de 4 unitats com s'estableix previament al codi python en la formació de les mateixes. 
     A les transformades de Fourier es pot observar un pic a 2500 al módul de la sinusoide de 4kHz i lòbuls secundaris simètricament dstribuits. 
     A la sinusoide de 800Hz, hi ha dos lóbuls principals a 500Hz i 2500hz simètrics.

2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat 
    (`x_r, fm = sf.read('nom_fitxer.wav')`).

    ```python
    x_r, fm = sf.read('so_exemple2.wav')

    fx=fm/10
    Tx = 1/fx                                                
    Tm=1/fm                           
    t=Tm*np.arange(len(x_r))                
    Ls=int(fm*5*Tx)                           

    plt.figure(4)                             
    plt.plot(t[0:Ls], x_r[0:Ls])                
    plt.xlabel('t en segons')               
    plt.title('5 periodes de la sinusoide 800Hz')   
    plt.show()
    ```
    <img src="figure_4.png" width="480" align="center"> 


    ```python                                      
    N=5000                     
    X=fft(x[0 : Ls], N)           

    k=np.arange(N)                        

    plt.figure(5)                         
    plt.subplot(211)                      
    plt.plot(k,abs(X))                    
    plt.title(f'Transformada del senyal')   
    plt.ylabel('|X[k]|')                  
    plt.subplot(212)                     
    plt.plot(k,np.unwrap(np.angle(X)))   
    plt.xlabel('Index k')                 
    plt.ylabel('$\phi_x[k]$')             
    plt.show()
     ```

    - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

    <img src="figure_5.png" width="480" align="center"> 

    - Explica el resultat del apartat anterior.
    Les gràfiques d'aquest apartat juntament amb l'anterior, ja que es tracten de la mateixa sinusoide de 800Hz, presenten la mateixa informació del senyal. A diferència de la saturació a la gràfica de representació del senyal, segurement deguda a qualque error de càlcul amb les variables llegides. 

3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de
    $0$ a $f_m/2$ en Hz.
    ```python  
    N=5000     
    k=np.arange(N)  
                
    X=fft(x[0 : L], N)           

    XdB = 20*np.log10(np.abs(X)/max(np.abs(X)))
    fk = k[0:N//2+1]*fm/N        

    plt.figure(6)                         
    plt.subplot(211)                      
    plt.plot(fk,XdB[0:N//2+1])                    
    plt.title(f'Transformada del senyal')   
    plt.ylabel('|dB|')                  
    plt.subplot(212)                     
    plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))   
    plt.xlabel('Hz')                 
    plt.ylabel('$\phi_x[k]$')             
    plt.show() 
    ```  
    <img src="figure_6.png" width="480" align="center"> 

    - Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.
    Com es pot observar a la gràfica de la transformada de Fourier, hi ha un pic de 800Hz, és a dir, la freqüència fonamental, que és la freqüència de la sinusoide creada. 

    - Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada? Comprova-ho amb el senyal generat.
    No es pot identificar, ja que la representació es troba normalitzada, és a dir, està dividida entre el valor màxim de la transformada.

> NOTES:
>
> - Per representar en dB has de fer servir la fórmula següent:
>
> $X_{dB}(f) = 20\log_{10}\left(\frac{\left|X(f)\right|}{\max(\left|X(f)\right|}\right)$
>
> - La relació entre els valors de l'índex k i la freqüència en Hz és:
>
> $f_k = \frac{k}{N} f_m$

4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). 
    Llegeix el fitxer d'àudio i comprova:

    - Freqüència de mostratge.
    - Nombre de mostres de senyal.
    ```python
    sf.info('Audio_mono.wav')

    Audio_mono.wav
    samplerate: 44100 Hz
    channels: 1
    duration: 28.294 s
    format: WAV (Microsoft) [WAV]
    subtype: Signed 16 bit PCM [PCM_16]
    ``` 

    - Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    ```python
    x_r, fm = sf.read('Audio_mono.wav')
    info= sf.info('Audio_mono.wav')

    T= 0.025
    L = int(fm * T)                      
    Tm=1/fm                             
    t=Tm*np.arange(L)                    
                                                    
    plt.figure(7)                           
    plt.plot(t[0:L], x_r[0:L])                
    plt.xlabel('t en segons')               
    plt.title('Audio mono 25ms')   
    plt.show()  
    ```
    <img src="figure_7.png" width="480" align="center"> 

    - Representa la seva transformada en dB en funció de la freqüència, en el marge $0\le f\le f_m/2$.
    ```python
    N=5000                     
    X=fft(x_r[0 : L], N)           
    k=np.arange(N)    

    XdB = 20*np.log10(np.abs(X)/max(np.abs(X))) 
        
    fk = k[0:N//2+1]*fm/N               

    plt.figure(7)                         
    plt.subplot(211)                      
    plt.plot(fk,XdB[0:N//2+1])                    
    plt.title(f'Transformada Audio mono')   
    plt.ylabel('|dB|')                  
    plt.subplot(212)                     
    plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))   
    plt.xlabel('Hz')                 
    plt.ylabel('$\phi_x[k]$')             
    plt.show() 
    ```
    <img src="figure_8.png" width="480" align="center"> 

    - Quines son les freqüències més importants del segment triat?
    En aquest cas, com es tracta d'un audio de reproducció de diferent d'un gran marge de freqüències, totes tenen una gran importància i presència.  

Entrega
-------

- L'alumne ha de respondre a totes les qüestions formulades en aquest mateix fitxer, README.md.
    - El format del fitxer es l'anomenat *Markdown* que permet generar textos amb capacitats gràfiques (com ara *cursiva*, **negreta**,
      fòrmules matemàtiques, taules, etc.), sense perdre la llegibilitat en mode text.
    - Disposa d'una petita introducció a llenguatge de Markdown al fitxer `MARKDOWN.md`.
- El repositori GitHub ha d'incloure un fitxer amb tot el codi necesari per respondre les qüestions i dibuixar les gràfiques.
- El nom del fitxer o fitxers amb el codi ha de començar amb les inicials de l'alumne (per exemple, `fvp_codi.py`).
- Recordéu ficar el el vostre nom complet a l'inici del fitxer o fitxers amb el codi i d'emplar el camp `Nom i cognoms` a dalt de tot
  d'aquest fitxer, README.md.
