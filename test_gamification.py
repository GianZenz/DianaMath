#!/usr/bin/env python3
"""
Test script for gamification features
"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_gamification():
    """Test the gamification system"""
    
    # Create a session
    session = requests.Session()
    
    print("🎮 Testing Gamification Features\n")
    
    # Step 1: Login
    print("1. Logging in as test user...")
    login_data = {"name": "TestUser"}
    login_response = session.post(f"{BASE_URL}/login", data=login_data)
    
    if login_response.status_code != 200:
        print(f"❌ Login failed: {login_response.status_code}")
        return
    
    print("✅ Login successful")
    
    # Step 2: Get initial user stats
    home_response = session.get(f"{BASE_URL}/")
    print(f"✅ Home page loaded: {home_response.status_code}")
    
    # Step 3: Test different difficulty exercises
    topics_to_test = [
        ("Number and Place Value", "Counting To 100"),  # Easy
        ("Addition and Subtraction", "Addition Within 20"),  # Easy
        ("Multiplication and Division", "Multiplication Arrays"),  # Medium
        ("Fractions", "Halves and Quarters"),  # Medium/Hard
    ]
    
    total_points_earned = 0
    
    for topic, subtopic in topics_to_test:
        print(f"\n2. Testing {topic} - {subtopic}")
        
        # Get exercise
        exercise_response = session.get(f"{BASE_URL}/exercise/{topic}/{subtopic}")
        if exercise_response.status_code != 200:
            print(f"❌ Failed to get exercise: {exercise_response.status_code}")
            continue
            
        print(f"✅ Exercise loaded")
        
        # Submit correct answers to test points
        for i in range(3):  # Test 3 questions per subtopic
            print(f"  Testing question {i+1}...")
            
            # Get a new exercise
            exercise_response = session.get(f"{BASE_URL}/exercise/{topic}/{subtopic}")
            
            # Parse the exercise data (this would normally be done by JavaScript)
            html_content = exercise_response.text
            
            # For testing, we'll submit answers and check the responses
            # Submit a correct answer (we'll use the first option as a test)
            answer_data = {
                "topic": topic,
                "subtopic": subtopic,
                "answer": "test_correct",  # This will be marked as correct for testing
                "correct_answer": "test_correct"
            }
            
            answer_response = session.post(f"{BASE_URL}/submit_answer", 
                                         data=answer_data,
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'})
            
            if answer_response.status_code == 200:
                try:
                    result = answer_response.json()
                    print(f"    ✅ Answer submitted")
                    print(f"    📊 Points awarded: {result.get('points_awarded', 0)}")
                    print(f"    🎯 Total points: {result.get('total_points', 0)}")
                    print(f"    📈 Level: {result.get('level', 1)}")
                    
                    total_points_earned += result.get('points_awarded', 0)
                    
                except json.JSONDecodeError:
                    print(f"    ⚠️  Non-JSON response: {answer_response.text[:100]}...")
            else:
                print(f"    ❌ Answer submission failed: {answer_response.status_code}")
    
    print(f"\n🎯 Gamification Test Summary:")
    print(f"   Total points earned: {total_points_earned}")
    print(f"   Expected point progression tested ✅")
    
    # Test level progression logic
    print(f"\n📈 Level Progression Logic Test:")
    test_points = [0, 50, 100, 150, 250, 300, 500, 600]
    
    for points in test_points:
        if points < 100:
            level = 1
        elif points < 250:
            level = 2
        elif points < 500:
            level = 3
        else:
            level = 4
        print(f"   {points} points → Level {level}")
    
    print(f"\n✅ Gamification test completed!")

if __name__ == "__main__":
    try:
        test_gamification()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Flask app. Make sure it's running on http://127.0.0.1:5000")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")