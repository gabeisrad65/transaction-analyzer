const startingBalance = 2450.00;

let transactions = [
  { amount: 749.17, category: "Investment Return" },
  { amount: -11.54, category: "Utilities" },
  { amount: -247.58, category: "Online Shopping" },
  { amount: 981.17, category: "Investment Return" },
  { amount: -410.65, category: "Rent" },
  { amount: 310.60, category: "Rent Refund" },
  { amount: 563.70, category: "Gift" },
  { amount: 220.79, category: "Salary" },
  { amount: -49.85, category: "Car Maintenance" },
  { amount: 308.49, category: "Salary" },
  { amount: -205.55, category: "Car Maintenance" },
  { amount: 870.64, category: "Salary" },
  { amount: -881.51, category: "Utilities" },
  { amount: 518.14, category: "Salary" },
  { amount: -264.66, category: "Groceries" }
];

function money(value) {
  return value.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
  });
}

function renderDashboard() {
  const balance = startingBalance + transactions.reduce((sum, item) => sum + item.amount, 0);
  const income = transactions
    .filter(item => item.amount > 0)
    .reduce((sum, item) => sum + item.amount, 0);

  const expenses = transactions
    .filter(item => item.amount < 0)
    .reduce((sum, item) => sum + item.amount, 0);

  document.getElementById("balance").textContent = money(balance);
  document.getElementById("income").textContent = money(income);
  document.getElementById("expenses").textContent = money(Math.abs(expenses));
  document.getElementById("count").textContent = transactions.length;

  const container = document.getElementById("transactions");
  container.innerHTML = "";

  transactions.forEach((item, index) => {
    const type = item.amount > 0 ? "Deposit" : "Withdrawal";

    const row = document.createElement("div");
    row.className = "transaction";
    row.style.animationDelay = `${index * 0.05}s`;

    row.innerHTML = `
      <strong>${item.category}</strong>
      <span class="${item.amount > 0 ? "deposit" : "withdrawal"}">${money(item.amount)}</span>
      <span class="tag">${type}</span>
    `;

    container.appendChild(row);
  });
}

function shuffleTransactions() {
  transactions = [...transactions].sort(() => Math.random() - 0.5);
  renderDashboard();
}

renderDashboard();