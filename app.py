from flask import Flask, render_template, request, jsonify, session, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import random
import os

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SECRET_KEY'] = 'diana-math-secret-key-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diana_math.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import curriculum module
from app.curriculum import get_curriculum_for_year, get_exercise

# Simple gamification functions
def calculate_points(is_correct, difficulty):
    """Calculate points earned based on correctness and difficulty"""
    if not is_correct:
        return 1  # Participation point
    base_points = 10
    difficulty_multiplier = difficulty
    return base_points * difficulty_multiplier

def get_user_level(total_points):
    """Calculate user level based on total points"""
    levels = [0, 100, 250, 500, 1000, 1750, 2750, 4000, 5500, 7500, 10000]
    for level, required_points in enumerate(levels):
        if total_points < required_points:
            return level
    return len(levels) + (total_points - levels[-1]) // 2000

def check_achievements(user, progress, is_correct):
    """Check and award achievements"""
    achievements = []
    
    # First Try - awarded for first attempt regardless of correctness
    if not Achievement.query.filter_by(user_id=user.id, badge_name="First Try").first():
        total_attempts = db.session.query(db.func.sum(Progress.total_attempts)).filter_by(user_id=user.id).scalar() or 0
        if total_attempts == 1:  # This should be 1 because we already incremented total_attempts above
            achievement = Achievement(user_id=user.id, badge_name="First Try", points_earned=2)
            db.session.add(achievement)
            achievements.append({"name": "First Try", "description": "Welcome! You took your first shot!", "points": 2, "type": "encouragement"})
    
    # Never Give Up - for getting a correct answer after a wrong answer
    if is_correct and progress.total_attempts >= 2 and not Achievement.query.filter_by(user_id=user.id, badge_name="Never Give Up").first():
        # Check if previous answer was wrong and this one is correct
        if progress.correct_answers / progress.total_attempts <= 0.5:  # Had some wrong answers
            achievement = Achievement(user_id=user.id, badge_name="Never Give Up", points_earned=8)
            db.session.add(achievement)
            achievements.append({"name": "Never Give Up", "description": "You kept trying and got it right!", "points": 8, "type": "encouragement"})
    
    # First Correct Answer - only if current answer is correct AND user has no previous correct answers
    if is_correct and not Achievement.query.filter_by(user_id=user.id, badge_name="First Success").first():
        # Check if this is truly the first correct answer by counting all correct answers across all topics
        total_correct = db.session.query(db.func.sum(Progress.correct_answers)).filter_by(user_id=user.id).scalar() or 0
        if total_correct == 1:  # This should be 1 because we already incremented correct_answers above
            achievement = Achievement(user_id=user.id, badge_name="First Success", points_earned=5)
            db.session.add(achievement)
            achievements.append({"name": "First Success", "description": "Got your first answer right!", "points": 5, "type": "success"})
    
    # Level Up achievements - only award when actually reaching the level
    if user.level >= 2 and not Achievement.query.filter_by(user_id=user.id, badge_name="Level 2 Master").first():
        achievement = Achievement(user_id=user.id, badge_name="Level 2 Master", points_earned=10)
        db.session.add(achievement)
        achievements.append({"name": "Level 2 Master", "description": "Reached Level 2!", "points": 10, "type": "success"})
    
    if user.level >= 3 and not Achievement.query.filter_by(user_id=user.id, badge_name="Level 3 Expert").first():
        achievement = Achievement(user_id=user.id, badge_name="Level 3 Expert", points_earned=15)
        db.session.add(achievement)
        achievements.append({"name": "Level 3 Expert", "description": "Reached Level 3!", "points": 15, "type": "success"})
    
    # Perfect Streak (good accuracy) - only if current answer is correct
    if is_correct and progress.total_attempts >= 3:
        accuracy = progress.correct_answers / progress.total_attempts
        if accuracy >= 0.75 and not Achievement.query.filter_by(user_id=user.id, badge_name="Perfect Streak").first():
            achievement = Achievement(user_id=user.id, badge_name="Perfect Streak", points_earned=20)
            db.session.add(achievement)
            achievements.append({"name": "Perfect Streak", "description": "Great accuracy in this topic!", "points": 20, "type": "success"})
    
    # Persistent Learner - for answering 10 questions regardless of correctness
    total_attempts = db.session.query(db.func.sum(Progress.total_attempts)).filter_by(user_id=user.id).scalar() or 0
    if total_attempts >= 10 and not Achievement.query.filter_by(user_id=user.id, badge_name="Persistent Learner").first():
        achievement = Achievement(user_id=user.id, badge_name="Persistent Learner", points_earned=15)
        db.session.add(achievement)
        achievements.append({"name": "Persistent Learner", "description": "Answered 10 questions! Keep going!", "points": 15, "type": "encouragement"})
    
    # Points milestones - only when actually reaching the milestone
    if user.total_points >= 100 and not Achievement.query.filter_by(user_id=user.id, badge_name="Century").first():
        achievement = Achievement(user_id=user.id, badge_name="Century", points_earned=25)
        db.session.add(achievement)
        achievements.append({"name": "Century", "description": "Earned 100 points!", "points": 25, "type": "success"})
    
    return achievements

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    current_year = db.Column(db.Integer, default=3)  # Northern Ireland Primary 3 (age 7)
    total_points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    subtopic = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.Integer, default=1)
    correct_answers = db.Column(db.Integer, default=0)
    total_attempts = db.Column(db.Integer, default=0)
    last_attempted = db.Column(db.DateTime, default=datetime.utcnow)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    badge_name = db.Column(db.String(100), nullable=False)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)
    points_earned = db.Column(db.Integer, default=0)

