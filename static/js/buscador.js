function soloNumeros(e) {
    var key = e.which | e.keyCode;
    return (key >= 48 && key <= 57);
}
var cpd = 1;
function nuevoProducto() {
    var div = $("#copiaProd").clone();
    var sf = div.find("input");
    sf.each(function (e) {
        var t = $(this);
        if (t.hasClass("solon")) {
            t.keydown(soloNumeros);
        }
        if (t.attr("id") == "id_producto") {
            t.typeahead({
                hint: true,
                highlight: true,
                minLength: 1
            }, {
                name: 'empresas',
                source: productos,
                display: 'nombre',
                itemSelected: function (item) {
                    return item;
                },
                templates: {
                    empty: [
                        '<div class="tt-suggestion">unable to find any Best Picture winners that match the current query</div>'
                    ].join('\n'),
                    suggestion: Handlebars.compile('<div>{{codigo}} - <strong>{{nombre}}</strong></div>')
                }
            }).bind('typeahead:select', function (ev, suggestion) {
                var tt = $(this);
                tt.attr("id-select", suggestion.pk);
                tt.parents(".s12").find("input").each(function(e){
                    this.removeAttribute("disabled");
                });
                nuevoProducto();
            });
        }else if(t.attr("id") == "id_exento"){
            
        }
        t.attr("id", t.attr("id") + cpd);
    });
    div.removeClass("hide").removeAttr("id").attr("data-cant", cpd);
    $("#productos").append(div);
    cpd++;
}
window.addEventListener("load", function (e) {
    nuevoProducto();
});
var empresas = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.whitespace,
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
        url: dir_empresa + "?name=%QUERY",
        wildcard: '%QUERY'
    }
});
var productos = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.whitespace,
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
        url: dir_producto + "?name=%QUERY",
        wildcard: '%QUERY'
    }
});

$('#id_empresa').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
}, {
    name: 'empresas',
    source: empresas,
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
        suggestion: Handlebars.compile('<div><strong>{{nombre}}</strong> - {{rif}}</div>')
    }
}).bind('typeahead:select', function (ev, suggestion) {
    $(this).attr("id-select", suggestion.pk);
});
/*
 $('#id_producto').typeahead({
 hint: true,
 highlight: true,
 minLength: 1
 }, {
 name: 'empresas',
 source: productos,
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
 suggestion: Handlebars.compile('<div>{{codigo}} - <strong>{{nombre}}</strong> </div>')
 }
 }).bind('typeahead:select', function (ev, suggestion) {
 $(this).attr("id-select", suggestion.pk);
 var sf = this.parentElement.parentElement.parentElement.getElementsByClassName("solon");
 for (var i = 0; i < sf.length; i++) {
 sf[i].onkeypress = soloNumeros;
 sf[i].removeAttribute("disabled");
 document.getElementsByTagName("input");
 }
 debugger;
 });
 */
document.getElementById("form_pedido").onsubmit = function (e) {
    $('#id_empresa').val($('#id_empresa').attr("id-select"));
};
