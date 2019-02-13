import sys
import re
import pandas as pd

class gestion_inventario():
    
    def __init__(self):
        pass
                
    def leer_inventario(self,input_invent):
        if re.search(r'.\.txt', input_invent):
            self.leer_inventario_txt(input_invent)
        elif re.search(r'.\.csv', input_invent):
            self.leer_inventario_csv(input_invent)
        else:
            print('Input files must be ".txt" or ".csv" files. Please input the files again')
            sys.exit()
   
    def leer_inventario_txt(self,input_invent):
        try:
            self.inventario = pd.read_csv(input_invent, 
                                          sep = ',', header = None, 
                                          names = ['Cod', 'Cmax', 'Umbral', 'Creal',
                                                   'Ubi', 'Desc'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_invent)
            sys.exit()        
   
    def leer_inventario_csv(self,input_invent):
        try:
            self.inventario = pd.read_csv(input_invent, header = None, 
                                          names = ['Cod', 'Cmax', 'Umbral', 'Creal',
                                                   'Ubi', 'Desc'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_invent)
            sys.exit()
            
            

    def leer_operaciones(self,input_oper):
        if re.search(r'.\.txt', input_oper):
            self.leer_oper_txt(input_oper)
        elif re.search(r'.\.csv', input_oper):
            self.leer_oper_csv(input_oper)
        else:
            print('Input files must be ".txt" or ".csv" files. Please input the files again')
            sys.exit()
   
    def leer_oper_txt(self,input_oper):
        try:
            self.operaciones = pd.read_csv(input_oper, 
                                          delim_whitespace = True, header = None, 
                                          names = ['TipoOper', 'Fecha', 'Hora', 'Cod','Qty'])
            
            
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_oper)
            sys.exit()
            
        print(self.operaciones)
        
   
    def leer_oper_csv(self,input_oper):
        try:
            self.operaciones = pd.read_csv(input_oper, sep = ',', 
                                           names = ['TipoOper', 'Fecha', 'Hora', 'Cod','Qty'])
        except FileNotFoundError:
            print('File %s not found. Please input a valid file' % input_oper)
            sys.exit()

    def realizar_oper(self):
        df = self.inventario.copy()
        df2 = self.operaciones.copy()
        
        
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
                    else:
                        print('\t ==========> AVISO: venta imposible. Comprobar el stock de este producto <==========')
                          
                    if (df.at[j,'Creal'] <= df.at[j,'Umbral']):
                        print('\t ==========> AVISO: es necesario reponer existencias <==========')
                    
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
        if re.search(r'.\.txt', input_invent):
            self.grabar_inventario_txt()
        elif re.search(r'.\.csv', input_invent):
            self.grabar_inventario_csv()
        
    def grabar_inventario_txt(self):
        self.inventario.to_csv('new_inventario.txt', index = False, header = False)
                          
    def grabar_inventario_csv(self):
        self.inventario.to_csv('new_inventario.csv', index = False, header = False)
        
    
def main():
    input_invent = str(sys.argv[1])
    input_oper = str(sys.argv[2])
   
    gestion = gestion_inventario()
    
    
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
