#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use Check_add_mem;
use Search_mem;
use DBI;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
my $username1 = $session->param('ADMIN');

if($session->param('ADMIN')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##

	my $id = $query->param("txtid");
	if(Check_add_mem::check_id($id)){
		my @member = Search_mem::search_id($id);
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_update_submit.tmpl'); 
		$template3->param(txtid=>$member[0]);
		$template3->param(txtname=>$member[1]);
		$template3->param(txtbirthdate=>$member[2]);
		$template3->param(txtaddress=>$member[3]);
		$template3->param(txtcity=>$member[4]);
		$template3->param(txtstate=>$member[5]);
		$template3->param($member[6]=>'selected');
		$template3->param(txtphno=>$member[7]);
		$template3->param(txtjoindate=>$member[8]);
		$template3->param($member[9]=>'selected');
		$template3->param(txtbookallow=>$member[10]);
		$template3->param(txtusername=>$member[11]);
		$template3->param(txtpassword=>$member[12]);
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;

	}
	else{
		my $template5 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_update.tmpl'); 
		$template5->param(varid=>"ID is not found");
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template5->output;
		print $template4->output;
	}
}

else{
		print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
