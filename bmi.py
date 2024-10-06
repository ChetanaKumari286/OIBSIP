def calculate_bmi(height,weight):
    bmi = weight / (height ** 2)
    return bmi

def categorize(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(height,weight)
        category = categorize(bmi)

        print("\nYour BMI is:",bmi)
        print("Category:",category)

if __name__ == "__main__":
    main()