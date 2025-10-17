// Function 1: Simple function that doesn't return anything
function greetUser(name) {
  console.log("Hello, " + name + "! Welcome to modern world.");
}

// Function 2: Function that returns something
function addNumbers(a, b) {
  return a + b;
}

// Function 3: Function with parameters and default values
function calculateTotal(price, quantity = 1, discount = 0) {
  let total = price * quantity;
  total = total - discount;
  return total;
}

// Function 4: Function mixing both returning and console output
function showCartSummary(item, price, quantity = 1) {
  let total = price * quantity;
  console.log(`You bought ${quantity} ${item}(s) for a total of $${total}.`);
  return total;
}

// Calling the functions to test them
greetUser("Pavan");
console.log("Sum:", addNumbers(5, 7));
console.log("Total Price:", calculateTotal(100, 2, 10));
showCartSummary("Book", 150, 3);
