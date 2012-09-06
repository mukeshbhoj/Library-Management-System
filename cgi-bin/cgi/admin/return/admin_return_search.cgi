#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Check_add_mem;
use SEARCH_BOOK;
use Search_mem;

my $query = CGI->new();
my $id = $query->param("txtid");
my $session = CGI::Session->new();																
my $username = $session->param('ADMIN');
if($session->param('ADMIN'))
{
	if(Check_add_mem::check_id($id))
	{
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/return/admin_return_search.tmpl'); 
		$template2->param(username=>$username);							

		my @member = Search_mem::search_id($id);
		$template3->param(mid=>$member[0]);
		$template3->param(name=>$member[1]);
		$template3->param(address=>"$member[3], $member[4], $member[5]");
		$template3->param(phno=>$member[7]);
		$template3->param(usertype=>$member[9]);

		my $return_book = SEARCH_BOOK::search($id);
		$template3->param(returnbooks=>$return_book);
		$template3->param(issued_book=>$member[1]." has issued ".@$return_book." book(s).");
		
		print $query->header();
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
	else
	{
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/return/admin_return.tmpl'); 
		$template2->param(username=>$username);							
		$template3->param(no_mem=>'This ID is not present');
		print $query->header();
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
