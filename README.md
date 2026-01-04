# Scraper de Tarifas de Luz - scrapluz.py

Este script extrae información sobre las tarifas de luz por horas desde el sitio web [tarifaluzhora.es](https://tarifaluzhora.es) y muestra las horas con sus respectivos precios, marcando con la etiqueta `[ECO]` aquellas horas que tienen un precio igual o menor a un umbral configurable.

## Descripción

El script `scrapluz.py` realiza un scraping del sitio web de tarifaluzhora.es para obtener:
- Las horas del día con sus tarifas de luz
- Los precios por kWh para cada hora
- Una identificación automática de las horas "ECO" (precio igual o menor al umbral configurado)

La salida muestra cada hora con su precio formateado, y las horas que cumplen el criterio de precio máximo se marcan con la etiqueta `[ECO]`.

## Requisitos previos

- **Python 3.6 o superior**
- **Conexión a internet** (el script necesita acceder a tarifaluzhora.es)

## Dependencias

El script requiere las siguientes bibliotecas de Python:

- `requests` - Para realizar peticiones HTTP al sitio web
- `beautifulsoup4` - Para parsear y extraer datos del HTML

La biblioteca `re` utilizada para expresiones regulares es parte de la biblioteca estándar de Python y no requiere instalación adicional.

## Instalación

### Opción 1: Instalación directa (recomendado para uso simple)

1. Instala las dependencias usando pip:

```bash
pip install requests beautifulsoup4
```

O si usas Python 3 específicamente:

```bash
pip3 install requests beautifulsoup4
```

### Opción 2: Usando un entorno virtual (recomendado para proyectos)

1. Crea un entorno virtual:

```bash
python3 -m venv venv
```

2. Activa el entorno virtual:

**En macOS/Linux:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install requests beautifulsoup4
```

4. (Opcional) Crea un archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

El contenido de `requirements.txt` debería incluir:
```
requests>=2.25.0
beautifulsoup4>=4.9.0
```

## Uso básico

Una vez instaladas las dependencias, ejecuta el script:

```bash
python scrapluz.py
```

O si usas Python 3:

```bash
python3 scrapluz.py
```

### Salida del script

El script mostrará una lista de horas con sus respectivos precios por kWh, por ejemplo:

```
[ECO] 00:00 - 01:00: 0.120 €/kWh
[ECO] 01:00 - 02:00: 0.115 €/kWh
02:00 - 03:00: 0.145 €/kWh
03:00 - 04:00: 0.150 €/kWh
[ECO] 04:00 - 05:00: 0.130 €/kWh
...
```

**Significado de la etiqueta [ECO]:**
- Las horas marcadas con `[ECO]` tienen un precio igual o menor al umbral configurado (por defecto 0.135 €/kWh)
- Las horas sin etiqueta tienen un precio superior al umbral

## Configuración

### Modificar el precio máximo (umbral ECO)

El precio máximo para considerar una hora como "ECO" está configurado en la función `main()` del script. Por defecto está establecido en **0.135 €/kWh**.

Para modificar este valor, edita la línea 33 del archivo `scrapluz.py`:

```python
precio_max = 0.135  # Cambia este valor según tus necesidades
```

Por ejemplo, para establecer el umbral en 0.100 €/kWh:

```python
precio_max = 0.100
```

### URL objetivo

La URL del sitio web está hardcodeada en la línea 32:

```python
url = 'https://tarifaluzhora.es'
```

Si necesitas cambiar la URL, modifica esta línea en el código.

## Ejemplo de ejecución completa

```bash
$ python3 scrapluz.py

[ECO] 00:00 - 01:00: 0.120 €/kWh
[ECO] 01:00 - 02:00: 0.115 €/kWh
02:00 - 03:00: 0.145 €/kWh
03:00 - 04:00: 0.150 €/kWh
[ECO] 04:00 - 05:00: 0.130 €/kWh
05:00 - 06:00: 0.142 €/kWh
...
```

## Despliegue

### Ejecución local

El script está diseñado para ejecutarse localmente en tu máquina. Solo necesitas:

1. Tener Python 3 instalado
2. Instalar las dependencias (ver sección de Instalación)
3. Ejecutar el script cuando necesites consultar las tarifas

## Estructura del código

El script está organizado en las siguientes funciones:

- `obtener_html(url)`: Obtiene el contenido HTML de la URL
- `extraer_bloques(html)`: Extrae los bloques de horas del HTML parseado
- `extraer_info_bloque(bloque)`: Extrae la información (hora y precio) de cada bloque
- `mostrar_resultados(resultados, precio_max)`: Muestra los resultados formateados con la etiqueta [ECO]
- `main()`: Función principal que orquesta el proceso

## Notas adicionales

- **Dependencia de la estructura del sitio web**: Este script depende de la estructura HTML específica de tarifaluzhora.es. Si el sitio web cambia su estructura, el script podría dejar de funcionar y requeriría actualizaciones.

- **Conectividad**: El script necesita una conexión activa a internet para funcionar.

- **Límites de uso**: Ten en cuenta las políticas de uso del sitio web. No abuses haciendo demasiadas peticiones en poco tiempo.

- **Manejo de errores**: Si el sitio web no está disponible o hay un error de conexión, el script mostrará un error. Puedes mejorar el script añadiendo manejo de excepciones si es necesario.

## Solución de problemas

### Error: `ModuleNotFoundError: No module named 'requests'`

**Solución**: Instala las dependencias como se indica en la sección de Instalación.

### Error: `ModuleNotFoundError: No module named 'bs4'`

**Solución**: Instala beautifulsoup4 con `pip install beautifulsoup4`.

### Error de conexión o el script no muestra resultados

**Posibles causas**:
- No hay conexión a internet
- El sitio web tarifaluzhora.es no está disponible
- La estructura HTML del sitio web ha cambiado (el script necesita actualización)

### El script no muestra la etiqueta [ECO] en ninguna hora

**Solución**: Verifica el valor de `precio_max` en el código. Si está muy bajo, es posible que ninguna hora cumpla el criterio. Ajusta el valor según tus necesidades.

## Autor

Daniel Gómez

## Licencia

Este script es de uso libre.(MIT) Asegúrate de respetar los términos de uso del sitio web objetivo (tarifaluzhora.es).

