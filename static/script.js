// Your JavaScript code here
document.addEventListener('DOMContentLoaded', function () {
    const calculatorForm = document.getElementById('calculator-form');
    const resultElement = document.getElementById('result');

    calculatorForm.addEventListener('submit', async function (e) {
        e.preventDefault();

        const input1 = parseFloat(document.getElementById('input1').value);
        const input2 = parseFloat(document.getElementById('input2').value);
        const operator = document.getElementById('operator').value;

        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ num1: input1, num2: input2, operator: operator })
        });

        const data = await response.json();
        resultElement.textContent = `Result: ${data.result}`;
    });
});


