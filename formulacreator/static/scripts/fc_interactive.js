$(function() {
	$( "#tabs" ).tabs();
});

var timer;
function trigger_update_timer(){
	$("#apply_formula").prop('disabled',true);	
	$("#apply_format").prop('disabled',true);
	window.clearTimeout(timer);
	$("#formulaImg").hide();
	timer = setTimeout(update_formula_image, 200);
}

function update_formula_image() {
	var parameters = {
 		"formula" : $("#formulaInput").val(),
 		"fontsize" : $("#fontsizeInput").val(),
 		"color" : $("#colorInput").val()
	}
	queryString = $.param(parameters)
	newSrc = "http://formulacreator.appspot.com/formula/?" + queryString;
	$("#formulaImg").attr("src", newSrc);
	update_embedding_code(newSrc)
}

function update_embedding_code(newSrc) {
	var linkInteractive = newSrc.replace("formula/","interactive");
	var embeddingCodeTemplate = "<a href=\"{0}\" target=_blank><img src=\"{1}\" alt=\"Formula rendered with Formula Creator\"></a>";
	var embeddingCode = embeddingCodeTemplate.format(linkInteractive, newSrc);
	$("#embeddingOutput").val(embeddingCode);
	$("#embeddingPreview").html(embeddingCode);
}

function is_arrow_key(e) {
 if (e.keyCode==37 || e.keyCode==38 || e.keyCode==39 || e.keyCode==40) return true;
 else return false;
}

$("#apply_formula").button({
		icons: {
			primary: "ui-icon-gear"
		},
		text: true	
	}).click(trigger_update_timer);
$("#apply_format").button({
		icons: {
			primary: "ui-icon-gear"
		},
		text: true	
	}).click(trigger_update_timer);

$('#formulaInput').keyup(function(e) {
	if (is_arrow_key(e)) return;
	trigger_update_timer();
});

$('#fontsizeInput').keypress(function(e) {
	if (is_arrow_key(e)) return;
	$("#apply_formula").prop("disabled", false);
	$("#apply_format").prop("disabled", false);
});
	
$('#colorInput').keypress(function(e) {
	if (is_arrow_key(e)) return;
	$("#apply_formula").prop("disabled", false);
	$("#apply_format").prop("disabled", false);

});

// Read parameters from URL and prefill form elements
default_params = {
	"formula" : "",
	"fontsize" : "12",
	"color" : "black"
}
url_params = get_url_vars(default_params);
$("[id$='Input']").each(function(){
	var param_name = this.id.replace('Input','');
	this.value = url_params[param_name];
	});

