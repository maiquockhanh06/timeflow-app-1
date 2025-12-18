@echo off
echo ====================================
echo   FIX ALL DEPLOYMENT FILES
echo ====================================
echo.

echo 1. Fixing requirements.txt...
echo Flask==3.1.2 > requirements.txt
echo Flask-SQLAlchemy==3.1.1 >> requirements.txt
echo gunicorn==21.2.0 >> requirements.txt

echo 2. Fixing runtime.txt...
echo python-3.9.0 > runtime.txt

echo 3. Fixing Procfile...
echo web: gunicorn app:app > Procfile

echo 4. Checking files...
echo.
echo --- requirements.txt ---
type requirements.txt
echo.
echo --- runtime.txt ---
type runtime.txt
echo.
echo --- Procfile ---
type Procfile
echo.

echo 5. Pushing to GitHub...
git add .
git commit -m "Fix all deployment files"
git push

echo.
echo ====================================
echo   ALL FILES FIXED!
echo   Wait for Render to redeploy...
echo ====================================
pause