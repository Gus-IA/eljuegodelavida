# Juego de la Vida en Python 🧬

Este proyecto implementa el clásico **Juego de la Vida de Conway** utilizando **Python**, como parte de un aprendizaje práctico de programación y temas introductorios de inteligencia artificial (IA).

## 🎯 Objetivo del Proyecto

- Aprender conceptos fundamentales de Python.
- Comprender la lógica de autómatas celulares.
- Introducir principios básicos de simulación y visualización.
- Explorar ideas de vida artificial, patrones emergentes y sus vínculos con IA.

## 🔍 ¿Qué es el Juego de la Vida?

El **Juego de la Vida** es un autómata celular creado por el matemático John Conway. Se trata de una simulación en una cuadrícula bidimensional donde cada celda puede estar viva o muerta, y evoluciona según un conjunto de reglas simples:

1. Una célula viva con menos de 2 vecinos vivos muere (soledad).
2. Una célula viva con 2 o 3 vecinos sobrevive.
3. Una célula viva con más de 3 vecinos muere (superpoblación).
4. Una célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva (nacimiento).

## 🧠 ¿Qué tiene que ver con IA?

Aunque no es IA per se, el Juego de la Vida introduce conceptos clave que se exploran en inteligencia artificial y sistemas complejos:

- **Sistemas emergentes**.
- **Simulación basada en agentes**.
- **Modelos sin supervisión de reglas**.
- **Computación basada en patrones**.

### Instalación

Instala las dependencias con:

```bash
pip install -r requirements.txt

🧑‍💻 Autor

Desarrollado por Gus como parte de su aprendizaje en Python e IA.
