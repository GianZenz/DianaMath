#!/usr/bin/env python3
"""
Test script to check visual content generation
"""

import sys
sys.path.append('.')

from app.curriculum import generate_length_height, generate_mass_weight

def test_visual_generation():
    print("🎨 Testing Visual Content Generation\n")
    
    # Test Length/Height exercise
    print("1. Testing Length/Height Exercise (Difficulty 1):")
    length_exercise = generate_length_height(1)
    print(f"   Question: {length_exercise['question']}")
    print(f"   Options: {length_exercise['options']}")
    print(f"   Correct Answer: {length_exercise['correct_answer']}")
    print(f"   Has visual_html: {'visual_html' in length_exercise}")
    if 'visual_html' in length_exercise:
        print(f"   Visual HTML length: {len(length_exercise['visual_html'])} characters")
        print(f"   Visual HTML preview: {length_exercise['visual_html'][:100]}...")
    print()
    
    # Test Length/Height exercise difficulty 2
    print("2. Testing Length/Height Exercise (Difficulty 2):")
    length_exercise2 = generate_length_height(2)
    print(f"   Question: {length_exercise2['question']}")
    print(f"   Options: {length_exercise2['options']}")
    print(f"   Correct Answer: {length_exercise2['correct_answer']}")
    print(f"   Has visual_html: {'visual_html' in length_exercise2}")
    if 'visual_html' in length_exercise2:
        print(f"   Visual HTML length: {len(length_exercise2['visual_html'])} characters")
        print(f"   Visual HTML preview: {length_exercise2['visual_html'][:100]}...")
    print()
    
    # Test Mass/Weight exercise
    print("3. Testing Mass/Weight Exercise (Difficulty 1):")
    weight_exercise = generate_mass_weight(1)
    print(f"   Question: {weight_exercise['question']}")
    print(f"   Options: {weight_exercise['options']}")
    print(f"   Correct Answer: {weight_exercise['correct_answer']}")
    print(f"   Has visual_html: {'visual_html' in weight_exercise}")
    if 'visual_html' in weight_exercise:
        print(f"   Visual HTML length: {len(weight_exercise['visual_html'])} characters")
        print(f"   Visual HTML preview: {weight_exercise['visual_html'][:100]}...")
    print()
    
    # Test Mass/Weight exercise difficulty 2
    print("4. Testing Mass/Weight Exercise (Difficulty 2):")
    weight_exercise2 = generate_mass_weight(2)
    print(f"   Question: {weight_exercise2['question']}")
    print(f"   Options: {weight_exercise2['options']}")
    print(f"   Correct Answer: {weight_exercise2['correct_answer']}")
    print(f"   Has visual_html: {'visual_html' in weight_exercise2}")
    if 'visual_html' in weight_exercise2:
        print(f"   Visual HTML length: {len(weight_exercise2['visual_html'])} characters")
        print(f"   Visual HTML preview: {weight_exercise2['visual_html'][:100]}...")
    print()
    
    print("✅ Visual content generation test completed!")

if __name__ == "__main__":
    test_visual_generation()