$(document).ready(function () {
        var departamentoOptions;  
        $.ajax({
              type: 'GET',
              url: 'colombia.json',
              dataType: 'json'
          }).done((data) => {
           
            $.each(data,  function(dkey,depto) {
            
              departamentoOptions += "<option value'" + depto.id + "'>" + depto.departamento + "</option>";
            });
            $('#departamento').html(departamentoOptions);

            $('#departamento').change(function() {
            
              var ciudadOptions = "";
            
              var value = $(this).val();
              
              $.each(data, function(key,depto) {
                
                if (value==depto.departamento) {
                  $.each(depto.ciudades,function(dkey,val) {
                    
                    ciudadOptions += "<option value'" + val  + "'>" +val + "</option>";

                  });
                } });
          
              $('#ciudad').html(ciudadOptions);
          
            });
            
          });
      });
  



