#!/usr/bin/perl -w

use warnings;
use HTML::Template;
use CGI;
use CGI::Session;
use CGI::Cookie;

my $cgi = CGI->new();
my $session = CGI::Session->new();

if($session->param('ADMIN')){
	my $username = $session->param('ADMIN');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   
    my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');
    my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_home.tmpl'); 
    my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 
	$template2->param(username=>$username);
    print "Content-Type:text/html\n\n";
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
		print $cgi->redirect(-url=>'/cgi-bin/library.cgi');
}
