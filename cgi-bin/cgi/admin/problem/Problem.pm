#!/usr/bin/perl
package Problem;
use strict;
use DBI;
use CGI;
use Data::Dumper;
use Time::localtime;

my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

sub search{
	my $query1 = $conn->prepare("select p_id,p_name,p_desc,m_id,p_date from problem where solvedby = 0");
	$query1->execute();

		my @loop_data = ();
		while(my @op = $query1->fetchrow_array()){
			my %row_data;
			my($p_id,$p_name,$desc,$mid,$date) = @op;
			$row_data{p_id}=$p_id;
			$row_data{m_id}=$mid;


			$row_data{p_name}=$p_name;
			$row_data{description}=$desc;
			$row_data{p_date}=$date;
		
			push(@loop_data,\%row_data);
		}
	return \@loop_data;
}

sub find_id{
	my $username = shift;
	my $query2 = $conn->prepare("select m_id from users where username = '$username'");
	$query2->execute();
	my @userid = $query2->fetchrow_array();
	return $userid[0];
}

sub solve{
	my ($userid,$pid)= @_;

	my $lt = localtime();
	my $year = $lt->year+1900;
	my $mon = $lt->mon+1;
	my $localdate = $mon."-".$lt->mday."-".$year;

	my $query1 = $conn->prepare("update problem set solvedby = '$userid', solve_date = '$localdate' where p_id = '$pid'");
	$query1->execute();
}

1;
