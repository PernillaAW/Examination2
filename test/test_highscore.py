import unittest
from unittest.mock import Mock, patch, mock_open
from pig import highscore


class TestHighscore(unittest.TestCase):

    @patch("builtins.print")
    def test_new_player(self, mock_print):
        highscor = highscore.Highscore()
        new_user = highscor.new_player("TestUser")

        self.assertIn(new_user, highscor.playerlist)


    @patch("builtins.print")
    def test_check_list_existing_player(self, mock_print):
        highscor = highscore.Highscore()
        existing_user = Mock(get_user_name=Mock(return_value="ExistingUser"))
        highscor.playerlist.append(existing_user)

        result = highscor.check_list(existing_user)
        self.assertIs(result, existing_user)

    @patch("builtins.print")
    def test_check_list_new_player(self, mock_print):
        highscor = highscore.Highscore()
        new_user_name = "NewUser"

        result = highscor.check_list(new_user_name)
        self.assertIsInstance(result, Mock)
        self.assertIn(result, highscor.playerlist)

    @patch("builtins.print")
    def test_check_highscore_same_score(self, mock_print):
        highscor = highscore.Highscore()
        player = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=10))
        current_user = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=12))

        result = highscor.check_highscore(current_user, player)
        self.assertIs(result, player)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("builtins.print")
    def test_read_to_file(self, mock_print, mock_file_open):
        highscor = highscore.Highscore()
        mock_user = Mock()
        highscor.playerlist = [mock_user]
        highscor.read_to_file()
        mock_file_open.assert_called_once_with(highscor.file, "wb")
        mock_file_open.return_value.write.assert_called_once_with(str(highscor.playerlist))

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("builtins.print")
    def test_read_from_file(self, mock_print, mock_file_open):
        highscor = highscore.Highscore()
        highscor.read_from_file()
        mock_file_open.assert_called_once_with(highscor.file, "wb")
        mock_file_open.return_value.read.assert_called_once()

    @patch("builtins.print")
    def test_sort_player_highscore(self, mock_print):
        highscor = highscore.Highscore()
        user1 = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=10))
        user2 = Mock(get_highscore=Mock(return_value=100), get_user_toss_count=Mock(return_value=12))
        highscor.playerlist = [user2, user1]
        highscor.sort_player_highscore()

        self.assertEqual(highscor.playerlist, [user2, user1])

    @patch("builtins.print")
    def test_update_highscore_list(self, mock_print):
        highscor = highscore.Highscore()
        player = Mock()
        user = Mock()
        highscor.playerlist = [player]

        result = highscor.update_highscore_list(player, user)
        self.assertNotIn(player, highscor.playerlist)
        self.assertIn(user, highscor.playerlist)
        self.assertTrue(result)

    @patch("builtins.print")
    def test_update_highscore_list_player_not_in_list(self, mock_print):
        highscor = highscore.Highscore()
        player = Mock()
        user = Mock()

        result = highscor.update_highscore_list(player, user)
        self.assertNotIn(player, highscor.playerlist)
        self.assertNotIn(user, highscor.playerlist)
        self.assertFalse(result)

    @patch("builtins.print")
    def test_update_highscore_list_current_user_higher_score(self, mock_print):
        highscor = highscore.Highscore()
        player = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=10))
        current_user = Mock(get_highscore=Mock(return_value=100), get_user_toss_count=Mock(return_value=12))
        highscor.playerlist = [player]

        result = highscor.update_highscore_list(player, current_user)
        self.assertNotIn(player, highscor.playerlist)
        self.assertIn(current_user, highscor.playerlist)
        self.assertTrue(result)

    @patch("builtins.print")
    def test_display(self, mock_print):
        highscor = highscore.Highscore()
        user1 = Mock(get_highscore=Mock(return_value=100), get_user_toss_count=Mock(return_value=10))
        user2 = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=12))
        highscor.playerlist(user2, user1)
        highscor.display()

        expected_output = [
            'User   Highscore   Toss Count',
            'User1  100.0       10.0      ',
            'User2  90.0        12.0      '
        ]

        mock_print.asser_has_calls([unittest.mock.call(line) for line in expected_output])


if __name__ == '__main__':
    unittest.main()
