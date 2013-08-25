import sublime, sublime_plugin
import os
import sys

sidebar_visible = False

class InsertDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        edit.insertCharacters("hello")
        #line = edit.line(region)
        #lineContents = 'Today' + '\n'
        #edit.insert(line.begin(), lineContents)

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(os.path.basename(self.view.file_name()))

class PathToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(self.view.file_name())

class MyChainedActionsCommand(sublime_plugin.WindowCommand):
   def run(self):
      if sys.platform == "win32":
        self.window.run_command("open_file", {"file": "${packages}/User/Default (Windows).sublime-keymap"})
        # self.window.run_command("open_file", {"file": "U:/.PyCharm20/config/keymaps/Win_Pycharm_Frictionless.xml"})
      else:
        self.window.run_command("open_file", {"file": "${packages}/User/Default (OSX).sublime-keymap"})
        self.window.run_command("open_file", {"file": "/Users/indika/Library/Preferences/PyCharm20/keymaps/OSX_Pycharm_Frictionless.xml"})

      self.window.run_command("open_file", {"file": "${packages}/User/extensions.py"})


class OpenSublimeExplorerCommand(sublime_plugin.WindowCommand):
   def run(self):
      # https://github.com/reu-res/ST2Assistant/blob/master/ST2Assistant.py
      global sidebar_visible
      if sidebar_visible:
        self.window.run_command("toggle_side_bar")
        sidebar_visible = False
      else:
        self.window.run_command("reveal_in_side_bar")
        self.window.run_command("focus_side_bar")
        sidebar_visible = True



