# PI_ML
Practicar ML, FastAPI y Render
PROYECTO INDIVIDUAL DATA SCIENCE 05
En este repositorio encontrarás mi primer proyecto individual de la carrera Data Science en Henry. Que lo disfrutes!
La idea de este proyecto es internalizar los conocimientos requeridos para la elaboración y ejecución de una API.
Application Programming Interface es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.
Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.
El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que se consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual dockerizado.
Los datos fueron provistos en archivos de diferentes extensiones, como csv o json. Se realizó un EDA para cada dataset y se corrigieron los tipos de datos, valores nulos, duplicados, entre otras tareas. Posteriormente, se relacionan los datasets para que se pueda acceder a su información por medio de consultas a la API. Los datasets se tratan de información acerca de Movies y Tv Shows de plataformas como Netflix, Amazon, Hulu y Disney; donde disponen de columnas como el año de publicación, la duración (en minutos o temporadas, depende del tipo), el año que se subió a la plataforma, el cast, director, entre otros.
Ejemplos de consultas a realizar son:
Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season]).
Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma).
Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero') Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.
Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año).
Para realizar este proyecto, primero se ingestaron y normalizaron los datos, lo que se puede ver en el archivo edayetl.ipynb y se relacionó el conjunto de datos, donde se creó la tabla necesaria para realizar consultas. Luego se creó la API en un entorno Docker.
Si queres conocer más sobre el proyecto, podés ingresar a ver las consignas acá
Bibliografía consultada:
Toda la bibliografía recomendada y provista durante el bootcamp y las clases de todos los días. (Si queres conocer más sobre esto, ingresá acá
Videos de youtube como: https://www.youtube.com/watch?v=_eWEmRWhk9A
https://www.youtube.com/watch?v=2tOhTGBWZXY&list=LL
https://www.youtube.com/watch?v=BvvH3ohis6E
