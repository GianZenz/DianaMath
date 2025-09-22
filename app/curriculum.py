"""
UK Curriculum-based math exercises for different year groups
"""
import random

def get_curriculum_for_year(year):
    """Get curriculum topics for a specific Northern Ireland Primary year group"""
    curricula = {
        3: {  # Primary 3 (Age 6-7) - Northern Ireland
            "Number and Place Value": [
                "counting_to_100",
                "place_value_tens_ones", 
                "comparing_numbers"
            ],
            "Addition and Subtraction": [
                "addition_within_20",
                "subtraction_within_20",
                "addition_two_digit"
            ],
            "Multiplication and Division": [
                "counting_in_2s_5s_10s",
                "multiplication_arrays",
                "simple_division"
            ],
            "Fractions": [
                "halves_quarters",
                "finding_fractions"
            ],
            "Measurement": [
                "length_height",
                "mass_weight", 
                "temperature",
                "time_hours_minutes"
            ],
            "Geometry": [
                "2d_shapes",
                "3d_shapes",
                "position_direction"
            ]
        },
        4: {  # Primary 4 (Age 7-8) - Northern Ireland
            "Number and Place Value": [
                "hundreds_tens_ones",
                "counting_in_4s_8s_50s_100s",
                "comparing_ordering_numbers"
            ],
            "Addition and Subtraction": [
                "addition_subtraction_3_digits",
                "mental_strategies",
                "estimation"
            ],
            "Multiplication and Division": [
                "multiplication_tables_3_4_8",
                "written_methods",
                "solving_problems"
            ],
            "Fractions": [
                "unit_fractions",
                "equivalent_fractions",
                "comparing_fractions"
            ],
            "Measurement": [
                "measuring_length_mm_cm_m",
                "measuring_mass_g_kg",
                "measuring_volume"
            ],
            "Geometry": [
                "drawing_shapes",
                "angles",
                "horizontal_vertical_parallel_perpendicular"
            ]
        },
        5: {  # Primary 5 (Age 8-9) - Northern Ireland
            "Number and Place Value": [
                "hundreds_tens_ones",
                "counting_in_4s_8s_50s_100s",
                "comparing_ordering_numbers"
            ],
            "Addition and Subtraction": [
                "addition_subtraction_3_digits",
                "mental_strategies",
                "estimation"
            ],
            "Multiplication and Division": [
                "multiplication_tables_3_4_8",
                "written_methods",
                "solving_problems"
            ],
            "Fractions": [
                "unit_fractions",
                "equivalent_fractions",
                "comparing_fractions"
            ],
            "Measurement": [
                "measuring_length_mm_cm_m",
                "measuring_mass_g_kg",
                "measuring_volume"
            ],
            "Geometry": [
                "drawing_shapes",
                "angles",
                "horizontal_vertical_parallel_perpendicular"
            ]
        }
    }
    return curricula.get(year, curricula[3])

def get_exercise(topic, subtopic, difficulty=1):
    """Generate an exercise based on topic, subtopic, and difficulty"""
    
    exercises = {
        "addition_within_20": generate_addition_within_20,
        "subtraction_within_20": generate_subtraction_within_20,
        "addition_two_digit": generate_addition_within_20,  # Reuse with higher difficulty
        "counting_to_100": generate_counting_to_100,
        "place_value_tens_ones": generate_place_value,
        "comparing_numbers": generate_comparing_numbers,
        "counting_in_2s_5s_10s": generate_skip_counting,
        "multiplication_arrays": generate_multiplication_arrays,
        "simple_division": generate_simple_division,
        "halves_quarters": generate_fractions_halves_quarters,
        "finding_fractions": generate_finding_fractions,
        "length_height": generate_length_height,
        "mass_weight": generate_mass_weight,
        "temperature": generate_temperature,
        "time_hours_minutes": generate_time_reading,
        "2d_shapes": generate_2d_shapes,
        "3d_shapes": generate_3d_shapes,
        "position_direction": generate_position_direction,
    }
    
    exercise_func = exercises.get(subtopic, generate_default_exercise)
    return exercise_func(difficulty)

