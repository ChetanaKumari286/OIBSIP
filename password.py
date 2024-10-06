import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    char_set = ''
    selected_char_types = []
    
    if use_upper:
        char_set += string.ascii_uppercase
        selected_char_types.append(random.choice(string.ascii_uppercase))
        
    if use_lower:
        char_set += string.ascii_lowercase
        selected_char_types.append(random.choice(string.ascii_lowercase))
        
    if use_digits:
        char_set += string.digits
        selected_char_types.append(random.choice(string.digits))
        
    if use_symbols:
        char_set += string.punctuation
        selected_char_types.append(random.choice(string.punctuation))

    if char_set == '':
        raise ValueError("At least one character type must be selected!")

    password = selected_char_types + [random.choice(char_set) for _ in range(length - len(selected_char_types))]
    
    random.shuffle(password)
    
    return ''.join(password)

try:
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print("Generated Password:", password)

except ValueError as e:
    print("Error:", e)
