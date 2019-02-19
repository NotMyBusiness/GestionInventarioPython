import sys
import re
import pandas as pd

class gestion_inventario():
    '''
    Clase gestión del inventario. Se encarga de leer la información del inventario
    y actualizarla con las diferentes ventas y reposiciones que tienen lugar.
    
    Atributos
    ---------
    inventario, operaciones: archivo
    
    '''
    
    def __init__(self, inventario, operaciones):
        '''
        Constructor
        
        Parámetros
        ----------
        inventario: archivo
        operaciones: archivo
        '''
        self.inventario = inventario
        self.operaciones = operaciones
                
    def leer_inventario(self,input_invent):
        '''
        Esta función se encarga de llamar a las funciones de lectura del inventario
        según sean los archivos de entrada .txt o .csv
        
        '''
        if re.search(r'.\.txt', input_invent):
            self.leer_inventario_txt(input_invent)
        elif re.search(r'.\.csv', input_invent):
            self.leer_inventario_csv(input_invent)
        else:
            print('Input files must be ".txt" or ".csv" files. Please input the files again')
            sys.exit()
   
    def leer_inventario_txt(self,input_invent):
        '''
        Esta función se encarga de leer y almacenar en un dataframe la información
        del inventario si el archivo de origen es un .txt
        '''
        try:
            self.inventario = pd.read_csv(input_invent, 
                                          sep = ',', header = None, 
                                          names = ['Cod', 'Cmax', 'Umbral', 'Creal',
                                                   'Ubi', 'Desc'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_invent)
            sys.exit()        
   
    def leer_inventario_csv(self,input_invent):
        '''
        Esta función se encarga de leer y almacenar en un dataframe la información
        del inventario si el archivo de origen es un .csv
        '''
        try:
            self.inventario = pd.read_csv(input_invent, header = None, 
                                          names = ['Cod', 'Cmax', 'Umbral', 'Creal',
                                                   'Ubi', 'Desc'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_invent)
            sys.exit()
            
            

    def leer_operaciones(self,input_oper):
        '''
        Esta función auxiliar se encarga de llamar a las funciones de lectura 
        de las operaciones (venta y reposición) según sean los archivos de 
        entrada .txt o .csv
        
        '''
        if re.search(r'.\.txt', input_oper):
            self.leer_oper_txt(input_oper)
        elif re.search(r'.\.csv', input_oper):
            self.leer_oper_csv(input_oper)
        else:
            print('Input files must be ".txt" or ".csv" files. Please input the files again')
            sys.exit()
   
    def leer_oper_txt(self,input_oper):
        '''
        Esta función es la encargada de leer y almacenar en un dataframe la 
        información correspondiente a las operaciones (venta y reposición) 
        si el archivo de origen es un .txt
        '''
        try:
            self.operaciones = pd.read_csv(input_oper, 
                                          delim_whitespace = True, header = None, 
                                          names = ['TipoOper', 'Fecha', 'Hora', 'Cod','Qty'])
            
            
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_oper)
            sys.exit()
            
        print(self.operaciones)
        
   
    def leer_oper_csv(self,input_oper):
        '''
        Esta función es la encargada de leer y almacenar en un dataframe la 
        información correspondiente a las operaciones (venta y reposición) 
        si el archivo de origen es un .csv
        '''
        try:
            self.operaciones = pd.read_csv(input_oper, sep = ',', 
                                           names = ['TipoOper', 'Fecha', 'Hora', 'Cod','Qty'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_oper)
            sys.exit()

    def realizar_oper(self):
        '''
        Esta función realiza las operaciones de venta y reposición. Itera a través
        de ambos dataframe para realizar la sustracción de las unidades de cada
        operación en caso de que sea una venta, y la suma de éstas en caso de 
        ser una reposición.
        
        En el caso de que la operación no se pueda realizar se imprimirá un aviso
        detallando la razón.
        '''
        df = self.inventario
        df2 = self.operaciones
        
        
        for i in range(0, df2['Cod'].size):
            print('-------------------------------------------------------------------------------')
            print(df2.at[i,'TipoOper'], '    : ', df2.at[i,'Fecha'], df2.at[i,'Hora'], df2.at[i,'Cod'],df2.at[i,'Qty'])
            for j in range(0, df['Cod'].size):
                if (df2.at[i,'Cod'] == df.at[j,'Cod'] and df2.at[i,'TipoOper'] == 'venta'):
                    print('Antes de  : ', df.at[j,'Cod'], df.at[j,'Cmax'], 
                  df.at[j,'Umbral'], df.at[j,'Creal'], df.at[j,'Ubi'], df.at[j, 'Desc'])
                    
                    if (df.at[j,'Creal'] - df2.at[i,'Qty'] > 0):
                        df.at[j,'Creal'] = (df.at[j,'Creal'] - df2.at[i,'Qty'])
                        print('Después de: ', df.at[j,'Cod'], df.at[j,'Cmax'], 
                  df.at[j,'Umbral'], df.at[j,'Creal'], df.at[j,'Ubi'], df.at[j, 'Desc'])
                        if (df.at[j,'Creal'] <= df.at[j,'Umbral']):
                            print('\t ==========> AVISO: es necesario reponer existencias <==========')
                    else:
                        print('\t ==========> AVISO: venta imposible. Comprobar el stock de este producto <==========')
                          
                   
                    
                elif (df2.at[i,'Cod'] == df.at[j,'Cod'] and df2.at[i,'TipoOper'] == 'repos'):
                    print('Antes de  : ', df.at[j,'Cod'], df.at[j,'Cmax'], 
                  df.at[j,'Umbral'], df.at[j,'Creal'], df.at[j,'Ubi'], df.at[j, 'Desc'])
                    
                    if (df.at[j,'Creal'] + df2.at[i,'Qty'] <= df.at[j,'Cmax']):
                        df.at[j,'Creal'] = (df.at[j,'Creal'] + df2.at[i,'Qty'])
                        print('Después de: ', df.at[j,'Cod'], df.at[j,'Cmax'], 
                  df.at[j,'Umbral'], df.at[j,'Creal'], df.at[j,'Ubi'], df.at[j, 'Desc'])
                    else:
                        print('\t ==========> AVISO: reposición imposible. Alcanzado límite en estantería <==========')
                
        self.inventario = df
   
    
    def grabar_inventario(self, input_invent):
        '''
        Esta función se encarga llamar a las funciones de grabación del inventario
        tras ser actualizado para que sean guardados en un archivo .txt o .csv
        
        Serán guardados en el mismo formato que el archivo de origen, es decir,
        si el inventario de origen era un archivo .txt, el inventario final será
        guardado en otro archivo .txt
        '''        
        if re.search(r'.\.txt', input_invent):
            self.grabar_inventario_txt()
        elif re.search(r'.\.csv', input_invent):
            self.grabar_inventario_csv()
        
    def grabar_inventario_txt(self):
        '''
        Esta función se encarga de grabar la información del inventario tras
        ser actualizado por las operaciones en un archivo .txt
        ''' 
        self.inventario.to_csv('nuevo_inventario.txt', index = False, header = False)
                          
    def grabar_inventario_csv(self):
        '''
        Esta función se encarga de grabar la información del inventario tras
        ser actualizado por las operaciones en un archivo .csv
        ''' 
        self.inventario.to_csv('nuevo_inventario.csv', index = False, header = False)
        
    
def main():
    input_invent = str(sys.argv[1])
    input_oper = str(sys.argv[2])
   
    gestion = gestion_inventario(input_invent,input_oper)
    
    
    print('-- Leyendo el archivo con el inventario ...')
    gestion.leer_inventario(input_invent)
    print('-- Leído el archivo con el inventario ...')
    print('-- Leyendo y procesando el archivo con las ventas y reposiciones ...')
    gestion.leer_operaciones(input_oper)
    gestion.realizar_oper()
    print('-- Fin de las ventas y reposiciones')
    print('-- Grabando el inventario en su estado actual')
    gestion.grabar_inventario(input_invent)
    print('-- Fin del programa')
    
  
if __name__ == '__main__':
    main()
