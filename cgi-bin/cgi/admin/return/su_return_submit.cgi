#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use SEARCH_BOOK;
use Data::Dumper;


my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();
if($session->param('ADMIN'))
{
	my $username1 = $session->param('ADMIN');
	print $query->header();
	my @books = $query->param('rd_bid');
	my @finebooks = ();
	my $total = 0;
	my $checked = 0;
	foreach my $bid(@books)
	{
		my $fine = SEARCH_BOOK::calculate_fine($bid);
		
#========= if fine is zero =================#
		if($fine == 0)
		{
			SEARCH_BOOK::return_book($bid,$username1);
			delete $books[$checked];
		}
		$total += $fine;
		$checked++;
	}
	for my $c (@books)
	{
		if($c)
		{
			my %row_data;
			$row_data{bookid}=$c;
			push(@finebooks,\%row_data);
		}
	}
	

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/su/su_header.tmpl');   	##	su_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/su/su_pageheader.tmpl');	##	su_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/su/su_footer.tmpl'); 		##
	$template2->param(username=>$username1);
	
#========= if all books without fine then =================#
	if($total == 0)
	{	
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/return/su_return.tmpl');
		$template3->param(SUCCESS=>" $checked Book(s) returned successfully");
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
#========= if fine is not zero ==============#
	else
	{
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/return/su_return_fine.tmpl');
	
		my $today = SEARCH_BOOK::today_date();
		my $name = SEARCH_BOOK::find_name($finebooks[0]->{bookid});

		$template3->param(library=>'The Central Library For Public');
		$template3->param(name=>$name);
		$template3->param(fine=>$total);
		$template3->param(finebooks=>\@finebooks);
		$template3->param(date=>$today);
		$template3->param(books=>$checked);
		foreach my $bid(@books)
		{
			SEARCH_BOOK::fine($bid,$username1);
			SEARCH_BOOK::return_book($bid,$username1);
		}
		
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
#===========================================#
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
