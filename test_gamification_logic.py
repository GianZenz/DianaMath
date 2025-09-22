#!/usr/bin/env python3
"""
Simple test of gamification logic
"""

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

def test_gamification_logic():
    """Test the gamification system logic"""
    
    print("🎮 Testing Gamification Logic\n")
    
    # Test 1: Points calculation
    print("1. Testing Points Calculation:")
    test_cases = [
        (True, 1, 10),   # Correct, difficulty 1 = 10 points
        (True, 2, 20),   # Correct, difficulty 2 = 20 points
        (True, 3, 30),   # Correct, difficulty 3 = 30 points
        (False, 1, 1),   # Incorrect, difficulty 1 = 1 point
        (False, 3, 1),   # Incorrect, difficulty 3 = 1 point
    ]
    
    for is_correct, difficulty, expected in test_cases:
        result = calculate_points(is_correct, difficulty)
        status = "✅" if result == expected else "❌"
        print(f"   {status} Correct: {is_correct}, Difficulty: {difficulty} → {result} points (expected {expected})")
    
    # Test 2: Level progression
    print(f"\n2. Testing Level Progression:")
    level_tests = [
        (0, 1),      # 0 points = Level 1
        (50, 1),     # 50 points = Level 1
        (99, 1),     # 99 points = Level 1
        (100, 2),    # 100 points = Level 2
        (200, 2),    # 200 points = Level 2
        (249, 2),    # 249 points = Level 2
        (250, 3),    # 250 points = Level 3
        (400, 3),    # 400 points = Level 3
        (499, 3),    # 499 points = Level 3
        (500, 4),    # 500 points = Level 4
        (1000, 5),   # 1000 points = Level 5
    ]
    
    for points, expected_level in level_tests:
        result = get_user_level(points)
        status = "✅" if result == expected_level else "❌"
        print(f"   {status} {points} points → Level {result} (expected {expected_level})")
    
    # Test 3: Simulated learning session
    print(f"\n3. Simulated Learning Session:")
    total_points = 0
    current_level = 1
    
    # Simulate answering questions
    questions = [
        (True, 1),   # Easy question, correct
        (True, 1),   # Easy question, correct
        (False, 1),  # Easy question, wrong
        (True, 2),   # Medium question, correct
        (True, 2),   # Medium question, correct
        (True, 2),   # Medium question, correct
        (True, 3),   # Hard question, correct
        (True, 3),   # Hard question, correct
    ]
    
    for i, (is_correct, difficulty) in enumerate(questions, 1):
        points_earned = calculate_points(is_correct, difficulty)
        total_points += points_earned
        new_level = get_user_level(total_points)
        level_up = new_level > current_level
        
        result_emoji = "✅" if is_correct else "❌"
        level_emoji = "🎉" if level_up else ""
        
        print(f"   Question {i}: {result_emoji} Difficulty {difficulty} → +{points_earned} points")
        print(f"              Total: {total_points} points, Level {new_level} {level_emoji}")
        
        if level_up:
            print(f"              🎉 LEVEL UP! {current_level} → {new_level}")
        
        current_level = new_level
        print()
    
    print(f"✅ Gamification logic test completed!")
    print(f"📊 Final Stats: {total_points} points, Level {current_level}")

if __name__ == "__main__":
    test_gamification_logic()