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

''' Get main instance for file operation '''
kuaipan_file = Kuaipan.KuaipanFile(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

''' Create a dummy test file '''
myfile = 'kuaipan_test.txt'
with open(myfile, 'wb') as fp:
    fp.write('This a demostration for Kuaipan API')
mydir = 'testdir'


print ' API demostration start! '

print '\n 1. show information of your account '
pprint.pprint( kuaipan_file.account_info() )

print '\n 2. Upload our test file '
pprint.pprint( kuaipan_file.upload_file(myfile, ForceOverwrite=True) )

print '\n 3. Get file metadata '
pprint.pprint( kuaipan_file.metadata(myfile) )

print '\n 4. Get file reference info '
pprint.pprint( kuaipan_file.copy_ref(myfile) )

print '\n 5. Get share link '
pprint.pprint( kuaipan_file.shares(myfile) )

print '\n 6. Get HTML document view '
pprint.pprint( kuaipan_file.fileops_documentView(myfile, zip=0) )

print '\n 7. Get thumbnail '
print( kuaipan_file.fileops_thumbnail(100, 100, myfile) )

print '\n 8. Get file history (If the file is never changed, the history would be 404 not found) '
pprint.pprint( kuaipan_file.upload_file(myfile, ForceOverwrite=True) ) # upload again to generate history
pprint.pprint( kuaipan_file.history(myfile) )

print '\n 7. Copy file (or directory) '
pprint.pprint( kuaipan_file.fileops_copy(myfile, myfile+'2') )

print '\n 8. Move file (or directory) '
pprint.pprint( kuaipan_file.fileops_move(myfile+'2', myfile+'3') )

print '\n 9. Delete file (or directory) '
pprint.pprint( kuaipan_file.fileops_delete(myfile+'3') )

print '\n 10. Create directory '
pprint.pprint( kuaipan_file.fileops_create_folder(mydir) )

print '\n 11. Download file to newfile.txt '
kuaipan_file.download_file(myfile, local_filepath="newfile.txt")
