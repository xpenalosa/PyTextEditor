from kivy.lang import Builder

import os

from editor.components.dialogs.ok_cancel_dialog import OkCancelDialog


class FileChooserDialog(OkCancelDialog):

    def __init__(self, **kwargs):
        path = kwargs.get("path", os.path.expanduser("~").replace("\\", "/"))
        dialog_widget = Builder.load_string(f'''
BoxLayout:
    size: root.size
    pos: root.pos
    orientation: "vertical"
    FileChooserListView:
        size: root.size
        id: file_chooser
        path: '{path}'
        on_selection: text_input.text =\
        self.selection and self.selection[0] or ''

    TextInput:
        id: text_input
        size_hint_y: None
        height: 30
        multiline: False
        text: '{path}'
        ''')
        super(FileChooserDialog, self).__init__(
            **kwargs,
            title="Choose a file",
            dialog_content=dialog_widget)

    def confirm(self):
        self.callback(self.ids['dialog_content'].ids['text_input'].text)
        self.used_callback = True
        self.dismiss()
