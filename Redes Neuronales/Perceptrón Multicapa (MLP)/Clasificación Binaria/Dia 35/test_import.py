try:
    from scikeras.wrappers import KerasClassifier
    print("scikeras importado exitosamente")
except ModuleNotFoundError as e:
    print("Error al importar scikeras:", e)
