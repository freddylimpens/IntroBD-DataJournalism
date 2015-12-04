#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#

import os, shutil
import sys
import re
import json
import markdown
import requests

from lxml import etree
from lxml import html
from slugify import slugify

def fetch_video_thumb(video_link):
    """
        fetch video thumbnail
        FIXME: vimeo-only code
    """
    # get video id
    video_id = video_link.rsplit('/', 1)[1]
    print ("== video ID = %s" % video_id)
    try: 
        # fetch json
        response = requests.request('GET', VIDEO_THUMB_API_URL+video_id+'.json')
        data = response.json()[0]
        # copy image link
        image_link = data['thumbnail_large']
        image_link = image_link.replace('wepb', 'jpg')
    except Exception:
        #raise
        print (" ----------------  error while fetching video %s" % (video_link))
        image_link = DEFAULT_VIDEO_THUMB_URL    
    
    return image_link


def main(argv):
    """
        get list of artists, in text file, for a given area code
    """
    # if len(sys.argv) != 3:
    #     print(" requires 2 arguments (file in + module_folder)")
    #     return False
    #area = sys.argv[1]
    area = '08310658-51eb-3801-80de-5a0739207115'
    artist_list = []
    # http://musicbrainz.org/ws/2/artist?area=08310658-51eb-3801-80de-5a0739207115&limit=100&fmt=json
    
    # first call to get count
    artist_count = 1000
    offset = 0
    while offset < artist_count:
        res = requests.get('http://musicbrainz.org/ws/2/artist', params={'area':area, 'limit':100, 'fmt':'json', 'offset':offset})
        print(" fetching %s" % res.url)
        #print("fetched : %s" % str(res.json()))
        data = res.json()
        artist_count = data['artist-count']
        offset +=100 
        for artist in data['artists']:
            artist_list.append(artist['name'])
        print ("offset = %d | artists list length = %d" % (offset, len(artist_list)))
        
    with open('artist_'+area+'.txt', 'w') as outfile:
        outfile.write(str(artist_list))


############### main ################
if __name__ == "__main__":
    main(sys.argv)
