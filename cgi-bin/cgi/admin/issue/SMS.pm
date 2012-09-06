#!/usr/bin/perl
package SMS;
use strict;
use Net::SMS::WAY2SMS;
use DBI;
use CGI;

sub issue{ 
	my ($bid,$mid) = @_;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
	my $query1 = $conn->prepare("select m_phno,m_name from member where m_id = '$mid'");
	$query1->execute();
	my @member =  $query1->fetchrow_array();
    my $s = Net::SMS::WAY2SMS->new(
       'user' => '8140845297',
       'password' => '8140845297',
       'mob'=>[$member[0]]
    );
 

	my $query2 = $conn->prepare("select b.book_id,bi.title from book b,book_info bi where b.group_id=bi.group_id and b.book_id='$bid'");
	$query2->execute();
	my @book =  $query2->fetchrow_array();
	$s->send("Book Id: $book[0] \n Title : $book[1] \n is issued successfully by $member[1]");
}


sub return{ 
	my ($bid,$mid,$fine) = @_;
	my $query = CGI->new();
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
	my $query1 = $conn->prepare("select m_phno,m_name from member where m_id = '$mid'");
	$query1->execute();
	my @member =  $query1->fetchrow_array();
    my $s = Net::SMS::WAY2SMS->new(
       'user' => '8140845297',
       'password' => '8140845297',
       'mob'=>[$member[0]]
    );

	$s->send("Book Id: @$bid  \n is/are returned successfully by $member[1].\nYou have paid $fine Rs fine.");
}


1;
