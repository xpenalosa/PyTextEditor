from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.codeinput import CodeInput
from pygments import highlight
from pygments.lexers.special import TextLexer

Builder.load_string("""
#:kivy 1.11.1

<ConsoleLog>
    readonly: True
    background_color: [0.9, 0.92, 0.92, 1]
""")


class ConsoleLog(CodeInput):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(ConsoleLog, self).__init__(**kwargs)
        # Override lexer to hide syntax highlighting
        self.lexer = TextLexer()

    def _get_bbcode(self, ntext):
        # get bb-coded text to log
        if ntext and len(ntext):
            # Parse error lines
            ntext = ntext.replace(u'[ERR]', u'[/color][color=#ff3333]')
            ntext = ntext.replace(
                u'[/ERR]',
                ''.join([u'[/color][color=', str(self.text_color), u']']))
            # Add coloring to the rest of the file
            ntext = ''.join((u'[color=', str(self.text_color), u']',
                             ntext, u'[/color]'))
            ntext = ntext.replace(u'\n', u'')
            ntext = ntext.replace(u'[u]', '').replace(u'[/u]', '')
            return ntext
        return ''

    def clear_output(self):
        self.text = ""

    def log(self, line):
        self.text += line

    def error(self, line):
        # Add error tag to line before logging
        self.log(f"[ERR]{line}[/ERR]")
