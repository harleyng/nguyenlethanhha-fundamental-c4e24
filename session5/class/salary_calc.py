salary_table = [
    {
    "name": "Huy",
    "vnd_per_hour": 20,
    "hour": 25,
},
{
    "name": "Quan",
    "vnd_per_hour": 30,
    "hour": 30,
},
{
    "name": "H.Duc",
    "vnd_per_hour": 25,
    "hour": 15,
},
]

wage_list = [ p["vnd_per_hour"] * p["hour"] for p in salary_table ]
total = sum(wage_list)
print(total)

# total = 0

# for p in salary_table:    
#     name = p["name"]
#     vnd = p["vnd_per_hour"]
#     hour = p["hour"]
#     wage = vnd * hour
#     print(name, wage, sep=": ")

#     total += wage 
# print("Total wage:", total)