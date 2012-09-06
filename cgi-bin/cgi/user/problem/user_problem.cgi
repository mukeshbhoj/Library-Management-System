#!/usr/bin/perl -w

use warnings;

use HTML::Template;
use CGI;
use CGI::Session;
use CGI::Cookie;

my $cgi = CGI->new();
my $session = CGI::Session->new();

if($session->param('USERNAME')){
	my $username = $session->param('USERNAME');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/user/user_header.tmpl');   
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/user/user_pageheader.tmpl');
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/user/problem/user_problem.tmpl'); 
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/user/user_footer.tmpl'); 
	print $cgi->header();
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
	print $cgi->redirect(-url=>'/cgi-bin/library.cgi');
}
