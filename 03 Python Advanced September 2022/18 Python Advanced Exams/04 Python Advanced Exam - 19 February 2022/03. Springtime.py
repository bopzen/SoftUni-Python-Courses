def start_spring(**kwargs):
    collection = {}
    result = []
    for key, value in kwargs.items():
        if value not in collection:
            collection[value] = []
        collection[value].append(key)
    sorted_collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, values in sorted_collection:
        result.append(f"{key}:")
        for value in sorted(values):
            result.append(f"-{value}")
    return "\n".join(result)