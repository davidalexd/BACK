
const select_protocol = $("#id-protocolos")
const table_secciones =$('#table-secciones')

fetch('http://127.0.0.1:8000/api/v2/Protocol/Protocolos/')
.then(response => response.json())
.then(data => add_options(select_protocol,data,"protocolo_titulo","id"));

select_protocol.change(function(e) {
    value = e.target.value;
    fetch(
        'http://127.0.0.1:8000/api/v2/Protocol/Protocolos/'+value
    )
    .then(
        response => response.json()
    )
    .then(data => datatable_secciones(data));
});

function datatable_secciones(attributes){;
    table_secciones.dataTable({
        data : attributes.secciones,
        lengthMenu: [5, 10, 20, 50, 100, 200, 500],
        pageLength: 50,
        createdRow: function(row, data, dataIndex, cells) {
            $(row).attr('data-toggle', 'collapse');
            $(row).attr('data-target', '#demo'+data.id);
            $(row).addClass('accordion-toggle');
        },
        columns: [
            {
                data : "id",
                render: function(data, type) {
                    return '<div class="custom-control custom-control-alternative custom-checkbox mb-3"><input class="custom-control-input" value="'+data+'" id="customCheck'+data+'" type="checkbox"><label class="custom-control-label" for="customCheck'+data+'"></label></div>'
                }
            },
            {
                data : "secciones_titulo",
                render: function(data, type) {
                    return '<div class="media align-items-center"><div class="media-body"><span class="mb-0 text-sm">'+data+'</span></div></div>'
                }
            },
            {
                data: "opcion",
                render: function(data, type) {
                    return data.map(function(value,key){
                        return '<tr><td colspan="2" class="hiddenRow"><div class="accordian-body collapse" id="demo1"> <table class="table table-condensed table-striped align-items-center table-dark"><thead class="thead-dark"><tr class="info"><th>#</th><th>Prueba</th></tr></thead>	<tbody class="list"><tr data-toggle="collapse"  class="accordion-toggle" data-target="#demo10"><td><div class="custom-control custom-control-alternative custom-checkbox mb-3"><input class="custom-control-input" id="customCheckprueba" type="checkbox"></input><label class="custom-control-label" for="customCheckprueba"></label></div></td><td>Prueba</td></tr></tbody></table></div> </td><tr>'
                    })
                }
            }
        ]
    })
}