<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual de la etapa de labs! Me encuentro en el rol de un ***MLOps Engineer***.  

<hr>  

## Descripción del problema

## Contexto

Hasta el momento de escribir estas lineas he llegado hasta crear el modelo de recomendación entrenado y aun no he estudiado las métricas :smirk:, y por ahora, sólo he podido hacer funcionar el Render con fastAPI para mostrar la primera parte. Aun me falta publicar el sistema de recomendación :eyes:

Todo ha sido cuesta arriba, desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento del modelo de ML. La falta de experiencia y conocimiento en este tema ponen a prueba la resistencia y motivacion que tienes para hacerte un **`Data Scientist`**.


## Rol a desarrollar

Despues de una semana de arduo trabajo soy conciente de que me falta mucho para llegar a ser un **`Data Scientist`** y por esto agradezo la oportunidad de incrementar mis conocimientos y destrezas con este tipo de trabajo. Mi primer modelo de ML que es este sistema de recomendación que aún no he podido mostrar al mundo ya que me falta el deploy! 

Lo que hoy muestro es mi **`MVP`** (_Minimum Viable Product_) faltandole aun varios detalles para considerarlo un buen trabajo!🤯. Creo que se ha cumplido con el objetivo de la primera semana y tengo mas claridad de los procesos que me hacen falta :exclamation:. Así que seguir mejorando en alguna de las debilidades de mi trabajo :muscle:

<p align="center">
<img src="https://github.com/soyHenry/DS_LABS/blob/main/Proyectos/Proyectos%20Individuales/PI01/Data07_MLops_API/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>

## **Propuesta de trabajo **

+ Utilice los notebooks ETL.ipynb y Tranformacion.ipynb para traer los datos desde los archivos csv de las peliculas y de ratings

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

+ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

+ Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


<br/>


**`Deployment`**: Conoces sobre [Render](https://render.com/docs/free#free-web-services) y tienes un [tutorial de Render](https://github.com/HX-FNegrete/render-fastapi-tutorial) que te hace la vida mas facil :smile: . Tambien podrias usar [Railway](https://railway.app/), pero ten en cuenta que con este si necesitas dockerizacion.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente :eyes: ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior.  Sabes que puedes apoyarte en librerías como _pandas profiling, sweetviz, autoviz_, entre otros y sacar de allí tus conclusiones 😉

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).

<br/>

**`Video`**: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

<br/>

## **Criterios de evaluación**

**`Código`**: Prolijidad de código, uso de clases y/o funciones, en caso de ser necesario, código comentado. 

**`Repositorio`**: Nombres de archivo adecuados, uso de carpetas para ordenar los archivos, README.md presentando el proyecto y el trabajo realizado

**`Cumplimiento`** de los requerimientos de aprobación indicados en el apartado `Propuesta de trabajo`

<p align="center">
</p>


## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn): La carpeta 'ratings' tiene varios archivos con las reseñas de los usuarios, la carpeta raíz tiene un dataset por proveedor de servicios de streaming.
<br/>

## **Material de apoyo**

En este mismo repositorio podras encontrar algunos [links de ayuda](https://github.com/soyHenry/DS_LABS/blob/main/Proyectos/Proyectos%20Individuales/PI01/Data08_MLops/Material%20de%20apoyo.md). Recuerda que no son los unicos recursos que puedes utilizar!


  
<br/>
