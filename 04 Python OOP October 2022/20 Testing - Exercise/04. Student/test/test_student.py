import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student_without_courses = Student('Ivan')
        self.student_with_courses = Student('Gosho', {'math': ['note1']})

    def test_init_method(self):
        self.assertEqual('Ivan', self.student_without_courses.name)
        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual('Gosho', self.student_with_courses.name)
        self.assertEqual({'math': ['note1']}, self.student_with_courses.courses)

    def test_enroll_method_course_name_exists_add_notes(self):
        result = self.student_with_courses.enroll('math', ['note2', 'note3'])
        self.assertEqual(['note1', 'note2', 'note3'],self.student_with_courses.courses['math'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_method_new_course_name_add_notes_empty(self):
        result = self.student_with_courses.enroll('math 2', ['note1', 'note2'])
        self.assertEqual(['note1', 'note2'], self.student_with_courses.courses['math 2'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_new_course_name_add_notes_y(self):
        result = self.student_without_courses.enroll('math 2', ['note1', 'note2'], 'Y')
        self.assertEqual(['note1', 'note2'], self.student_without_courses.courses['math 2'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_new_course_name_no_notes(self):
        result = self.student_with_courses.enroll('math 2', ['note1', 'note2'], 'N')
        self.assertEqual([], self.student_with_courses.courses['math 2'])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_method_course_exists(self):
        result = self.student_with_courses.add_notes('math', 'note2')
        self.assertEqual(['note1', 'note2'], self.student_with_courses.courses['math'])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_method_course_does_not_exist(self):
        with self.assertRaises(Exception) as ee:
            self.student_with_courses.add_notes('math2', 'note2')
        self.assertEqual("Cannot add notes. Course not found.", str(ee.exception))

    def test_leave_course_method_course_exists(self):
        result = self.student_with_courses.leave_course('math')
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_method_course_does_not_exit(self):
        with self.assertRaises(Exception) as ee:
            self.student_with_courses.leave_course('math2')
        self.assertEqual("Cannot remove course. Course not found.", str(ee.exception))


if __name__ == '__main__':
    unittest.main()