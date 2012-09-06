#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Data::Dumper;
use Check_add_book;

my $query = CGI->new();



if($query->param("txtbid")){
	my $bid = $query->param("txtbid");

	if(Check_add_book::check_bid($bid)){
		if(Check_add_book::check_issued($bid)){
			print $query->header();
			print 'Book is currently issued.';
			return;
		}
		print $query->header();
		print 'true';
		return;
	}
	
	else{
		print $query->header();
		print "Invalid Book Id";
		return;
	}
}



else{ 
print $query->header();print "Use proper characters";
return;
}
