# laboratorio-modulo8-leccion02-ModelosNoLineales
## Modelos Generados
Hay un total de 6 Modelos
### Modelo 1
- Este Modelo sigue el transcurso de los Labs del módulo 7, añadiendo las predicciones.
- Los resultados:
    - R2 decision Tree train: 0.60
    - R2 decision Tree test:  0.74
    - RMSE decision Tree train: 8,649.82
    - RMSE decision Tree test:  9,503.12
### Modelo 2
- Basado en el **Modelo 1**, Este Modelo, Reemplaza el KNN Imputer por en RandomForest para Rellenar los Nulos.
- Lo demás se mantiene igual
- Los resultados:
    - R2 decision Tree train: 0.55
    - R2 decision Tree test:  0.28
    - RMSE decision Tree train: 8,549.07
    - RMSE decision Tree test:  17,115.71
### Modelo 3
- Basado en el **Modelo 2**
- También elimina "brand" a la hora de realizar predicciones
- Los resultados:
    - R2 decision Tree train: 0.82
    - R2 decision Tree test:  0.18
    - RMSE decision Tree train: 5,423.61
    - RMSE decision Tree test:  18,271.85

### Modelo 4
- Basado en el **Modelo 2**
- Además gestiona los duplicados al principio, para no perder tanta información (que perdia casi 100.000 filas)
- Los resultados:
    - R2 decision Tree train: 0.44
    - R2 decision Tree test:  0.31
    - RMSE decision Tree train: 11,086.86
    - RMSE decision Tree test:  10,065.41
### Modelo 5
- Basado en el **Modelo 4**
- Y ahora la categoría "brand" la hemos categorizado por gama. quedando así:
    - gama extinta: Marcas que ya no fabrican coches
    - gama baja: Marcas más baratas en general
    - gama media: Marcas gama media
    - gama alta: Marcas de gama alta
    - gama lujo: Marcas de lujo
- Los resultados:
    - R2 decision Tree train: 0.87
    - R2 decision Tree test:  -0.55
    - RMSE decision Tree train: 5,397.90
    - RMSE decision Tree test:  14,816.10
### Modelo 6 (Modelo Final)
- Basado en el **Modelo 5**
- Además voy a ser más estricto el ajuste de nulos y precios erróneos.
- Los resultados:
    - R2 decision Tree train: 0.84
    - R2 decision Tree test:  0.80
    - RMSE decision Tree train: 3,006.66
    - RMSE decision Tree test:  13,271.97
