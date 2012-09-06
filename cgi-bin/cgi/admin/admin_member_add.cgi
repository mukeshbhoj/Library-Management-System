#!/usr/bin/perl -w
use warnings;
use HTML::Template;
use CGI;
use CGI::Session;
use CGI::Cookie;
use Check_add_mem;

my $cgi = CGI->new();																					##	get session of user
my $session = CGI::Session->new();																		##	and call
my $username = $session->param('ADMIN');																##	admin_header.tmpl

if($session->param('ADMIN')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	$template2->param(username=>$username);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_add.tmpl'); 
	$template3->param(txtid=>Check_add_mem::newid());
	print "Content-Type:text/html\n\n";
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
	print $cgi->redirect(-url=>'/cgi-bin/library.cgi');
}
