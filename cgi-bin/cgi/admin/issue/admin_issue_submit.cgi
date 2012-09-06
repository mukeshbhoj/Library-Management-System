#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use Data::Dumper;
use HTML::Template;
use CGI::Session;
use Check_add_book;
use SEARCH_BOOK;
use lib '..';
use Check_add_mem;
use SMS;



my $query = CGI->new();
my $id  = $query->param("txtid");
my $mid = $query->param("txtmid");
my $bid = $query->param("rd_bid");
my $session = CGI::Session->new();																
my $username = $session->param('ADMIN');

if($session->param('ADMIN')){
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	$template2->param(username=>$username);	
	print $query->header();
	my $flag = 0;
	if($query->param("search_books")){
		
		if(!($id)){
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
			$template3->param(no_group=>'Please memntion Group ID');
			$template3->param(search_table=>'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_id($id)){							
			my $loop_data = SEARCH_BOOK::search_for_issue($id);	
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl'); 
			$template3->param(issuebooks=>$loop_data);
			$template3->param(SUCCESS=>@$loop_data." book(s) available");
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		else{
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
			$template3->param(no_group=>'This Group ID is not present');
			$template3->param(search_table=>'hidden');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
	}
	elsif($query->param("issue_books")){
		if(!($mid)){
				my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
				$template3->param(no_mem=>'Please memntion Member ID');
				$template3->param(search_table=>'hidden');
				print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(!(Check_add_mem::check_id($mid))){
				my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
				$template3->param(no_mem=>'Invalid Member ID');
				$template3->param(search_table=>'hidden');
				print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(!($bid)){
				my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
				$template3->param(no_mem=>'Please select any book');
				print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_bookallow($mid)){
				my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
				$template3->param(no_mem=>'Member cannot issue more than total allowed books.');
				print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_book_group($mid,$bid)){
				my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
				$template3->param(no_mem=>'Member cannot issue more than one book of same group.');
				print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		elsif(Check_add_book::check_bid($bid)){							
			SEARCH_BOOK::issue_book($bid,$mid,$username);
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl'); 
			$template3->param(SUCCESS=>"Book issued successfully");
			if(SMS::issue($bid,$mid)){}
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
		else{
			my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/issue/admin_issue.tmpl');
			$template3->param(no_mid=>'This Book Id is not present');
			print $template1->output,$template2->output,$template3->output,$template4->output;
		}
	}
}

else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
