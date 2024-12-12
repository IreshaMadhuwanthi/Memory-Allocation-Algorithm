from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QTextEdit, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sys

# Initial memory blocks
memory_blocks = {
    50: 10,  # 10 blocks of 50KB
    100: 10,  # 10 blocks of 100KB
    200: 10,  # 10 blocks of 200KB
    500: 10,  # 10 blocks of 500KB
}

allocated_memory = {}  # To track allocated memory blocks

class MemoryAllocationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quick Fit Memory Allocation Simulator")
        self.setGeometry(350, 50, 700, 660)

        # Set window icon
        self.setWindowIcon(QIcon("E:\\PRACTICE\\Memory-Allocation-Algorithm(MP)\\Memory-Allocation-Algorithm\\QuickFitAlgorithm\\QF.ico"))

        # Main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Layout
        self.main_layout = QVBoxLayout(self.main_widget)

        # Title label
        self.title_label = QLabel("Enter the Process size:")
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Input field container layout
        self.input_layout = QHBoxLayout()
        self.input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Input field with right-aligned text and static KB suffix
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 14))
        self.input_field.setAlignment(Qt.AlignRight)
        self.input_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                border-radius: 10px;
                padding: 10px;
                max-width: 1000px;
                margin-right: 10px; /* Allow space for KB label */
            }
        """)
        self.input_field.textChanged.connect(self.update_input_text)

        # Add "KB" label to the right of the input field
        self.kb_label = QLabel("KB")
        self.kb_label.setFont(QFont("Arial", 14))
        self.kb_label.setStyleSheet("color: darkgrey;")

        self.input_container = QHBoxLayout()
        self.input_container.addWidget(self.input_field)
        self.input_container.addWidget(self.kb_label)

        self.input_layout.addLayout(self.input_container)
        self.input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.main_layout.addLayout(self.input_layout)

        # Buttons layout
        self.button_layout = QHBoxLayout()

        # Allocate Button
        self.allocate_button = QPushButton("Allocate")
        self.allocate_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 16px;
                padding: 3px 8px;
                border-radius: 10px;
                max-width: 350px;
                height: 40px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.allocate_button.clicked.connect(self.allocate_memory)
        self.button_layout.addWidget(self.allocate_button)

        # Show Lists Button
        self.show_lists_button = QPushButton("Show Lists")
        self.show_lists_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                font-size: 16px;
                padding: 3px 8px;
                border-radius: 10px;
                max-width: 350px;
                height: 40px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.show_lists_button.clicked.connect(self.show_free_lists)
        self.button_layout.addWidget(self.show_lists_button)

        # Deallocate Button
        self.deallocate_button = QPushButton("Deallocate")
        self.deallocate_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                font-size: 16px;
                padding: 3px 8px;
                border-radius: 10px;
                max-width: 350px;
                height: 40px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.deallocate_button.clicked.connect(self.deallocate_memory)
        self.button_layout.addWidget(self.deallocate_button)

        self.main_layout.addLayout(self.button_layout)

        # Output box layout
        self.output_layout = QHBoxLayout()
        self.output_box = QTextEdit()
        self.output_box.setFont(QFont("Courier", 12))
        self.output_box.setStyleSheet("""
            QTextEdit {
                background-color: #084F6A;
                color: white;
                border-radius: 10px;
                padding: 10px;
                max-width: 1200px;
            }
        """)
        self.output_box.setReadOnly(True)
        self.output_layout.addWidget(self.output_box)
        self.main_layout.addLayout(self.output_layout)

        self.show_free_lists()

    def update_input_text(self):
        """Ensure the input value displays properly aligned with the KB suffix."""
        self.input_field.setAlignment(Qt.AlignRight)

    # Allocate memory
    def allocate_memory(self):
        try:
            process_size = int(self.input_field.text())
            if process_size <= 0:
                raise ValueError

            best_fit_key = None
            for block_size in memory_blocks:
                if block_size >= process_size and memory_blocks[block_size] > 0:
                    if best_fit_key is None or block_size < best_fit_key:
                        best_fit_key = block_size

            if best_fit_key is not None:
                memory_blocks[best_fit_key] -= 1
                allocated_memory[process_size] = allocated_memory.get(process_size, 0) + 1

                leftover = best_fit_key - process_size
                if leftover > 0:
                    memory_blocks[leftover] = memory_blocks.get(leftover, 0) + 1

                allocation_details = f"-------------------------------\n\nAllocated {process_size}KB from {best_fit_key}KB list.\n"
                if leftover > 0:
                    allocation_details += f"Created a {leftover}KB leftover block.\n"
            else:
                allocation_details = "Error: Not enough memory available for allocation.\n"

            self.show_free_lists()
            self.output_box.append(allocation_details)
        except ValueError:
            self.output_box.setText("Invalid Input: Please enter a valid process size.")

    # Deallocate Memory
    def deallocate_memory(self):
        try:
            process_size = int(self.input_field.text())
            if process_size <= 0:
                raise ValueError

            if process_size in allocated_memory and allocated_memory[process_size] > 0:
                allocated_memory[process_size] -= 1
                memory_blocks[process_size] = memory_blocks.get(process_size, 0) + 1
                deallocation_details = f"---------------------------\n\nDeallocated {process_size}KB and returned it to the free list.\n"
            else:
                deallocation_details = "---------------------------\n\nNo allocated memory to deallocate. All memory is free.\n"

            self.show_free_lists()
            self.output_box.append(deallocation_details)
        except ValueError:
            self.output_box.setText("Invalid Input: Please enter a valid process size.")

    # Show List
    def show_free_lists(self):
        free_lists = "________Free Lists________\n\n"
        for size, count in memory_blocks.items():
            free_lists += f"{size}KB List: {count} Blocks\n"

        allocated = "\n---------------------------\n\n"
        for size, count in allocated_memory.items():
            allocated += f"{size}KB Allocated: {count} Blocks\n"

        self.output_box.setText(free_lists + allocated)

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryAllocationApp()
    window.show()
    sys.exit(app.exec_())