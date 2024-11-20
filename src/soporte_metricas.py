# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Visualizaciones
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree

# Para realizar la regresión lineal y la evaluación del modelo
# -----------------------------------------------------------------------
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


from sklearn.model_selection import KFold,LeaveOneOut, cross_val_score


from sklearn.preprocessing import StandardScaler

from tqdm import tqdm


# Ignorar los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings('ignore')

def obtener_metricas(y_train,y_pred_train,y_test,y_pred_test):
    metricas = {
        'train': {
        'r2_score': r2_score(y_train, y_pred_train),
        'MAE': mean_absolute_error(y_train, y_pred_train),
        'MSE': mean_squared_error(y_train, y_pred_train),
        'RMSE': np.sqrt(mean_squared_error(y_train, y_pred_train))
        },
        'test': {
        'r2_score': r2_score(y_test, y_pred_test),
        'MAE': mean_absolute_error(y_test, y_pred_test),
        'MSE': mean_squared_error(y_test, y_pred_test),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_test))
        }
    }
    df_metricas = pd.DataFrame(metricas).T
    return df_metricas

def comparar_arbol(df_previo, df_final, nombre_modelo = "Default"):
    """
    Compara dos DataFrames de métricas (inicial y final) y calcula las diferencias porcentuales
    entre ellos para mostrar mejoras o empeoramientos en las métricas.

    Args:
        df_previo (pd.DataFrame): DataFrame con las métricas iniciales.
        df_final (pd.DataFrame): DataFrame con las métricas finales.
    """
    print(f"------------------------------------------------")
    print(f"Métricas Árbol inicial:")
    display(df_previo)
    print(f"------------------------------------------------")
    print(f"Métricas Árbol final:")
    display(df_final)
    print(f"------------------------------------------------")
    
    # Crear un DataFrame con las diferencias porcentuales
    df_comparar = pd.concat
    df_comparar["%_r2_score"] = ((df_final["r2_score"] - df_previo["r2_score"]) / df_previo["r2_score"]) * 100
    df_comparar["%_MAE"] = ((df_final["MAE"] - df_previo["MAE"]) / df_previo["MAE"]) * 100
    df_comparar["%_MSE"] = ((df_final["MSE"] - df_previo["MSE"]) / df_previo["MSE"]) * 100
    df_comparar["%_RMSE"] = ((df_final["RMSE"] - df_previo["RMSE"]) / df_previo["RMSE"]) * 100
    
    print(f"Diferencias porcentuales (%):")
    display(df_comparar)
    print(f"------------------------------------------------")


def comparar_arboles(df_previos, df_final,lista_previos=False,nombre_modelo = "modelo_previo"):
    """
    Compara dos DataFrames de métricas (inicial y final) y calcula las diferencias porcentuales
    entre ellos para mostrar mejoras o empeoramientos en las métricas.

    Args:
        df_previo (pd.DataFrame): DataFrame con las métricas iniciales.
        df_final (pd.DataFrame): DataFrame con las métricas finales.
    """
    if lista_previos == True:
        df_unir = pd.DataFrame()
        
        for i, df in enumerate(df_previos):
            df.reset_index(inplace=True)
            df = df.rename(columns={"index":"entrenamiento"})
            df["modelo"] = f"modelo {i}"
            df = df[["modelo","entrenamiento","r2_score","MAE","MSE","RMSE"]]
            
            df_unir = pd.concat([df_unir,df], axis=0)
        
        df_final.reset_index(inplace=True)
        df_final = df_final.rename(columns={"index":"entrenamiento"})
        df_final["modelo"] = f"modelo final"
        df_final = df_final[["modelo","entrenamiento","r2_score","MAE","MSE","RMSE"]]
        df_unido = pd.concat([df_unir,df_final])
        display(df_unido)
    else:
        df_previos.reset_index(inplace=True)
        df_previos = df_previos.rename(columns={"index":"entrenamiento"})
        df_previos["modelo"] = f"{nombre_modelo}"
        df_previos = df_previos[["modelo","entrenamiento","r2_score","MAE","MSE","RMSE"]]
        
        df_final.reset_index(inplace=True)
        df_final = df_final.rename(columns={"index":"entrenamiento"})
        df_final["modelo"] = f"modelo final"
        df_final = df_final[["modelo","entrenamiento","r2_score","MAE","MSE","RMSE"]]
        df_unido = pd.concat([df_previos,df_final])
        display(df_unido)
        
