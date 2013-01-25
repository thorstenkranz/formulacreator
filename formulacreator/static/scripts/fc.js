window.fadeIn = function(obj) {
	$(obj).fadeIn(2000);
}

function get_url_vars(dict_to_update)
// Read a page's GET URL variables and return them as an associative array.
{
	 if (arguments.length==0) {
	 	var vars = {} //[], hash;
	 } else {
	 	var vars = dict_to_update;	
	 }
    
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        //vars.push(hash[0]);
        vars[hash[0]] = decodeURIComponent(hash[1]);
    }
    return vars;
}

String.prototype.format = function() {
  var args = arguments;
  return this.replace(/{(\d+)}/g, function(match, number) { 
    return typeof args[number] != 'undefined'
      ? args[number]
      : match
    ;
  });
};