class User:
  firstname = ""
  lastname = ""
  gender = ""
  birthdate = ""
  employment_status = ""
  username = ""
  password = ""
  email = ""
  province = ""
  city = ""
  income = ""
  phone = ""
  education = ""
  resumelink = ""
  website = ""
  work_experience = ""
  citizenship = ""
  salary_expectation = ""
  filename = ""

   # take information from file and create dictionary ------------------
  def readFile(self):
    userProfile = {}
    with open(self.fileName, 'r') as file:    
        for line in file:
            key = str(str(line.split()).strip('[]')).strip("''")
            line = next(file, None)
            value = str(str(line.split()).strip('[]')).strip("''")

            if key is None:
                # oops, we got to the end of the file early
                raise ValueError('Invalid file format, missing key')
              
            userProfile[key]=value
    return userProfile
    
    # assign attributes ------------------------------------
  def assignAttributes(self, dictionary):
    for key in dictionary:
      setattr(self, key.lower(), dictionary[key])

    # ask questions ----------------------------------------        
  def askQuestions(self):
    a = input("What do you look for in a job? Choose 3 of the following: Sustainability, Fun work environment, Work life balance, Income, Community engagement, Recognition, Opportunities: ")
    b = input("Which of the following describes your personality? Choose 3 that fit you best. Effecient, Flexible, Compassionate, Analytical, Adaptable, Organized, Goal Oriented, Creative, People Friendly: ")
    c = input("How often do you help others without being asked? Choose one: Never, Sometimes, Often, Always: ")
    d = input("When is a time that you went above and beyond in a workplace? ")
    e = input("What were your responsibilities at your previous job? If you have not worked before, what do you hope to do at your first job? ")

    a = a.split(",")
    b = b.split(",")

    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e

  def __init__(self, filename):
      self.a = ""
      self.c = ""
      self.d = ""
      self.e = ""
      self.fileName = filename
      raw_data = self.readFile()
      self.assignAttributes(raw_data)
      self.askQuestions()

#sampleUser = User("87654299.txt")
#print(sampleUser.city)