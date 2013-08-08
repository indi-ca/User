import sublime, sublime_plugin

class Bob(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "LocateMe")
