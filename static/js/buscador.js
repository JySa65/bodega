var countries = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  remote: {
    url: dir_empresa + "?name=%QUERY",
    wildcard: '%QUERY'
}
});

$('#id_empresa').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
},
{
    name: 'empresas',
    source: countries,
    display: 'nombre',
    itemSelected: function (item) {
        return item;
    },
    templates: {
        empty: [
        '<div class="empty-message">',
        'unable to find any Best Picture winners that match the current query',
        '</div>'
        ].join('\n'),
        suggestion: Handlebars.compile('<div><strong>{{nombre}}</strong> – {{rif}}</div>')
    }
}).bind('typeahead:select', function(ev, suggestion) {
    $(this).attr("id-select", suggestion.pk);
});

document.getElementById("form_pedido").onsubmit=function(e){
    $('#id_empresa').val($('#id_empresa').attr("id-select"));
};
