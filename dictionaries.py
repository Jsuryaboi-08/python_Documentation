#dictionary is a changeable, unordered collection of unique key:value pairs

capitals = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
print(capitals)
print(capitals['USA'])
print(capitals.get('India'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals['Germany'] = 'Berlin'
print(capitals)

capitals.update({'UK':'London'})
print(capitals)
capitals.update({'USA':'Las Vegas'})#updates the value of the key
print(capitals)
capitals.pop('China')#removes the key:value pair
print(capitals)
capitals.popitem()#removes the last key:value pair
print(capitals)
del capitals['India']#removes the key:value pair
print(capitals)
capitals.clear()#removes all key:value pairs