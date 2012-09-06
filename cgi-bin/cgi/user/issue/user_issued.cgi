#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use Data::Dumper;
use HTML::Template;
use CGI::Session;
use Search_mem;
use SEARCH_BOOK;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('USERNAME')){
	my $username1 = $session->param('USERNAME');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/user/user_header.tmpl');   	##	user_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/user/user_pageheader.tmpl');	##	user_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/user/user_footer.tmpl'); 		##
	my $id = Search_mem::search_id($username1);
	my $template3 = HTML::Template->new(filename => '/var/www/project/html/user/issue/user_issue.tmpl'); 
	my $issued_book = SEARCH_BOOK::search_issued($id);
	$template2->param(username=>$username1);		
	$template3->param(issued_book=>$issued_book);
	$template3->param(total_book=>@$issued_book." book(s) are issued .");
	if(@$issued_book == 0){
		$template3->param(total_book=>"No book(s) are issued .");
		$template3->param(search_table=>"hidden");
	}

	print $query->header();
	print $template1->output;
	print $template2->output;
	print $template3->output;
	print $template4->output;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
