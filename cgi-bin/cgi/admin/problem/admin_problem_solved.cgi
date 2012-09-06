#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Data::Dumper;
use Problem;

my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();
if($session->param('ADMIN'))
{
	my $username1 = $session->param('ADMIN');
	my @problem = $query->param('p_id');

	my $userid = Problem::find_id($username1);	

	foreach my $pid(@problem)
	{
		Problem::solve($userid,$pid);
	}

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	$template2->param(username=>$username1);
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/problem/admin_problem.tmpl'); 
	$template3->param(SUCCESS=>@problem." problem(s) solved successfully.");
	$template3->param(problem=>Problem::search());

	print $query->header();
	print $template1->output,$template2->output,$template3->output,$template4->output;	
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
