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
            {'data': 'reception_date'},
            {'data': 'reception_date'},
            {'data': 'seed_type'},
            {'data': 'crop_type'},
            {'data': 'geo_zone'},
            {'data': 'plant_size'},
            {'data': 'leaves_size'},
            {'data': 'leaves_size'},
        ],
        columnDefs: [
            {
                targets: [7],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let edition
                    edition = '<a href="/traceability/add/'+row.id+'/" type="button" rel="tooltip" class="btn btn-info btn-xs btn-just-icon btn-simple"><i class="material-icons">lock</i</a>';
                    return edition;
                }
            },
            {
                targets: [0],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let edition
                    edition = '<a href="/traceability/add/'+row.id+'/" type="button" rel="tooltip" class="btn btn-info btn-xs btn-just-icon btn-simple"><i class="material-icons">loupe</i</a>';
                    return edition;
                }
            },
            {
                targets: [1,2,3,4,6],
                class: 'td-actions text-center'
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});