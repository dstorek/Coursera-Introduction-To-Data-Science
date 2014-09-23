import MapReduce
import sys

"""
Problem 4
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce
 algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.

Map Input
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person
 and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case
  that the personA is a friend of personB.

Reduce Output
The output should be the full symmetric relation. For every pair (person, friend), you will emit BOTH (person, friend)
 AND (friend, person). However, be aware that (friend, person) may already appear in the dataset, so you may produce
  duplicates if you are not careful.

You can test your solution to this problem using friends.json: $ python asymmetric_friendships.py friends.json

You can verify your solution by comparing your result with the file asymmetric_friendships.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: person friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value) # relationship
    mr.emit_intermediate(value, key) # inverted relationship

def reducer(key, list_of_friendships):
    # key: person name
    # value: list containing friendships and inverted friendships
    for friend in list_of_friendships:
        count = list_of_friendships.count(friend)
        if count == 1:                              # if count == 2 then it is a symmetrical relationship
            mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)