from fastapi import FastAPI
import pandas as pd
#título, descripción y versión de la FastApi.
app = FastAPI(title='Proyecto Individual',
            description='Data 08',
            version='1.1')

#Leer el dataframe para las consultas.
@app.get('/')
async def read_root():
    return {'Primera API'}
    
@app.on_event('startup')
async def startup():
    global df
    df = pd.read_csv('películas.csv') 

#activa servidor local
@app.get('/')
async def index():
    return {'API por Federico Gomez'}

@app.get('/about/')
async def about():
    return {'PI cohorte DTS-08'}

#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
# (la función debe llamarse get_max_duration(year, platform, duration_type))
@app.get('/get_max_duration/({year}, {platform}, {duration_type})')
async def get_max_duration(anio:int,plataforma:str,tipo_peli:str):
    #colocamos dentro de una variable llamada result, el resultado de buscar un año y la plataforma
    result = df[(df['release_year']==anio) & (df['platform']==plataforma)]
    #ahora dentro del if, la función toma en cuenta si se ingresa como parámetro la palabra 
    # "min" o "seasons", para ver si se quiere buscar una serie o una película
    if tipo_peli == 'min':
    #dentro de a se va guardando en resultado maximo de la columna correspondiente a min, 
    # lo cual va llenando una lista para luego devolver la de mayor duración en esa plataforma y en ese año
        a = result['duration_type'].max()
        name = result[result['duration_type']==a] ['title']
        name = name.to_list()
        name = name[0]
    else:
        a = result['duration_type'].max()
        #dentro de a se va guardando en resultado maximo de la columna correspondiente a seasons, 
        # lo cual va llenando una lista para luego devolver la de mayor duración en esa plataforma y en ese año
        name = result[result['duration_type']==a] ['title']
        name = name.to_list()
        name = name[0]
    return name

#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 
# (la función debe llamarse get_score_count(platform, scored, year))
@app.get('/get_score_count/({platform}, {scored},{year})')
async def get_score_count(plataforma:str,scored:float,anio:int):
    df_ratings = pd.read_csv('ratings.csv') 
    result = df_ratings[(df_ratings['date']==anio) & (df_ratings['platform']==plataforma) & (df_ratings['rating'] >= scored)]
    return {"En la plataforma": f"{plataforma} hay {int(result.platform.value_counts())} películas con un puntaje mayor a  {scored}" }

#Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
@app.get('/get_count_platform/({platform})')
async def get_count_platform(plataforma:str):
    #sumamos las cantidad de películas según la plataforma
    result=df[(df.platform == plataforma)].type.value_counts()
    return {"La cantidad de peliculas y series para la plataforma": f"{plataforma} es de {result['movie']} películas y {result['tv show']} series." }


#Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get('/get_actor/({platform},{year})')
def get_actor(platform:str, anio:int):
    result = df[(df['platform']==platform) & (df['release_year']==anio)]
    for i in result['cast']:
        if i != 'sin dato':
            i=i.replace(', ', ',')
        else:
            pass
    #ahora si se crea una lista para ir guardando los actores como valores únicos, separándolos por la coma.
    lista=[]
    for i in result['cast']:
        if i != 'sin dato':
            s=i.split(',')
            for j in range(len(s)):             
                if s[j] not in lista:
                    lista.append(s[j])
                else:
                    pass
        else:
            pass
    lista=list(set(lista))
    #iniciamos un contador en 0, y creamos un diccionario para ir guardando la cantidad de veces que se repite cada actor
    contador = 0
    dict={}
    for i in lista:
        contador = 0
        for j in result['cast']:
            if i in j.split(','):
                contador+=1
        dict[i]=contador
    return max(dict,key=dict.get)
