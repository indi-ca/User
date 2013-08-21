import sublime, sublime_plugin, os

class Bob(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "LocateMe")

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(os.path.basename(self.view.file_name()))

class PathToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sublime.set_clipboard(self.view.file_name())

class MyChainedActionsCommand(sublime_plugin.WindowCommand):
   def run(self):
      #self.window.run_command("reveal_in_side_bar")
      #self.window.run_command("focus_side_bar")
      self.window.run_command("open_file", {"file": "${packages}/User/Default (Windows).sublime-keymap"})
      self.window.run_command("open_file", {"file": "${packages}/User/Default (OSX).sublime-keymap"})
      self.window.run_command("open_file", {"file": "${packages}/User/first.py"})


