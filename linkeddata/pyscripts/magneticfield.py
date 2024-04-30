from rdflib import Graph, URIRef, Literal
import csv


g=Graph()
with open('../../project_datasets/barrow/barrow_magnetic_raw_data.csv', newline='') as csvfile:
    wsreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in wsreader:
        print(row)
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/ns/sosa/Sensor")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Barrow "+str(str(row["barrow_id"])),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Barrow "+str(str(row["barrow_id"])),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/ns/sosa/Observation")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux"),URIRef("http://www.w3.org/ns/sosa/observedProperty"),URIRef("http://atlantgis.squirrel.link/ontology#MagneticFlux")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux"),URIRef("http://www.w3.org/ns/sosa/phenomenonTime"),URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_phentime")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_phentime"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2006/time#Instant")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_phentime"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Magnetic flux observation time for Barrow "+str(str(row["barrow_id"])),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_phentime"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Beobachtungszeit für den Magnetfluss gemessen von Barrow "+str(str(row["barrow_id"])),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_phentime"),URIRef("http://www.w3.org/2006/time#inXSDgYear"),Literal("2017",datatype="http://www.w3.org/2001/XMLSchema#gYear")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux"),URIRef("http://www.w3.org/ns/sosa/madeBySensor"),URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"]))))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux"),URIRef("http://www.w3.org/ns/sosa/hasResult"),URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/Measure")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Magnetic flux observation result for barrow "+str(row["barrow_id"]),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Messergebnis für den Magnetfluss gemessen von Barrow "+str(row["barrow_id"]),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasNumericalValue"),Literal(str(row["magnetic_flux_in_nT"]),datatype="http://www.w3.org/2001/XMLSchema#double")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_2017_magneticflux_result"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasUnit"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/nanoTesla")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"]))+"_geom"))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Barrow Magnetic Data "+str(str(row["barrow_id"]))+" Geometry",lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Wetterstation "+str(str(row["barrow_id"]))+" Geometrie",lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/barrow/barrow"+str(row["barrow_id"])+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal("<http://www.opengis.net/def/crs/EPSG/0/32628> POINT("+str(row["y"]).replace(",",".")+" "+str(row["x"]).replace(",",".")+")",datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
        
g.serialize("magneticflux.ttl")