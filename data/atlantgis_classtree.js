var tree={
  "plugins": [
    "defaults",
    "search",
    "sort",
    "state",
    "types",
    "contextmenu"
  ],
  "search": {
    "show_only_matches": true
  },
  "types": {
    "class": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/class.png"
    },
    "geoclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geoclass.png"
    },
    "halfgeoclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/halfgeoclass.png"
    },
    "collectionclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/collectionclass.png"
    },
    "geocollection": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geometrycollection.png"
    },
    "featurecollection": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/featurecollection.png"
    },
    "instance": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/instance.png"
    },
    "geoinstance": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geoinstance.png"
    }
  },
  "core": {
    "themes": {
      "responsive": true
    },
    "check_callback": true,
    "data": [
      {
        "id": "http://atlantgis.squirrel.link/ontology#Ampheres",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Ampheres (:Ampheres)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Atlas",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Atlas (:Atlas)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Autochthon",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Autochthon (:Autochthon)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Azaes",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Azaes (:Azaes)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Diaprepes",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Diaprepes (:Diaprepes)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Elasippos",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Elasippos (:Elasippos)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Euaimon",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Euaimon (:Euaimon)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Eumelos_Gadeiros",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Eumelos_Gadeiros (:Eumelos_Gadeiros)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Mestor",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Mestor (:Mestor)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Mneseus",
        "parent": "http://atlantgis.squirrel.link/ontology#Archont",
        "type": "instance",
        "text": "Mneseus (:Mneseus)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Archont",
        "parent": "http://atlantgis.squirrel.link/ontology#HumanEntity",
        "type": "class",
        "text": "Archont (:Archont) [10]",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#HumanEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "class",
        "text": "HumanEntity (:HumanEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/data/nonns_CoastLine_Style.html",
        "parent": "http://www.opengis.net/ont/geosparql#Style",
        "type": "instance",
        "text": "CoastLine_Style (:CoastLine_Style)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Style",
        "parent": "#",
        "type": "class",
        "text": "Style (gsp:Style) [1]",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#ArchaeologicalSite",
        "parent": "http://atlantgis.squirrel.link/ontology#Site",
        "type": "class",
        "text": "ArchaeologicalSite (:ArchaeologicalSite)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Site",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "class",
        "text": "Site (:Site)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "parent": "#",
        "type": "class",
        "text": "AtlantGIS_Classes (:AtlantGIS_Classes)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#CoastLine",
        "parent": "#",
        "type": "class",
        "text": "CoastLine (:CoastLine)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Find",
        "parent": "http://atlantgis.squirrel.link/ontology#FindingsEntity",
        "type": "class",
        "text": "Find (:Find)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#FindingsEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "class",
        "text": "FindingsEntity (:FindingsEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Goldkupfererz",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "class",
        "text": "Goldkupfererz (:Goldkupfererz)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Resource",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "class",
        "text": "Resource (:Resource)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#LandType",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "class",
        "text": "LandType (:LandType)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Feature",
        "parent": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "type": "class",
        "text": "Feature (gsp:Feature)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Period",
        "parent": "http://atlantgis.squirrel.link/ontology#TemporalEntity",
        "type": "class",
        "text": "Period (:Period)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#TemporalEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "class",
        "text": "TemporalEntity (:TemporalEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Silber",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "class",
        "text": "Silber (:Silber)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Stream",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "class",
        "text": "Stream (:Stream)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#VesselType",
        "parent": "http://atlantgis.squirrel.link/ontology#Find",
        "type": "class",
        "text": "VesselType (:VesselType)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Voronoi",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "class",
        "text": "Voronoi (:Voronoi)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "parent": "#",
        "type": "class",
        "text": "Wikidata_Classes (:Wikidata_Classes)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Zinn",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "class",
        "text": "Zinn (:Zinn)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "class",
        "text": "SpatialObject (gsp:SpatialObject)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Geometry",
        "parent": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "type": "class",
        "text": "Geometry (gsp:Geometry)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiLineString",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "class",
        "text": "MultiLineString (sf:MultiLineString)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiPoint",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "class",
        "text": "MultiPoint (sf:MultiPoint)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiPolygon",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "class",
        "text": "MultiPolygon (sf:MultiPolygon)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#Point",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "class",
        "text": "Point (sf:Point)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q1554231",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q1554231 (wde:Q1554231)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q1701967",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q1701967 (wde:Q1701967)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q17334923",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q17334923 (wde:Q17334923)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q193379",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q193379 (wde:Q193379)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q3001793",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q3001793 (wde:Q3001793)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q355304",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q355304 (wde:Q355304)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q6428674",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q6428674 (wde:Q6428674)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q757267",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q757267 (wde:Q757267)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q839954",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "class",
        "text": "Q839954 (wde:Q839954)",
        "data": {}
      }
    ]
  },
  "@context": {
    "@version": 1.1,
    "foaf": "http://xmlns.com/foaf/0.1/",
    "ct": "http://purl.org/vocab/classtree#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "icon": "foaf:image",
    "id": "@id",
    "parent": "rdfs:subClassOf",
    "halfgeoclass": "ct:HalfGeoClass",
    "geoclass": {
      "@type": "ct:icontype",
      "@id": "ct:GeoClass"
    },
    "collectionclass": {
      "@type": "ct:icontype",
      "@id": "ct:CollectionClass"
    },
    "featurecollectionclass": {
      "@type": "ct:icontype",
      "@id": "ct:FeatureCollectionClass"
    },
    "class": "owl:Class",
    "instance": "owl:NamedIndividual",
    "geoinstance": {
      "@type": "ct:Icontype",
      "@id": "ct:GeoNamedIndividual"
    },
    "text": "rdfs:label",
    "type": "ct:icontype",
    "types": "ct:icontypes",
    "core": {
      "@type": "ct:TreeConfig",
      "@id": "@nest"
    },
    "data": {
      "@id": "ct:treeitem",
      "@type": "ct:TreeItem"
    }
  }
}