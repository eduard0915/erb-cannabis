$(function ()  {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': 'is_active'},
            {'data': 'first_name'},
            {'data': 'username'},
            {'data': 'cargo'},
            {'data': 'groups__name'},
            {'data': 'email'},
            {'data': 'is_active'},
            {'data': 'is_active'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let edition
                    edition = '<a href="/user/update-password/'+row.id+'/" type="button" rel="tooltip" class="btn btn-info btn-xs btn-just-icon btn-simple"><i class="material-icons">lock</i</a>';
                    return edition;
                }
            },
            {
                targets: [-8],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let edition
                    edition = '<a href="/user/detail/'+row.id+'/" type="button" rel="tooltip" class="btn btn-info btn-xs btn-just-icon btn-simple"><i class="material-icons">loupe</i</a>';
                    return edition;
                }
            },
            {
                targets: [-3,-5,-6,],
                class: 'td-actions text-center'
            },
            {
                targets: [-4],
                class: 'td-actions text-center',
                render: function (data, type, row) {
                    var html = '';
                        html+='<span style="font-weight: bold">'+row.groups__name+'</span>'
                    return html
                }
            },
            {
                 targets: [-7],
                 className: 'td-actions text-center',
                 render: function (data, type, row) {
                     return row.first_name + ' ' +row.last_name;
                 }
             },
            {
                targets: [-2],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    var estado = null
                    switch (row.is_active) {
                        case true:
                            estado = 'Activo'
                            break;
                        case false:
                            estado = 'Inactivo'
                            break;
                    }
                    return estado;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});