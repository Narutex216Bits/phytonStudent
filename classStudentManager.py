class StudentManager:
    def __init__(self):

        def add_student(self, name: str, grades: list):
            if name in self.students:
                raise ValueError(f"Estudante{name} já existe.")
                if not all(isinstance(grade, (int,float))for grade in grades):
                    raise ValueError("As notas precisam ser uma lista de números")
                    self.students[name] = grades
           
            def get_average(self, name: str) -> float:
                if name not in self.students:
                    raise ValueError(f"Student{name}does not exists")
                    return sum(self.students[name]/len(self.students[name]))
            
            def is_passed(self. name:str, passing_grade: float = 6.0)->bool:
                average = self.get_average(name)
                return average >= passing_grade

import unittest

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        #configuração inicial para cada teste.
        self.manager = studentManager()

        def test_add_student(self):
            self.manager.add_student("Alice", [8.0,7.5,9.0])
            self.assertln("Alice", self.manager.students)

        def test_add_student_existing(self):
            self.manager.add_student("Alice",[8.0,7.5,9.0])
            with self.assertRaises(ValueError):
                self.manager.add_student("Alice",[6.0,7.0])

