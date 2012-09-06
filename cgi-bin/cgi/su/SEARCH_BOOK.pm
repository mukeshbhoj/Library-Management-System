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
my $search = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select * from book_info where $search order by group_id");
$query1->execute();
	while(my @op = $query1->fetchrow_array())
	{
		my %row_data;
		my($gid,$title,$sub,$tag,$auth,$publisher,$edition,$copy,$price) = @op;
		$row_data{GID}=$gid;
		$row_data{TITLE}=$title;
		$row_data{SUB}=$sub;
		$row_data{TAG}=$tag;
		$row_data{AUTH}=$auth;
		$row_data{EDITION}=$edition;
		$row_data{PUBLISHER}=$publisher;
		$row_data{COPY_TOTAL}=$copy;
		my $query2 = $conn->prepare("select count(*) from book where group_id = '$gid' and status = 'available'");
		$query2->execute();
		my @avail = $query2->fetchrow_array();
		$row_data{COPY_AVAIL}=$avail[0];
		push(@loop_data,\%row_data);
	}
return \@loop_data;
}

sub search_all
{
my $search = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select b.book_id,b.status,bi.* from book b,book_info bi where b.group_id=bi.group_id order by bi.group_id");
$query1->execute();
	while(my @op = $query1->fetchrow_array())
	{
		my %row_data;
		my($bid,$status,$gid,$title,$sub,$tag,$auth,$publisher,$edition,$copy,$price) = @op;
		$row_data{BID}=$bid;
		$row_data{TITLE}=$title;
		$row_data{SUB}=$sub;
		$row_data{TAG}=$tag;
		$row_data{AUTH}=$auth;
		$row_data{EDITION}=$edition;
		$row_data{PUBLISHER}=$publisher;
		$row_data{AVAIL}=$status;
		push(@loop_data,\%row_data);
	}
return \@loop_data;
}


sub search_for_update
{
my $id = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select * from book_info where group_id = '$id'");
$query1->execute();
my @op = $query1->fetchrow_array();
return @op;
}


sub search_for_delete
{
my $id = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select b.book_id,b.status,bi.* from book b,book_info bi where b.group_id=bi.group_id and b.group_id = '$id'");
$query1->execute();
	while(my @op = $query1->fetchrow_array())
	{
		my %row_data;
		my($bid,$status,$gid,$title,$sub,$tag,$auth,$edition,$publisher,$copy,$price) = @op;
		$row_data{BID}=$bid;
		$row_data{TITLE}=$title;
		$row_data{SUB}=$sub;
		$row_data{TAG}=$tag;
		$row_data{AUTH}=$auth;
		$row_data{EDITION}=$edition;
		$row_data{PUBLISHER}=$publisher;
		$row_data{AVAIL}=$status;
		push(@loop_data,\%row_data);
	}
return \@loop_data;
}

sub delete_book
{
my $bid = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select b.group_id, bi.copy from book b, book_info bi where b.group_id=bi.group_id and book_id = '$bid'");
$query1->execute();
my @op = $query1->fetchrow_array();
my $id = $op[0];
my $copy = $op[1]-1;
my $query2 = $conn->prepare("delete from book where book_id = '$bid'");
$query2->execute();
my $query3;
if($copy)
{
	$query3 = $conn->prepare("update book_info set copy = $copy where group_id = '$id'");
}
else
{
	$query3 = $conn->prepare("delete from book_info where group_id = '$id'");
}
$query3->execute();
}

sub search_issued
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


1;
