# 🛡️ ThreatLens — UNSW-NB15 Analysis & Classification Toolkit
**Autor:** Carlos Joseph Guagnelli  
**Fecha de inicio:** 2025-06-24  
**Estado:** 🚧 En desarrollo activo

## 📘 Descripción del proyecto
ThreatLens es una herramienta de análisis, preprocesamiento y clasificación del dataset UNSW-NB15, diseñado para entrenar y evaluar sistemas de detección de intrusos (IDS). Esta herramienta busca construir un pipeline completo de machine learning, desde la exploración de datos hasta la clasificación multiclase de ataques utilizando redes neuronales.

## 🧠 Motivación
En un mundo cada vez más interconectado, las amenazas cibernéticas requieren respuestas automatizadas y adaptativas. ThreatLens nace de la necesidad de entrenar modelos inteligentes capaces de reconocer patrones maliciosos en grandes volúmenes de tráfico de red. Este proyecto fusiona análisis de datos, visualización y deep learning en una sola estructura modular y escalable.

## 📂 Dataset utilizado
- **Nombre:** UNSW-NB15 (training-set)
- **Origen:** Australian Centre for Cyber Security
- **Registros:** 175,341  
- **Columnas:** 45 (variables numéricas y categóricas)  
- **Etiquetas:**
  - `label`: 0 = tráfico normal, 1 = ataque
  - `attack_cat`: categoría del ataque (10 clases)

## ✅ Avances actuales

- ✅ Exploración del dataset con `pandas`
- ✅ Visualización y análisis de distribución normal vs ataque (`label`)
- ✅ Conteo y análisis por categoría de ataque (`attack_cat`)
- ✅ Codificación numérica de `attack_cat` con `LabelEncoder`
- ✅ One-Hot Encoding para variables categóricas (`proto`, `service`, `state`)
- ✅ División del dataset en entrenamiento y prueba (80/20, estratificada)
- ✅ Escalado de características numéricas con `StandardScaler`
- ✅ Entrenamiento de red neuronal con `TensorFlow` y `Keras`
- ✅ Precisión de validación superior al 99% en clasificación multiclase

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.11 (entorno virtual con venv)
- **Librerías principales:**
  - `pandas`, `numpy` → manejo de datos
  - `matplotlib`, `seaborn` → visualización
  - `scikit-learn` → preprocesamiento, codificación, partición
  - `tensorflow`, `keras` → red neuronal multicapa
  - *(pendiente: `imbalanced-learn` para balanceo de clases)*

## 📊 Resultados iniciales del modelo
Modelo secuencial simple con 2 capas ocultas (ReLU) y softmax final:
- 🔹 Accuracy de validación (`val_accuracy`): **99.93%**
- 🔹 Loss de validación (`val_loss`): **0.0047**
- 🔹 Epochs entrenadas: 10
> ⚠️ Aunque los resultados son excelentes, es necesario revisar el balance de clases y evaluar con métricas adicionales como F1-score y matriz de confusión para evitar falsas certezas.

## 📈 Próximos pasos

- [ ] Rebalancear el dataset con **SMOTE** u otras técnicas (`imbalanced-learn`)
- [ ] Implementar métricas adicionales: F1-score, recall por clase, matriz de confusión
- [ ] Añadir **validación cruzada** y **early stopping**
- [ ] Experimentar con arquitecturas más profundas o convolucionales
- [ ] Guardar y reutilizar el modelo entrenado (`.h5`)
- [ ] Documentar pipeline completo para futuras pruebas

## ✍️ Notas personales
Este proyecto representa una transición entre teoría y práctica en ciberseguridad basada en datos. La idea es construir una base sólida para aplicar inteligencia artificial a problemas reales de defensa digital. Agradezco sugerencias, pull requests y cualquier retroalimentación constructiva.

## 📬 Contacto

📧 joseph.guagnelli@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/carlos-joseph-guagnelli-villagran-544849216/)  
🐙 [GitHub](https://github.com/GuagnelliData)

## 🚀 Ejecutar el script

```bash
# Activar entorno virtual (PowerShell)
.\.venv311\Scripts\Activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script principal
python Threatlens1.py
