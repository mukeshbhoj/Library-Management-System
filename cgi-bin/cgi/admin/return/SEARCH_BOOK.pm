#!/usr/bin/perl
package SEARCH_BOOK;
use strict;
use DBI;
use CGI;
use HTML::Template;
use Time::localtime;
use Date::Calc qw(Delta_Days);

sub search
{
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
			if($days > 30)
			{
				$fine = $days-30;
			}
			#==================================================
			$row_data{Fine}=$fine;
			push(@loop_data,\%row_data);
		}
	return \@loop_data;
}


sub calculate_fine
{
	my $bid = shift;
	my $fine = 0;
	my @loop_data;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

	my $query1 = $conn->prepare("select issue_date from issue_book where book_id = '$bid' and return_by = '0'");
	$query1->execute();
	my @op = $query1->fetchrow_array();

	my $lt = localtime();
	my $year = $lt->year+1900;
	my $mon = $lt->mon+1;
	my @today = ($year,$mon,$lt->mday);
	my @date = split /-/,$op[0];
	my $days = Delta_Days(@date, @today);
	if($days > 30)
	{
		$fine = $days-30;
	}
	return $fine;
}

sub fine
{
	my ($bid,$username) = @_;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
	my $fine = calculate_fine($bid);

	my $query1 = $conn->prepare("select m_id from issue_book where book_id = '$bid' and return_by = '0'");
	$query1->execute();
	my @op = $query1->fetchrow_array();
	
	my $query2 = $conn->prepare("select m_id from users where username = '$username'");
	$query2->execute();
	my @userid = $query2->fetchrow_array();

	my $days = $fine + 30;
	my $query3 = $conn->prepare("insert into fine (m_id,book_id,days,fine,taken_by) values ('$op[0]','$bid','$days','$fine','$userid[0]')");
	$query3->execute();

}

sub return_book
{
	my ($bid,$username) = @_;
	my $fine = 0;
	my @loop_data;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
	
	my $lt = localtime();
	my $year = $lt->year+1900;
	my $mon = $lt->mon+1;
	my $today = $mon."-".$lt->mday."-".$year;
	
	my $query2 = $conn->prepare("select m_id from users where username = '$username'");
	$query2->execute();
	my @userid = $query2->fetchrow_array();

	my $query1 = $conn->prepare("update issue_book set return_date = '$today', return_by = '$userid[0]' where book_id = '$bid' and return_by = '0'");
	$query1->execute();

	my $query3 = $conn->prepare("update book set status = 'available' where book_id = '$bid' ");
	$query3->execute();

}

sub today_date
{
	my $lt = localtime();
	my $year = $lt->year+1900;
	my $mon = $lt->mon+1;
	my $today = $lt->mday."-".$mon."-".$year;
	return $today;
}

sub find_name
{
	my $bid = shift;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

	my $query1 = $conn->prepare("select m_id from issue_book where book_id = '$bid' and return_by = '0'");
	$query1->execute();
	my @op = $query1->fetchrow_array();

	my $query2 = $conn->prepare("select m_name from member where m_id = '$op[0]'");
	$query2->execute();
	my @username = $query2->fetchrow_array();
	return $username[0];
}

1;
