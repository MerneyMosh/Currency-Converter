ab = [{'mo': '1'}, {'ms':'2'}, {'mis':'3'}]

for abb in ab:
    code, _  = list(abb.items())[1]
    print(code)