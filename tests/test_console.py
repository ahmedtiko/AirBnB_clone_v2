#!/usr/bin/python3

import unittest
from unittest.mock import patch
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def create(self):
        return HBNBCommand()

    def test_quit(self):
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        con = self.create()
        con.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("** instance id missing **"))
