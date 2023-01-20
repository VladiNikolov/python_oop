
from unittest import TestCase, main

from project.team import Team


class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")

    def test_correct_init(self):
        team_name = "Team"
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_raises_when_name_contains_non_alpha(self):
        with self.assertRaises(ValueError) as ve:
            team = Team("asdjd;lkasdfji3&*(123$")
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_adds_only_new_player_to_the_team(self):
        self.team.members["ivan"] = 18

        result = self.team.add_member(ivan=18, gosho=13, stoqn=15)
        self.assertEqual(f"Successfully added: gosho, stoqn", result)
        self.assertEqual(13, self.team.members["gosho"])
        self.assertEqual(15, self.team.members["stoqn"])

    def test_remove_member_returns_error_message_when_player_does_not_exist(self):
        member_name = "Vladi"
        result = self.team.remove_member(member_name)
        self.assertEqual(f"Member with name {member_name} does not exist", result)

    def test_remove_member_removes_member_from_the_team(self):
        self.team.members['gosho'] = 20
        self.team.members['pesho'] = 21

        result = self.team.remove_member("pesho")
        self.assertEqual(f"Member pesho removed", result)
        self.assertEqual(20, self.team.members['gosho'])
        self.assertTrue("pesho" not in self.team.members)

    def test_gt_compares_team_by_members_count(self):
        self.team.members["member1"] = 10
        self.team.members["member2"] = 11

        another_team = Team("Another")
        another_team.members["member1"] = 10
        another_team.members["member2"] = 11
        another_team.members["member3"] = 12

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, self.team > another_team)

    def test_len_returns_members_count(self):
        self.team.members["member1"] = 10
        self.team.members["member2"] = 11

        self.assertEqual(2, len(self.team))

    def test_add_returns_new_team_with_combined_members(self):
        self.team.members["member1"] = 10
        self.team.members["member2"] = 11

        another_team = Team("Another")
        another_team.members["member3"] = 10
        another_team.members["member4"] = 11
        another_team.members["member5"] = 12

        result = self.team + another_team
        expecter_result_members = {
            "member1": 10,
            "member2": 11,
            "member3": 10,
            "member4": 11,
            "member5": 12,

        }
        self.assertEqual("TeamAnother", result.name)
        self.assertEqual(expecter_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_order_by_age_in_proper_string_format(self):
        self.team.members["member3"] = 12
        self.team.members["member1"] = 10
        self.team.members["member2"] = 11

        result = str(self.team)
        expected_result = f"Team name: Team\n" + \
                        f"Member: member3 - 12-years old\n" + \
                        f"Member: member2 - 11-years old\n" + \
                        f"Member: member1 - 10-years old"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()