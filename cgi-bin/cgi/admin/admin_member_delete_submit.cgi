#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Check_add_mem;

my $query = CGI->new();
my $id = $query->param("txtid");
my $session = CGI::Session->new();																
my $username = $session->param('ADMIN');
if($session->param('ADMIN'))
{
	if(Check_add_mem::check_id($id)){
		my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
		my $query1 = $conn->prepare("delete from users where m_id = '$id'");
		my $query2 = $conn->prepare("delete from member where m_id = '$id'");
		my $query3 = $conn->prepare("delete from issue_book where m_id = '$id'");
		my $query4 = $conn->prepare("delete from fine where m_id = '$id'");
		my $query5 = $conn->prepare("delete from problem where m_id = '$id'");
		$query5->execute();
		$query4->execute();
		$query3->execute();
		$query1->execute();
		$query2->execute();
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_home.tmpl'); 
		$template2->param(username=>$username);							
		$template3->param('SUCCESS'=>'Member deleted successfully.');

		print $query->header();

	#	print "$id, $name , $birthdate ,$address , $city , $state , $sex , $phno , $joindate , $username , $password , $confpassword";
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
	else{
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_delete.tmpl'); 
		$template2->param(username=>$username);							
		$template3->param(no_mem=>'This ID is not present');
		print $query->header();

	#	print "$id, $name , $birthdate ,$address , $city , $state , $sex , $phno , $joindate , $username , $password , $confpassword";
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
}

else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
