class Persona:
    cod_persona = ""
    nombre = ""
    apellido_paterno = ""
    apellido_materno = ""
    
    fecha_nacimiento = ""

    # constructor
    def __init__(self, cod_persona,nombre, apellido_paterno, apellido_materno,fecha_nacimiento ):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
    
    def get_cod_persona(self):
        return self.cod_persona
    
    def set_cod_persona(self, cod_persona):
        self.cod_persona = cod_persona
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_apellido_paterno(self):
        return self.apellido_paterno
    
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    
    def imprimir(self):
        codigo = self.cod_persona
        nombres = self.nombre
        apellidos = self.apellido_paterno + ' ' + self.apellido_materno
        fecha_nacimiento = self.fecha_nacimiento
        return f' {codigo=}, {nombres=},  {apellidos=}, {fecha_nacimiento=}'