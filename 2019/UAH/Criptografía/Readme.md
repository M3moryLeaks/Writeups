#### Complutum message (15pts)

##### Descripción:

PbzcyhgvHeovfHavirefvgnf

##### Solución:

Se trata del cifrado del César. Además, el propio título hace referencia de ello:

> **Complutum** era un asentamiento de la península ibérica dentro de la Tarraconense. ... El yacimiento arqueológico de Complutum es un conjunto de restos arqueológicos correspondientes a Complutum, la antigua ciudad romana sobre la que hoy se asienta Alcalá de Henares, en la Comunidad de Madrid.

Existen multitud de herramientas, para resolver esto. De las más completas y disponibles online, encontramos:

[https://www.dcode.fr/shift-cipher](https://www.dcode.fr/shift-cipher)

Obtenemos el siguiente resultado:

`COMPLUTIURBISUNIVERSITAS`

**Flag:** `flag{COMPLUTIURBISUNIVERSITAS}`

#### Alien message from XXXI century (50pts)

##### Descripción:

Hemos recibido un mensaje alienígena!! ¿Nos puedes ayudar a entenderlo?


`sha256 - alienMessage.png: 852e54e06fc4eed951ede96998fef12169c0e94cbfe6eecf20eb621eb1068748`

##### Solución:

En este caso, si el lenguaje es conocido, ya no se trata de un reto de criptografía sino de traducción, y puesto que en este caso, la [simbología es conocida](https://theinfosphere.org/Alien_languages), haremos caso omiso a esta información, y procederemos a analizarlo.

Se trata de un cifrado de sustitución simple, por lo que asignando a cada símbolo una letra, obtenemos:

`abcdef egaheii jck`

Haciendo un [análisis estadístico](https://quipqiup.com/) con diccionario inglés, obtenemos:

`planet express uah`

Dado que no hay caracteres suficientes como para realizar un análisis estadístico que recupere el texto 100%, en lo referente a los 3 últimos caracteres, `uah`, ahí jugó el papel del guessing y del sentido común.

Sin embargo, vamos a darle una vuelta y realizar suposiciones. ¿Y si el texto fuese enorme? ¿Y si no se pudiera extraerlo con facilidad?

Bien, claro que se pueden dar esos casos, por lo que también se decidió abordar el reto usando OCR y creando modelos de entrenamiento para detectar los símbolos:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/symbolDetection.png" width=350>

Ahora podemos realizar una asignación manual para realizar el modelo de entrenamiento:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/mapSymbols.png" width=350>

Y finalmente, elaboramos el script usando OCR para interpretar los símbolos de la imagen:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/scriptOcr.png" width=350>

Dándonos como resultado:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/resultOcr.png" width=350>

Verificamos que efectivamente obtenemos el mismo resultado que el mencionado anteriormente. Ahora si que sí ;)

**Flag:** flag{planetexpressuah}

#### Clásica (75pts)

##### Descripción:

En la criptografía, como en la cerveza. Siempre viene bien alguna clásica:

> sa okhbx dpejaja gc uad ei wlk tau becufwielhtkfaf effi uw sa okhbx pvmxauan ne zlm sgygjigxtbv oszvfaa fo chdohs jw btkvimdce xrhvn fo cbudls p ubyc loghmpe jw llcloedce eillscxaypfrxv hhsq k drqpqmesysg waurv gprkpcc on zlm rsmwjigxtbv oszvfaa a drrv ei gfdvr fyrngp ewgwjtq lrvomerkw f cworcr nshvjhdq nefwbge ggy sw caors wyrnl y deea hrymcairky ea epge jm hrqwa rv mmkvjv ahbugdes gff aopys sopvecwz dg vúphop psj hyipmicdmiw zfnrgnirquiw jgu lgfaqxse plhblq kghd z qeclh sqwof pvc gcszieys rq ushf hhrc va phsziqs f pcba yd dvmglvgtkfvd qsv vkv hgwof gfgmuako ootru fwxv tvnkdo ilhirvjl lc plnj fw lrurapnbrhsw ulw zop nof fpwej ibe uo lyhwer dmf bkon crs iwf vllgqaplpr siyhnkjaod fp zzsqe c va sdcvmts ke nk cruwidr 

##### Solución:

Se trata del cifrado Vigenere. Haciendo un análisis estadístico, se puede obtener tanto la clave que se utilizo para cifrar el texto como el texto en plano. Para ello, se ha utilizado la siguiente web:

[https://www.guballa.de/vigenere-solver](https://www.guballa.de/vigenere-solver)

La clave usada para cifrar: `hackandbeers`

Texto en claro:


`la mahou clasica es una de sus mas representativas bebe de la mahou original de mil ochocientos noventa de cuando se utilizaba tapon de corcho y cuya botella se elaboraba artesanalmente paso a denominarse mahou clasica en mil novecientos noventa y tres de color dorado aspecto brillante y cuerpo moderado destaca por su sabor suave y buen equilibrio en boca su aroma es ligero afrutado con tonos florales de lúpulo los principales ingredientes son levadura lupulo agua y malta somos muy clasicos en todo para la cerveza y para la criptografia por eso hemos decidido meter este bonito vigenere la flag es hackandbeers que son dos cosas que se llevan muy bien por eso delegacion organizaba el viaje a la fabrica de la cerveza`

**Flag:** flag{hackandbeers}

#### Cryptography is not steganography (150pts)

##### Descripción:

¡Que quede claro! ¡Ocultar no es cifrar!

Video: [https://drive.google.com/open?id=13eUUK7Lk9XDgSwKPArxX54cxIMSSglOd](https://drive.google.com/open?id=13eUUK7Lk9XDgSwKPArxX54cxIMSSglOd)

`sha256-harder.mp4: a472ad60a557b3d7bc2c33f74f8ba17c85faf0022e306150f61d41111fb83a1c`

##### Solución:

El vídeo como tal, no parece tener nada oculto, pero si nos fijamos en los frames del vídeo, el primer pixel aparece y desaparece. ¿Que podría ser esto? 

¡Exacto! Un mensaje en binario. Lo primero que deberemos hacer es extraer los fotogramas del vídeo:

`ffmpeg -i harder.mp4 frames/frame%04d.png`

Ahora que tenemos los frames, podemos utilizar PIL para comprobar el primer pixel de la imagen y obtener el mensaje binario:

```python
import os, sys
from PIL import Image

binary_str = ''
for idx,frame in enumerate(sorted(os.listdir('./frames'))):
    if idx == 144:
        break
    try:
        result = "./frames/" + frame
        img = Image.open(result)
        # Convert image to white and black
        img = img.convert('1')
        pix = img.load()

        if pix[0, 0] == 0:
            binary_str += '1'
        else:
            binary_str += '0'
    except Exception as e:
        print(e)

print("Binary: {}\n".format(binary_str))
n = int('0b'+binary_str, 2)
flag = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

# We add the missing '}' ;)
print("Flag: {}".format(flag+"}"))
```

Resultando:

```
Binary: 011001100110110001100001011001110111101101100100011000010110111001100011011010010110111001100111010111110111000001101001011110000110010101101100

Flag: flag{dancing_pixel}
```

**Flag:** flag{dancing_pixel} 

#### To be XOR not to be (200pts) 

##### Descripción:

Han censurado la emisión de video, pero a ver si conseguimos el nombre del personaje que aperece en él.

Link: [https://drive.google.com/open?id=1MWcJtoBXbDTiD-CB8LAxSGGAUPhiXFkQ](https://drive.google.com/open?id=1MWcJtoBXbDTiD-CB8LAxSGGAUPhiXFkQ)

`sha256.result.mp4: 75d835ac1d030ac1639d37df508cf666c44b1fbfec7c889fed888c19ddc795e9`

> **Hint!** En este CTF no llegamos a crear la categoría de OSINT, pero... ¿Te has planteado buscar los fotogramas descifrados en internet? Recuerda: ¡Buscamos el nombre del personaje!

> **Hint!** Hemos dejado una pista en nuestra cuenta de Twitter: [https://twitter.com/ciberseguah/status/1086750900167819265](https://twitter.com/ciberseguah/status/1086750900167819265)

##### Solución

Inspeccionando el vídeo, podemos observar como la imagen se encuentra con mucho ruido, y tal y como sugiere el título del reto, esto va de hacer XOR.

La primera pregunta que se nos viene a la cabeza es, ¿con qué hago XOR? En seguida salimos de dudas al observar que el primer frame es diferente al resto. Por lo que elaboramos el siguiente script para crear un nuevo video haciendo un XOR de los frames con el primero:

```python
import cv2
import numpy as np
import os

# set video file path of input video with name and extension
vid = cv2.VideoCapture('./result.mp4')


if not os.path.exists('frames'):
    os.makedirs('frames')

#for frame identity
index = 0
keyFrame = None
while(True):
    # Extract images
    ret, frame = vid.read()

    # end of frames
    if not ret:
        break

    if index == 0:
        keyFrame = frame
    else:
        frame = frame ^ keyFrame

    # Saves images
    name = './frames/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1


frames = sorted(os.listdir('./frames'))
frame_array = []

for i in range(len(frames)):
    filename = './frames/' + frames[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)

    #inserting the frames into an image array
    frame_array.append(img)

    out = cv2.VideoWriter('./xoredResult.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 25, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
```

A pesar de haber realizado correctamente el XOR, el vídeo como tal no dice gran cosa (por lo menos para mi...), por lo que los administradores dieron una pista, una imagen (`pista.png`). Por lo que volvemos a hacer XOR:

`convert pista.png ./frames/frame0.jpg -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" imgXOR.jpg`

Y obtenemos:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/pistaXOR.jpg" width=350>

El texto: `Si nos pinchan, ¿acaso no sangramos?`

Haciendo una busqueda rápida en Google del texto, podemos observar que es parte de un monologo que realiza el personaje Shylock en la película `El mercader de Venecia`. Y puesto que el reto nos pedía el nombre del personaje, ya tenemos la flag.

**Flag:** flag{shylock}

#### YUVEYUVEYU (350pts)

##### Descripción:

Desde las llanuras de Ulan Bator nos llega una extraña señal...

`.wav:` https://drive.google.com/open?id=1fzhGbUKrt7E0y4-nJAhQWIG859WICqCw

`sha256-20190116_120900Z_106520122Hz_IQ.wav: a59759e7323d623f82c76c75366760310c6fe3bc42edf20b4f821e2a949fa04d`

##### Solución

Nos encontramos con una captura en crudo del espectro FM. ¿Cómo sabemos que es FM? Bien, aquí juega un poco el nombre del fichero, el cual es:

`20190116_120900Z_106520122Hz_IQ.wav`

Para los que sepan de radio, hay dos cosas que saltan a la vista, por un lado IQ (señales en cuadratura) y por otro lado Hz. 

Hz es la abreviature de Herzios y es la unidad del SI (Sistema Internacional) para la frecuencia. Y sabemos que la frecuencia por el titulo es: 106520122 Hz.

Esa frecuencia equivale a 106.52 MHz de manera aproximada. Y como enta dentro de la banda FM comercial, que va de los 87,5 MHz a los 108 MHz. Entonces de primeras parace FM.

La captura en sí, tiene el centro de frecuencias en 106.52 MHz, pero aún así, hay que sintonizarlo en alguna señal portadora para poder demodular la señal que queremos.

Si representamos la potencia en frecuencia:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/waterfall.jpg" width=350>

En la gráfica las frecuencias están representadas en banda base.

Lo que podemos ver, es que habrá que desplazarnos para poder sintonizar en la señal portadora y poder demodular correctamente la señal. Para ello, utilizaremos GNU Radio:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/flowgraph.png" width=350>

De manera resumida, lo que hace es, obtener la fuente del archivo .wav, procesarlo, demodularlo y volcarlo a un archivo `.mp3`.

Aspectos a entender del flowgraph del GNU Radio. Las frecuencias de muestreo no son han tomado aleatoriamente, hay que coger las frecuencias utilizadas en el archivo .wav porque sino estaremos destruyendo la señal

Para desplazar la señal y sintonizarla, multiplicamos por una señal seno en la frecuencia deseada. En nuestro caso 107MHz de manera aproximada. Como veis, ahora si se encuentra sintonizada:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/waterfall2.png" width=350>

Si observamos el espectrograma del archivo `.mp3` obtenido:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Criptograf%C3%ADa/Images/spectrogram.png" width=350>

**Flag:** flag{lord_chinggis}
