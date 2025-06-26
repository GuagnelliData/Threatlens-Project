# 🛡️ ThreatLens — UNSW-NB15 Analysis Toolkit

**Autor:** Carlos Joseph Guagnelli  
**Fecha de inicio:** 2025-06-24  
**Estado:** 🚧 En desarrollo

## 📘 Descripción del proyecto

**ThreatLens** es una herramienta de análisis y visualización inicial del dataset UNSW-NB15, un conjunto de datos realista y ampliamente utilizado para tareas de detección de intrusos en redes. El objetivo del proyecto es entender la distribución del tráfico, diferenciar eventos normales de ataques y preparar el camino hacia la creación de modelos de detección basados en machine learning.

## 🧠 Motivación

En un mundo donde las amenazas cibernéticas son cada vez más frecuentes y sofisticadas, entrenar sistemas que puedan reconocer comportamientos anómalos es una prioridad. Este proyecto nace de la necesidad de explorar y comprender cómo se representan estos eventos en datos y cómo podemos utilizar herramientas como Python para analizarlos de forma visual, estructurada y escalable.

## 📂 Dataset utilizado

- **Nombre:** UNSW-NB15 (versión training-set)
- **Origen:** Australian Centre for Cyber Security
- **Características:**  
  - 45 columnas (características numéricas y categóricas)
  - 175,341 registros
  - Incluye etiquetas binarias (`label`: 0 = normal, 1 = ataque) y categorías de ataque (`attack_cat`)

## ✅ Avances actuales

- ✅ Dataset cargado y explorado con `pandas`
- ✅ Verificación de tipos de datos y valores nulos
- ✅ Estadísticas descriptivas generales
- ✅ Análisis de distribución entre tráfico normal y malicioso

## 🛠️ Tecnologías utilizadas

- Python 3.13 (entorno virtual activado)
- Bibliotecas: `pandas`, `numpy`, `seaborn`, `matplotlib`

## 🗺️ Próximos pasos

1. Análisis detallado por categoría de ataque (`attack_cat`)
2. Codificación de variables categóricas
3. Detección de outliers y correlaciones
4. Preparación de datos para Machine Learning (normalización, partición, etc.)
5. Entrenamiento de modelos (SVM, Árboles, Random Forest, etc.)
6. Evaluación y visualización de desempeño

## ✍️ Notas personales

> Este repositorio forma parte de un proceso de aprendizaje continuo, con el objetivo de dominar análisis de datos aplicados a ciberseguridad. Cualquier sugerencia, pull request o crítica constructiva es bienvenida.


📬 Contacto
📧 joseph.guagnelli@gmail.com
🔗 LinkedIn
🐙 GitHub
---

### 🚀 Ejecutar el script

```bash
# Activar entorno virtual
.\venv\Scripts\Activate

# Ejecutar el script principal
python Threatlens1.py


