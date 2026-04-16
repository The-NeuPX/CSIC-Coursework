#!/usr/bin/env python3
"""
TOEBEANS Backend - Complete Setup Guide
Run this script or follow manual steps below
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a shell command and report status"""
    print(f"\n▶ {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ Success")
            return True
        else:
            print(f"  ✗ Failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("TOEBEANS Django Backend - Setup Script")
    print("=" * 60)
    
    # Step 1: Virtual Environment
    if not os.path.exists("venv"):
        if not run_command("python3 -m venv venv", "Creating virtual environment"):
            return False
    else:
        print("\n✓ Virtual environment already exists")
    
    # Step 2: Install dependencies
    pip_cmd = "./venv/bin/pip" if os.name != 'nt' else ".\\venv\\Scripts\\pip"
    if not run_command(f"{pip_cmd} install -q -r requirements.txt", "Installing dependencies"):
        return False
    
    # Step 3: Run migrations
    python_cmd = "./venv/bin/python" if os.name != 'nt' else ".\\venv\\Scripts\\python"
    if not run_command(f"{python_cmd} manage.py migrate", "Running database migrations"):
        return False
    
    # Step 4: Collect static files
    if not run_command(f"{python_cmd} manage.py collectstatic --noinput", "Collecting static files"):
        return False
    
    # Step 5: Create superuser (interactive)
    print("\n▶ Creating superuser account...")
    print("  You'll be prompted to enter admin credentials")
    os.system(f"{python_cmd} manage.py createsuperuser")
    
    # Step 6: Load sample data (optional)
    print("\n▶ Load sample data? (Optional - for testing)")
    choice = input("  Enter 'yes' to load sample data: ")
    if choice.lower() == 'yes':
        run_command(f"{python_cmd} manage.py init_data", "Loading sample data")
    
    print("\n" + "=" * 60)
    print("✓ Setup Complete!")
    print("=" * 60)
    print("\n🚀 To start the server:")
    if os.name == 'nt':
        print("   .\\venv\\Scripts\\activate")
        print("   python manage.py runserver")
    else:
        print("   source venv/bin/activate")
        print("   python manage.py runserver")
    print("\n🌐 Then visit:")
    print("   Website: http://localhost:8000")
    print("   Admin: http://localhost:8000/admin/")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
