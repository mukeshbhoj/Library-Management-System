#!/usr/bin/perl
package Check_add_book;
use strict;
use DBI;
use CGI;
use HTML::Template;

my $query = CGI->new();
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});


sub check_id{
	my $id = shift;
	$query = $conn->prepare("select group_id from book_info");
	$query->execute();
	while(my @op = $query->fetchrow_array()){
		if (grep {$_ eq $id} @op){
			return 1;
		}
	}
	return 0;
}

sub check_bid{
	my $id = shift;
	$query = $conn->prepare("select book_id from book");
	$query->execute();
	while(my @op = $query->fetchrow_array()){
		if (grep {$_ eq $id} @op){
			return 1;
		}
	}
	return 0;
}

sub check_bookallow{
	my $mid = shift;
	$query = $conn->prepare("select count(*) from issue_book where m_id = '$mid' and return_by = '0'");
	$query->execute();
	my @op = $query->fetchrow_array();
	$query = $conn->prepare("select max_book_allow from member where m_id = '$mid'");
	$query->execute();
	my @op1 = $query->fetchrow_array();
	
	if($op1[0] <= $op[0])
	{return 1;}
	return 0;

}

sub check_book_group{
	my ($mid,$bid) = @_;
	$query = $conn->prepare("select count(*) from issue_book ib, book b where ib.m_id = '$mid' and ib.book_id=b.book_id and b.group_id in (select group_id from book b where b.book_id='$bid') and return_by = '0'");
	$query->execute();
	my @op = $query->fetchrow_array();
	return $op[0];

}
1;