def generate_addition_within_20(difficulty):
    """Generate addition problems within 20"""
    if difficulty == 1:
        # Simple addition up to 10
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        hint = f"💡 Try counting on your fingers! Start with {a}, then count up {b} more: {a + 1}, {a + 2}..."
    elif difficulty == 2:
        # Addition up to 15
        a = random.randint(3, 8)
        b = random.randint(2, 7)
        hint = f"💡 Break it down! Try {a} + {b//2} + {b - b//2} = {a + b//2} + {b - b//2} = ?"
    else:
        # Addition up to 20
        a = random.randint(5, 15)
        b = random.randint(1, 20-a)
        if a + b > 10:
            hint = f"💡 Use the 'make 10' strategy! {a} + {b} = {a} + {10-a} + {b-(10-a)} = 10 + {b-(10-a)} = ?"
        else:
            hint = f"💡 You can use doubles! Is {a} or {b} close to a double you know?"
    
    question = f"What is {a} + {b}?"
    correct_answer = a + b
    
    # Generate wrong answers
    options = [correct_answer]
    while len(options) < 4:
        wrong = correct_answer + random.randint(-3, 3)
        if wrong > 0 and wrong not in options and wrong <= 30:
            options.append(wrong)
    
    random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": f"🔵 " * a + " + " + "🔴 " * b + " = ?",
        "hint": hint
    }

def generate_subtraction_within_20(difficulty):
    """Generate subtraction problems within 20"""
    if difficulty == 1:
        # Simple subtraction from numbers up to 10
        result = random.randint(0, 5)
        subtract = random.randint(1, 5)
        start = result + subtract
        hint = f"💡 Think: what number plus {subtract} equals {start}? You can count backwards or use objects to take away!"
    else:
        # Subtraction from numbers up to 20
        result = random.randint(0, 10)
        subtract = random.randint(1, 10)
        start = result + subtract
        if start > 10:
            hint = f"💡 Try breaking it down: {start} - {10} = {start-10}, then {start-10} - {subtract-10} = ?"
        else:
            hint = f"💡 Count backwards from {start}: {start-1}, {start-2}... or think 'what plus {subtract} equals {start}?'"
    
    question = f"What is {start} - {subtract}?"
    correct_answer = result
    
    options = [correct_answer]
    while len(options) < 4:
        wrong = correct_answer + random.randint(-3, 3)
        if wrong >= 0 and wrong not in options and wrong <= 20:
            options.append(wrong)
    
    random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": f"Start with {start} blocks, take away {subtract}",
        "hint": hint
    }

def generate_counting_to_100(difficulty):
    """Generate counting exercises"""
    start = random.randint(1, 80)
    step = 1 if difficulty == 1 else random.choice([2, 5, 10])
    
    sequence = [start + i * step for i in range(5)]
    missing_index = random.randint(1, 3)
    missing_number = sequence[missing_index]
    
    sequence_str = [str(x) if i != missing_index else "?" for i, x in enumerate(sequence)]
    
    question = f"What number is missing? {' → '.join(sequence_str)}"
    
    if step == 1:
        hint = f"💡 Count one by one: {sequence[0]}, {sequence[1] if missing_index != 1 else '?'}... What comes next?"
    else:
        hint = f"💡 You're counting by {step}s! Add {step} each time: {sequence[0]} + {step} = {sequence[1]}"
    
    options = [missing_number]
    while len(options) < 4:
        wrong = missing_number + random.randint(-5, 5)
        if wrong > 0 and wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": missing_number,
        "hint": hint
    }

def generate_place_value(difficulty):
    """Generate place value exercises"""
    if difficulty == 1:
        number = random.randint(10, 99)
        tens = number // 10
        ones = number % 10
        
        if random.choice([True, False]):
            question = f"How many tens are in {number}?"
            correct_answer = tens
        else:
            question = f"How many ones are in {number}?"
            correct_answer = ones
    else:
        number = random.randint(100, 999)
        hundreds = number // 100
        question = f"How many hundreds are in {number}?"
        correct_answer = hundreds
    
    options = [correct_answer]
    while len(options) < 4:
        wrong = correct_answer + random.randint(-2, 2)
        if wrong >= 0 and wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    
    # Generate contextual hints
    if difficulty == 1:
        if "tens" in question:
            hint = f"💡 Look at the tens place (the leftmost digit in {number}). The digit {tens} means {tens} groups of 10!"
        else:  # ones
            hint = f"💡 Look at the ones place (the rightmost digit in {number}). The digit {ones} means {ones} single units!"
    else:  # hundreds
        hint = f"💡 Look at the hundreds place (the leftmost digit in {number}). The digit {hundreds} means {hundreds} groups of 100!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": f"Think about {number} as groups of tens and ones",
        "hint": hint
    }

