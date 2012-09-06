#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Check_add_mem;

my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('LIBRARIAN'))
{
	my $username1 = $session->param('LIBRARIAN');
	my $id = $query->param("txtid");
	my $oldpassword = $query->param('txtoldpassword');
	my $newpassword = $query->param('txtnewpassword');
	my $confpassword = $query->param('txtconfpassword');

	$oldpassword =~ s/'/\\'/g;
	$newpassword =~ s/'/\\'/g;
	$confpassword =~ s/'/\\'/g;

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/su/su_header.tmpl');   	##	su_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/su/su_pageheader.tmpl');	##	su_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/su/su_footer.tmpl'); 		##
	$template2->param(username=>$username1);

	my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/profile/su_change_password.tmpl'); 
	if(!($oldpassword))
	{$template3->param('varoldpassword'=>"Password is required");$flag = 1;}
	if(!($newpassword))
	{$template3->param('varnewpassword'=>"Password is required");$flag = 1;}

	if(!(Check_add_mem::check_password($oldpassword,$username1)))
	{$template3->param('varoldpassword'=>"Wrong Password");$flag = 1;}

	if(!($newpassword eq $confpassword))
	{$template3->param('varnewpassword'=>"Passwords are not matched");$flag = 1;}

	if($flag == 0)
	{
		my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
		my $query1 = $conn->prepare(" update users set password='$newpassword' where username='$username1'");
		$query1->execute();

		$session->param('profile','Password is changed successfully.');

		print $query->redirect(-url=>'/cgi-bin/su/profile/su_profile.cgi');
	}
	else
	{
		print $query->header();
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
