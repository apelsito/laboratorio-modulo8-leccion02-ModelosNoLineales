# Modelos No Lineales - Laboratorio del Módulo 8

Este repositorio contiene el desarrollo y los resultados del laboratorio correspondiente al módulo 8, donde se trabajan **Modelos No Lineales**. A continuación, se describen los pasos seguidos y los resultados obtenidos en cada uno de los modelos creados.

---

## Descripción General

Se desarrollaron un total de 6 modelos con el objetivo de mejorar las predicciones utilizando modelos no lineales basados en **árboles de decisión**. Cada modelo se basa en el anterior, introduciendo mejoras iterativas para optimizar métricas como el **R²** y el **RMSE** (Root Mean Square Error) en los conjuntos de entrenamiento y prueba.

---

## Modelos Generados

### **Modelo 1**
- **Descripción**: 
  Este modelo sigue el flujo base de los laboratorios del módulo 7, implementando predicciones básicas con Árboles de Decisión.
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.60
    - Prueba: 0.74
  - **RMSE**:
    - Entrenamiento: 8,649.82
    - Prueba: 9,503.12

---

### **Modelo 2**
- **Descripción**: 
  Basado en el **Modelo 1**, reemplaza el **KNN Imputer** por **RandomForest** para rellenar los nulos, manteniendo el resto igual.
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.55
    - Prueba: 0.28
  - **RMSE**:
    - Entrenamiento: 8,549.07
    - Prueba: 17,115.71

---

### **Modelo 3**
- **Descripción**: 
  Basado en el **Modelo 2**, elimina la variable `brand` a la hora de realizar predicciones.
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.82
    - Prueba: 0.18
  - **RMSE**:
    - Entrenamiento: 5,423.61
    - Prueba: 18,271.85

---

### **Modelo 4**
- **Descripción**: 
  Basado en el **Modelo 2**, gestiona los duplicados al inicio del pipeline para reducir la pérdida de información (anteriormente, se perdían casi 100,000 filas).
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.44
    - Prueba: 0.31
  - **RMSE**:
    - Entrenamiento: 11,086.86
    - Prueba: 10,065.41

---

### **Modelo 5**
- **Descripción**: 
  Basado en el **Modelo 4**, se categoriza la variable `brand` en rangos de gama:
  - **Gama extinta**: Marcas que ya no fabrican coches.
  - **Gama baja**: Marcas más baratas en general.
  - **Gama media**: Marcas de gama media.
  - **Gama alta**: Marcas de gama alta.
  - **Gama lujo**: Marcas de lujo.
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.87
    - Prueba: -0.55
  - **RMSE**:
    - Entrenamiento: 5,397.90
    - Prueba: 14,816.10

---

### **Modelo 6 (Modelo Final)**
- **Descripción**: 
  Basado en el **Modelo 5**, realiza un ajuste más estricto de los nulos y valores de precios erróneos para mejorar la calidad de los datos.
- **Resultados**: 
  - **R²**:
    - Entrenamiento: 0.84
    - Prueba: 0.80
  - **RMSE**:
    - Entrenamiento: 3,006.66
    - Prueba: 3,271.97

---

## Conclusiones
El **Modelo 6** logra un equilibrio óptimo entre entrenamiento y prueba, con un ajuste más estricto de los datos y un enfoque mejorado en la limpieza inicial. Los resultados reflejan un incremento significativo en el rendimiento general, destacando una reducción considerable en el error y una mejora en la capacidad predictiva.

---
