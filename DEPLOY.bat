@echo off
REM Quick GitHub Deploy Script for RJMedia
REM This script pushes your archive to GitHub and enables GitHub Pages

echo.
echo ========================================
echo RJMedia Archive — Quick GitHub Deploy
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git not installed. Download from https://git-scm.com/
    pause
    exit /b 1
)

echo.
echo STEP 1: Enter your GitHub username
set /p USERNAME="Your GitHub username: "

echo.
echo STEP 2: Creating GitHub repo...
echo Go to https://github.com/new and create a repo named: rjmedia-liner-notes
echo Then come back here and press ENTER.
pause

echo.
echo STEP 3: Pushing code to GitHub...
cd C:\Dev\memoryos\rjmedia-liner-notes

git remote add origin https://github.com/%USERNAME%/rjmedia-liner-notes.git
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo ERROR: Failed to push. Check your username and repo name.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS!
echo ========================================
echo.
echo Your code is now on GitHub!
echo.
echo NEXT STEPS:
echo.
echo 1. Go to: https://github.com/%USERNAME%/rjmedia-liner-notes
echo 2. Click Settings (gear icon)
echo 3. Click Pages (left sidebar)
echo 4. Select "main" branch as source
echo 5. Click Save
echo.
echo Your site will be live at:
echo https://%USERNAME%.github.io/rjmedia-liner-notes/
echo.
echo Wait 1-2 minutes, then add that link to your Smiths video pinned comment!
echo.
pause
