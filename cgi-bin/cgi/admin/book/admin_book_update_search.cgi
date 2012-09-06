#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use HTML::Template;
use Check_add_book;
use SEARCH_BOOK;
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
	if(Check_add_book::check_id($id)){
		my @book = SEARCH_BOOK::search_for_update($id);
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_update_submit.tmpl'); 
		$template3->param(txtid=>$book[0]);
		$template3->param(txttitle=>$book[1]);
		$template3->param(txtsubject=>$book[2]);
		$template3->param(txttag=>$book[3]);
		$template3->param(txtauthor=>$book[4]);
		$template3->param(txtpublisher=>$book[5]);
		$template3->param(txtedition=>$book[6]);
		$template3->param(txtcopy=>$book[7]);
		$template3->param(txtprice=>$book[8]);
		print $query->header();
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;
	}
	else{
		my $template5 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_update.tmpl'); 
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
