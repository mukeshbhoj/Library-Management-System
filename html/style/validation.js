function valid_username(str)
{
var xmlhttp;

	if(str == "")
	{
	 document.getElementById("varusername").innerHTML="Username is required";
	 return;
	}
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
		  if (xmlhttp.readyState==4)
			{
			document.getElementById("varusername").innerHTML=xmlhttp.responseText;
			}
	  }
xmlhttp.open("GET","/cgi-bin/admin/validation.asp?txtusername="+str,true);
xmlhttp.send();
}


function valid_name(str)
{
var xmlhttp;   
	if(str == "")
	{
	 document.getElementById("varname").innerHTML="name is required";
	 return;
	}
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
		  if (xmlhttp.readyState==4)
			{
			document.getElementById("varname").innerHTML=xmlhttp.responseText;
			}
	  }
xmlhttp.open("GET","/cgi-bin/admin/validation.asp?txtname="+str,true);
xmlhttp.send();
}


function valid_phno(str)
{
var xmlhttp;   
	if(str == "")
	{
	 document.getElementById("varphno").innerHTML="Mobile number is required";
	 return;
	}
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
		  if (xmlhttp.readyState==4)
			{
			document.getElementById("varphno").innerHTML=xmlhttp.responseText;
			}
	  }
xmlhttp.open("GET","/cgi-bin/admin/validation.asp?txtphno="+str,true);
xmlhttp.send();
}


function valid_phno(str)
{
var xmlhttp;   
	if(str == "")
	{
	 document.getElementById("varphno").innerHTML="Mobile number is required";
	 return;
	}
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
		  if (xmlhttp.readyState==4)
			{
			document.getElementById("varphno").innerHTML=xmlhttp.responseText;
			}
	  }
xmlhttp.open("GET","/cgi-bin/admin/validation.asp?txtphno="+str,true);
xmlhttp.send();
}


function valid_city(str)
{
var xmlhttp;   
	if(str == "")
	{
	 document.getElementById("varcity").innerHTML="City is required";
	 return;
	}
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
		  if (xmlhttp.readyState==4)
			{
			document.getElementById("varcity").innerHTML=xmlhttp.responseText;
			}
	  }
xmlhttp.open("GET","/cgi-bin/admin/validation.asp?txtcity="+str,true);
xmlhttp.send();
}


function notchanged(str)
{
	 document.getElementById(str).innerHTML="Only admin can change it";
	 return;
}




/*==================== validation for Librarian in issue book (Group Id and Member ID) ==================*/

function valid_gid_search(gid){
	var xmlhttp;
	if(gid == ""){
		document.getElementById("no_group").innerHTML="Group Id is required.";
		return false;
	}

	if (window.XMLHttpRequest){		// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	}
	else{							// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4){
			document.getElementById("no_group").innerHTML=xmlhttp.responseText;
			check = xmlhttp.responseText;
			if(check == "true"){
				document.getElementById("no_group").innerHTML="";
				document.forms["search_book"].submit();
			}
		}
	}
	xmlhttp.open("GET","/cgi-bin/admin/book/validation.asp?txtgid="+gid,true);
	xmlhttp.send();
	return false;
}


f

function valid_mid_bid(mid){
	var bid=document.getElementsByName("rd_bid");	
	var check = 0;
	if(mid == ""){
		document.getElementById("no_mem").innerHTML="Member Id is required.";
		return false;
	}
	for(i=0;i<bid.length;i++){
		if(bid[i].checked){
			check = 1;
		}
	}
	if(check == 0){
		document.getElementById("no_mem").innerHTML="You must have to select a book.";
		return false;	
	}
}


function valid_bid(){
	var bid=document.getElementsByName("rd_bid");	
	var check = 0;
	for(i=0;i<bid.length;i++){
		if(bid[i].checked){
			check = 1;
		}
	}
	if(check == 0){
		document.getElementById("no_book").innerHTML="You must have to select a book.";
		return false;	
	}
}


function valid_mid(mid){
	if(mid == ""){
		document.getElementById("no_mem").innerHTML="Member Id is required.";
		return false;
	}
}

function valid_gid(gid){
	var xmlhttp;
	if(gid == ""){
		document.getElementById("no_group").innerHTML="Group Id required.";
		return false;
	}


}

function valid_mid_delete(mid){

	var xmlhttp;
	var check;

	if(mid == ""){
		document.getElementById("no_mem").innerHTML="Member Id is required.";
		return false;
	}
	else{
		if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp=new XMLHttpRequest();
		}
		else{// code for IE6, IE5
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function(){
			if (xmlhttp.readyState==4){
				document.getElementById("no_mem").innerHTML=xmlhttp.responseText;
				check = xmlhttp.responseText;
				if(check == "true"){
					if(confirm("Do you want to delete Member Id : "+mid+" ?")){
						document.getElementById("no_mem").innerHTML="";
						document.forms["delete_member"].submit();
					}
					else{	
						document.getElementById("no_mem").innerHTML="";
						return false;
					}
				}
			}
		}
		xmlhttp.open("GET","/cgi-bin/admin/delete.asp?txtmid="+mid,true);
		xmlhttp.send();
	}
return false;
}



function valid_bid_delete(bid)
{
	var xmlhttp;
	var check;

	if(bid == ""){
		document.getElementById("no_book").innerHTML="Book Id is required.";
		return false;
	}
	else{
		if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp=new XMLHttpRequest();
		}
		else{// code for IE6, IE5
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function(){
			if (xmlhttp.readyState==4){
				document.getElementById("no_book").innerHTML=xmlhttp.responseText;
				check = xmlhttp.responseText;
				if(check == "true"){
					if(confirm("Do you want to delete Book Id : "+bid+" ?")){
						document.getElementById("no_book").innerHTML="";
						document.forms["delete_book"].submit();
					}
					else{	
						document.getElementById("no_book").innerHTML="";
						return false;
					}
				}
			}
		}
		xmlhttp.open("GET","/cgi-bin/admin/book/delete.asp?txtbid="+bid,true);
		xmlhttp.send();
	}
return false;

}


