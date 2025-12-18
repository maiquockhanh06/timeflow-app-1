from flask import Flask, render_template
from models import db, Category, Task
from datetime import datetime
import os

app = Flask(__name__)

# Cấu hình database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Khởi tạo database
db.init_app(app)

# Khởi tạo database và tạo dữ liệu mẫu
def init_database():
    with app.app_context():
        db.create_all()
        
        # Kiểm tra nếu chưa có dữ liệu mẫu
        if Category.query.count() == 0:
            # Tạo các phân loại mặc định
            categories = [
                Category(name='Học tập', is_active=True),
                Category(name='Cá nhân', is_active=True),
                Category(name='Công việc', is_active=True)
            ]
            
            for cat in categories:
                db.session.add(cat)
            db.session.commit()
            
            print("Default categories created!")
        
        print("Database ready!")

# Gọi hàm khởi tạo
init_database()

@app.route('/')
def index():
    """Home page - Hình 1"""
    # Get today's tasks
    today = datetime.now().date()
    tasks_today = Task.query.filter(
        Task.due_date == today,
        Task.status != 'Hoàn thành'
    ).all()
    
    # Get not started tasks
    not_started = Task.query.filter_by(status='Chưa làm').all()
    
    return render_template('index.html', 
                         tasks_today=tasks_today,
                         not_started=not_started,
                         today=today)

@app.route('/init_db')
def init_db():
    """Initialize database with sample data"""
    with app.app_context():
        # Xóa tất cả dữ liệu cũ
        Task.query.delete()
        Category.query.delete()
        
        # Tạo các phân loại mặc định
        categories = [
            Category(name='Học tập', is_active=True),
            Category(name='Cá nhân', is_active=True),
            Category(name='Công việc', is_active=True)
        ]
        
        for cat in categories:
            db.session.add(cat)
        
        db.session.commit()
        
        # Tạo công việc mẫu
        from datetime import date, time
        
        tasks = [
            Task(
                name='Hoàn thành bài tập lập trình',
                description='Làm bài tập tuần 5',
                due_date=date(2025, 12, 20),
                category_id=1,
                status='Đang làm',
                created_at=datetime(2025, 12, 15)
            ),
            Task(
                name='Đọc sách chương 3',
                description='Đọc và ghi chú',
                due_date=date(2025, 12, 18),
                due_time=time(18, 0),
                category_id=1,
                status='Chưa làm',
                created_at=datetime(2025, 12, 16)
            ),
            Task(
                name='Tập thể dục',
                description='Chạy bộ 30 phút',
                due_date=date(2025, 12, 17),
                due_time=time(7, 0),
                category_id=2,
                status='Hoàn thành',
                created_at=datetime(2025, 12, 17)
            )
        ]
        
        for task in tasks:
            db.session.add(task)
        
        db.session.commit()
    
    return 'Database initialized with sample data!'

# Import và đăng ký routes SAU KHI tạo app
# Import và đăng ký routes SAU KHI tạo app
from routes import tasks_bp, categories_bp, tracking_bp

app.register_blueprint(tasks_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(tracking_bp)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)