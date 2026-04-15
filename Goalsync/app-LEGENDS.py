import json
import os
from datetime import datetime
from tkinter import messagebox, ttk

import customtkinter as ctk

FILE_NAME = "tasks.json"

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


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


class TaskManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GoalSync")
        self.geometry("980x650")
        self.minsize(860, 580)

        self.tasks = load_tasks()
        self.visible_task_indices = []

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.create_ui()
        self.refresh_table()

    def create_ui(self):
        header = ctk.CTkFrame(self, corner_radius=12)
        header.grid(row=0, column=0, padx=20, pady=(16, 10), sticky="ew")

        ctk.CTkLabel(
            header,
            text="GoalSync",
            font=("Segoe UI", 30, "bold"),
        ).grid(row=0, column=0, padx=16, pady=(10, 0), sticky="w")

        ctk.CTkLabel(
            header,
            text="Minimal task planner for student workflow",
            font=("Segoe UI", 14),
            text_color=("gray25", "gray75"),
        ).grid(row=1, column=0, padx=16, pady=(0, 12), sticky="w")

        input_frame = ctk.CTkFrame(self)
        input_frame.grid(row=1, column=0, padx=20, pady=8, sticky="ew")
        input_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.title_entry = ctk.CTkEntry(input_frame, placeholder_text="Task title")
        self.title_entry.grid(row=0, column=0, padx=8, pady=10, sticky="ew")

        self.deadline_entry = ctk.CTkEntry(input_frame, placeholder_text="Deadline (YYYY-MM-DD)")
        self.deadline_entry.grid(row=0, column=1, padx=8, pady=10, sticky="ew")

        self.priority_box = ctk.CTkOptionMenu(input_frame, values=["Low", "Medium", "High"])
        self.priority_box.set("Medium")
        self.priority_box.grid(row=0, column=2, padx=8, pady=10, sticky="ew")

        ctk.CTkButton(input_frame, text="Add", command=self.add_task).grid(
            row=0, column=3, padx=8, pady=10, sticky="ew"
        )
        ctk.CTkButton(input_frame, text="Update", command=self.update_task).grid(
            row=0, column=4, padx=8, pady=10, sticky="ew"
        )

        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=2, column=0, padx=20, pady=8, sticky="ew")
        toolbar.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.search_entry = ctk.CTkEntry(toolbar, placeholder_text="Search title")
        self.search_entry.grid(row=0, column=0, padx=8, pady=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", lambda _event: self.refresh_table())

        self.filter_box = ctk.CTkOptionMenu(
            toolbar,
            values=["All", "Pending", "Done", "Overdue"],
            command=lambda _value: self.refresh_table(),
        )
        self.filter_box.set("All")
        self.filter_box.grid(row=0, column=1, padx=8, pady=10, sticky="ew")

        ctk.CTkButton(toolbar, text="Mark Done", command=self.mark_done).grid(
            row=0, column=2, padx=8, pady=10, sticky="ew"
        )
        ctk.CTkButton(toolbar, text="Delete", command=self.delete_task).grid(
            row=0, column=3, padx=8, pady=10, sticky="ew"
        )
        ctk.CTkButton(toolbar, text="Clear Done", command=self.clear_completed).grid(
            row=0, column=4, padx=8, pady=10, sticky="ew"
        )

        table_wrap = ctk.CTkFrame(self)
        table_wrap.grid(row=3, column=0, padx=20, pady=(8, 10), sticky="nsew")
        table_wrap.grid_rowconfigure(0, weight=1)
        table_wrap.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 11),
            background="#1e2633",
            foreground="#e5e7eb",
            fieldbackground="#1e2633",
            bordercolor="#2a3441",
            borderwidth=1,
        )
        style.map(
            "Treeview",
            background=[("selected", "#2b3f5c")],
            foreground=[("selected", "#ffffff")],
        )
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 11, "bold"),
            background="#273447",
            foreground="#f3f4f6",
            bordercolor="#2a3441",
            relief="flat",
        )
        style.map("Treeview.Heading", background=[("active", "#2f425a")])

        self.task_table = ttk.Treeview(
            table_wrap,
            columns=("no", "status", "title", "deadline", "priority"),
            show="headings",
            selectmode="browse",
        )
        self.task_table.heading("no", text="#")
        self.task_table.heading("status", text="Status")
        self.task_table.heading("title", text="Task")
        self.task_table.heading("deadline", text="Deadline")
        self.task_table.heading("priority", text="Priority")

        self.task_table.column("no", width=50, anchor="center", stretch=False)
        self.task_table.column("status", width=110, anchor="center", stretch=False)
        self.task_table.column("title", width=420, anchor="w")
        self.task_table.column("deadline", width=160, anchor="center", stretch=False)
        self.task_table.column("priority", width=140, anchor="center", stretch=False)

        self.task_table.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        self.task_table.bind("<<TreeviewSelect>>", self.on_row_select)

        scrollbar = ttk.Scrollbar(table_wrap, orient="vertical", command=self.task_table.yview)
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10, padx=(0, 10))
        self.task_table.configure(yscrollcommand=scrollbar.set)

        self.task_table.tag_configure("done", foreground="#15803d")
        self.task_table.tag_configure("pending", foreground="#b45309")
        self.task_table.tag_configure("overdue", foreground="#dc2626")

        self.stats_label = ctk.CTkLabel(
            self,
            text="",
            font=("Consolas", 12),
            text_color=("gray25", "gray80"),
        )
        self.stats_label.grid(row=4, column=0, padx=24, pady=(0, 14), sticky="w")

    def refresh_table(self):
        for row_id in self.task_table.get_children():
            self.task_table.delete(row_id)

        self.visible_task_indices = self.filtered_task_indices()

        for display_no, task_index in enumerate(self.visible_task_indices, start=1):
            task = self.tasks[task_index]
            status = task["status"]
            tag = "pending"
            if status == "Done":
                tag = "done"
            elif self.is_overdue(task):
                tag = "overdue"

            self.task_table.insert(
                "",
                "end",
                iid=str(task_index),
                values=(display_no, status, task["title"], task["deadline"], task["priority"]),
                tags=(tag,),
            )

        self.update_stats()

    def filtered_task_indices(self):
        search_text = self.search_entry.get().strip().lower()
        selected_filter = self.filter_box.get()

        indices = []
        for idx, task in enumerate(self.tasks):
            if search_text and search_text not in task["title"].lower():
                continue
            if selected_filter == "Pending" and task["status"] != "Pending":
                continue
            if selected_filter == "Done" and task["status"] != "Done":
                continue
            if selected_filter == "Overdue" and not self.is_overdue(task):
                continue
            indices.append(idx)

        return sorted(indices, reverse=True)

    def on_row_select(self, _event):
        task_index = self.get_selected_task_index()
        if task_index is None:
            return

        task = self.tasks[task_index]
        self.title_entry.delete(0, "end")
        self.title_entry.insert(0, task["title"])
        self.deadline_entry.delete(0, "end")
        self.deadline_entry.insert(0, task["deadline"])
        self.priority_box.set(task["priority"])

    def get_selected_task_index(self):
        selected = self.task_table.selection()
        if not selected:
            return None
        try:
            return int(selected[0])
        except ValueError:
            return None

    def add_task(self):
        title = self.title_entry.get().strip()
        raw_deadline = self.deadline_entry.get().strip()
        priority = self.priority_box.get()

        if not title:
            messagebox.showwarning("Missing Title", "Please enter a task title.")
            return

        parsed = parse_deadline(raw_deadline)
        if parsed is None:
            messagebox.showwarning(
                "Invalid Deadline",
                "Use YYYY-MM-DD (example: 2026-10-20).",
            )
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

    def update_task(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            messagebox.showwarning("Select Task", "Select a row in the table first.")
            return

        title = self.title_entry.get().strip()
        raw_deadline = self.deadline_entry.get().strip()
        priority = self.priority_box.get()

        if not title:
            messagebox.showwarning("Missing Title", "Please enter a task title.")
            return

        parsed = parse_deadline(raw_deadline)
        if parsed is None:
            messagebox.showwarning("Invalid Deadline", "Use YYYY-MM-DD.")
            return

        self.tasks[task_index]["title"] = title
        self.tasks[task_index]["deadline"] = parsed.strftime("%Y-%m-%d")
        self.tasks[task_index]["priority"] = priority
        save_tasks(self.tasks)
        self.refresh_table()

    def mark_done(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            messagebox.showwarning("Select Task", "Select a row in the table first.")
            return

        self.tasks[task_index]["status"] = "Done"
        save_tasks(self.tasks)
        self.refresh_table()

    def delete_task(self):
        task_index = self.get_selected_task_index()
        if task_index is None:
            messagebox.showwarning("Select Task", "Select a row in the table first.")
            return

        self.tasks.pop(task_index)
        save_tasks(self.tasks)
        self.refresh_table()
        self.clear_fields()

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if task["status"] != "Done"]
        save_tasks(self.tasks)
        self.refresh_table()

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
        self.stats_label.configure(
            text=f"Total: {total}   Pending: {pending}   Done: {done}   Overdue: {overdue}"
        )

    def clear_fields(self):
        self.title_entry.delete(0, "end")
        self.deadline_entry.delete(0, "end")
        self.priority_box.set("Medium")


if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
