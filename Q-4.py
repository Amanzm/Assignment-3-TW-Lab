# Function to compute gross salary
def calculate_gross_salary(basic, grade):
    # Constants
    HRA_PERCENTAGE = 0.20
    DA_PERCENTAGE = 0.50
    ALLOWANCES = {'A': 1700, 'B': 1500, 'C': 1300}
    PF_PERCENTAGE = 0.11

    # Calculate HRA, DA, Allowance, and PF
    hra = basic * HRA_PERCENTAGE
    da = basic * DA_PERCENTAGE
    allowance = ALLOWANCES.get(grade, 0)
    pf = basic * PF_PERCENTAGE

    # Calculate Gross Salary
    gross_salary = basic + hra + da + allowance - pf

    return gross_salary

# Example (A)
basic_A = 10000
grade_A = 'A'
gross_salary_A = calculate_gross_salary(basic_A, grade_A)
print(f"Gross Salary (Grade A): {gross_salary_A}")

# Example (B)
basic_B = 4567
grade_B = 'B'
gross_salary_B = calculate_gross_salary(basic_B, grade_B)
print(f"Gross Salary (Grade B): {gross_salary_B}")
