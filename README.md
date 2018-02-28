var win = window.open("", "Title", "toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=780,height=200,top="+(screen.height-400)+",left="+(screen.width-840));

setInterval( function() {
var divs = document.querySelectorAll("div.Grid-cell.u-size1of2.u-lg-size1of3.u-mb10 span.username.u-dir b.u-linkComplex-target"), i;

for (i = 0; i < divs.length; ++i) {
  win.document.body.innerHTML = win.document.body.innerHTML + "<br>" + divs[i].innerText;
}
	$("div.Grid-cell.u-size1of2.u-lg-size1of3.u-mb10").remove();
	setTimeout(function() { window.scrollTo(0,1);},1000);
	setTimeout(function() { window.scrollTo(0, document.body.scrollHeight);},2000);
} , 4000);
