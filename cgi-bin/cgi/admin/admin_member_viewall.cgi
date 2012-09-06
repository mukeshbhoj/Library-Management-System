#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use Check_add_mem;
use Search_mem;
use DBI;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('ADMIN')){
	my $username1 = $session->param('ADMIN');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##

	my @member = Search_mem::search_all_mem();
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_viewall.tmpl'); 
	$template3->param(THIS_LOOP=>\@member);
	print $query->header();
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
