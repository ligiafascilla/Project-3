document.addEventListener('DOMContentLoaded', function() {
    loadDropdownValues('year-select', '/api/years');
    loadDropdownValues('country-select', '/api/countries');
    loadDropdownValues('type-select', '/api/types');
});

function loadDropdownValues(selectId, apiUrl) {
    var select = document.getElementById(selectId);

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            data.forEach(value => {
                var option = document.createElement('option');
                option.value = value;
                option.text = value;
                select.appendChild(option);
            });
        });
}

function filterData() {
    var Year = document.getElementById('year-select').value;
    var Country = document.getElementById('country-select').value;
    var Type = document.getElementById('type-select').value;
    var filteredResults = document.getElementById('filtered-results');

    // Make an AJAX request to Flask with the selected filters
    fetch('/api/filter?Year=' + year + '&Country=' + country + '&Type=' + type)
        .then(response => response.json())
        .then(data => {
            // Clear previous results
            filteredResults.innerHTML = '';

            // Display filtered results
            data.forEach(result => {
                var div = document.createElement('div');
                div.textContent = JSON.stringify(result);
                filteredResults.appendChild(div);
            });
        });
}