# Routes
@app.route('/')
def home():
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = db.session.get(User, user_id)
    
    return render_template('home.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name', '').strip()
    if not name:
        return redirect('/')
    
    # Find existing user or create new one
    user = User.query.filter_by(name=name).first()
    if not user:
        user = User(name=name, current_year=3)
        db.session.add(user)
        db.session.commit()
    
    session['user_id'] = user.id
    return redirect('/')

@app.route('/learn/<topic>')
def learn_topic(topic):
    user_id = session.get('user_id')
    if not user_id:
        user = User.query.first()
        session['user_id'] = user.id if user else 1
        user_id = session['user_id']
    
    user = User.query.get_or_404(user_id)
    curriculum = get_curriculum_for_year(user.current_year)
    
    if topic not in curriculum:
        return "Topic not found", 404
        
    return render_template('learn.html', user=user, topic=topic, curriculum=curriculum[topic])

@app.route('/exercise/<topic>/<subtopic>')
def exercise(topic, subtopic):
    user_id = session.get('user_id')
    if not user_id:
        user = User.query.first()
        session['user_id'] = user.id if user else 1
        user_id = session['user_id']
    
    user = User.query.get_or_404(user_id)
    
    # Get user's progress for this subtopic
    progress = Progress.query.filter_by(
        user_id=user_id, topic=topic, subtopic=subtopic
    ).first()
    
    difficulty = progress.difficulty if progress else 1
    exercise_data = get_exercise(topic, subtopic, difficulty)
    
    return render_template('exercise.html', 
                         user=user, 
                         topic=topic, 
                         subtopic=subtopic,
                         exercise=exercise_data)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        print("Submit answer route called")  # Debug
        
        # Get JSON data
        if not request.json:
            print("No JSON data received")
            return jsonify({'error': 'No data received'}), 400
            
        data = request.json
        print(f"Received data: {data}")  # Debug
        
        # Get or create user session
        user_id = session.get('user_id')
        if not user_id:
            user = User.query.first()
            if not user:
                user = User(name="Diana", current_year=3)
                db.session.add(user)
                db.session.commit()
            session['user_id'] = user.id
            user_id = user.id
        
        user = db.session.get(User, user_id)
        if not user:
            print(f"User not found: {user_id}")
            return jsonify({'error': 'User not found'}), 404
        
        # Extract answer data
        topic = data.get('topic', '')
        subtopic = data.get('subtopic', '')
        answer = str(data.get('answer', '')).strip()
        correct_answer = str(data.get('correct_answer', '')).strip()
        
        print(f"DEBUG - Answer comparison:")
        print(f"  User answer: '{answer}' (type: {type(answer)}, length: {len(answer)})")
        print(f"  Correct answer: '{correct_answer}' (type: {type(correct_answer)}, length: {len(correct_answer)})")
        print(f"  Answers equal: {answer == correct_answer}")
        print(f"  Answer bytes: {answer.encode('utf-8')}")
        print(f"  Correct bytes: {correct_answer.encode('utf-8')}")
        
        is_correct = answer == correct_answer
        
        # Get or create progress record
        progress = Progress.query.filter_by(
            user_id=user_id, topic=topic, subtopic=subtopic
        ).first()
        
        if not progress:
            progress = Progress(
                user_id=user_id, 
                topic=topic, 
                subtopic=subtopic,
                difficulty=1,
                correct_answers=0,
                total_attempts=0
            )
            db.session.add(progress)
        
        # Update progress
        progress.total_attempts += 1
        if is_correct:
            progress.correct_answers += 1
        progress.last_attempted = datetime.utcnow()
        
        # Calculate points
        points_earned = calculate_points(is_correct, progress.difficulty)
        user.total_points += points_earned
        
        # Calculate level
        new_level = get_user_level(user.total_points)
        level_up = new_level > user.level
        user.level = new_level
        
        # Check for achievements
        earned_achievements = check_achievements(user, progress, is_correct)
        
        # Add achievement points
        for achievement in earned_achievements:
            user.total_points += achievement["points"]
        
        # Recalculate level after achievement points
        user.level = get_user_level(user.total_points)
        
        # Adjust difficulty based on performance
        if progress.total_attempts >= 3:
            accuracy = progress.correct_answers / progress.total_attempts
            if accuracy >= 0.8 and progress.difficulty < 5:
                progress.difficulty += 1
            elif accuracy < 0.5 and progress.difficulty > 1:
                progress.difficulty -= 1
        
        # Save to database
        db.session.commit()
        print("Database updated successfully")  # Debug
        
        # Calculate accuracy percentage
        accuracy_percent = round((progress.correct_answers / progress.total_attempts) * 100, 1) if progress.total_attempts > 0 else 0
        
        response_data = {
            'correct': is_correct,
            'points_earned': points_earned,
            'total_points': user.total_points,
            'level': user.level,
            'level_up': level_up,
            'achievements': earned_achievements,
            'accuracy': accuracy_percent
        }
        
        print(f"Sending response: {response_data}")  # Debug
        return jsonify(response_data)
    
    except Exception as e:
        print(f"Error in submit_answer: {str(e)}")  # Debug
        import traceback
        traceback.print_exc()  # Print full error traceback
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        user = User.query.first()
        session['user_id'] = user.id if user else 1
        user_id = session['user_id']
    
    user = User.query.get_or_404(user_id)
    progress_data = Progress.query.filter_by(user_id=user_id).all()
    achievements = Achievement.query.filter_by(user_id=user_id).all()
    
    return render_template('dashboard.html', 
                         user=user, 
                         progress_data=progress_data,
                         achievements=achievements)

@app.route('/settings')
def settings():
    """User settings page"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/')
    
    user = User.query.get_or_404(user_id)
    return render_template('settings.html', user=user)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    """Update user profile settings"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/')
    
    user = User.query.get_or_404(user_id)
    
    # Get form data
    name = request.form.get('name', '').strip()
    current_year = request.form.get('current_year', type=int)
    
    # Validate inputs
    if name and len(name) <= 100:
        user.name = name
    
    if current_year and 1 <= current_year <= 7:  # Primary 1-7
        user.current_year = current_year
    
    db.session.commit()
    return redirect('/settings?updated=1')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'app/static'),
                          'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Create default user if none exists
        if not User.query.first():
            diana = User(name="Diana", current_year=3)  # Northern Ireland Primary 3
            db.session.add(diana)
            db.session.commit()
    
    app.run(debug=True, host='0.0.0.0', port=5000)