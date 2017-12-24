function keyDown(e) {
    var r = false, key = e.which || e.keyCode;
    //[LEFT - DOWN]
    if (key >= 37 && key <= 40) {
        r = !r;
    }
    //BackSpace, Tab, Enter
    if (key == 8 || key == 9 || key == 13) {
        r = !r;
    }
    //SPACE
    if (key == 32) {
        r = !r;
    }
    //[F1 - F12]
    if (key >= 112 && key <= 123) {
        r = !r;
    }
    //[0 - 9]
    if (key >= 48 && key <= 57) {
        r = !r;
    }
    return r;
}
function soloMonto(e) {
    var key = e.which || e.keyCode;
    return (key >= 48 && key <= 57 || key >= 37 && key <= 40 || key == 188 || key == 8);
}
function calcularTotal(e) {
    console.log(e.type);
    return true;
    /*
     if (id.indexOf("precioc") > 0 || id.indexOf("cant") > 0) {
     var prec, cant, dt = t.parent().parent();
     if (!isNaN(e.key)) {
     prec = (id.indexOf("precioc") > 0) ? t.val() + e.key : dt.find("[name='precioc[]']").val();
     cant = (id.indexOf("precioc") > 0) ? dt.find("[name='cant[]']").val() : t.val() + e.key;
     prec = parseFloat(prec) || 0;
     cant = parseInt(cant) || 0;
     prec = (prec * cant).toFixed(0);
     dt.find("[name='preciov[]']").val(prec);
     }
     }*/
}
//Contador - id productos
var cpd = 1, ipd = [];
function nuevoProducto() {
    var div = $("#copiaProd").clone();
    var sf = div.find("input");
    sf.each(function (e) {
        var t = $(this);
        if (t.hasClass("solon")) {
            t.keydown(calcularTotal);
            t.keyup(calcularTotal);
            t.keypress(calcularTotal);
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
                    tt.parent().parent().parent().find("input").each(function (e) {
                        this.removeAttribute("disabled");
                    });
                    nuevoProducto();
                } else {
                    ev.target.value = "";
                    console.log(suggestion);
                    debugger;
                    return "";
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
nuevoProducto();