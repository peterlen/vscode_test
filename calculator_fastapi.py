
from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# **** TO RUN THIS: python -m uvicorn calculator_fastapi:app --reload

app = FastAPI(title="Simple Calculator")


class Calculation(BaseModel):
        first_number: float
        operation: Literal["add", "subtract", "multiply", "divide"]
        second_number: float


@app.get("/", response_class=HTMLResponse)
def calculator_page() -> str:
        return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Simple Calculator</title>
    <style>
        body { background: beige; max-width: 28rem; margin: 3rem auto; padding: 0 1rem; font: 1rem system-ui, sans-serif; }
        form { display: grid; gap: 1rem; }
        input, select, button { box-sizing: border-box; width: 100%; padding: .7rem; font: inherit; }
        #result { min-height: 1.5rem; font-weight: 600; }
    </style>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form id="calculator">
        <label>First number <input name="first_number" type="number" step="any" required></label>
        <label>Operation
            <select name="operation">
                <option value="add">Add (+)</option>
                <option value="subtract">Subtract (-)</option>
                <option value="multiply">Multiply (×)</option>
                <option value="divide">Divide (÷)</option>
            </select>
        </label>
        <label>Second number <input name="second_number" type="number" step="any" required></label>
        <button type="submit">Calculate</button>
    </form>
    <p id="result" role="status" aria-live="polite"></p>
    <script>
        const form = document.querySelector("#calculator");
        const result = document.querySelector("#result");
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            const values = Object.fromEntries(new FormData(form));
            values.first_number = Number(values.first_number);
            values.second_number = Number(values.second_number);
            const response = await fetch("/calculate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(values)
            });
            const data = await response.json();
            result.textContent = response.ok ? `Result: ${data.result}` : data.detail;
        });
    </script>
</body>
</html>"""


@app.post("/calculate")
def calculate(calculation: Calculation) -> dict[str, float]:
        first = calculation.first_number
        second = calculation.second_number

        if calculation.operation == "add":
                result = first + second
        elif calculation.operation == "subtract":
                result = first - second
        elif calculation.operation == "multiply":
                result = first * second
        else:
                if second == 0:
                        raise HTTPException(status_code=400, detail="Cannot divide by zero")
                result = first / second

        return {"result": result}