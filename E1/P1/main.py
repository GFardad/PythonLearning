url = "https://code.visualstudio.com/docs/sourcecontrol/overview"
tdl_hint = [".com", ".ir", ".net", ".org", ".co"]
parts = url.split("://", 1)
rest_of_url = parts[1]
protocol = parts[0]


tdl, path = "unknown", "unknown"
for key in tdl_hint:
    new_rest_of_url = rest_of_url.split(key, 1)
    if len(new_rest_of_url) != len(rest_of_url):
        tdl = key
        path = rest_of_url.split(tdl, 1)[1]
        break


domain = rest_of_url.split(tdl, 1)[0]


print(f"protocol : {protocol}")
print(f"url : {rest_of_url}")
print(f"TDL : {tdl}")
print(f"path : {path}")
print(f"Domain : {domain}{tdl}")
