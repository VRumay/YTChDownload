""" 
YT-Coyote is a very small script I developed to help my girlfriend extract over 200 videos from a channel she has without having to do it manually or use a third party service. 

The initial idea was to use selenium, but fortunately, I came across the pytube library, which makes things so much simpler!

I expect to expand the application later on. 

"""

import pytube

vidList =  ['https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/watch?v=cUYSGojUuAU',
            'https://www.youtube.com/watch?v=ZZ5LpwO-An4']

print(len(vidList))

for eachVid in vidList:
    getUrl = pytube.YouTube(eachVid)
    getVid = getUrl.streams.get_highest_resolution()
    print(f'Attempting download on: {getVid.title} from {eachVid}')
    getVid.download(r'G:\...\Destination Folder')
    print(f'Download complete: {getVid.title} from {eachVid}')

            
