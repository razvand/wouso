#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/update_passwords.py utils/sample-data/sample-user-password-list.csv

import sys
import csv
import codecs
import wouso.utils.user_util

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def main():
    if len(sys.argv) != 2:
        print 'Usage: python add_users.py <file.csv>'
        print " CSV columns: username, first name, last name, email, active, is_staff, is_superuser, school_id, school_name, password"
        sys.exit(1)

    csvfile = open(sys.argv[1], 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        username = row[0]
        password = row[9]
        try:
            ret = wouso.utils.user_util.change_password(username, password)
        except:
            print "Failed changing password for user %s." %(username)
            continue
        if ret:
            print "Successfully changed password for user %s." %(username)
        else:
            print "Failed changing password for user %s." %(username)


if __name__ == "__main__":
    sys.exit(main())
