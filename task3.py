import re

def assess_password_strength(password):
    # Criteria
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_number = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Check length
    length_valid = len(password) >= min_length
    
    # Assessing strength
    if all([length_valid, has_uppercase, has_lowercase, has_number, has_special]):
        strength = "Strong"
    elif any([length_valid, has_uppercase, has_lowercase, has_number, has_special]):
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Feedback
    feedback = []
    if not length_valid:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if not has_uppercase:
        feedback.append("Password should contain at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password should contain at least one lowercase letter.")
    if not has_number:
        feedback.append("Password should contain at least one number.")
    if not has_special:
        feedback.append("Password should contain at least one special character.")
    
    return strength, feedback

def main():
    password = input("Enter the password to assess: ").strip()
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for line in feedback:
            print(f"- {line}")

if __name__ == "__main__":
    main()
