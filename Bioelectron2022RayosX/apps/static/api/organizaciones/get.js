fetch('http://127.0.0.1:8000/api/v2/Customer/Organizaciones/')
  .then(response => response.json())
  .then(data => datatable_data(data));

  function datatable_data(attributes){
    $("#example").dataTable({
        data : attributes,
        columns: [
            {"data" : "id"},
            {"data" : "ruc"},
            {"data" : "razon_social"}            
        ],
    });
  }