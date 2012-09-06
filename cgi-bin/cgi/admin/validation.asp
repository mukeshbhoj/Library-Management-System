#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Data::Dumper;
use Check_add_mem;

my $query = CGI->new();
my $flag=0;


#############========== check username ==============##############

if($query->param("txtusername")){
	my $username = $query->param("txtusername");
	$username =~ s/'/\\'/g;

	if(Check_add_mem::check_username($username)){
		print $query->header();
		print "Username is already used";
		return;
	}
	
	else{
		print $query->header();
		print "Valid username";
		return;
	}
}

#############========== check name ==============##############

if($query->param("txtname")){ 
	my $name = $query->param("txtname");	

	if(!($name =~ m/^([a-zA-Z]+\s*)+$/)){
		print $query->header();
		print "Use proper characters";
		return;
	}
	
	else{
		print $query->header();
		return;
	}
}

#############========== check mobile number ==============##############

if($query->param("txtphno")){ 
	my $phno = $query->param("txtphno");	

	if(!($phno =~ m/^\d{10}$/)){
		print $query->header();
		print "Mobile number must be of 10 digit";
		return;
	}
	
	else{
		print $query->header();
		return;
	}
}

#############========== check city ==============##############

if($query->param("txtcity")){ 
	my $city = $query->param("txtcity");	

	if(!($city =~ m/^[A-Za-z]+$/)){
		print $query->header();
		print "Cityname contains characters only";
		return;
	}
	
	else{
		print $query->header();
		return;
	}
}

#############========== check city ==============##############

if($query->param("txtcity")){ 
	my $city = $query->param("txtcity");	

	if(!($city =~ m/^[A-Za-z]+$/)){
		print $query->header();
		print "Cityname contains characters only";
		return;
	}
	
	else{
		print $query->header();
		return;
	}
}


else{ 
print $query->header();print "Use proper characters";
}





