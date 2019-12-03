// from data.js
var tableData = data;


var filter = d3.select("#filter-btn");

var reset = d3.select("#reset-btn");

var tbody = d3.select("tbody");



function renderTable(ufoDatas) {
	ufoDatas.forEach(datas => {
		var row = tbody.append("tr");
		Object.values(datas).forEach(value =>{
        var cell = row.append("td");
        cell.text(value);
	});
	});	
}

function filterTableBottun() {
	
	d3.event.preventDefault();
	
	var searchDate = d3.select("#datetime").property("value");
	var searchCity = d3.select("#city").property("value");
	var searchState = d3.select("#state").property("value");
	var searchCountry = d3.select("#country").property("value");
	var searchShape = d3.select("#shape").property("value");

	var filteredDatas = data;

	if (searchDate != ""){
    	filteredDatas = filteredDatas.filter(filterdata => filterdata.datetime === searchDate);
    }
    if (searchCity !=""){
    	filteredDatas = filteredDatas.filter(filterdata => filterdata.city.toLowerCase() === searchCity.toLowerCase());
    }
    if (searchState !=""){
        filteredDatas = filteredDatas.filter(filterdata => filterdata.state.toLowerCase() === searchState.toLowerCase());
        }
    if (searchCountry !=""){
        filteredDatas = filteredDatas.filter(filterdata => filterdata.country.toLowerCase() === searchCountry.toLowerCase());
        }
    if (searchShape !=""){
        filteredDatas = filteredDatas.filter(filterdata => filterdata.shape.toLowerCase() === searchShape.toLowerCase());
        }

    tbody.html('');
    renderTable(filteredDatas);
}

function resetTableBottun() {
	tbody.html('');
	renderTable(tableData);
}


renderTable(tableData);
filter.on("click", filterTableBottun );
reset.on("click", resetTableBottun );
