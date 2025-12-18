from flask import Blueprint, render_template, request, jsonify, current_app
from models import db, Category

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/manage_categories')
def manage_categories():
    """Manage categories - Hình 3"""
    with current_app.app_context():
        categories = Category.query.all()
    return render_template('manage_categories.html', categories=categories)

@categories_bp.route('/add_category', methods=['POST'])
def add_category():
    """Add new category"""
    name = request.form.get('name')
    
    if name:
        with current_app.app_context():
            category = Category(name=name, is_active=True)
            db.session.add(category)
            db.session.commit()
            return jsonify({'success': True, 'id': category.id, 'name': category.name})
    
    return jsonify({'success': False, 'error': 'Name is required'}), 400

@categories_bp.route('/toggle_category/<int:category_id>', methods=['POST'])
def toggle_category(category_id):
    """Toggle category active state"""
    with current_app.app_context():
        category = Category.query.get_or_404(category_id)
        category.is_active = not category.is_active
        db.session.commit()
        
        return jsonify({
            'success': True, 
            'is_active': category.is_active
        })

@categories_bp.route('/delete_category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    """Delete category (soft delete)"""
    with current_app.app_context():
        category = Category.query.get_or_404(category_id)
        category.is_active = False
        db.session.commit()
        
        return jsonify({'success': True})