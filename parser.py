import rdflib

# Load the TTL file
graph = rdflib.Graph()
graph.parse("survey7.ttl", format="ttl")

# Find all instances of "rdfs:seeAlso"
seeAlso_triples = graph.triples((None, rdflib.RDFS.seeAlso, None))

# Write the "rdfs:seeAlso" values to a text file with UTF-8 encoding
with open("seeAlso_values.txt", "w", encoding="utf-8") as f:
    for s, p, o in seeAlso_triples:
        f.write(str(o) + "\n")

