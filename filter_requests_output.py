dbpedia = "http://dbpedia.org/resource/"

with open("requests_output.txt", "r", encoding="utf-8") as f, open("requests_output_filtered.txt", "w", encoding="utf-8") as g:
    lines_seen = set()
    for line in f:
        split = line.split('"')
        for word in split:
            if dbpedia in word and word not in lines_seen:
                g.write("        dbr:hasResource        <" + word + "> ;" + "\n")
                lines_seen.add(word)