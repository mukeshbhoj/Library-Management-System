#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use Check_add_mem;
use Search_mem;
use SEARCH_BOOK;
use DBI;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('ADMIN')){
	my $username1 = $session->param('ADMIN');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##

	my $id = $query->param("txtid");

	if(Check_add_mem::check_id($id)){
		my @member = Search_mem::search_mem($id);
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_search.tmpl'); 
		$template3->param(THIS_LOOP=>\@member);

		my $issued_book = SEARCH_BOOK::search_issued($id);
		$template3->param(issued_book=>$issued_book);
		$template3->param(total_book=>$member[0]->{name}." has issued ".@$issued_book." book(s).");
		
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;

	}
	else{
		my $template5 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_member_search.tmpl'); 
		$template5->param(varid=>"ID is not found");
		$template5->param(search_table=>'hidden');
		$template5->param(search_books=>'hidden');
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
