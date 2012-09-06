#!/usr/bin/perl
package SEARCH_BOOK;
use strict;
use DBI;
use CGI;
use HTML::Template;
use Time::localtime;
use Date::Calc qw(Delta_Days);

sub search_issued{
	my $mid = shift;
	my @loop_data;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
	my $query1 = $conn->prepare("select ib.book_id, bi.title, ib.issue_date, ib.issue_by from issue_book ib, book b, book_info bi where ib.book_id = b.book_id and b.group_id = bi.group_id and ib.m_id = '$mid' and ib.return_by = '0' order by ib.issue_date");
	$query1->execute();
	while(my @op = $query1->fetchrow_array())
	{
		my $fine = 0;
		my %row_data;
		my($bid,$title,$issuedate,$issueby) = @op;
		$row_data{bid}=$bid;
		$row_data{title}=$title;
		$row_data{issuedate}=$issuedate;
		$row_data{issueby}=$issueby;
		#==============calculate fine=====================		
		my $lt = localtime();
		my $year = $lt->year+1900;
		my $mon = $lt->mon+1;
		my @today = ($year,$mon,$lt->mday);
		my @date = split /-/,$issuedate;
		my $days = Delta_Days(@date, @today);
		if($days > 30){
			$fine = $days-30;
		}
		#==================================================
		$row_data{Fine}=$fine;
		push(@loop_data,\%row_data);
	}
	return \@loop_data;
}
1;
