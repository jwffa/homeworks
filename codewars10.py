def domain_name(url): #5kyu
    replaced_url = url.replace("http://", "").replace("https://", "").replace("www.", "").replace(".com", "").replace("/kata/", "")
    replaced_url = replaced_url.split(".")
    return replaced_url[0]
