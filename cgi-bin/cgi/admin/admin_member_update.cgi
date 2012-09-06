#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;

my $query = CGI->new();
my $session = CGI::Session->new();										
my $username1 = $session->param('ADMIN');

if($session->param('ADMIN')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	$template2->param(username=>$username1);
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_update.tmpl'); 

	print $query->header();
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}

