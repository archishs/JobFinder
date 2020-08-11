import matcher as match
import job
import user


jb = job.Jobs("job1.txt")
mp = user.User("user1.txt")

score_count = 0
# city = 0-1
if jb.city == mp.city:
  score_count += 1

print("Job city: ", jb.city)
print("User city: ", mp.city)
print("City", score_count)

# education = 0-1-2
if jb.requirededucation == "None":
     score_count += 1
print("Job edu: ", jb.requirededucation)
print("User edu: ", mp.education)

if jb.requirededucation == "HS":
  if mp.education == "HS" or mp.education == "U" or mp.education == "G":
     score_count += 1

if jb.requirededucation == "U":
  if mp.education == "U" or mp.education == "G":
     score_count += 1

if jb.requirededucation == "G":
  if mp.education == "G":
     score_count += 1
print("Eductation", score_count)

# expected salary = employers offer / user expected salary
score_count += min(int(jb.income)/int(mp.income),1)
print("JB income:", jb.income)
print("MP income", mp.income)
print("Salary", score_count)

# work/hands on experience in field = 0 years --> 0: 1-4 --> 1: 5-9 --> 2: 10+ --> 3
if int(mp.work_experience) == 0:
  score_count += 0
elif int(mp.work_experience) <= 4:
  score_count += 1
elif int(mp.work_experience) <= 9:
  score_count += 2
else:
  score_count +=3
print("User Experinece: ", mp.work_experience)
print("Work Experience", score_count)
  
# question a = 0-1-2-3 
if jb.a[0] == mp.a[0]:
  score_count += 1
if jb.a[1] == mp.a[1]:
  score_count += 1
if jb.a[2] == mp.a[2]:
  score_count += 1
print("jb A:", jb.a)
print("mp A:", mp.a)
print("A", score_count)

# question b = 0-1-2-3
if jb.b[0] == mp.b[0]:
  score_count += 1
if jb.b[1] == mp.b[1]:
  score_count += 1
if jb.b[2] == mp.b[2]:
  score_count += 1
print("jb B:", jb.b)
print("mp B:", mp.b)
print("B", score_count)
  
# question c = 0-1
if jb.c == mp.c:
  score_count += 1
print("jb C:", jb.c)
print("mp C:", mp.c)
print("C", score_count)
  
# question d = score from matcher.py
score_count += match.levenshtein_ratio_and_distance(jb.d, mp.d, True)
print("LRD", score_count)
# question e = score from matcher.py
score_count += match.levenshtein_ratio_and_distance(jb.e, mp.e, True)
print("LRD2", score_count)

print("you scored ", (score_count/13)*100, "%")
