var datos = 

$('#id_empresa').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
},
{
    name: 'empresas',
    source: function (query, process) {
        return $.get(dir_empresa, { name: query }, function (data) {
            return process(data);
        });
    },
    display: 'nombre',
    templates: {
        empty: [
        '<div class="empty-message">',
        'unable to find any Best Picture winners that match the current query',
        '</div>'
        ].join('\n'),
        suggestion: Handlebars.compile('<div><strong>{{nombre}}</strong> – {{rif}}</div>')
    }
    /*,
    */
});
