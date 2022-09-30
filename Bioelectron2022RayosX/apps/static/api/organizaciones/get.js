fetch('http://127.0.0.1:8000/api/v2/Customer/Organizaciones/')
.then(response => response.json())
.then(data => datatable_data(data));

function datatable_data(attributes){
    $("#example").dataTable({
        data : attributes,
        columns: [
            {"data" : "id"},
            {   
                data : "razon_social",
                render: function(data, type) {
                    return '<div class="media align-items-center"><a class="avatar rounded-circle mr-3"><img alt="Image placeholder" src="/static/assets/img/theme/bootstrap.jpg"></a><div class="media-body"><span class="name mb-0 text-sm">'+data+'</span></div></div>'
                }
            },
            {"data" : "ruc"},
            {"data" : "nombre_comercial"},  
            {"data" : "tipo"},  
            {
                className : "td-actions text-center",
                data : "members",
                render: function(data, type) {
                    return '<button type="button" rel="tooltip" class="btn btn-info btn-icon btn-sm" onclick="'+members_with_element(data)+'" data-toggle="modal" data-target="#model-members" data-original-title="" title="">'+data.length+'</button>'
                }
            },  
            {
                data : "is_enabled",
                render: function(data, type) {
                    if (data == false) {
                        return '<span class="badge badge-dot mr-4"><i class="bg-warning"></i> <span class="status">Deshabilitado</span></span>';
                    } else {
                        return '<span class="badge badge-dot mr-4"><i class="bg-success"></i> <span class="status">Habilitado</span></span>';
                    }
                }
            },   
            {
                data : "edit_url",
                render: function(data, type) {
                    return '<button type="button" rel="tooltip" class="btn btn-success btn-icon btn-sm" data-original-title="" title=""><i class="ni ni-settings-gear-65 pt-1"></i></button> <button type="button" rel="tooltip" class="btn btn-danger btn-icon btn-sm btn-simple" data-original-title="" title=""><i class="ni ni-fat-remove pt-1"></i></button>';
                }
            }
        ],
    });
}

function members_with_element(json){
    $("#members-list").dataTable({
        data : json,
        columns: [
            {"data" : "id"},
            {"data" : "nombre_departamento"},
            {"data" : "direccion_departamento"},
            {
                className : "td-actions text-center",
                data : "members",
                render: function(data, type) {
                    return '<button type="button" rel="tooltip" class="btn btn-info btn-icon btn-sm" data-toggle="modal" data-target="#model-members" data-original-title="" title="">'+data.length+'</button>'
                }
            }, 
            {
                data : "is_enabled",
                render: function(data, type) {
                    if (data == false) {
                        return '<span class="badge badge-dot mr-4"><i class="bg-warning"></i> <span class="status">Deshabilitado</span></span>';
                    } else {
                        return '<span class="badge badge-dot mr-4"><i class="bg-success"></i> <span class="status">Habilitado</span></span>';
                    }
                }
            },  
            {
                data : "edit_url",
                render: function(data, type) {
                    return '<button type="button" rel="tooltip" class="btn btn-success btn-icon btn-sm" data-original-title="" title=""><i class="ni ni-settings-gear-65 pt-1"></i></button> <button type="button" rel="tooltip" class="btn btn-danger btn-icon btn-sm btn-simple" data-original-title="" title=""><i class="ni ni-fat-remove pt-1"></i></button>';
                }
            },
        ]
    })
}