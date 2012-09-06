#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Problem;

my $query = CGI->new();
my $session = CGI::Session->new();																
my $username = $session->param('ADMIN');
if($session->param('ADMIN'))
{

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/problem/admin_problem.tmpl'); 
	$template2->param(username=>$username);	

	my $problem = Problem::search();
	
	my $count = @$problem;
	$template3->param(problem=>$problem);
	if($count != 0){
		$template3->param(COUNT=>$count." problem(s) is/are not solved");
	}
	else{
		$template3->param(visibility=>"hidden");
		$template3->param(SUCCESS=>"No problems are found.");
	}
	print $query->header();
	print $template1->output,$template2->output,$template3->output,$template4->output;	
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
