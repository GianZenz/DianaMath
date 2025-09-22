# 🎯 Diana's Math Adventure

A beautiful, gamified math learning web application designed specifically for 7-year-old Diana, following the Northern Ireland Primary 3 curriculum.

![Diana's Math Adventure](https://img.shields.io/badge/Grade-Primary%203-brightgreen) ![Status](https://img.shields.io/badge/Status-Production%20Ready-success) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Flask](https://img.shields.io/badge/Flask-3.0+-lightgrey)

## ✨ Features

### 🎨 **Beautiful Interface**
- **Child-friendly design** with purple gradients and animations
- **Diana cartoon integration** with contextual encouragement and celebration
- **Smooth animations** and engaging visual feedback
- **Responsive design** that works on tablets and computers

### 🧮 **Comprehensive Math Curriculum**
- **Number and Place Value**: Counting, comparing, ordering
- **Addition and Subtraction**: Mental math and written methods
- **Multiplication and Division**: Times tables and problem solving
- **Fractions**: Halves, quarters, thirds
- **Measurement**: Length, height, mass, weight with visual exercises
- **Geometry**: 2D and 3D shapes
- **Statistics**: Charts and data handling

### 🏆 **Gamification System**
- **Achievement system** with encouragement and success types
- **Level progression** based on accumulated points
- **Adaptive difficulty** that responds to performance
- **Progress tracking** with accuracy percentages
- **Confirmation modals** to prevent accidental submissions

### 🎭 **Diana Integration**
- **Celebration Diana** for correct answers with sparkles
- **Encouraging Diana** with thumbs up for motivation
- **Navigation Diana** throughout the app
- **Achievement banners** with contextual Diana images

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/GianZenz/DianaMath.git
cd DianaMath

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://127.0.0.1:5000` in your browser and start learning!

## 📁 Project Structure

```
DianaMath/
├── app/
│   ├── templates/          # Jinja2 HTML templates
│   ├── static/            # CSS, JS, images
│   └── curriculum.py      # Math exercise generation
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 Educational Goals

Designed to help Diana master:
- **Number confidence** through engaging counting exercises
- **Problem-solving skills** with visual and interactive questions
- **Mathematical reasoning** through progressive difficulty
- **Persistence** through encouraging feedback system
- **Achievement motivation** with gamified progress tracking

## 🔧 Technical Features

- **Flask 3.0** web framework
- **SQLAlchemy 2.0** for progress tracking
- **SQLite** database for simplicity
- **Responsive CSS** with child-friendly animations
- **Achievement system** with proper type classification
- **Visual measurement exercises** with proportional scaling

## 📚 Curriculum Alignment

Follows **Northern Ireland Primary 3** mathematics curriculum including:
- Numbers to 1000
- Mental addition and subtraction
- 2, 5, and 10 times tables
- Fractions (halves, quarters, thirds)
- Measurement units and comparisons
- 2D and 3D shape recognition

## 🎨 Design Philosophy

- **Child-first design** with large buttons and clear typography
- **Positive reinforcement** through Diana's encouraging presence
- **Visual learning** with measurement exercises and shape recognition
- **Error-friendly** environment that encourages experimentation
- **Achievement celebration** to build confidence

## 🔄 Backup System

The project includes comprehensive backup files:
- `exercise_working_backup.html` - Template backup
- `app_working_backup.py` - Application backup
- `style_working_backup.css` - Styling backup

See `WORKING_VERSION_BACKUP.md` for restoration instructions.

## 📝 License

This project is created with love for Diana's mathematical journey. Feel free to adapt it for other young learners!

## 🎉 Made with Love

Created specifically for Diana's 7th year mathematics adventure. Every feature is designed to make learning math joyful, engaging, and confidence-building.

---

*"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding."* - William Paul Thurston