def ReadFile(): 
    userProfile = {}

    with open('87654299.txt', 'r') as file:    
        for line in file:
            key = str(str(line.split()).strip('[]')).strip("''")
            line = next(file, None)
            value = str(str(line.split()).strip('[]')).strip("''")

            if key is None:
                # oops, we got to the end of the file early
                raise ValueError('Invalid file format, missing key')
            
            userProfile[key]=value
    return userProfile

userProfile = ReadFile()
print(userProfile)