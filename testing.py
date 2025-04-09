with open("links_2deep.txt", "r") as f:
    url_list = [line.strip() for line in f if line.strip()]
    
for url in url_list:
    if ".edu" not in url:
        print(url)