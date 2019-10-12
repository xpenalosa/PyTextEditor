from kivy.lang import Builder
from kivy.uix.popup import Popup

Builder.load_string("""
#:kivy 1.11.1

<OkCancelDialog>:
    id: dialog
    BoxLayout:
        id: layout
        size: root.size
        pos: root.pos
        orientation: 'vertical'
        BoxLayout:
            id: dialog_content
            height: root.height - 30
        BoxLayout:
            id: buttons
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()
            Button:
                text: "Ok"
                on_release: root.confirm()
""")


class OkCancelDialog(Popup):

    def __init__(self, **kwargs):
        dialog_kwargs = kwargs.pop('dialog_content')
        super(Popup, self).__init__(**kwargs)
        self.callback = None
        self.used_callback = False
        # FIXME Customizable dialog content is not displayed
        self.ids['dialog_content'] = dialog_kwargs if dialog_kwargs else None

    def set_callback(self, callback):
        self.callback = callback

    def cancel(self):
        self.dismiss()

    def confirm(self):
        self.callback(self.dialog_content)
        self.used_callback = True
        self.dismiss()

    def on_dismiss(self):
        if not self.used_callback:
            self.callback(None)
            self.used_callback = True
        super(OkCancelDialog, self).on_dismiss()
