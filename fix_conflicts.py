import os

print("=" * 60)
print("FIXING GIT MERGE CONFLICTS")
print("=" * 60)

files_to_fix = {
    'requirements.txt': """Flask==3.1.2
Flask-SQLAlchemy==3.1.1
gunicorn==21.2.0""",
    
    'runtime.txt': 'python-3.9.0',
    
    'Procfile': 'web: gunicorn app:app'
}

for filename, content in files_to_fix.items():
    print(f"\n📝 Fixing {filename}...")
    
    # Đọc nội dung hiện tại
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            current = f.read()
        
        # Kiểm tra có conflict markers không
        if '<<<<<<<' in current or '=======' in current or '>>>>>>>' in current:
            print(f"  ❌ Found conflict markers in {filename}")
            
            # Ghi đè với nội dung đúng
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Fixed {filename}")
        else:
            print(f"  ✅ {filename} looks good")
            
    except FileNotFoundError:
        print(f"  ⚠️  {filename} not found, creating...")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("\n" + "=" * 60)
print("FILES AFTER FIXING:")
print("=" * 60)

for filename in files_to_fix.keys():
    print(f"\n--- {filename} ---")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except:
        print("File not found")

# Git operations
print("\n" + "=" * 60)
print("PUSHING TO GITHUB...")
print("=" * 60)

import subprocess

commands = [
    ['git', 'add', '.'],
    ['git', 'commit', '-m', 'Fix all merge conflicts'],
    ['git', 'push', 'origin', 'main']
]

for cmd in commands:
    print(f"\nRunning: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success")
        else:
            print(f"❌ Failed: {result.stderr[:100]}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n" + "=" * 60)
print("✅ DONE!")
print("Render will auto-redeploy in 2-3 minutes")
print("Check: https://timeflow-app.onrender.com")
print("=" * 60)