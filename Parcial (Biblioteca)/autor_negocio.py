import pandas as pd
from openpyxl import Workbook
from autor import Autor
from datetime import datetime

class AutorNegocio():
    listado_autor = []
    registros_autor = "listado_autor.xlsx"
    
    def __init__(self):
        self.listado_autor = []
        self.registros_autor = "listado_autor.xlsx"
    
    def obtener_autor(self):
        df = pd.read_excel(self.registros_autor)
        listado_autor = []
        for index, row in df.iterrows():
            autor = Autor(row['Indice'],row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'],row['Fecha_de_Nacimiento'],row['Codigo_Autor'],row['Pais'],row['Editorial'],row['Estado_Autor'])
            listado_autor.append(autor)
        return listado_autor
    
    def registrar_autor(self,_indice,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_codigo_autor,_pais,_editorial,_estado_autor):
            print(f'{_indice},{_nombre},{_apellido_paterno},{_apellido_materno},{_fecha_nacimiento},{_codigo_autor}, {_pais},{_editorial},{_estado_autor}')
            self.listado_autor = self.obtener_autor()
            autor = Autor(_indice,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_codigo_autor,_pais,_editorial,_estado_autor)
            self.listado_autor.append(autor)
            print(f'se agrego un alumno : {len(self.listado_autor)}')
    
    def guardar_autor(self):
            print(f'listado de alumnos es: {len(self.listado_autor)}')
            if len(self.listado_autor) > 0:
                data =[]
                for autor in self.listado_autor:
                    data.append([autor.cod_persona,autor.nombre,autor.apellido_paterno,autor.apellido_materno,autor.fecha_nacimiento,autor.codigo_autor,autor.pais,autor.editorial,autor.estado_autor])
                columnas = ['Indice','Nombre','Apellido_Paterno','Apellido_Materno','Fecha_de_Nacimiento','Codigo_Autor','Pais','Editorial','Estado_Autor']
                df = pd.DataFrame(data, columns=columnas)
                df.to_excel(self.registros_autor, index=False, engine='openpyxl')
                return f'se registro correctamento los datos del autor'
            else:
                return f'se genero un error al registrar el autor'

    def editar_autor(self,_indice,_nombre,_apellido_paterno,_apellido_materno,_fecha_nacimiento,_codigo_autor,_pais,_editorial,_estado_autor):
        df = pd.read_excel(self.registros_autor)
        df.loc[_indice, 'Nombre'] = _nombre
        df.loc[_indice, 'Apellido_Paterno'] = _apellido_paterno
        df.loc[_indice, 'Apellido_Materno'] = _apellido_materno
        df.loc[_indice, 'Fecha_Nacimiento'] = _fecha_nacimiento
        df.loc[_indice, 'Codigo_Autor'] = _codigo_autor
        df.loc[_indice, 'Pais'] = _pais
        df.loc[_indice, 'Editorial'] = _editorial
        df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def eliminar_autor(self,_indice,_estado_autor):
        df = pd.read_excel(self.registros_autor)
        df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def reactivar_autor(self,_indice,_estado_autor):
        df = pd.read_excel(self.registros_autor)
        df.loc[_indice, 'Estado_Autor'] = _estado_autor
        df.to_excel(self.registros_autor, index=False, engine='openpyxl')
        return f'actualización correcta'
    
    def generar_reporte(self):
        print("Generando el Reporte de autor")
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime("%d_%m_%Y")
        print("Fecha actual en formato 'día_mes_año':", formato)
        nom_reporte = 'reporte_'+ formato + '.txt'
        with open(nom_reporte, 'w') as archivo:
            archivo.write("*******Listado de Alumnos registrados en el Sistema*******************.\n")
            for autor in self.listado_autor:
                archivo.write(autor.imprimir())
            archivo.write("*************************************************.\n")