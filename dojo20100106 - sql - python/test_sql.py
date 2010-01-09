import unittest
from sql import *

class TestesGeradorSql(unittest.TestCase):

    def teste_select_tabela_project_com_coluna_name(self):
        sql = Sql()
        table_name = "project"
        columns = ["name"]
        self.assertEqual('SELECT name FROM project', 
                          sql.select(table_name, columns))

    def teste_select_tabela_com_uma_coluna(self):
        sql = Sql()
        table_name = "abacaxi"
        columns = ["description"]
        self.assertEqual('SELECT description FROM abacaxi',
                          sql.select(table_name, columns))
    
    def teste_select_tabela_com_duas_colunas(self):
        sql = Sql()
        table_name = "project"
        columns = ["description", "whatever"]
        self.assertEqual('SELECT description, whatever FROM project',
                          sql.select(table_name, columns))

    def teste_select_tabela_com_varias_colunas(self):
        sql = Sql()
        table_name = "project"
        columns = ["description",
                   "whatever",
                   "forever",
                   "never",
                   "whenever"]
        self.assertEqual('SELECT description, whatever, forever, never, whenever FROM project',
                          sql.select(table_name, columns))

    def teste_insert_valor_na_tabela_project_com_a_coluna_whatever(self):
        sql = Sql()
        table_name = "project"
        columns = ["whatever"]
        values = ["never"]
        self.assertEqual('INSERT INTO project (whatever) VALUES("never")', 
                        sql.insert(table_name, columns, values))
     
    def teste_insert_valor_em_uma_tabela_qualquer_com_uma_coluna(self):
        sql = Sql()
        table_name = "abacaxi"
        columns = ["description"]
        values = ["é uma fruta"]
        self.assertEqual('INSERT INTO abacaxi (description) VALUES("é uma fruta")', 
                        sql.insert(table_name, columns, values))
               
    def teste_insert_valores_em_uma_tabela_qualquer_com_varias_colunas(self):
        sql = Sql()
        table_name = "fruta"
        columns = ["name", "description"]
        values = ["abacaxi", "é uma fruta"]
        self.assertEqual('INSERT INTO fruta (name, description) VALUES("abacaxi", "é uma fruta")', 
                        sql.insert(table_name, columns, values))
    
    def teste_insert_valores_em_uma_tabela_com_varias_colunas_e_nr_valores_diferentes(self):
        sql = Sql()
        table_name = "fruta"
        columns = ["name", "description"]
        values = ["abacaxi"]
        self.assertRaises(ListasDiferentesException, sql.insert(table_name, columns, values))
     
unittest.main()