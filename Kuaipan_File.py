#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Deren Wu <deren.g@gmail.com> (author).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# @file: Kuaipan_File.py
# @date: 2013-11-8

'''
A demonstration for Kuaipan operation
'''

__author__ = 'deren.g@gmail.com (Deren Wu)'

import Kuaipan
import pprint

consumer_key = 'your_kuaipan_consumer_key'
consumer_secret = 'your_kuaipan_consumer_secret'
oauth_token        = 'your_kuaipan_oauth_token'
oauth_token_secret = 'your_kuaipan_oauth_token_secret'

''' Make sure we are running in UTF-8 encoding by default '''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

''' Get main instance for file operation '''
kuaipan_file = Kuaipan.KuaipanFile(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

''' Create a dummy test file '''
myfile = 'demo_test.txt'
with open(myfile, 'wb') as fp:
    fp.write(u'English: This a demostration for API usage!\n'+
				u'繁體中文： 範例測試\n'+
				u'简体中文： 范例测试\n')
mydir = 'testdir'
myfile_kuaipan = '/'+mydir+'/'+myfile

print ' API demostration start! '

print '\n 1. show information of your account '
pprint.pprint( kuaipan_file.account_info() )

print '\n 2. Create directory '
pprint.pprint( kuaipan_file.fileops_create_folder(mydir) )

print '\n 3. Upload our test file '
pprint.pprint( kuaipan_file.upload_file(myfile, kuaipan_path=myfile_kuaipan, ForceOverwrite=True) )

print '\n 4. Get file metadata '
pprint.pprint( kuaipan_file.metadata(myfile_kuaipan) )

print '\n 5. Get file reference info '
pprint.pprint( kuaipan_file.copy_ref(myfile_kuaipan) )

print '\n 6. Get share link (Response [{u\'msg\': u\'PSA_OUTLINK_STATUS_REVIEWING\'}] means the file is under review by Kuaipan office. You need to wait!)'
try:
    pprint.pprint( kuaipan_file.shares(myfile_kuaipan) )
except:
    pprint.pprint('Is your file with zero size or include invalid file name?')

print '\n 7. Get HTML document view '
pprint.pprint( kuaipan_file.fileops_documentView(myfile_kuaipan, zip=0) )

print '\n 8. Get thumbnail '
print( kuaipan_file.fileops_thumbnail(100, 100, myfile_kuaipan) )

print '\n 9. Get file history (If the file is never changed, the history would be 404 not found) '
pprint.pprint( kuaipan_file.upload_file(myfile, kuaipan_path=myfile_kuaipan, ForceOverwrite=True) ) # upload again to generate history
pprint.pprint( kuaipan_file.history(myfile_kuaipan) )

print '\n 10. Copy file (or directory) '
pprint.pprint( kuaipan_file.fileops_copy(myfile_kuaipan, myfile_kuaipan+'2') )

print '\n 11. Move file (or directory) '
pprint.pprint( kuaipan_file.fileops_move(myfile_kuaipan+'2', myfile_kuaipan+'3') )

print '\n 12. Delete file (or directory) '
pprint.pprint( kuaipan_file.fileops_delete(myfile_kuaipan+'3') )

print '\n 13. Download file to newfile.txt '
kuaipan_file.download_file(myfile_kuaipan, local_filepath="newfile.txt")
