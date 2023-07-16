document.addEventListener('DOMContentLoaded', function() {
    loadDropdownValues('year-select', '/api/years');
    loadDropdownValues('activity-select', '/api/activities');
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
    var year = document.getElementById('year-select').value;
    var activity = document.getElementById('activity-select').value;
    var filteredResults = document.getElementById('filtered-results');

    // Make an AJAX request to Flask with the selected filters
    fetch('/api/filter?year=' + year + '&activity=' + activity)
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

