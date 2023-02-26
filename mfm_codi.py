
# Marina Fresneda Manzano

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd    
from numpy.fft import fft    


# 1a
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav


Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('sinusoide 4K')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.


sd.play(x, fm)                # Reproducció d'àudio


N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

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


# 1b
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

# 2
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

# 3
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


# 4
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

N=5000                     
X=fft(x_r[0 : L], N)           
k=np.arange(N)    

XdB = 20*np.log10(np.abs(X)/max(np.abs(X))) 

fk = k[0:N//2+1]*fm/N               

plt.figure(8)                         
plt.subplot(211)                      
plt.plot(fk,XdB[0:N//2+1])                    
plt.title(f'Transformada Audio mono')   
plt.ylabel('|dB|')                  
plt.subplot(212)                     
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))   
plt.xlabel('Hz')                 
plt.ylabel('$\phi_x[k]$')             
plt.show() 