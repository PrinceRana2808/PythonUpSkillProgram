#Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, 
# create a new dictionary containing only the students who scored above 80
#Expected output : {'Alice': 85, 'Charlie': 90}

scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
result={}

for key,val in scores.items():
    if val>80:
        result[key]=val
    
print(result)