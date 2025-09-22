"""
Gamification system for DianaMath
"""
import random

def calculate_points(is_correct, difficulty):
    """Calculate points earned based on correctness and difficulty"""
    if not is_correct:
        return 1  # Participation point
    
    base_points = 10
    difficulty_multiplier = difficulty
    return base_points * difficulty_multiplier

def get_user_level(total_points):
    """Calculate user level based on total points"""
    # Level progression: 100, 250, 500, 1000, 1750, 2750, 4000, etc.
    levels = [0, 100, 250, 500, 1000, 1750, 2750, 4000, 5500, 7500, 10000]
    
    for level, required_points in enumerate(levels):
        if total_points < required_points:
            return level
    
    # For points beyond the defined levels
    return len(levels) + (total_points - levels[-1]) // 2000

def check_achievements(user, progress):
    """Check for new achievements and return list of earned badges"""
    achievements = []
    
    # First correct answer
    if progress.correct_answers == 1 and progress.total_attempts == 1:
        achievements.append({
            "name": "First Steps",
            "description": "Got your first answer correct!",
            "points": 25,
            "icon": "🌟"
        })
    
    # Perfect streak of 5
    if progress.total_attempts >= 5 and progress.correct_answers == progress.total_attempts:
        achievements.append({
            "name": "Perfect Streak",
            "description": "5 correct answers in a row!",
            "points": 50,
            "icon": "🔥"
        })
    
    # Math Explorer - try 5 different subtopics
    if user.total_points >= 500:
        achievements.append({
            "name": "Math Explorer",
            "description": "Explored many math topics!",
            "points": 100,
            "icon": "🗺️"
        })
    
    # Speed Racer - high accuracy
    accuracy = progress.correct_answers / progress.total_attempts if progress.total_attempts > 0 else 0
    if progress.total_attempts >= 10 and accuracy >= 0.9:
        achievements.append({
            "name": "Accuracy Expert",
            "description": "90% accuracy with 10+ problems!",
            "points": 75,
            "icon": "🎯"
        })
    
    # Level milestones
    if user.level == 5:
        achievements.append({
            "name": "Rising Star",
            "description": "Reached level 5!",
            "points": 100,
            "icon": "⭐"
        })
    elif user.level == 10:
        achievements.append({
            "name": "Math Champion",
            "description": "Reached level 10!",
            "points": 200,
            "icon": "🏆"
        })
    
    return achievements

def get_badge_list():
    """Return all possible badges for the achievements page"""
    return [
        {"name": "First Steps", "description": "Got your first answer correct!", "icon": "🌟"},
        {"name": "Perfect Streak", "description": "5 correct answers in a row!", "icon": "🔥"},
        {"name": "Math Explorer", "description": "Explored many math topics!", "icon": "🗺️"},
        {"name": "Accuracy Expert", "description": "90% accuracy with 10+ problems!", "icon": "🎯"},
        {"name": "Rising Star", "description": "Reached level 5!", "icon": "⭐"},
        {"name": "Math Champion", "description": "Reached level 10!", "icon": "🏆"},
        {"name": "Addition Master", "description": "Completed 50 addition problems!", "icon": "➕"},
        {"name": "Subtraction Star", "description": "Completed 50 subtraction problems!", "icon": "➖"},
        {"name": "Multiplication Marvel", "description": "Completed 50 multiplication problems!", "icon": "✖️"},
        {"name": "Fraction Friend", "description": "Completed 25 fraction problems!", "icon": "🍰"},
        {"name": "Shape Detective", "description": "Completed 25 geometry problems!", "icon": "🔍"},
        {"name": "Time Keeper", "description": "Completed 25 time problems!", "icon": "⏰"},
        {"name": "Daily Learner", "description": "Learned for 7 days in a row!", "icon": "📅"},
        {"name": "Problem Solver", "description": "Solved 100 problems!", "icon": "🧩"},
        {"name": "Math Genius", "description": "Reached level 20!", "icon": "🧠"}
    ]

def get_motivational_message(points_earned, is_correct, level_up=False):
    """Get encouraging message based on performance"""
    if level_up:
        return "🎉 Level Up! You're becoming a math superstar!"
    
    if is_correct:
        messages = [
            "🌟 Excellent work!",
            "🎯 Perfect! You're getting stronger!",
            "⭐ Amazing! Keep it up!",
            "🚀 Fantastic! You're on fire!",
            "🏆 Outstanding! Well done!",
            "💫 Brilliant! You're a math star!"
        ]
        return random.choice(messages)
    else:
        messages = [
            "🤔 Good try! Let's practice more!",
            "💪 Keep going! You're learning!",
            "🌱 Every mistake helps you grow!",
            "🎯 Close! Try the next one!",
            "🌟 Don't give up! You've got this!",
            "📚 Great effort! Learning takes practice!"
        ]
        return random.choice(messages)