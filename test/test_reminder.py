import unittest

from unittest.mock import patch

from reminder_proj.src.reminder import Reminder


class TestReminder(unittest.TestCase):
    def setUp(self):
        self.title = "TITLE"
        self.text = "TEXT"
        self.reminder = Reminder(self.title, self.text)

    def test_reminder_fields(self):
        assert self.reminder.title == self.title
        assert self.reminder.text == self.text

    @patch('reminder_proj.src.reminder.get_input')
    def test_reminder_times(self, mock_get_input):
        input_time = '18:50'
        mock_get_input.return_value = input_time
        self.reminder.set_time()
        assert self.reminder.times == input_time
