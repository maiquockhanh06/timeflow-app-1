// Common JavaScript functions

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
}

// Show loading spinner
function showLoading() {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    spinner.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(spinner);
}

function hideLoading() {
    const spinner = document.querySelector('.loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

// Handle form submission with loading
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form[data-loading="true"]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            showLoading();
        });
    });
});

// Confirm before deletion
function confirmAction(message) {
    return confirm(message || 'Bạn có chắc chắn muốn thực hiện hành động này?');
}

// Show toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    // Trigger animation
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    // Remove after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 3000);
}

// Filter tasks by category
function filterTasks(categoryId) {
    const rows = document.querySelectorAll('.tasks-table tbody tr');
    
    rows.forEach(row => {
        if (categoryId === 'all') {
            row.style.display = '';
        } else {
            const rowCategory = row.querySelector('.category-label').textContent;
            // You'll need to implement category filtering logic
            row.style.display = 'none'; // Placeholder
        }
    });
}

// Initialize tooltips
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.dataset.tooltip;
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + 'px';
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
            
            this._tooltip = tooltip;
        });
        
        element.addEventListener('mouseleave', function() {
            if (this._tooltip) {
                this._tooltip.remove();
            }
        });
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initTooltips();
    
    // Initialize date pickers
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        if (!input.value) {
            const today = new Date().toISOString().split('T')[0];
            input.value = today;
        }
    });
    
    // Initialize time pickers
    const timeInputs = document.querySelectorAll('input[type="time"]');
    timeInputs.forEach(input => {
        if (!input.value) {
            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            input.value = `${hours}:${minutes}`;
        }
    });
});

// Add CSS for dynamic elements
const style = document.createElement('style');
style.textContent = `
    .loading-spinner {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }
    
    .spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-top: 5px solid #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .toast {
        position: fixed;
        bottom: 20px;
        right: 20px;
        padding: 15px 25px;
        border-radius: 5px;
        color: white;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .toast.show {
        opacity: 1;
        transform: translateY(0);
    }
    
    .toast-info {
        background: #3498db;
    }
    
    .toast-success {
        background: #2ecc71;
    }
    
    .toast-error {
        background: #e74c3c;
    }
    
    .tooltip {
        position: absolute;
        background: #333;
        color: white;
        padding: 5px 10px;
        border-radius: 3px;
        font-size: 0.9rem;
        z-index: 1000;
        pointer-events: none;
    }
`;
document.head.appendChild(style);