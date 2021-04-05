#utilidades para manejo de errores

class AppErrorBaseClass(Exception):
    pass
class ObjectNotFound(AppErrorBaseClass):
    pass