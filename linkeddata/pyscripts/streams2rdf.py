from rdflib import Graph,URIRef, Literal
import json
import os
from shapely.geometry import shape

datans="http://atlantgis.squirrel.link/data/"
ontns="http://atlantgis.squirrel.link/ontology#"
 
g=Graph()
f = open ("../../vector/geojson/streams.geojson", "r")
roads = json.loads(f.read())
featcounter=0
for rd in roads["features"]:
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Stream")))
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Stream "+str(featcounter),lang="en")))
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Strom "+str(featcounter),lang="de")))
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://atlantgis.squirrel.link/ontology#stream_cat"),Literal(str(rd["properties"]["cat"]),datatype="http://www.w3.org/2001/XMLSchema#double")))
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://atlantgis.squirrel.link/ontology#stream_value"),Literal(str(rd["properties"]["value"]),datatype="http://www.w3.org/2001/XMLSchema#double")))    
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef(ontns+"discharge"),URIRef(datans+"stream"+str(featcounter)+"_discharge"))) 
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge",URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/Quantity")))
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge",URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Water discharge of stream "+str(featcounter),lang="en")))
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge",URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Wasserablass von Strom "+str(featcounter),lang="de")))
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge",URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasValue"),URIRef(datans+"stream"+str(featcounter)+"_discharge_value")))      
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge_value",URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasUnit"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/cubicMetrePerSecond-Time")))  
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge_value",URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/hasNumericalValue"),Literal(str(rd["properties"]["discharge"]),datatype="http://www.w3.org/2001/XMLSchema#double")))  
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge_value",URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.ontology-of-units-of-measure.org/resource/om-2/Measure")))
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge_value",URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Water discharge value of stream "+str(featcounter),lang="en")))
    g.add((URIRef(datans+"stream"+str(featcounter))+"_discharge_value",URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Wasserablasswert von Strom "+str(featcounter),lang="de")))
    g.add((URIRef(datans+"stream"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+"stream"+str(featcounter)+"_geom"))) 
    print(rd["geometry"])
    if "geometry" in rd and rd["geometry"]!=None and "coordinates" in rd["geometry"]:
        wktgeom = shape(rd["geometry"])
        g.add((URIRef(datans+"stream"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#LineString")))
        g.add((URIRef(datans+"stream"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Stream "+str(featcounter)+" Geometry",lang="en")))
        g.add((URIRef(datans+"stream"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Strom "+str(featcounter)+" Geometrie",lang="de")))
        g.add((URIRef(datans+"stream"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(str(wktgeom).replace("MULTILINESTRING ((","LINESTRING (").replace("))",")"),datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))  
    featcounter+=1
g.add((URIRef("http://www.opengis.net/ont/sf#LineString"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Geometry")))
g.add((URIRef(ontns+"Sream"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Feature")))
g.serialize("streams.ttl")
    

