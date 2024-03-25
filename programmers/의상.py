from collections import defaultdict

# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
data = defaultdict(list)

for cl in clothes:
    name, category = cl
    data[category].append(name)

count_list = [len(data[category])+1 for category in data]

answer = 1

for count in count_list:
    answer *= count

print(answer - 1)
