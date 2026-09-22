# Agentic AI: Foundations and Open-Source Practice

## Project: College Fee Assistance System

### Scenario
The project uses private course-fee information:
- CS101: ₹12,000
- AI202: ₹18,000
- DS303: ₹15,000

The same type of user request is demonstrated using:
1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

### Plain Chatbot
The plain chatbot generates natural-language responses but does not directly access the private fee database.

### Rule-Based Workflow
The rule-based system uses predefined Python functions and conditions to retrieve course fees and calculate scholarship amounts. Its execution is predictable because the steps are fixed.

### AI Agent
The agent demonstrates:

**Agent = LLM + Tools + Loop**

Tools:
- `get_course_fee`
- `calculator`

Example:
For CS101 and AI202 with a 10% scholarship:

(12000 + 18000) × 0.90 = ₹27,000

The program demonstrates the sequence:
1. Get CS101 fee.
2. Get AI202 fee.
3. Use the calculator.
4. Generate the final response.

### How to Run

Save `college_fee_assistance_agent.py` and run:

```bash
python college_fee_assistance_agent.py
```

Choose:
- `1` for Plain Chatbot
- `2` for Rule-Based Workflow
- `3` for AI Agent
- `4` to Exit

### Important Note
This implementation is a local educational demonstration. The AI-agent decision step is simulated in Python so that the project can run without an external LLM API key. A real LLM-based version would connect an LLM to the same tools and allow the model to select tool calls dynamically.
