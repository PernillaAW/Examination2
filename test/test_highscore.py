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

    @patch('pig.user.User')
    @patch("builtins.print")
    def test_check_list_new_player(self, mock_print, mock_user):
        highscor = highscore.Highscore()
        with patch.object(highscor, "new_player", return_value=(True)):
            with patch.object(mock_user, "NewUser"):
                new_user_name = "NewUser"

                result = highscor.check_list(new_user_name)
                self.assertTrue(result)

    @patch("builtins.print")
    def test_check_highscore_same_score(self, mock_print):
        highscor = highscore.Highscore()
        player = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=10))
        current_user = Mock(get_highscore=Mock(return_value=90), get_user_toss_count=Mock(return_value=12))

        result = highscor.check_highscore(current_user, player)
        self.assertIs(result, player)

    @patch('builtins.open', new_callable=MagicMock)
    @patch('pickle.load')
    def test_read_from_file_higscore(self, mock_load, mock_open_file):
        """Control that the program can read from a file."""
        highscor = highscore.Highscore()
        filename = "highscore.pickle."
        highscor.read_from_file()

        mock_open_file.assert_called_once_with(filename, 'rb')
        mock_load.assert_called_once_with(mock_open_file().__enter__())

        @patch('pickle.dump')
        def test_read_to_file(self, mock_dump):
            """Check so it can save to a file successfully."""
            highscor = highscore.Highscore()
            with patch.object(highscor, 'playerlist', []):
                sucess = highscor.read_to_file()
                self.assertTrue(sucess)

    @patch("pig.user.User")
    @patch("builtins.print")
    def test_sort_player_highscore(self, mock_print, mock_user):
        highscor = highscore.Highscore()
        with patch.object(mock_user, "get_user_name", side_effect=("User1", "User2")):
            with patch.object(mock_user, "get_highscore", side_effect=(90, 100)):
                with patch.object(mock_user, "get_user_toss_count", side_effect=(10, 12)):
                    highscor.playerlist.append(mock_user)
                    highscor.playerlist.append(mock_user)
                    highscor.sort_player_highscore()

                    self.assertEqual(highscor.playerlist, [mock_user, mock_user])

    @patch('pig.user.User')
    @patch("builtins.print")
    def test_update_highscore_list(self, mock_print, mock_user):
        highscor = highscore.Highscore()
        with patch.object(mock_user, 'get_user_name', side_effect=('user1', 'user2')):
            with patch.object(mock_user, 'get_highscore', side_effect=(90, 100)):
                with patch.object(mock_user, 'get_user_toss_count', side_effect=(90, 12)):
                    with patch.object(highscor, 'read_to_file', return_value=True):
                        highscor.playerlist.append(mock_user)
                        result = highscor.update_highscore_list(mock_user, mock_user)
                        self.assertIn(mock_user, highscor.playerlist)
                        self.assertTrue(result)

    @patch('pig.user.User')
    @patch("builtins.print")
    def test_display(self, mock_print, mock_user):
        highscor = highscore.Highscore()
        with patch.object(mock_user, 'get_user_name', side_effect=('user1', 'user2')):
            with patch.object(mock_user, 'get_highscore', side_effect=(90, 100)):
                with patch.object(mock_user, 'get_user_toss_count', side_effect=(90, 12)):
                    highscor.playerlist.append(mock_user)
                    highscor.playerlist.append(mock_user)
                    highscor.display()

                    expected_output = [
                        'User   Highscore   Toss Count',
                        'User1  100.0       10.0      ',
                        'User2  90.0        12.0      '
                        ]
                    mock_print.asser_has_calls([unittest.mock.call(line) for line in expected_output])


if __name__ == '__main__':
    unittest.main()
