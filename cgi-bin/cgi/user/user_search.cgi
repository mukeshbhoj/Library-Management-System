#!/usr/bin/perl -w
use strict;
use CGI;
use HTML::Template;
use CGI::Session;

my $query = CGI->new();
my $session = CGI::Session->new();										
my $username1 = $session->param('USERNAME');
if($session->param('USERNAME')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/user/user_header.tmpl');
	my $template11 = HTML::Template->new(filename => '/var/www/project/html/user/user_pageheader.tmpl');
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/user/user_search.tmpl');
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/user/user_footer.tmpl'); 
	$template2->param(search_table=>'hidden');
	$template11->param(username=>$username1);
	print "Content-Type:text/html\n\n", $template1->output,$template11->output,$template2->output,$template3->output;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}

