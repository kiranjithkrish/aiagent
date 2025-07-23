class Calculator:
    def evaluate(self, expression):
        return self.calculate(expression)

    def calculate(self, expression):
        parts = expression.split()
        print(f"Initial parts: {parts}")

        # Handle multiplication first
        i = 1
        while i < len(parts) - 1 and len(parts) > 2:
            print(f"Before multiplication check: i={i}, parts={parts}")
            if parts[i] == '*':
                num1 = float(parts[i-1])
                num2 = float(parts[i+1])
                result = num1 * num2
                parts = parts[:i-1] + [str(result)] + parts[i+2:]
                print(f"Multiplication performed: result={result}, parts={parts}")
                if len(parts) <= 2:
                    break
                i = 1  # Reset index to start from beginning
            else:
                i += 2
            print(f"After iteration: i={i}, parts={parts}")

        # Handle addition and subtraction
        result = float(parts[0])
        i = 1
        while i < len(parts) - 1:
            if parts[i] == '+':
                result += float(parts[i+1])
            elif parts[i] == '-':
                result -= float(parts[i+1])
            i += 2
        return result


# Get user input
expression = input("Enter expression (e.g., 3 + 7 * 2): ")

# Perform calculation
calculator = Calculator()
result = calculator.evaluate(expression)

# Print the result
print("Result:", result)

# Test case
calculator = Calculator()
test_expression = "3 + 7 * 2"
test_result = calculator.evaluate(test_expression)
assert test_result == 17, f"Test failed: Expected 17, got {test_result}"
print("Test passed!")