#!/usr/bin/env python
######################################################################
##                
## Copyright (C) 2006,  Goedson Teixeira Paixao
##                
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor Boston, 
## MA 02110-1301, USA
##                
## Filename:      check_pass_pam.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   Check ejabberd user password using PAM
##                
## Created at:    Wed Aug  2 09:50:56 2006
## Modified at:   Tue Aug 22 09:54:59 2006
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################
'''
An external script for ejabberd to check user passwords against PAM
'''

__revision__ = '0.1'




import sys
import traceback
import struct
import time



def main():
    log_file = open('/home/ejabberd/logs/error.log', 'w')
    log_file.write('YOO HERE')

if __name__ == '__main__':
    main()