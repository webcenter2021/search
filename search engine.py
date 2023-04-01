# Read data from text file
with open('data.txt', 'r') as f:
    text = f.read()

# Split text into items
items = text.strip().split('\n\n')

# Create index of keywords
index = {}
for i, item in enumerate(items):
    lines = item.strip().split('\n')
    keywords = lines[-1].strip().lower().split(',')
    for keyword in keywords:
        keyword = keyword.strip()
        if keyword not in index:
            index[keyword] = set()
        index[keyword].add(i)

# Search function
def search(query):
    results = set()
    for keyword in query.lower().split():
        keyword = keyword.strip()
        if keyword in index:
            results.update(index[keyword])
    return [items[i] for i in results]

question = input('Search from our database:')

results = search(question)
for item in results:
    print(item)
