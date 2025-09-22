#!/usr/bin/env python3
import os
import hashlib

def test_avatar_logic():
    print("Testing avatar logic...")
    
    # Test different usernames
    test_names = ['Diana', 'TestUser', 'John', 'Sarah', 'Mike']
    
    avatars = [
        'images/student_avatar_1.png',
        'images/student_avatar_2.png', 
        'images/student_avatar_3.png',
        'images/student_avatar_4.png',
        'images/student_avatar_5.png'
    ]
    
    for name in test_names:
        if name.lower() == 'diana':
            avatar = 'images/diana_cartoon.png'
        else:
            name_hash = int(hashlib.md5(name.lower().encode()).hexdigest(), 16)
            avatar_index = name_hash % len(avatars)
            avatar = avatars[avatar_index]
            
            # Check if file exists
            avatar_path = os.path.join('app/static', avatar)
            if not os.path.exists(avatar_path):
                avatar = 'images/diana_cartoon.png'
        
        print(f"{name}: {avatar}")
        
        # Check if the file actually exists
        full_path = os.path.join('app/static', avatar)
        exists = os.path.exists(full_path)
        print(f"  File exists: {exists}")

if __name__ == "__main__":
    test_avatar_logic()