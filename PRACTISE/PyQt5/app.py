import json
import os
from datetime import datetime
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            raw_tasks = json.load(file)
    except Exception:
        return []

    cleaned = []
    for task in raw_tasks:
        if not isinstance(task, dict):
            continue
        cleaned.append(
            {
                "title": str(task.get("title", "Untitled Task")).strip() or "Untitled Task",
                "deadline": str(task.get("deadline", "")).strip(),
                "priority": task.get("priority", "Medium")
                if task.get("priority", "Medium") in ["Low", "Medium", "High"]
                else "Medium",
                "status": task.get("status", "Pending")
                if task.get("status", "Pending") in ["Pending", "Done"]
                else "Pending",
            }
        )
    return cleaned


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def parse_deadline(deadline_text):
    formats = ["%Y-%m-%d", "%d %B %Y", "%d %b %Y"]
    for fmt in formats:
        try:
            return datetime.strptime(deadline_text.strip(), fmt).date()
        except ValueError:
            continue
    return None


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GoalSync")
        self.resize(980, 650)
        self.setMinimumSize(860, 580)

        self.tasks = load_tasks()
        self.visible_task_indices = []

        self.create_ui()
        self.refresh_table()

    def create_ui(self):
        central = QWidget(self)
        self.setCentralWidget(central)

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(18, 14, 18, 14)
        root_layout.setSpacing(8)

        header = QFrame()
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(12, 10, 12, 10)
        header_layout.setSpacing(2)

        title = QLabel("GoalSync")
        title.setStyleSheet("font-size: 22px; font-weight: 700;")
        subtitle = QLabel("Minimal task planner")
        subtitle.setStyleSheet("font-size: 12px; color: #6b7280;")
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        root_layout.addWidget(header)

        input_frame = QFrame()
        input_layout = QGridLayout(input_frame)
        input_layout.setContentsMargins(8, 8, 8, 8)
        input_layout.setHorizontalSpacing(8)
        input_layout.setVerticalSpacing(8)

        self.title_entry = QLineEdit()
        self.title_entry.setPlaceholderText("Task title")
        input_layout.addWidget(self.title_entry, 0, 0)

        self.deadline_entry = QLineEdit()
        self.deadline_entry.setPlaceholderText("Deadline (YYYY-MM-DD)")
        self.deadline_entry.returnPressed.connect(self.add_task)
        input_layout.addWidget(self.deadline_entry, 0, 1)

        self.priority_box = QComboBox()
        self.priority_box.addItems(["Low", "Medium", "High"])
        self.priority_box.setCurrentText("Medium")
        input_layout.addWidget(self.priority_box, 0, 2)

        add_btn = QPushButton("Add")
        add_btn.clicked.connect(self.add_task)
        input_layout.addWidget(add_btn, 0, 3)

        for col in range(4):
            input_layout.setColumnStretch(col, 1)

        root_layout.addWidget(input_frame)

        toolbar = QFrame()
        toolbar_layout = QGridLayout(toolbar)
        toolbar_layout.setContentsMargins(8, 8, 8, 8)
        toolbar_layout.setHorizontalSpacing(8)

        done_btn = QPushButton("Mark Done")
        done_btn.clicked.connect(self.mark_done)
        toolbar_layout.addWidget(done_btn, 0, 0)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.delete_task)
        toolbar_layout.addWidget(delete_btn, 0, 1)

        for col in range(2):
            toolbar_layout.setColumnStretch(col, 1)

        root_layout.addWidget(toolbar)

        self.task_table = QTableWidget(0, 5)
        self.task_table.setHorizontalHeaderLabels(["#", "Status", "Task", "Deadline", "Priority"])
        self.task_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.task_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.task_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.task_table.verticalHeader().setVisible(False)
        self.task_table.setAlternatingRowColors(True)
        self.task_table.setShowGrid(False)
        self.task_table.setSortingEnabled(False)
        self.task_table.itemSelectionChanged.connect(self.on_row_select)

        header_view = self.task_table.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.Fixed)
        header_view.setSectionResizeMode(1, QHeaderView.Fixed)
        header_view.setSectionResizeMode(2, QHeaderView.Stretch)
        header_view.setSectionResizeMode(3, QHeaderView.Fixed)
        header_view.setSectionResizeMode(4, QHeaderView.Fixed)
        header_view.setStretchLastSection(False)
        self.task_table.setColumnWidth(0, 50)
        self.task_table.setColumnWidth(1, 100)
        self.task_table.setColumnWidth(3, 140)
        self.task_table.setColumnWidth(4, 120)

        root_layout.addWidget(self.task_table, 1)

        self.stats_label = QLabel("")
        self.stats_label.setStyleSheet("font-size: 12px; color: #6b7280;")
        root_layout.addWidget(self.stats_label)

        self.setStyleSheet(
            """
            QMainWindow { background: #ffffff; color: #111827; }
            QFrame { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 8px; }
            QLineEdit, QComboBox { background: #ffffff; border: 1px solid #d1d5db; border-radius: 6px; padding: 6px; color: #111827; }
            QLineEdit:focus, QComboBox:focus { border: 1px solid #3b82f6; }
            QPushButton { background: #111827; border: none; border-radius: 6px; padding: 7px 10px; color: #ffffff; font-weight: 600; }
            QPushButton:hover { background: #1f2937; }
            QPushButton:pressed { background: #030712; }
            QTableWidget { background: #ffffff; alternate-background-color: #f9fafb; border: 1px solid #e5e7eb; color: #111827; }
            QTableWidget::item:selected { background: #e5e7eb; color: #111827; }
            QHeaderView::section { background: #f3f4f6; color: #111827; border: 1px solid #e5e7eb; padding: 6px; }
            """
        )

    def refresh_table(self):
        self.task_table.setRowCount(0)
        self.visible_task_indices = list(range(len(self.tasks) - 1, -1, -1))

        for display_no, task_index in enumerate(self.visible_task_indices, start=1):
            task = self.tasks[task_index]
            status = task["status"]

            row = self.task_table.rowCount()
            self.task_table.insertRow(row)

            values = [
                str(display_no),
                status,
                task["title"],
                task["deadline"],
                task["priority"],
            ]

            if status == "Done":
                color = QColor("#15803d")
            elif self.is_overdue(task):
                color = QColor("#dc2626")
            else:
                color = QColor("#a16207")

            for col, value in enumerate(values):
                item = QTableWidgetItem(value)
                if col in (0, 1, 3, 4):
                    item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(color)
                self.task_table.setItem(row, col, item)

        self.update_stats()

    def on_row_select(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            return

        task = self.tasks[task_index]
        self.title_entry.setText(task["title"])
        self.deadline_entry.setText(task["deadline"])
        self.priority_box.setCurrentText(task["priority"])

    def get_selected_task_index(self):
        selected_items = self.task_table.selectedItems()
        if not selected_items:
            return None

        row = selected_items[0].row()
        if row < 0 or row >= len(self.visible_task_indices):
            return None
        return self.visible_task_indices[row]

    def show_warning(self, title, message):
        QMessageBox.warning(self, title, message)

    def add_task(self):
        title = self.title_entry.text().strip()
        raw_deadline = self.deadline_entry.text().strip()
        priority = self.priority_box.currentText()

        if not title:
            self.show_warning("Missing Title", "Please enter a task title.")
            return

        parsed = parse_deadline(raw_deadline)
        if parsed is None:
            self.show_warning("Invalid Deadline", "Use YYYY-MM-DD (example: 2026-10-20).")
            return

        self.tasks.append(
            {
                "title": title,
                "deadline": parsed.strftime("%Y-%m-%d"),
                "priority": priority,
                "status": "Pending",
            }
        )
        save_tasks(self.tasks)
        self.refresh_table()
        self.clear_fields()

    def mark_done(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            self.show_warning("Select Task", "Select a row in the table first.")
            return

        self.tasks[task_index]["status"] = "Done"
        save_tasks(self.tasks)
        self.refresh_table()

    def delete_task(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            self.show_warning("Select Task", "Select a row in the table first.")
            return

        self.tasks.pop(task_index)
        save_tasks(self.tasks)
        self.refresh_table()
        self.clear_fields()

    def is_overdue(self, task):
        if task.get("status") == "Done":
            return False
        parsed = parse_deadline(task.get("deadline", ""))
        if parsed is None:
            return False
        return parsed < datetime.today().date()

    def update_stats(self):
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task["status"] == "Done")
        pending = total - done
        overdue = sum(1 for task in self.tasks if self.is_overdue(task))
        self.stats_label.setText(
            f"Total: {total}   Pending: {pending}   Done: {done}   Overdue: {overdue}"
        )

    def clear_fields(self):
        self.title_entry.clear()
        self.deadline_entry.clear()
        self.priority_box.setCurrentText("Medium")


if __name__ == "__main__":
    qt_app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(qt_app.exec_())