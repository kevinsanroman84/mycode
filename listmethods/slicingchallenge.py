challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

word1 = challenge[2][1]
word2 = challenge[2][0]
word3 = challenge[3]

print(f"My {word1}! The {word2} do {word3}!")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

word1 = trial[2]["goggles"]
word2 = trial[2]["eyes"]
word3 = trial[3]

print(f"My {word1}! The {word2} do {word3}!")

nightmare= [
    {"slappy": "a", 
    "text": "b", 
    "kumquat": "goggles", 
    "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},
    "banana": 15, 
    "d": "nothing"}
    ]

word1 = nightmare[0]["user"]["name"]["first"]
word2 = nightmare[0]["kumquat"]
word3 = nightmare[0]["d"]

print(f"My {word1}! The {word2} do {word3}!")