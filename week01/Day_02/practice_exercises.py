
def word_frequency(text):
    wordcount = {}
    wordlist = text.split()
    for word in wordlist:
        word = word.lower()
        wordcount[word] = wordcount.get(word, 0)+1
    return wordcount

assert word_frequency("GET get post") == {"get": 2,"post": 1}

def dedupe_keep_order(items):
    seen=set()
    result=[]
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# print(dedupe_keep_order([4,2,2,2,6,1,8,4,2]))
assert dedupe_keep_order([4,2,2,2,6,1,8,4,2]) == [4,2,6,1,8]

def group_by_city(users):
    grouped_users={}
    for user in users:
        city = user["city"]
        grouped_users.setdefault(city, []).append(user.get("name"))
    return grouped_users

assert group_by_city([{"name": "Asha", "city": "Buffalo"}, {"name":"Bisha", "city":"Syracuse"}, {"name": "Usha", "city":"Buffalo"}]) == {"Buffalo":["Asha", "Usha"], "Syracuse":["Bisha"]}

def invert(d):
    inverted_d={}
    for d_key, d_value in d.items():
        inverted_d[d_value]=d_key
    return inverted_d

assert invert({"a":1, "b":2}) == {1: "a", 2: "b"}
# In invert() function, if in the intial dict 2 keys share same value, then during inversion only 1 key-value pair will be created and the key will hold the value that occured latest.
# Also, there is a risk that if the argument dict d has any value that is not hashable (eg: a list), it will not become a key during inversion, and give an error

# Better approach for URL builder
from urllib.parse import urlencode
def build_url(base, *paths, **query):
    url = "/".join([base.rstrip("/"), *paths])
    if query:
        url += "?" + urlencode(query)    # 'red shoes & socks' → 'red+shoes+%26+socks'
    return url

def build_url(base, *paths, **query):
    """"build_url("https://api.x.com", "v1", "users", limit=10, page=2) → "https://api.x.com/v1/users?limit=10&page=2". With no query args, there's no ?"""
    url = base
    path_set = paths
    query_dict = query
    if path_set is not None:
        for p in path_set:
            url = url+"/"+p
    if query_dict:
        url = url + "?"
        for k, v in query_dict.items():
            url = url + str(k) + "=" + str(v) + "&"
    url = url[:-1]
    return url

assert build_url("https://api.x.com", "v1", "users", limit=10, page=2) == "https://api.x.com/v1/users?limit=10&page=2"

def top_n_employees(employees, n):
    result = sorted(employees, key=lambda e:(-e[1], e[0]))[:n]
    return [e[0] for e in result]

# print(top_n_employees([("A", 100), ("C", 800), ("F", 600), ("B", 50), ("H", 100)], 3))
assert top_n_employees([("A", 100), ("C", 800), ("F", 600), ("B", 50), ("H", 100)], 3) == ['C', 'F', 'A']