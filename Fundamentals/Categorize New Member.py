'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs.
Each pair contains information for a single potential member.
Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior)
stating whether the respective member is to be placed in the senior or open category.
'''
def open_or_senior(data):
    new_data = []
    for x in data:
        if x[0] >= 55 and x[1] >7:
            new_data.append('Senior')
        else:
            new_data.append('Open')
    return new_data

def openOrSenior1(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

'''a = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
new_a = []
for i in a:
    if i[0] >= 55 and i[1] > 7:
        new_a.append('Senior')
    else:
        new_a.append('Open')
print(new_a)'''

