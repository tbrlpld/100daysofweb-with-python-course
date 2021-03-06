const foodBalanceWrapper = document.getElementById("foodBalanceWrapper")
foodBalanceWrapper.style.display = "none";

// provided: vanilla JS autocomplete
// https://goodies.pixabay.com/javascript/auto-complete/demo.html
new autoComplete({
  selector: 'input[name="foodPicker"]',
  minChars: 2,
  source: function(term, suggest){
    term = term.toLowerCase();
    let choices = Object.keys(foodDb);  // defined in food.js
    let matches = [];
    for(i=0; i<choices.length; i++){
      let kcal = foodDb[choices[i]];
      if(kcal == 0){
        continue;
      }

      if(~choices[i].toLowerCase().indexOf(term)){
        let item = `${choices[i]} (${kcal} kcal)`;
        matches.push(item);
      }
    }
    suggest(matches);
  }
});


// provided: handle form submission to not do it as inline JS
// https://stackoverflow.com/a/5384732
function processForm(e) {
    if (e.preventDefault) e.preventDefault();
    updateFoodLog();
    return false;
}
var form = document.getElementById('foodPickerForm');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}


// helpers
function recalculateTotal(){
  // get all table cells (tds) and sum the calories = td with kcal
  let kcalElements = document.getElementsByClassName("kcal");
  total = 0;
  for (item of kcalElements) {
    total += parseFloat(item.innerHTML);
  }
  return total;
}

function updateTotalKcal(){
  // write the total kcal count into  the total id, if 0 hide the
  // foodBalanceWrapper div
  let total = recalculateTotal();
  console.log(total);
  if (total === 0) {
    foodBalanceWrapper.style.display = "none";
  } else {
    foodBalanceWrapper.style.display = "initial";
  }
  let totalElement = document.getElementById("total");
  totalElement.innerHTML = total;
}

function emptyFoodPicker(){
  // reset the foodPicker ID value
  let foodPicker = document.getElementById("foodPicker");
  foodPicker.value = "";
}

function removeRow(event){
  // remove a table row and update the total kcal
  // https://stackoverflow.com/a/53085148
  console.log("clicked delete button");
  let deleteButton = event.target
  console.log(deleteButton);
  let rowOfClickedButton = deleteButton.parentElement.parentElement;
  rowOfClickedButton.remove();
  updateTotalKcal();
}

function removeCalFromName(fullString) {
  // The input values also include the calories. This is different from the keys
  // in the foodDb. Here I am removing everything after the last "]".
  let bracketIndex = fullString.lastIndexOf("]");
  return fullString.substring(0, bracketIndex + 1);
}

function addFoodRowToTable() {
  let food =  document.getElementById("foodPicker").value;
  console.log(food)

  parsedFood = removeCalFromName(food);
  console.log(parsedFood);
  let calories = foodDb[parsedFood];
  if (calories === undefined) {
    alert("Unknown food! Please select an available option.");
  } else {
    let newNameCell = document.createElement("td");
    newNameCell.innerHTML = parsedFood;
    let newCalorieCell = document.createElement("td");
    newCalorieCell.innerHTML = calories;
    newCalorieCell.classList.add('kcal')

    let newRowDeleteButton = document.createElement("input");
    newRowDeleteButton.type = "button";
    newRowDeleteButton.className = "delete";
    newRowDeleteButton.addEventListener("click", removeRow);
    let newRowDeleteCell = document.createElement("td");
    newRowDeleteCell.appendChild(newRowDeleteButton);

    let newRow = document.createElement("tr");
    newRow.appendChild(newNameCell);
    newRow.appendChild(newCalorieCell);
    newRow.appendChild(newRowDeleteCell);

    let foodBalanceBody = document.getElementById("foodBalanceBody");
    foodBalanceBody.appendChild(newRow);

    return newRow
  }
}

function updateFoodLog(){
  // udate the food table with the new food, building up the inner dom
  // elements, including adding a delete button / onclick handler
  // finally call updateTotalKcal and emptyFoodPicker
  let newRow = addFoodRowToTable();
  updateTotalKcal();
  emptyFoodPicker();
}


