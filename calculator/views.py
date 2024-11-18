from django.shortcuts import render
from .models import Calculation

def basic_calculator(request):
    result = None
    error_message = None
    if request.method == 'POST':
        try:
            # Retrieve input values and operation
            num1 = request.POST.get('num1', '').strip()
            num2 = request.POST.get('num2', '').strip()
            operation = request.POST.get('operation', '')

            # Validate operation
            if not operation:
                raise ValueError("No operation selected.")

            # Validate input for operations that require two numbers
            if operation != "sqrt":
                if not num1 or not num2:
                    raise ValueError("Both numbers are required.")
                num1 = float(num1)
                num2 = float(num2)

            # Validate input for square root operation
            elif operation == "sqrt":
                if not num1:
                    raise ValueError("Number is required for square root.")
                num1 = float(num1)

            # Perform operations
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Division by zero is not allowed.")
                result = num1 / num2
            elif operation == "sqrt":
                if num1 < 0:
                    raise ValueError("Cannot calculate the square root of a negative number.")
                result = num1 ** 0.5
            elif operation == "percent":
                if num2 == 0:
                    raise ValueError("Cannot calculate percentage with a denominator of zero.")
                result = (num1 / num2) * 100
            else:
                raise ValueError("Invalid operation selected.")
        except ValueError as e:
            error_message = str(e)

    return render(request, 'calculator/basic.html', {'result': result, 'error_message': error_message})
