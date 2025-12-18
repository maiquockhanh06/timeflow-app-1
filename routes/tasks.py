from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from models import db, Task, Category
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/create_task', methods=['GET', 'POST'])
def create_task():
    """Create new task - Hình 2"""
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description', '')
        due_date_str = request.form.get('due_date')
        due_time_str = request.form.get('due_time')
        category_id = request.form.get('category_id')
        
        # Parse date and time
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
            due_time = datetime.strptime(due_time_str, '%H:%M').time() if due_time_str else None
        except ValueError:
            return "Invalid date or time format", 400
        
        if name and due_date and category_id:
            with current_app.app_context():
                task = Task(
                    name=name,
                    description=description,
                    due_date=due_date,
                    due_time=due_time,
                    category_id=int(category_id),
                    status='Chưa làm'
                )
                db.session.add(task)
                db.session.commit()
            return redirect(url_for('index'))
    
    # GET request - show form
    with current_app.app_context():
        categories = Category.query.filter_by(is_active=True).all()
    return render_template('create_task.html', categories=categories)

@tasks_bp.route('/update_task_status/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    """Update task status"""
    with current_app.app_context():
        task = Task.query.get_or_404(task_id)
        new_status = request.form.get('status')
        
        if new_status in ['Chưa làm', 'Đang làm', 'Hoàn thành']:
            task.status = new_status
            db.session.commit()
            return jsonify({'success': True, 'status': new_status})
        
        return jsonify({'success': False, 'error': 'Invalid status'}), 400

@tasks_bp.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task"""
    with current_app.app_context():
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'success': True})