import requests_api
import filter_requests_output

with open("seeAlso.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    t = tuple(line.strip() for line in lines)

    with open("survey7.ttl", "r", encoding="utf-8") as g:
        with open("requests_output_filtered.txt", "w+", encoding="utf-8") as h:
            with open("survey7_modified.ttl", "w+", encoding="utf-8") as j:
                with open("requests_output.txt", "w+", encoding="utf-8") as k:
                    h.truncate(0)
                    k.truncate(0)
                    j.truncate(0)
                    seealso_count = 0
                    for line in g:
                        if "seeAlso" in line:
                            seealso_count += 1
                            if seealso_count <= len(t):
                                word = t[seealso_count-1]
                                requests_api.db_api(word)
                                filter_requests_output.iteration()
                                h.seek(0)
                                j.write(line)
                                j.write(h.read())
                            else:
                                j.write(line)
                        else:
                            j.write(line)
                    h.truncate(0)
                    k.truncate(0)
