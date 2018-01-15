var $tbody = document.querySelector("tbody");
var $stateInput = document.querySelector("#state");
var $searchBtn = document.querySelector("#search");
var $cityInput = document.querySelector("#city");

var $dateInput = document.querySelector("#date");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");


// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
// Set filteredalienes to alienData initially
//dataSetSmall=dataSet[0,10]
//console.log(dataSetSmall)
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
  var filterState = $stateInput.value.trim().toLowerCase();
  // Set filteredAddresses to an array of all addresses whose "state" matches the filter
  if (filterState !== "") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienState = alien.state.toLowerCase();
    // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
    return alienState === filterState;
  }); }
   
  var filterShape = $shapeInput.value.trim().toLowerCase();
  if (filterShape !== "") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienShape = alien.shape.toLowerCase();
    return alienShape === filterShape;
  }); }

  var filterCity = $cityInput.value.trim().toLowerCase();
  if (filterCity !== "") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienCity = alien.city.toLowerCase();
    return alienCity === filterCity;
  }); }

  var filterCountry = $countryInput.value.trim().toLowerCase();
  if (filterCountry !== "") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienCountry = alien.country.toLowerCase();
    return alienCountry === filterCountry;
  }); }

  var filterDate = Date.parse($dateInput.value);
  if (filterDate !== "") {
  filteredAliens = dataSet.filter(function(alien) {
    var alienDate = Date.parse(alien.datetime);
    console.log(alienDate);
    console.log(filterDate);
    return alienDate === filterDate;
  }); }


  renderTable();
}
// Render the table for the first time on page load
renderTable();