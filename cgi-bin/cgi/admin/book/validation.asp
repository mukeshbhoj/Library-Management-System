#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Data::Dumper;
use Check_add_book;

my $query = CGI->new();

if($query->param("txtgid")){
	my $gid = $query->param("txtgid");

	if(Check_add_book::check_id($gid)){
		print $query->header();
		print "true";
		return;
	}
	
	else{
		print $query->header();
		print "Invalid Group Id";
		return;
	}
}



else{ 
	print $query->header();print "Use proper characters";
	return;
}
