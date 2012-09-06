#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use Data::Dumper;
use HTML::Template;
use CGI::Session;
use Check_add_book;
use SEARCH_BOOK;

my $query = CGI->new();
my $id  = $query->param("txtid");
my $bid = $query->param("txtbid");
my $session = CGI::Session->new();																
my $username = $session->param('ADMIN');
if($session->param('ADMIN'))
{
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	$template2->param(username=>$username);	
	print $query->header();

	if($query->param("search_books")){
		if(!($id)){
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_delete.tmpl');
			$template3->param(no_group=>'Please mention Group ID');
			$template3->param(delete_table => 'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_id($id)){							
			my $loop_data = SEARCH_BOOK::search_for_delete($id);	
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_delete.tmpl'); 
			$template3->param(deletebooks=>$loop_data);
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		else{
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_delete.tmpl');
			$template3->param(no_group=>'This Group ID is not present');
			$template3->param(delete_table => 'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
	}
	elsif($query->param("delete_books") or $query->param("txtbid")){
		if(!($bid)){
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_delete.tmpl');
			$template3->param(no_book=>'Please mention Book ID');
			$template3->param(delete_table => 'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_bid($bid)){							
			SEARCH_BOOK::delete_book($bid);
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_home.tmpl'); 
			$template3->param(SUCCESS=>"Book deleted successfully");
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		else{
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_delete.tmpl');
			$template3->param(no_book=>'This Book Id is not present');
			$template3->param(delete_table => 'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
	}
	else{
		print $query->redirect(-url=>'/cgi-bin/library.cgi');
	}
}

else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
