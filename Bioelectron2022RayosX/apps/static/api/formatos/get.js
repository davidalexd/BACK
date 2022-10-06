
const select_protocol = $("#id-protocolos")
const table_secciones =$('#table-secciones')

fetch('http://127.0.0.1:8000/api/v2/Protocol/Protocolos/',{
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
    },
})
.then(response => response.json())
.then(data => add_options(select_protocol,data,"protocolo_titulo","id"));

select_protocol.change(function(e) {
    e.preventDefault();
    value = e.target.value;
    fetch(
        'http://127.0.0.1:8000/api/v2/Protocol/Protocolos/'+value
    )
    .then(
        response => response.json()
    )
    .then(data => datatable_secciones(data));
});

function datatable_secciones(attributes){
    table_secciones.dataTable().fnDestroy();
    table_secciones.dataTable({
        data : attributes.secciones,
        lengthMenu: [5, 10, 20, 50, 100, 200, 500],
        pageLength: 50,
        createdRow: function(row, data, dataIndex, cells) {
            // $(row).attr('data-toggle', 'collapse');
            // $(row).attr('data-target', '#demo'+data.id);
            // $(row).addClass('accordion-toggle');
        },
        columns: [
            {
                data : "id",
                render: function(data, type) {
                    return '<div class="custom-control custom-control-alternative custom-checkbox mb-3"><input class="custom-control-input" name="secciones" value="'+data+'" id="customCheck'+data+'" type="checkbox"  checked=""><label class="custom-control-label" for="customCheck'+data+'"></label></div>'
                }
            },
            {
                data : "secciones_titulo",
                render: function(data, type,row) {
                    return '<div class="media align-items-center"><div class="media-body"><span class="mb-0 text-sm">'+data+'</span></div></div>'
                }
            },
            {
                className : "td-actions text-center",
                data : "opcion",
                render: function ( data, type, row) {
                    return ( 
                        '<button type="button" class="btn btn-info btn-icon btn-sm  accordion-toggle" data-toggle="collapse" onclick=change_icon("dow-left_opcion'+row.id+'","demo'+row.id+'") data-target="#demo_opcion'+row.id+'">'+data.length+
                            '<i id="dow-left_opcion'+row.id+'" class="ni ni-bold-down"></i>'+
                        '</button>'+
                        '<div class="accordian-body collapse" id="demo_opcion'+row.id+'">'+
                            data.map(function(value,key){
                                return (
                                    '<div class="custom-control custom-control-alternative custom-checkbox mb-3">'+
                                        '<input class="custom-control-input" name="opcion"  value="'+value.id+'" id="customCheckPruebaOpcion'+key+''+row.id+'" type="checkbox"  checked="">'+
                                        '<label class="custom-control-label" for="customCheckPruebaOpcion'+key+''+row.id+'">'+value.pruebas_titulo+'</label>'+
                                    '</div>'
                                )
                            })
                        +'</div>'
                    )
                }
            },
            {
                className : "td-actions text-center",
                data : "calculo",
                render: function ( data, type, row) {
                    return ( 
                        '<button type="button" class="btn btn-info btn-icon btn-sm  accordion-toggle" data-toggle="collapse" onclick=change_icon("dow-left_calculo'+row.id+'","demo_calculo'+row.id+'") data-target="#demo_calculo'+row.id+'">'+data.length+
                            '<i id="dow-left_calculo'+row.id+'" class="ni ni-bold-down"></i>'+
                        '</button>'+
                        '<div class="accordian-body collapse" id="demo_calculo'+row.id+'">'+
                            data.map(function(value,key){
                                return (
                                    '<div class="custom-control custom-control-alternative custom-checkbox mb-3">'+
                                        '<input class="custom-control-input" name="calculo"  value="'+value.id+'" id="customCheckPruebaCalculo'+key+''+row.id+'" type="checkbox"  checked="">'+
                                        '<label class="custom-control-label" for="customCheckPruebaCalculo'+key+''+row.id+'">'+value.pruebas_titulo+'</label>'+
                                    '</div>'
                                )
                            })
                        +'</div>'
                    )
                }
            }
        ],
    }).api();
}

function change_icon(etiqueta,etiqueta_relacion){
    if ($('#'+etiqueta_relacion).hasClass("show")) {
        $('#'+etiqueta).removeClass("ni ni-bold-up");
        $('#'+etiqueta).addClass("ni ni-bold-down");
    }
    else{
        $('#'+etiqueta).removeClass("ni ni-bold-down");
        $('#'+etiqueta).addClass("ni ni-bold-up");
    }
}