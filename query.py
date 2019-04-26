from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:3030/edh/sparql")
sparql.setQuery("""
    SELECT *
    WHERE { <http://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD028583> ?p ?o }
    LIMIT 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)

