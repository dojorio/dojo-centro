# coding:utf-8
import csv

reader = csv.DictReader(open(r'C:\dojo\git\2011\20111221 - dadosabertos - python\TransferenciaRecursosEstadoMunicipiosRJ.csv', 'rb'), delimiter=';')

from portal_da_transparencia import agrupar
from pprint import pprint
pprint(agrupar(list(reader)))