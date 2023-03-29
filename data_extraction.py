with open("survey7.ttl", "r", encoding="utf-8") as f, open("seeAlso.txt", "w", encoding="utf-8") as g:
        for line in f:
            if "seeAlso" in line:
                new_line = line[31:]
                g.write(new_line)