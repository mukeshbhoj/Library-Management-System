#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Data::Dumper;
use Check_add_mem;

my $query = CGI->new();


if($query->param("txtmid")){
	my $mid = $query->param("txtmid");

	if(Check_add_mem::check_id($mid)){
		if(Check_add_mem::check_issued($mid)){
			print $query->header();
			print 'Member has not returned some books';
			return;
		}
		print $query->header();
		print "true";
		return;
	}
	
	else{
		print $query->header();
		print "Invalid Member Id";
		return;
	}
}

else{ 
print $query->header();print "Use proper characters";
return;
}
