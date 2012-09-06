#!/usr/bin/perl
package SEARCH_BOOK;
use strict;
use DBI;
use CGI;
use HTML::Template;

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
		my($gid,$title,$sub,$tag,$auth,$edition,$publisher,$copy,$price,$bid,$status) = @op;
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
1;
