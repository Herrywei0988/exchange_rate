async function convert() {
    // Get input values from the form
    const from = document.getElementById("from").value;
    const to = document.getElementById("to").value;
    const amount = document.getElementById("amount").value;
  
    // Optional: handle date if needed later
    // const date = document.getElementById("date").value;
  
    // Send request to Flask backend
    const response = await fetch(`/convert?from=${from}&to=${to}&amount=${amount}`);
    const data = await response.json();
  
    const resultDiv = document.getElementById("result");
    
    if (data.error) {
        resultDiv.innerText = `Error: ${data.error}`;
        resultDiv.style.display = "block";
      } else {
        resultDiv.innerText = `${amount} ${from} = ${data.converted_amount} ${to} (Rate: ${data.rate})`;
        resultDiv.style.display = "block";
      }
  }

  // Sample data: historical exchange rate for USD to JPY
const mockLabels = ["2024-04-01", "2024-04-02", "2024-04-03", "2024-04-04", "2024-04-05"];
const mockData = [148.2, 147.8, 148.5, 149.1, 148.9];

function drawChart(labels, data, currency) {
  const ctx = document.getElementById("rateChart").getContext("2d");

  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: `USD to ${currency}`,
        data: data,
        borderColor: "#007bff",
        fill: false,
        tension: 0.2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true },
        tooltip: { enabled: true }
      },
      scales: {
        x: { display: true, title: { display: true, text: 'Date' } },
        y: { display: true, title: { display: true, text: 'Rate' } }
      }
    }
  });
}

// Draw chart after conversion
async function convert() {
  const from = "USD";
  const to = document.getElementById("to").value;
  const amount = document.getElementById("amount").value;

  const response = await fetch(`/convert?from=${from}&to=${to}&amount=${amount}`);
  const data = await response.json();

  const resultDiv = document.getElementById("result");
  if (data.error) {
    resultDiv.innerText = `Error: ${data.error}`;
    resultDiv.style.display = "block";
  } else {
    resultDiv.innerText = `${amount} ${from} = ${data.converted_amount} ${to} (Rate: ${data.rate})`;
    resultDiv.style.display = "block";

    // Show mock chart for selected currency
    drawChart(mockLabels, mockData, to);
  }
}
  