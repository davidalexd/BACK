function add_options(etiqueta,attributes,text_option,value_option){
    var options = [],_options;
    var option_default = '<option value="" selected disabled>Seleccione una opción</option>';
    collection = attributes.map(function(value,key){
        var option = '<option value="' + value[value_option] + '">' + value[text_option]  +'</option>';
        return options.push(option);
    });
    _options = options.join('');    
    etiqueta.html([option_default,_options]); 
}