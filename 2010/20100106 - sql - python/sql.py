class ListasDiferentesException(Exception): pass
class Sql:
    def select(self, table_name, columns):
        return 'SELECT %s FROM %s' % (
                ", ".join(columns), table_name)
    
    def insert(self, table_name, columns, values):
        if len(columns) != len(values): 
            raise ListasDiferentesException
        
    
        return 'INSERT INTO %s (%s) VALUES("%s")' % (
                table_name, ", ".join(columns), '", "'.join(values))
        
        
        