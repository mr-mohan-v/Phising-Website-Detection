function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
		tablink = tab.url;
		$("#p1").text("The URL being tested is"+tablink);

		var xhr=new XMLHttpRequest();
		params="url="+tablink;
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		xhr.open("POST","http://localhost:8000/check/",false);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		let pattern1 = /SAFE WEBSITE/g
		let pattern2 = /MALICIOUS WEBSITE/g
		let res = xhr.responseText
		
		if(res.match(pattern1))
		{
			$("#div1").text('Safe website');
			document.getElementById('div1').style.color = "#55ba57";
		}
		else if (res.match(pattern2)) 
		{
			$("#div1").text('Not Safe - Phishing Website');
			document.getElementById('div1').style.color = "#e85c35";
		}
		else
		{
			$("#div1").text('ERROR');
		}
		return xhr.responseText;
	});
}

$(document).ready(function(){
    $("button").click(function(){	
		var val = transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