def generate_comparing_numbers(difficulty):
    """Generate number comparison exercises"""
    if difficulty == 1:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
    else:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
    
    if a == b:
        a += 1
    
    question = f"Which symbol goes between these numbers? {a} __ {b}"
    
    if a > b:
        correct_answer = ">"
        hint = f"💡 {a} is bigger than {b}. The symbol > opens to the bigger number. Think: 'alligator mouth eats the bigger number'!"
    else:
        correct_answer = "<"
        hint = f"💡 {a} is smaller than {b}. The symbol < opens to the bigger number. Think: 'alligator mouth eats the bigger number'!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": [">", "<", "="],
        "correct_answer": correct_answer,
        "hint": hint
    }

def generate_multiplication_arrays(difficulty):
    """Generate multiplication using arrays/groups"""
    if difficulty == 1:
        multiplier = random.choice([2, 5, 10])
        multiplicand = random.randint(1, 5)
    else:
        multiplier = random.choice([2, 3, 4, 5, 10])
        multiplicand = random.randint(1, 8)
    
    question = f"What is {multiplicand} groups of {multiplier}?"
    correct_answer = multiplier * multiplicand
    
    options = [correct_answer]
    while len(options) < 4:
        wrong = correct_answer + random.randint(-5, 5)
        if wrong > 0 and wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    
    # Generate contextual hints
    if multiplier in [2, 5, 10]:
        if multiplier == 2:
            hint = f"💡 Think: {multiplicand} groups of 2 means adding 2 + 2 + 2... Count by 2s: 2, 4, 6..."
        elif multiplier == 5:
            hint = f"💡 Think: {multiplicand} groups of 5. Count by 5s: 5, 10, 15... Use your fingers!"
        else:  # multiplier == 10
            hint = f"💡 Think: {multiplicand} groups of 10. Count by 10s: 10, 20, 30... Just add a zero to {multiplicand}!"
    else:
        hint = f"💡 Think: {multiplicand} groups of {multiplier}. You can add {multiplier} + {multiplier} + {multiplier}... or draw {multiplicand} circles with {multiplier} dots in each!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": f"Draw {multiplicand} groups with {multiplier} items in each group",
        "hint": hint
    }

def generate_fractions_halves_quarters(difficulty):
    """Generate fraction exercises with visual representations"""
    shapes = ["circle", "rectangle", "square"]
    shape = random.choice(shapes)
    
    # Add more variety: sometimes show halves, sometimes quarters, sometimes different amounts
    fraction_types = [
        {"fraction": "1/2", "parts": 2, "shaded": 1, "name": "half"},
        {"fraction": "1/4", "parts": 4, "shaded": 1, "name": "quarter"},
        {"fraction": "2/4", "parts": 4, "shaded": 2, "name": "two quarters"},
        {"fraction": "3/4", "parts": 4, "shaded": 3, "name": "three quarters"},
    ]
    
    if difficulty == 1:
        # Easier fractions: halves and simple quarters
        fraction_options = [fraction_types[0], fraction_types[1]]  # 1/2, 1/4
    else:
        # All fraction types
        fraction_options = fraction_types
    
    chosen_fraction = random.choice(fraction_options)
    correct_answer = chosen_fraction["fraction"]
    parts = chosen_fraction["parts"]
    shaded = chosen_fraction["shaded"]
    name = chosen_fraction["name"]
    
    question = f"What fraction of this {shape} is shaded?"
    
    # Generate options based on the correct answer
    if correct_answer == "1/2":
        options = ["1/2", "1/4", "2/4", "1/3"]
    elif correct_answer == "1/4":
        options = ["1/4", "1/2", "2/4", "1/3"]
    elif correct_answer == "2/4":
        options = ["2/4", "1/2", "1/4", "3/4"]
    else:  # 3/4
        options = ["3/4", "1/4", "2/4", "1/2"]
    
    # Create visual representation
    visual_help = create_fraction_visual(shape, parts, shaded, name)
    
    # Generate contextual hints
    if correct_answer == "1/2":
        hint = f"💡 The shape is split into 2 equal parts and 1 is shaded. This is 'one half' or 1/2!"
    elif correct_answer == "1/4":
        hint = f"💡 The shape is split into 4 equal parts and 1 is shaded. This is 'one quarter' or 1/4!"
    elif correct_answer == "2/4":
        hint = f"💡 The shape has 4 equal parts and 2 are shaded. Count: 2 out of 4 = 2/4!"
    else:  # 3/4
        hint = f"💡 Count the shaded parts: 3 out of 4 total parts are shaded. That's 3/4!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": visual_help,
        "hint": hint
    }

