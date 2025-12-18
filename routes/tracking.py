from flask import Blueprint, render_template, jsonify, current_app
from models import db, Task, Category

tracking_bp = Blueprint('tracking', __name__)

@tracking_bp.route('/tracking')
def tracking():
    """Task tracking page - Hình 4"""
    with current_app.app_context():
        tasks = Task.query.order_by(Task.due_date.desc()).all()
        
        # Count tasks by status
        not_started_count = Task.query.filter_by(status='Chưa làm').count()
        in_progress_count = Task.query.filter_by(status='Đang làm').count()
        completed_count = Task.query.filter_by(status='Hoàn thành').count()
        
        return render_template('tracking.html', 
                             tasks=tasks,
                             not_started_count=not_started_count,
                             in_progress_count=in_progress_count,
                             completed_count=completed_count)

@tracking_bp.route('/get_tasks_by_category/<int:category_id>')
def get_tasks_by_category(category_id):
    """Get tasks by category"""
    with current_app.app_context():
        tasks = Task.query.filter_by(category_id=category_id).all()
        
        tasks_data = []
        for task in tasks:
            tasks_data.append({
                'id': task.id,
                'name': task.name,
                'description': task.description,
                'due_date': task.due_date.strftime('%d/%m/%Y') if task.due_date else '',
                'due_time': task.due_time.strftime('%H:%M') if task.due_time else '',
                'status': task.status,
                'created_at': task.created_at.strftime('%d/%m/%Y') if task.created_at else ''
            })
        
        return jsonify(tasks_data)