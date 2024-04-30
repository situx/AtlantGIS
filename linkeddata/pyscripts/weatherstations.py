from rdflib import Graph, URIRef, Literal
import csv


g=Graph()
with open('../../raster/precipitation/atlantgis_weather_stations.csv', newline='') as csvfile:
    wsreader = csv.DictReader(csvfile, delimiter='\t', quotechar='|')
    for row in wsreader:
        g.add((URIRef("http://atlantgis.squirrel.link/ontology#WeatherStation"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.w3.org/ns/sosa/Sensor")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://atlantgis.squirrel.link/ontology#WeatherStation")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Weather Station "+str(row["ws_id"]),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Wetterstation "+str(row["ws_id"]),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/ns/sosa/Observation")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation"),URIRef("http://www.w3.org/ns/sosa/observedProperty"),URIRef("http://atlantgis.squirrel.link/ontology#Precipitation")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation"),URIRef("http://www.w3.org/ns/sosa/phenomenonTime"),URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_phentime")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_phentime"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2006/time#Instant")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_phentime"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Precipitation observation time for Weather Station "+str(row["ws_id"]),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_phentime"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Beobachtungszeit für die Niederschlagsmenge gemessen von Wetterstation "+str(row["ws_id"]),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_phentime"),URIRef("http://www.w3.org/2006/time#inXSDgYear"),Literal("2017",datatype="http://www.w3.org/2001/XMLSchema#gYear")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation"),URIRef("http://www.w3.org/ns/sosa/madeBySensor"),URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"])))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation"),URIRef("http://www.w3.org/ns/sosa/hasResult"),URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/Measure")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Precipitation observation result for weather station "+str(row["ws_id"]),lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Messergebnis für die Niederschlagsmenge gemessen von Wetterstation "+str(row["ws_id"]),lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasNumericalValue"),Literal(str(row["prcpt"]),datatype="http://www.w3.org/2001/XMLSchema#double")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_2017_precipitation_result"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasUnit"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/millimetre")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://atlantgis.squirrel.link/ontology#Precipitation")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"])+"_geom"))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Weather Station "+str(row["ws_id"])+" Geometry",lang="en")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("AtlantGIS Wetterstation "+str(row["ws_id"])+" Geometrie",lang="de")))
        g.add((URIRef("http://atlantgis.squirrel.link/data/weatherstation/ws"+row["ws_id"]+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal("POINT("+str(row["lat"]).replace(",",".")+" "+str(row["lon"]).replace(",",".")+")",datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
        
g.serialize("weatherstations.ttl")