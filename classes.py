
#grades( a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16])
class grades:
    def __init__(self, user, c1c, c1e1, c1e2, c1f, c2c, c2e1, c2e2, c2f, c3c, c3e1, c3e2, c3f, c4c, c4e1, c4e2, c4f):
        self.student = user
        
        self.class1credits = c1c
        self.class1exam1 = c1e1
        self.class1exam2 = c1e2
        self.class1final = c1f

        self.class2credits = c2c
        self.class2exam1 = c2e1
        self.class2exam2 = c2e2
        self.class2final = c2f

        self.class3credits = c3c
        self.class3exam1 = c3e1
        self.class3exam2 = c3e2
        self.class3final = c3f

        self.class4credits = c4c
        self.class4exam1 = c4e1
        self.class4exam2 = c4e2
        self.class4final = c4f

    def lettergrade(self, grade):
        if int(self.grade) > 60:
            return 'D'
        elif int(self.grade) > 70:
            return 'C'
        elif int(self.grade) > 80:
            return 'B'
        elif int(self.grade) > 90:
            return 'A'
        else:
            return 'F'
