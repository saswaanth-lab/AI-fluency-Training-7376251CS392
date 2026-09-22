
"""Tools for the college fee assistant."""

import ast
import operator


# Course fee database
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


# Tool 1: Get course fee
def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        return f"{course_code} fee is Rs. {COURSE_FEES[course_code]}"

    return f"Course {course_code} not found."


# Tool 2: Safe calculator
def calculator(expression):
    try:
        tree = ast.parse(expression, mode="eval")

        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

        def evaluate(node):
            if isinstance(node, ast.Expression):
                return evaluate(node.body)

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Invalid number")

            if isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)
                operation = allowed_operators.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not allowed")

                return operation(left, right)

            raise ValueError("Invalid expression")

        result = evaluate(tree)
        return str(result)

    except Exception as error:
        return f"Calculation error: {error}"


# Tool 3: Find course combinations within budget
def find_course_combinations(budget):
    courses = {
        "CS101": 12000,
        "AI202": 18000,
        "DS303": 15000
    }

    results = []
    course_codes = list(courses.keys())

    for i in range(len(course_codes)):
        for j in range(i + 1, len(course_codes)):

            course1 = course_codes[i]
            course2 = course_codes[j]

            total = courses[course1] + courses[course2]

            if total <= budget:
                results.append(
                    f"{course1} + {course2} = Rs. {total}"
                )

    if results:
        return "\n".join(results)

    return "No course combination found within this budget."


# Python functions available to the agent
TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee,
    "calculator": calculator,
    "find_course_combinations": find_course_combinations
}


# Tool descriptions for the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303."
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression such as 12000+18000."
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_course_combinations",
            "description": "Find all pairs of courses whose combined fees are within a given budget.",
            "parameters": {
                "type": "object",
                "properties": {
                    "budget": {
                        "type": "number",
                        "description": "Maximum total budget in rupees."
                    }
                },
                "required": ["budget"]
            }
        }
    }
]