#!/usr/bin/perl -w
use strict;
use CGI;
use HTML::Template;
use CGI::Session;

my $query = CGI->new();
my $session = CGI::Session->new();
if($session->param('ADMIN')){
	my $username = $session->param('ADMIN');	
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl'); 
	$template2->param(username => "$username");
	$template3->param(search_table=>'hidden');
	print $query->header();
	print $template1->output,$template2->output,$template3->output;
	print $template4->output;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
