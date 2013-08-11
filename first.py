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
