#!/bin/bash

# Ecommerce MongoDB Django Project Setup Script

echo "🚀 Setting up Ecommerce MongoDB Django Project..."

# Check Python version
echo "📋 Checking Python version..."
python3 --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check MongoDB
echo "🔍 Checking MongoDB..."
if ! command -v mongod &> /dev/null; then
    echo "⚠️  MongoDB not found. Please install MongoDB:"
    echo "   macOS: brew install mongodb-community"
    echo "   Or use Docker: docker run -d -p 27017:27017 --name mongodb mongo:latest"
    echo ""
    echo "After installing MongoDB, make sure it's running before continuing."
    read -p "Press Enter to continue after MongoDB is installed and running..."
fi

# Run migrations
echo "🗄️  Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the development server:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Make sure MongoDB is running"
echo "  3. Run: python manage.py runserver"
echo ""
echo "Optional: Create superuser with: python manage.py createsuperuser"