def create_fraction_visual(shape, parts, shaded, name):
    """Create HTML for fraction visualization"""
    if shape == "circle":
        if parts == 2:
            return f'<div class="fraction-visual circle-half"><div class="shaded-half"></div></div><p>{shaded} out of {parts} parts is shaded</p>'
        elif parts == 4:
            if shaded == 1:
                return f'<div class="fraction-visual circle-quarter-1"></div><p>{shaded} out of {parts} parts shaded</p>'
            elif shaded == 2:
                return f'<div class="fraction-visual circle-quarter-2"></div><p>{shaded} out of {parts} parts shaded</p>'
            else:  # 3
                return f'<div class="fraction-visual circle-quarter-3"></div><p>{shaded} out of {parts} parts shaded</p>'
    
    elif shape == "rectangle":
        if parts == 2:
            return f'<div class="fraction-visual rectangle-half"><div class="part shaded"></div><div class="part unshaded"></div></div><p>{shaded} out of {parts} parts shaded</p>'
        elif parts == 4:
            shaded_html = ''.join(['<div class="part shaded"></div>' for _ in range(shaded)])
            unshaded_html = ''.join(['<div class="part unshaded"></div>' for _ in range(parts - shaded)])
            return f'<div class="fraction-visual rectangle-quarter">{shaded_html}{unshaded_html}</div><p>{shaded} out of {parts} parts shaded</p>'
    
    else:  # square
        if parts == 2:
            return f'<div class="fraction-visual square-half"><div class="part shaded"></div><div class="part unshaded"></div></div><p>{shaded} out of {parts} parts shaded</p>'
        elif parts == 4:
            shaded_html = ''.join(['<div class="part shaded"></div>' for _ in range(shaded)])
            unshaded_html = ''.join(['<div class="part unshaded"></div>' for _ in range(parts - shaded)])
            return f'<div class="fraction-visual square-quarter">{shaded_html}{unshaded_html}</div><p>{shaded} out of {parts} parts shaded</p>'

