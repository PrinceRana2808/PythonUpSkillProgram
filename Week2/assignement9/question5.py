#Write a code to perform multiple inheritance.

class Father:
    def skill1(self):
        print("Gardening Skill")

class Mother:
    def skill2(self):
        print("Cooking Skill")

class Son(Father,Mother):
    def skill3(self):
        print("Playing")

c=Son()

c.skill1()
c.skill2()
c.skill3()