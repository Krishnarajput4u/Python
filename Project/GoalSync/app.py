from flask import Flask, render_template, request, redirect, session
from datetime import date
from db import get_db
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from urllib.parse import quote

# Use non-interactive backend for matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
app.secret_key = "secretkey"

# Home → Login page
@app.route('/')
def home():
    return render_template('login.html')

# Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Handle Signup
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
        (username, password, role)
    )
    db.commit()

    return redirect('/')

# Handle Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()

    if user:
        session['user_id'] = user[0]
        session['role'] = user[3]

        if user[3] == 'professor':
            return redirect('/professor')
        else:
            return redirect('/student')

    return "Invalid Credentials"

# Generate completion graph
def generate_completion_graph(user_id):
    """Generate a completion rate graph based on task history"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    # Get progress history
    cursor.execute(
        "SELECT status, COUNT(*) as count FROM progress WHERE user_id=%s GROUP BY status",
        (user_id,)
    )
    progress_summary = cursor.fetchall()
    
    # Get total tasks added
    cursor.execute("SELECT COUNT(*) as total FROM tasks WHERE user_id=%s", (user_id,))
    task_count = cursor.fetchone()['total']
    
    # Calculate completion rate
    completed = sum(p['count'] for p in progress_summary if p['status'] == 'completed')
    total_attempts = sum(p['count'] for p in progress_summary)
    
    if total_attempts == 0:
        completion_rate = 0
    else:
        completion_rate = (completed / total_attempts) * 100
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor('#f5f5f5')
    
    # Pie chart - Completion Status
    statuses = [p['status'].capitalize() for p in progress_summary]
    counts = [p['count'] for p in progress_summary]
    colors = ['#27ae60', '#e74c3c']
    
    if statuses:
        ax1.pie(counts, labels=statuses, autopct='%1.1f%%', colors=colors[:len(statuses)], startangle=90)
        ax1.set_title('Task Completion Status', fontsize=14, fontweight='bold', pad=20)
    else:
        ax1.text(0.5, 0.5, 'No Data Yet', ha='center', va='center', fontsize=12)
        ax1.set_title('Task Completion Status', fontsize=14, fontweight='bold')
        ax1.axis('off')
    
    # Bar chart - Motivation Metrics
    metrics = ['Tasks\nAdded', 'Completed', 'Completion\nRate (%)']
    values = [task_count, completed, completion_rate]
    bar_colors = ['#3498db', '#27ae60', '#f39c12']
    
    bars = ax2.bar(metrics, values, color=bar_colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Count / Percentage', fontsize=11, fontweight='bold')
    ax2.set_title('Motivation Dashboard', fontsize=14, fontweight='bold', pad=20)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(value) if value != completion_rate else f"{value:.1f}%"}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    
    # Convert to base64 for embedding in HTML
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100, bbox_inches='tight')
    img.seek(0)
    plt.close()
    
    img_base64 = base64.b64encode(img.getvalue()).decode()
    return img_base64

# Student Dashboard
@app.route('/student')
def student_dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Get tasks
    cursor.execute("SELECT * FROM tasks WHERE user_id=%s", (user_id,))
    tasks = cursor.fetchall()

    # Get progress
    cursor.execute("SELECT * FROM progress WHERE user_id=%s", (user_id,))
    progress_data = cursor.fetchall()

    completed = sum(1 for p in progress_data if p['status'] == 'completed')
    total = len(progress_data)
    pending = total - completed
    
    # Generate completion graph
    graph_image = generate_completion_graph(user_id)

    return render_template(
        'dashboard.html',
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        today=date.today(),
        graph_image=graph_image
    )

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    deadline = request.form['deadline']
    priority = request.form['priority']

    user_id = session['user_id']

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, deadline, priority, user_id, type) VALUES (%s, %s, %s, %s, 'personal')",
        (title, deadline, priority, user_id)
    )
    db.commit()

    return redirect('/student')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT title FROM tasks WHERE id=%s AND user_id=%s",
        (task_id, user_id)
    )
    task = cursor.fetchone()

    if not task:
        return redirect('/student')

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s AND user_id=%s",
        (task_id, user_id)
    )
    db.commit()

    # Try recording completion for stats if a compatible progress table exists.
    try:
        progress_cursor = db.cursor()
        progress_cursor.execute(
            "INSERT INTO progress (user_id, status) VALUES (%s, %s)",
            (user_id, 'completed')
        )
        db.commit()
    except Exception:
        db.rollback()

    return redirect('/student')

# Professor Dashboard
@app.route('/professor')
def professor_dashboard():
    return "Professor Dashboard"

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)