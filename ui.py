import io
import sys
from PyQt5.QtWidgets import (QApplication, 
                            QWidget, 
                            QVBoxLayout, 
                            QTextEdit, 
                            QPushButton, 
                            QHBoxLayout, 
                            QComboBox,
                            QFileDialog)
from doc_formatter import format_bytes

max_paragraph_lines = 15


class TextFormatter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Formatter")

        # Layouts
        main_layout = QVBoxLayout()
        combobox_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Multiline text box
        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        main_layout.addWidget(self.text_edit)

        # Combobox for lines per paragraph 
        self.combobox_label = QTextEdit("Lines per paragraph:")
        self.combobox_label.setReadOnly(True)
        self.combobox_label.setFixedHeight(20)
        self.combobox_label.setFixedWidth(150)
        self.combobox_label.setStyleSheet("background-color: #323232")
        combobox_layout.addWidget(self.combobox_label)

        self.lines_per_paragraph = 2
        self.dropdown = QComboBox()
        self.dropdown.addItems([str(i) for i in range(1, max_paragraph_lines + 1)])
        self.dropdown.setCurrentText(str(self.lines_per_paragraph))
        self.dropdown.currentTextChanged.connect(self.__on_combobox_changed)

        combobox_layout.addWidget(self.dropdown)
        combobox_layout.addStretch()
        main_layout.addLayout(combobox_layout)

        # Format Button
        self.format_button = QPushButton("Format")
        self.format_button.clicked.connect(self.__on_clicked)
        button_layout.addWidget(self.format_button)
        button_layout.addStretch()  # pushes button to the left

        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.__on_save_file_clicked)
        button_layout.addWidget(self.save_button)


        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def __on_clicked(self):
        input = io.BytesIO(self.text_edit.toPlainText().encode("utf-8"))
        output = format_bytes(self.lines_per_paragraph, input)
        self.text_edit.setPlainText(output.decode("utf-8"))

    def __on_combobox_changed(self, text):
        self.lines_per_paragraph = int(text)

    def __on_save_file_clicked(self):
        # Open file dialog to save the formatted text
        file_path, _ = QFileDialog.getSaveFileUrl(self, "Save", filter="Text Files (*.txt);;All Files (*)")
        if file_path.isValid():
            with open(file_path.toLocalFile(), 'w') as file:
                file.write(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextFormatter()
    window.text_edit.copy()
    window.show()
    sys.exit(app.exec_())