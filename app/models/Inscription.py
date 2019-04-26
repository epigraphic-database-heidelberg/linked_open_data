from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON


class Inscription:

    def __init__(self,
                 hd_nr,
                 provinz,
                 land,
                 bearbeiter,
                 datum,
                 beleg,
                 **kwargs):
        prop_defaults = {
            "fo_modern": None,
            "fo_antik": None,
            "fundstelle": None,
            "verw_bezirk": None,
            "fundjahr": None,
            "aufbewahrung": None,
            "i_gattung": None,
            "i_traeger": None,
            "material": None,
            "hoehe": None,
            "breite": None,
            "tiefe": None,
            "if_h": None,
            "if_b": None,
            "bh": None,
            "tm_nr": None,
            "gdb_id": None,
            "sprache": None,
            "metrik": None,
            "dekor": None,
            "schreibtechnik": None,
            "interpunktion": None,
            "dat_jahr_a": None,
            "dat_jahr_e": None,
            "dat_monat": None,
            "dat_tag": None,
            "religion": None,
            "militaer": None,
            "geographie": None,
            "sowire": None,
            "literatur": None,
            "kommentar": None,
            "atext": None,
            "btext": None,
        }
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))
        self.hd_nr = hd_nr
        self.provinz = provinz
        self.land = land
        self.bearbeiter = bearbeiter
        self.datum = datum
        self.beleg = beleg

    def query(hd_nr):
        sparql = SPARQLWrapper("http://localhost:3030/edh/sparql")
        query = """
            SELECT *
            WHERE { <http://edh-www.adw.uni-heidelberg.de/edh/inschrift/%s> ?p ?o }
            LIMIT 10
        """ % hd_nr
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            print(result)

        # load data into inscription model


        if results:
            return results
