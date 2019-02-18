from mrjob.job import MRJob

class MRTotalOperaciones(MRJob):
    
    def mapper(self, _, line):
        line = line.split()
        if line[0] == 'venta':
            yield 'Ventas del producto: %s' % line[3], int(line[4])
        elif line[0] == 'repos':
            yield 'Reposiciones del producto: %s' % line[3], int(line[4])
    
    def reducer(self, key, values):
        yield key, sum(values)

    
if __name__ == '__main__':
    MRTotalOperaciones.run()
