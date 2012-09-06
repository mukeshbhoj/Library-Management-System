#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use Search_mem;
use DBI;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
my $username1 = $session->param('LIBRARIAN');
if($session->param('LIBRARIAN'))
{
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/su/su_header.tmpl');   	##	su_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/su/su_pageheader.tmpl');	##	su_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/su/su_footer.tmpl'); 		##

	if($query->param('changeprofile'))
	{
		my $id = Search_mem::search_id($username1);
		my @member = Search_mem::search_mem_arr($id);
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/profile/su_change_profile.tmpl'); 
		$template3->param(txtid=>$member[0]);
		$template3->param(txtname=>$member[1]);
		$template3->param(txtbirthdate=>$member[2]);
		$template3->param(txtaddress=>$member[3]);
		$template3->param(txtcity=>$member[4]);
		$template3->param(txtstate=>$member[5]);
		$template3->param($member[6]=>'selected');
		$template3->param(txtphno=>$member[7]);
		$template3->param(txtjoindate=>$member[8]);
		$template3->param(txttype=>$member[9]);
		$template3->param(txtbookallow=>$member[10]);
		$template3->param(txtusername=>$member[11]);
		print "Content-Type:text/html\n\n";
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;
	}
	
	elsif($query->param('changepassword'))
	{
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/profile/su_change_password.tmpl'); 
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;
	}
	
}

else
	{
		print $query->redirect(-url=>'/cgi-bin/library.cgi');
	}