def generate_finding_fractions(difficulty):
    """Generate exercises about finding fractions of amounts"""
    amounts = [4, 6, 8, 10, 12, 16, 20]
    amount = random.choice(amounts)
    
    if difficulty == 1:
        # Find half
        if amount % 2 == 0:  # Make sure amount is even for exact halves
            question = f"What is half of {amount}?"
            correct_answer = str(amount // 2)
            wrong_answers = [str(amount // 4), str(amount), str((amount // 2) + 1)]
            visual_help = f'<div class="fraction-visual finding-fractions"><div class="amount-visual">' + \
                         '●' * amount + '</div><p>Split these into 2 equal groups</p></div>'
        else:
            amount = random.choice([4, 6, 8, 10, 12])  # Ensure even number
            question = f"What is half of {amount}?"
            correct_answer = str(amount // 2)
            wrong_answers = [str(amount // 4), str(amount), str((amount // 2) + 1)]
            visual_help = f'<div class="fraction-visual finding-fractions"><div class="amount-visual">' + \
                         '●' * amount + '</div><p>Split these into 2 equal groups</p></div>'
    else:
        # Find quarter (difficulty 2)
        amount = random.choice([4, 8, 12, 16, 20])  # Ensure divisible by 4
        question = f"What is one quarter (1/4) of {amount}?"
        correct_answer = str(amount // 4)
        wrong_answers = [str(amount // 2), str(amount), str((amount // 4) + 1)]
        visual_help = f'<div class="fraction-visual finding-fractions"><div class="amount-visual">' + \
                     '●' * amount + '</div><p>Split these into 4 equal groups</p></div>'
    
    # Remove duplicates and ensure we have 4 unique options
    options = [correct_answer] + wrong_answers
    options = list(set(options))  # Remove duplicates
    while len(options) < 4:
        options.append(str(random.randint(1, amount)))
    options = list(set(options))[:4]  # Keep only 4 unique options
    random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": visual_help
    }

def generate_2d_shapes(difficulty):
    """Generate 2D shape recognition exercises"""
    shapes = {
        "triangle": "3 sides, 3 corners",
        "square": "4 equal sides, 4 corners",
        "rectangle": "4 sides (opposite sides equal), 4 corners",
        "circle": "round, no corners",
        "pentagon": "5 sides, 5 corners",
        "hexagon": "6 sides, 6 corners"
    }
    
    if difficulty == 1:
        available_shapes = ["triangle", "square", "rectangle", "circle"]
    else:
        available_shapes = list(shapes.keys())
    
    correct_shape = random.choice(available_shapes)
    description = shapes[correct_shape]
    
    question = f"Which shape has {description}?"
    
    options = [correct_shape]
    while len(options) < 4:
        wrong_shape = random.choice(available_shapes)
        if wrong_shape not in options:
            options.append(wrong_shape)
    
    random.shuffle(options)
    
    # Generate contextual hints
    if correct_shape == "triangle":
        hint = f"💡 Think about shapes you see every day! A triangle has 3 sides and 3 corners - like a slice of pizza! 🍕"
    elif correct_shape == "square":
        hint = f"💡 A square has 4 equal sides and 4 corners - like a window or dice! All sides are the same length. 🎲"
    elif correct_shape == "rectangle":
        hint = f"💡 A rectangle has 4 sides and 4 corners, but opposite sides are equal - like a door or book! 📚"
    elif correct_shape == "circle":
        hint = f"💡 A circle is perfectly round with no corners - like a wheel or ball! ⚽"
    elif correct_shape == "pentagon":
        hint = f"💡 A pentagon has 5 sides and 5 corners - like a house shape with a roof! Count the sides carefully."
    else:  # hexagon
        hint = f"💡 A hexagon has 6 sides and 6 corners - like a stop sign! Count each side: 1, 2, 3, 4, 5, 6."
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_shape,
        "hint": hint
    }

def generate_time_reading(difficulty):
    """Generate time reading exercises with clock visuals"""
    hour = random.randint(1, 12)
    
    if difficulty == 1:
        # O'clock times
        minute = 0
        question = f"What time does this clock show?"
        correct_answer = f"{hour} o'clock"
        
        # Generate wrong options
        wrong_options = []
        while len(wrong_options) < 3:
            wrong_hour = random.randint(1, 12)
            wrong_time = f"{wrong_hour} o'clock"
            if wrong_time != correct_answer and wrong_time not in wrong_options:
                wrong_options.append(wrong_time)
        
        # Combine all options
        all_options = [correct_answer] + wrong_options
        
        # Calculate hour hand rotation (30 degrees per hour)
        hour_rotation = (hour % 12) * 30
        minute_rotation = 0
        
        # Create simple clock visual with proper transforms
        visual_help = f'''
        <div class="clock-visual">
            <div class="clock-face">
                <div class="hour-hand" style="transform: translateX(-50%) translateY(-100%) rotate({hour_rotation}deg);"></div>
                <div class="minute-hand" style="transform: translateX(-50%) translateY(-100%) rotate({minute_rotation}deg);"></div>
                <div class="clock-center"></div>
                <div class="clock-numbers">
                    <span class="clock-12">12</span>
                    <span class="clock-3">3</span>
                    <span class="clock-6">6</span>
                    <span class="clock-9">9</span>
                </div>
            </div>
            <p>🕐 The hour hand points to {hour}, minute hand points to 12</p>
        </div>
        '''
    else:
        # Half past times
        minute = 30
        question = f"What time does this clock show?"
        correct_answer = f"half past {hour}"
        
        # Generate wrong options
        wrong_options = []
        while len(wrong_options) < 3:
            wrong_hour = random.randint(1, 12)
            wrong_option = random.choice([f"half past {wrong_hour}", f"{wrong_hour} o'clock"])
            if wrong_option != correct_answer and wrong_option not in wrong_options:
                wrong_options.append(wrong_option)
        
        # Combine all options
        all_options = [correct_answer] + wrong_options
        
        # Calculate rotations: hour hand moves halfway between hours at 30 minutes
        hour_rotation = (hour % 12) * 30 + 15  # Add 15 degrees for half past
        minute_rotation = 180  # 30 minutes = 180 degrees (pointing to 6)
        
        # Create half-past clock visual with proper transforms
        visual_help = f'''
        <div class="clock-visual">
            <div class="clock-face">
                <div class="hour-hand" style="transform: translateX(-50%) translateY(-100%) rotate({hour_rotation}deg);"></div>
                <div class="minute-hand" style="transform: translateX(-50%) translateY(-100%) rotate({minute_rotation}deg);"></div>
                <div class="clock-center"></div>
                <div class="clock-numbers">
                    <span class="clock-12">12</span>
                    <span class="clock-3">3</span>
                    <span class="clock-6">6</span>
                    <span class="clock-9">9</span>
                </div>
            </div>
            <p>🕕 The minute hand points to 6 (30 minutes), hour hand between {hour} and {hour + 1 if hour < 12 else 1}</p>
        </div>
        '''
    
    # Shuffle the options AFTER we've stored the correct answer
    random.shuffle(all_options)
    
    # Generate contextual hints
    if minute == 0:
        hint = f"💡 Look at the short hand (hour hand) - it points to {hour}. When the long hand points to 12, it's 'o'clock'!"
    else:  # minute == 30
        hint = f"💡 The long hand (minute hand) points to 6, which means 30 minutes or 'half past'. The short hand is between {hour} and {hour + 1 if hour < 12 else 1}!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": all_options,
        "correct_answer": correct_answer,  # This stays the same regardless of shuffle
        "visual_help": visual_help,
        "hint": hint
    }

def generate_skip_counting(difficulty):
    """Generate skip counting exercises"""
    if difficulty == 1:
        step = random.choice([2, 5, 10])
        start = step
        length = 5
    else:
        step = random.choice([2, 3, 4, 5, 10])
        start = step * random.randint(1, 3)
        length = 6
    
    sequence = [start + i * step for i in range(length)]
    missing_index = random.randint(1, length - 2)
    missing_number = sequence[missing_index]
    
    sequence_str = [str(x) if i != missing_index else "?" for i, x in enumerate(sequence)]
    
    question = f"What number is missing? Counting in {step}s: {' → '.join(sequence_str)}"
    
    options = [missing_number]
    while len(options) < 4:
        wrong = missing_number + random.choice([-step, step, -step//2, step//2])
        if wrong > 0 and wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    
    # Generate contextual hints
    if step == 2:
        hint = f"💡 Counting by 2s! Start at {start}, add 2 each time: {start}, {start+step}, {start+2*step}... What comes next?"
    elif step == 5:
        hint = f"💡 Counting by 5s! Think of your fingers - each hand has 5 fingers. Count: {start}, {start+step}, {start+2*step}..."
    elif step == 10:
        hint = f"💡 Counting by 10s! This is easy - just add 10 each time: {start}, {start+step}, {start+2*step}..."
    else:
        hint = f"💡 You're counting by {step}s! Add {step} each time. What number comes before and after the missing spot?"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": missing_number,
        "visual_help": f"Count in steps of {step}",
        "hint": hint
    }

def generate_simple_division(difficulty):
    """Generate simple division exercises using sharing/grouping"""
    if difficulty == 1:
        # Simple division with small numbers
        divisors = [2, 3, 4, 5]
        divisor = random.choice(divisors)
        quotient = random.randint(1, 4)
        dividend = divisor * quotient
    else:
        # Slightly larger numbers
        divisors = [2, 3, 4, 5, 6, 10]
        divisor = random.choice(divisors)
        quotient = random.randint(1, 6)
        dividend = divisor * quotient
    
    question = f"Share {dividend} equally among {divisor} groups. How many in each group?"
    correct_answer = quotient
    
    options = [correct_answer]
    while len(options) < 4:
        wrong = correct_answer + random.randint(-2, 2)
        if wrong > 0 and wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    
    # Generate contextual hints
    hint = f"💡 Think: you have {dividend} items to share fairly among {divisor} groups. Try drawing {divisor} circles and putting one item in each circle at a time until all items are shared!"
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": f"Draw {divisor} groups and share {dividend} items equally",
        "hint": hint
    }

def generate_length_height(difficulty):
    """Generate length and height measurement exercises with visual representations"""
    if difficulty == 1:
        # Simple comparisons with visual objects
        objects_data = {
            "finger": {"height": 8, "emoji": "👆", "description": "finger"},
            "pencil": {"height": 15, "emoji": "✏️", "description": "pencil"}, 
            "book": {"height": 25, "emoji": "📚", "description": "book"},
            "desk": {"height": 75, "emoji": "🪑", "description": "desk"},
            "door": {"height": 200, "emoji": "🚪", "description": "door"}
        }
        
        obj1, obj2 = random.sample(list(objects_data.keys()), 2)
        obj1_data = objects_data[obj1]
        obj2_data = objects_data[obj2]
        
        # Create visual comparison
        visual_html = f"""
        <div class="measurement-comparison">
            <div class="object-display">
                <div class="object-item">
                    <div class="object-visual" style="height: 180px; width: 120px; background: linear-gradient(45deg, #4CAF50, #45a049); display: flex; align-items: center; justify-content: center; font-size: 32px; color: white; border-radius: 5px; margin: 5px; position: relative;">
                        {obj1_data['emoji']}
                        <div style="position: absolute; bottom: 5px; right: 5px; background: rgba(0,0,0,0.7); color: white; padding: 2px 6px; border-radius: 3px; font-size: 12px; font-weight: bold;">
                            {obj1_data['height']}cm
                        </div>
                    </div>
                    <div class="object-label">{obj1_data['description']}</div>
                </div>
                <div class="vs-separator">VS</div>
                <div class="object-item">
                    <div class="object-visual" style="height: 180px; width: 120px; background: linear-gradient(45deg, #2196F3, #1976D2); display: flex; align-items: center; justify-content: center; font-size: 32px; color: white; border-radius: 5px; margin: 5px; position: relative;">
                        {obj2_data['emoji']}
                        <div style="position: absolute; bottom: 5px; right: 5px; background: rgba(0,0,0,0.7); color: white; padding: 2px 6px; border-radius: 3px; font-size: 12px; font-weight: bold;">
                            {obj2_data['height']}cm
                        </div>
                    </div>
                    <div class="object-label">{obj2_data['description']}</div>
                </div>
            </div>
        </div>
        """
        
        if obj1_data['height'] > obj2_data['height']:
            question = f"Which is longer/taller?"
            correct_answer = obj1
            options = [obj1, obj2, "they are the same", "cannot tell"]
        else:
            question = f"Which is longer/taller?"
            correct_answer = obj2
            options = [obj1, obj2, "they are the same", "cannot tell"]
            
    else:
        # Measuring with ruler visualization
        length = random.randint(5, 25)
        unit = random.choice(["cm", "inches"])
        
        # Create ruler visual
        visual_html = f"""
        <div class="ruler-measurement">
            <div class="ruler">
                <div class="ruler-scale">
                    {''.join([f'<div class="ruler-mark" style="left: {i*15}px;"><span>{i}</span></div>' for i in range(0, min(length+5, 30))])}
                </div>
                <div class="measured-object" style="width: {length*15}px; background: linear-gradient(45deg, #FF9800, #F57C00); height: 20px; margin-top: 30px; border-radius: 3px; position: relative;">
                    <span style="position: absolute; top: 25px; left: 50%; transform: translateX(-50%); font-weight: bold;">📏 Object</span>
                </div>
            </div>
            <div class="ruler-label">Ruler showing measurement in {unit}</div>
        </div>
        """
        
        question = f"Look at the ruler. How long is the object?"
        correct_answer = f"{length} {unit}"
        
        options = [correct_answer]
        while len(options) < 4:
            wrong_length = length + random.randint(-3, 3)
            if wrong_length > 0 and wrong_length != length:
                option = f"{wrong_length} {unit}"
                if option not in options:
                    options.append(option)
        
        random.shuffle(options)
    
    return {
        'question': question,
        'options': options,
        'correct_answer': correct_answer,
        'visual_html': visual_html,
        'difficulty': difficulty
    }


def generate_mass_weight(difficulty):
    """Generate mass and weight measurement exercises with visual representations"""
    if difficulty == 1:
        # Simple comparisons with visual objects
        objects_data = {
            "feather": {"weight": 1, "emoji": "🪶", "description": "feather", "color": "#E8F5E8"},
            "apple": {"weight": 3, "emoji": "🍎", "description": "apple", "color": "#FFE8E8"}, 
            "book": {"weight": 5, "emoji": "📚", "description": "book", "color": "#E8E8FF"},
            "cat": {"weight": 8, "emoji": "🐱", "description": "cat", "color": "#FFF8E8"},
            "car": {"weight": 10, "emoji": "🚗", "description": "car", "color": "#F0E8FF"}
        }
        
        obj1, obj2 = random.sample(list(objects_data.keys()), 2)
        obj1_data = objects_data[obj1]
        obj2_data = objects_data[obj2]
        
        # Create visual scale comparison
        visual_html = f"""
        <div class="weight-comparison">
            <div class="balance-scale">
                <div class="scale-arm"></div>
                <div class="scale-left" style="transform: rotate({(obj2_data['weight'] - obj1_data['weight']) * 2}deg);">
                    <div class="scale-plate" style="background: {obj1_data['color']};">
                        <div class="object-on-scale">
                            <span style="font-size: 2em;">{obj1_data['emoji']}</span>
                            <div class="object-label">{obj1_data['description']}</div>
                        </div>
                    </div>
                </div>
                <div class="scale-right" style="transform: rotate({(obj1_data['weight'] - obj2_data['weight']) * 2}deg);">
                    <div class="scale-plate" style="background: {obj2_data['color']};">
                        <div class="object-on-scale">
                            <span style="font-size: 2em;">{obj2_data['emoji']}</span>
                            <div class="object-label">{obj2_data['description']}</div>
                        </div>
                    </div>
                </div>
                <div class="scale-base">⚖️</div>
            </div>
        </div>
        """
        
        if obj1_data['weight'] > obj2_data['weight']:
            question = f"Which is heavier?"
            correct_answer = obj1
        else:
            question = f"Which is heavier?"
            correct_answer = obj2
        
        options = [obj1, obj2, "they weigh the same", "cannot tell"]
        
    else:
        # Weight measurements with scale visual
        weight = random.randint(1, 10)
        unit = random.choice(["kg", "pounds"])
        
        # Create digital scale visual
        visual_html = f"""
        <div class="digital-scale">
            <div class="scale-display">
                <div class="scale-screen">
                    <div class="weight-reading">{weight} {unit}</div>
                </div>
                <div class="scale-platform">
                    <div class="mystery-object">📦</div>
                </div>
            </div>
            <div class="scale-label">Digital Scale Reading</div>
        </div>
        """
        
        question = f"Look at the scale reading. What does the object weigh?"
        correct_answer = f"{weight} {unit}"
        
        options = [correct_answer]
        while len(options) < 4:
            wrong_weight = weight + random.randint(-2, 2)
            wrong_answer = f"{wrong_weight} {unit}"
            if wrong_weight > 0 and wrong_answer not in options:
                options.append(wrong_answer)
        
        random.shuffle(options)
    
    return {
        'question': question,
        'options': options,
        'correct_answer': correct_answer,
        'visual_html': visual_html,
        'difficulty': difficulty
    }

def generate_temperature(difficulty):
    """Generate temperature measurement exercises"""
    if difficulty == 1:
        # Simple temperature comparisons
        situations = {
            "ice cream": "cold",
            "hot soup": "hot", 
            "snow": "cold",
            "summer day": "hot",
            "winter day": "cold",
            "oven": "hot"
        }
        
        situation = random.choice(list(situations.keys()))
        correct_answer = situations[situation]
        
        question = f"Is {situation} usually hot or cold?"
        options = ["hot", "cold", "warm", "freezing"]
    else:
        # Simple temperature reading
        temp = random.randint(0, 40)
        unit = "°C"
        question = f"The thermometer shows {temp}{unit}. What is the temperature?"
        correct_answer = f"{temp}{unit}"
        
        options = [correct_answer]
        while len(options) < 4:
            wrong_temp = temp + random.randint(-5, 5)
            wrong_answer = f"{wrong_temp}{unit}"
            if wrong_answer not in options:
                options.append(wrong_answer)
        
        random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": "🌡️ Think about temperature in everyday situations"
    }

def generate_3d_shapes(difficulty):
    """Generate 3D shape recognition exercises"""
    shapes = {
        "cube": "6 square faces, 8 corners, 12 edges",
        "sphere": "round ball shape, no corners or edges",
        "cylinder": "circular ends, curved surface",
        "cone": "circular base, pointed top",
        "pyramid": "triangular faces meeting at a point"
    }
    
    if difficulty == 1:
        available_shapes = ["cube", "sphere", "cylinder"]
    else:
        available_shapes = list(shapes.keys())
    
    correct_shape = random.choice(available_shapes)
    description = shapes[correct_shape]
    
    question = f"Which 3D shape has {description}?"
    
    options = [correct_shape]
    while len(options) < 4:
        wrong_shape = random.choice(available_shapes)
        if wrong_shape not in options:
            options.append(wrong_shape)
    
    random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_shape,
        "visual_help": "🎲 Think about everyday objects with these shapes"
    }

def generate_position_direction(difficulty):
    """Generate position and direction exercises"""
    if difficulty == 1:
        # Simple position words
        positions = ["above", "below", "left", "right", "in front of", "behind"]
        objects = ["the box", "the table", "the chair", "the door"]
        
        position = random.choice(positions)
        obj = random.choice(objects)
        
        question = f"Where is the cat? The cat is {position} {obj}."
        correct_answer = position
        
        # Create realistic wrong options
        wrong_positions = [p for p in positions if p != position]
        options = [position] + random.sample(wrong_positions, 3)
        random.shuffle(options)
    else:
        # Directions (left/right, clockwise)
        directions = ["left", "right", "forward", "backward"]
        direction = random.choice(directions)
        
        question = f"If you face north and turn {direction}, which way are you facing?"
        
        compass = {"north": 0, "east": 1, "south": 2, "west": 3}
        current = 0  # north
        
        if direction == "right":
            new_direction = (current + 1) % 4
        elif direction == "left":
            new_direction = (current - 1) % 4
        else:
            new_direction = current
        
        direction_names = ["north", "east", "south", "west"]
        correct_answer = direction_names[new_direction]
        
        options = direction_names.copy()
        random.shuffle(options)
    
    return {
        "type": "multiple_choice",
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "visual_help": "🧭 Use your hands to help figure out directions"
    }

def generate_default_exercise(difficulty):
    """Default exercise when specific type not found"""
    return {
        "type": "multiple_choice",
        "question": "What is 2 + 2?",
        "options": [4, 3, 5, 6],
        "correct_answer": 4,
        "visual_help": "Count on your fingers!"
    }