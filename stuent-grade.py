
class Student:
    '''
    Student（学号、姓名、性别、专业）
    '''

    def __init__(self, id, name, gender, major):
        self.id = id
        self.name = name
        self.gender = gender
        self.major = major
        self.stuCourseGrade = dict()
        self.getCredit = 0

    def addCourseGrade(self, course, score):
        self.stuCourseGrade.update({course: score})

    def showCourseScore(self):
        total_course_credit = 0
        print("学生 {} ".format(self.name))
        for k in self.stuCourseGrade:
            course_name = k.name
            course_credit = k.credit
            course_score = self.stuCourseGrade.get(k)
            total_course_credit += course_credit
            if course_score >= 60:
                self.getCredit += course_credit

                print("{}: {} \t 应获学分{},实际获得学分{} \t".format(course_name, course_score,course_credit, course_credit))
            else:
                print("{}: {} \t 应获学分{},实际获得学分{} \t".format(course_name, course_score,course_credit, 0))
        print("总学分{}/{}".format(self.getCredit ,total_course_credit))


    # 录入成绩
    # def addGrade(self, grade):
    #     self.stuGrade.append(grade.)

class Course:
    '''
    Course（编号、名称、学时、学分）
    '''
    def __init__(self, id, name, hour, credit):
        self.id = id
        self.name = name
        self.hour = hour
        self.credit = credit

    def __str__(self):
        return 'id:{}, name:{}, hour:{}, credit:{}'.format(self.id, self.name, self.hour, self.credit)

# class Grade:
#     '''
#     学生课程成绩类Grade（课程、分数）63


#     可以为一个学生添加一个或多个课程成绩，可以对某个学生所获学分进行计算
#     '''
#     def __init__(self, course, score):
#         self.gradeslist = {}
#
#     def showGrade(self):
#         for i in self.gradeslist:
#             print(i, self.gradeslist[i])
#
#     def appendCourseGrade(self, course, score):
#         # score是学生考试成绩
#         if score >= 60:
#             self.gradeslist[course]

stu1 = Student(1, '小明', '男', '信管')

c1 = Course(id=1, name='计算机基础', hour='36', credit=4)
c2 = Course(id=2, name='python', hour='24', credit=2)



stu1.addCourseGrade(course=c1, score=99)
stu1.addCourseGrade(course=c2, score=59)
stu1.addCourseGrade(course=c1, score=79)
stu1.showCourseScore()
