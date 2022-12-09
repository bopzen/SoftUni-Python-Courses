from project.team import Team


import unittest


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team('TeamName')
        self.members = {'Ivan': 20, 'Gosho': 30}

    def test_init_method(self):
        self.assertEqual('TeamName', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "team1"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_method_name_not_in_members(self):
        result = self.team.add_member(**self.members)
        self.assertEqual('Successfully added: Ivan, Gosho', result)
        self.assertEqual({'Ivan': 20, 'Gosho': 30}, self.team.members)

    def test_add_member_method_name_exists_in_members(self):
        self.team.members = self.members
        self.name_age = {'Ivan': 30}
        result = self.team.add_member(**self.name_age)
        self.assertEqual('Successfully added: ', result)
        self.assertEqual({'Ivan': 20, 'Gosho': 30}, self.team.members)

    def test_remove_member_method_name_exists_in_members(self):
        self.team.members = self.members
        result = self.team.remove_member('Ivan')
        self.assertEqual("Member Ivan removed", result)
        self.assertEqual({'Gosho': 30}, self.team.members)

    def test_remove_member_method_name_does_not_exist(self):
        self.team.members = self.members
        result = self.team.remove_member('Pesho')
        self.assertEqual("Member with name Pesho does not exist", result)
        self.assertEqual({'Ivan': 20, 'Gosho': 30}, self.team.members)

    def test_overriding_gt_method_return_false(self):
        self.team.members = {'Ivan': 20, 'Gosho': 30}
        self.other_team = Team('OtherName')
        self.other_team.members = {'Pesho': 5, 'Ivan': 5}
        result = self.team > self.other_team
        self.assertFalse(result)

    def test_overriding_gt_method_return_true(self):
        self.team.members = {'Ivan': 20, 'Gosho': 30, 'Pesho': 20}
        self.other_team = Team('OtherName')
        self.other_team.members = {'Pesho': 5, 'Ivan': 5}
        result = self.team > self.other_team
        self.assertEqual(True, result)

    def test_overriding_len_method(self):
        self.team.members = self.members
        result = self.team.__len__()
        self.assertEqual(2, result)

    def test_overriding_add_method(self):
        self.team.members = self.members
        self.other_team = Team('OtherName')
        self.other_team.members = {'Pesho': 5}
        self.new_team = self.team.__add__(self.other_team)
        self.assertEqual('TeamNameOtherName', self.new_team.name)
        self.assertEqual({'Ivan': 20, 'Gosho': 30, 'Pesho': 5}, self.new_team.members)

    def test_overriding_str_method(self):
        self.team.members = {'Ivan': 20, 'Gosho': 30, 'Gesho': 30}
        result = self.team.__str__()
        self.assertEqual("Team name: TeamName\n"
                         "Member: Gesho - 30-years old\n"
                         "Member: Gosho - 30-years old\n"
                         "Member: Ivan - 20-years old"
                         , result)


if __name__ == '__main__':
    unittest.main()
