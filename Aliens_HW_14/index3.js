// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $stateInput = document.querySelector("#state");
var $searchBtn = document.querySelector("#search");
var $cityInput = document.querySelector("#city");

var $dateInput = document.querySelector("#date");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
//var $durationInput = document.querySelector("#duration");


// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
// Set filteredalienes to alienData initially
var filteredAliens = dataSet;
//console.log(filteredAliens)
// renderTable renders the filteredalienes to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredAliens.length; i++) {
    // Get get the current alien object and its fields
    var alien = filteredAliens[i];
    var fields = Object.keys(alien);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the alien object, create a new cell at set its inner text to be the current value at the current alien's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = alien[field];
    }
  }
  console.log(filteredAliens)
}
function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  // Set filteredalienes to an array of all alienes whose "state" matches the filter
  var filterShape = $shapeInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterDate = $dateInput.value.trim().toLowerCase();

  if (filterState !=="") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienState = alien.state.toLowerCase();
    var filterState = $stateInput.value.trim().toLowerCase();
    return alienState === filterState;
  }); }
    if (filterCity !=="") {
    filteredAliens = filteredAliens.filter(function(alien) {
    var filterCity = $cityInput.value.trim().toLowerCase();
    var alienCity = alien.city.toLowerCase();
    return alienCity === filterCity;
  }) };
    if (filterShape !=="") {
    filteredAliens = filteredAliens.filter(function(alien) {
      var filterShape = $shapeInput.value.trim().toLowerCase();
      var alienShape = alien.shape.toLowerCase();
      return alienShape === filterShape;
      
  })  }; 
    if (isNaN(filterDate)) {
    filteredAliens = filteredAliens.filter(function(alien) {
      var filterDate = Date.parse($dateInput.value);
      var alienDate = Date.parse(alien.datetime);
      return alienDate === filterDate;
  }); }


  renderTable();
}
// Render the table for the first time on page load
renderTable();



