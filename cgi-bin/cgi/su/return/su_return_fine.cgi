#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use SEARCH_BOOK;
use Data::Dumper;


my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('LIBRARIAN'))
{
	my $username1 = $session->param('LIBRARIAN');
	print $query->header();
	print $session->param('totalbooks');
	print "mukesh";
}
