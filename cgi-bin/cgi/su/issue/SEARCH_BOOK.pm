#!/usr/bin/perl
package SEARCH_BOOK;
use strict;
use DBI;
use CGI;
use HTML::Template;
use Time::localtime;

sub search_for_issue
{
my $id = shift;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select b.book_id,b.status,bi.* from book b,book_info bi where b.group_id=bi.group_id and b.group_id = '$id' and b.status = 'available' order by b.book_id");
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

sub issue_book
{
my ($bid,$mid,$username) = @_;
my @loop_data;
my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

my $query1 = $conn->prepare("update book set status = 'not available' where book_id = '$bid'");
$query1->execute();
my $query2 = $conn->prepare("select m_id from users where username = '$username'");
$query2->execute();
my @userid = $query2->fetchrow_array();

my $lt = localtime();
my $year = $lt->year+1900;
my $mon = $lt->mon+1;
my $localdate = $mon."-".$lt->mday."-".$year;

my $query3 = $conn->prepare("insert into issue_book (m_id, book_id, issue_date, issue_by) values('$mid','$bid','$localdate','$userid[0]')");
$query3->execute();

}

1;
