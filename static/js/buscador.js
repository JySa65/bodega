function soloNumeros(e) {
    var key = e.which | e.keyCode;
    var inp = $(e.target);
    if (inp.attr("id").indexOf("precioc") > 0 || inp.attr("id").indexOf("cant") > 0) {
        var prec = parseFloat(inp.val() + e.key);
        var cant = parseInt(inp.parent().parent().find("[name='cant[]']").val()) || 1;
        if (!isNaN(prec)) {
            prec = (prec * cant * 1.12 * 1.30).toFixed(0);
            $("#" + inp.attr("id").replace("oc", "ov")).val(prec);
        }
    }
    return (key >= 48 && key <= 57 || key == 8);
}
function precioVenta(e) {

}
//Contador - id productos
var cpd = 1, ipd = [];
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
                if (ipd.indexOf(suggestion.pk) < 0) {
                    ipd.push(suggestion.pk);
                    tt.attr("id-select", suggestion.pk);
                    tt.parents(".s12").find("input").each(function (e) {
                        this.removeAttribute("disabled");
                    });
                    nuevoProducto();
                } else {
                    //ALERTA YA EXISTE
                    tt.val("");
                }
            });
        } else if (t.attr("id") == "id_exento") {
            div.find("label").attr("for", t.attr("id") + cpd);
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

$('#id_empresa2').typeahead({
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
    $('#id_empresa').val(suggestion.pk);
});
document.getElementById("form_pedido").onsubmit = function (e) {
    //$('#id_empresa').val($('#id_empresa').attr("id-select"));
};
