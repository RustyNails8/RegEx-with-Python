import re

string = "begin:learner1:scientific:learner2:scientific:learner3:end"
print(re.findall(r"(\w+)(?=:scientific)", string))
