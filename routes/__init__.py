# Để tránh circular imports, chúng ta sẽ export từng cái một
# File này để đánh dấu thư mục routes là package

from .tasks import tasks_bp
from .categories import categories_bp
from .tracking import tracking_bp

__all__ = ['tasks_bp', 'categories_bp', 'tracking_bp']