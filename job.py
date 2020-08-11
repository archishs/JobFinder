class Jobs:
  job = ""
  company = ""
  province = ""
  city = ""
  income = ""
  benefits = ""
  requirededucation = ""
  email = ""
  phone = ""
  website = ""
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
    
    # assign attributes ------------------------------------.
  def assignAttributes(self, dictionary):
    for key in dictionary:
      setattr(self, key.lower() , dictionary[key])

    # ask questions ----------------------------------------        
  def askQuestions(self):
    x = 0
    while x == 0:
        a = input("What does your work environment provide? Choose 3 of the following: Sustainability, Fun work environment, Work life balance, Income, Community engagement, Recognition, Opportunities: ")
        a = a.split(", ")
        b = input("Which of the following describes your companies principles? Choose 3 that fit you best. Effecient, Flexible, Compassionate, Analytical, Adaptable, Organized, Goal Oriented, Creative, People Friendly: ")
        b = b.split(", ")
        c = input("How often do you help others without being asked? Choose one: Never, Sometimes, Often, Always: ")
        d = input("How would you describe your management style? ")
        e = input("What responsibilities does this job entail?")

        y = a
        if len(a) == 3:
            self.a = a
            x = 1
        else:
            x = 0

        y = b
        if len(b) == 3:
            self.b = b
            x = 1
        else:
            x = 0

        if c == "Never" or c == "never" or c == "Sometimes" or c == "sometimes" or c == "Often" or c == "often" or c == "Always" or c == "always":
            self.c = c
            x = 1
        else:
            x = 0

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

#sampleJob = Jobs("99486277.txt")