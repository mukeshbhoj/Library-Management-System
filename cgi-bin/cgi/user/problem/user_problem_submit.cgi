#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use DBI;
use Time::localtime;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
my $username1 = $session->param('USERNAME');
my $subject = $query->param('txtsubject');
my $description = $query->param('txtdescription');
if($session->param('USERNAME')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/user/user_header.tmpl');   	##	user_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/user/user_pageheader.tmpl');	##	user_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/user/user_footer.tmpl'); 		##
	
	$subject =~ s/'/\\'/g;
	$description =~ s/'/\\'/g;

	if($subject and $description){
		my $query1 = $query->new();		
		my $lt = localtime();
		my $year = $lt->year+1900;
		my $mon = $lt->mon+1;
		my $localdate = $mon."-".$lt->mday."-".$year;

		my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
		$query1 = $conn->prepare("insert into problem(p_name,p_desc,p_date,m_id) values ('$subject','$description','$localdate','4')");
		$query1->execute();
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/user/problem/user_problem.tmpl'); 
		$template3->param(SUCCESS=>"Your problem is submited Successfully.");
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;
	}
	else{
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/user/problem/user_problem.tmpl'); 
		$template3->param(SUCCESS=>"Your problem is not submited.\nPlease Try again later.$subject $description");
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;
	}
}
