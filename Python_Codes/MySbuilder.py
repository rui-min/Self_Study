"""
@completion: June 29, 2021
@author: Rui Min
@topic: String Builder built by myself
"""
class MySbuilder():
    def __init__(self, initial = None):
        # ensure defaults "None" for mutable data!
        self.charList = []
        
        if type(initial) == str:
            for char in initial:
                self.charList.append(char)
        
        if (type(initial) == list) and (initial != []) and (type(list[0]) == str):
            for strele in initial:
                for char in strele:
                    self.charList.append(char)

    # @classmethod
    # def from_string(cls, str0):
    #     return cls(str0)

    def append(self, addition = None):
        if type(addition) == MySbuilder:
            for char in addition.charList:
                self.charList.append(char)
            return True
        
        if type(addition) == str:
            for char in addition:
                self.charList.append(char)
            return True
        
        if type(addition) == int:
            str0 = str(int)
            for char in str0:
                self.charList.append(char)
            return True

        return False

    def insert(self, offset, addition):
        if (offset >= len(self.charList)) or (offset < 0):
            return False

        counter = offset
        if type(addition) == str:
            for char in addition:
                self.charList.insert(counter, char)
                counter += 1
            return True

        if type(addition) == MySbuilder:
            for char in addition.charList:
                self.charList.insert(counter, char)
                counter += 1
            return True
    
        return False


    def length(self):
        return len(self.charList)


    def reverse(self):
        cloneList = self.charList.copy()    # shallow copy enough for primitive elements
        for i in range(len(cloneList)):
            self.charList[i] = cloneList[len(cloneList)-i-1]
        return None

    def toLowerCase(self):
        for i in range(len(self.charList)):
            # string is special: its methods' return changed but itself not changed
            # avoid using "char in charList" because primitive type is copied, NOT aliased!
            self.charList[i] = self.charList[i].lower()     
        return None

    def toUpperCase(self):
        for i in range(len(self.charList)):
            # string is special: its methods' return changed but itself not changed
            # avoid using "char in charList" because primitive type is copied, NOT aliased!
            self.charList[i] = self.charList[i].upper()
            
        return None
    



    # @Override (@Override without # disallowed)
    def __str__(self):
        # this is cheating, but we canNOT directly deal with characters in Python
        return "".join(self.charList)

    # @Override
    def __repr__(self):
        return '{self.__class.__name__}({self.charList})'.format(self=self)


# procedural paradigm for obtaining substring: used in format "substring(args)"
def substring(self, begin=0, end = -1):
    if end == -1:
        end = len(self.charList)
    subList = []
    for i in range(begin,end,1):
        subList.append(self.charList[i])
    # this is cheating, but we canNOT directly deal with characters in Python
    return "".join(subList)

# procedural paradigm for sample run: avoid @staticmethod
def exampleRun():  
    str1 = "haha"
    str2 = "hehe"
    str3 = "hihi"
    s1 = MySbuilder("haha")
    s2 = MySbuilder(str2)
    s1.append(s2)
    print(s1);	# hahahehe
    s1.insert(1,str3)
    print(s1);  # hhihiahahehe
    print(substring(s1,0,2))    # hh
    s1.toUpperCase()
    print(s1)   # HHIHIAHAHEHE
    s1.toLowerCase()
    s1.reverse()
    print(s1)   # ehehahaihihh


if __name__ == "__main__":
    exampleRun()
    