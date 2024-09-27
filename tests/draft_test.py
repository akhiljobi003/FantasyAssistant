import unittest
import io
import sys
from contextlib import redirect_stdout
from ..src.draft import draft_players

output1 = "How many players would you like to play with?Welcome to the Player Draft!\n\nRound 1:\nTeam 1, What player would you like to select?\nTeam 1 selects 2.\n\nRound 2:\nTeam 1, What player would you like to select?"
class TestDraftFunction(unittest.TestCase):
    def test_draft_output(self):
        # Redirect stuff
        original_stdin = sys.stdin
        sys.stdin = io.StringIO(user_input)
        output = io.StringIO()
        user_input = "1\n2\nexit\n"

        with redirect_stdout(output):

            sys.stdin = io.StringIO()
            draft_players()
            

        printed_output = output.getvalue()

        self.assertEqual(printed_output, output1)