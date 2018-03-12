import os
import sys
import re
import subprocess
import datetime


def system(cmd):
	print cmd
	ret = os.system(cmd)
	if ret!=0:
		sys.exit(ret)

def rm(filename):
	os.system("rm -Rf %s" % filename.replace("\\","/") )

def copy(src,dst):
	system("cp %s %s" % (src,dst) )

loan_years = 30
loan = 80*10000
lending_yearly_rate = 0.0546
lending_monthly_rate = lending_yearly_rate / 12
monthly_repayment = float(loan) * lending_monthly_rate * ((1 + lending_monthly_rate) ** (12 * loan_years)) / \
    ((1 + lending_monthly_rate) ** (12 * loan_years) - 1)

print(monthly_repayment)
