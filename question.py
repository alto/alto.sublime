import datetime, getpass
import sublime, sublime_plugin

class QuestionCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        question = "# QUESTION: question [%s %s]" % (datetime.datetime.now().strftime("%Y-%m-%d"), getpass.getuser())

        # self.view.insert(edit, 0, question)
        for r in self.view.sel():
          self.view.replace(edit, r, question)
        # self.view.replace(edit, 0, question)
