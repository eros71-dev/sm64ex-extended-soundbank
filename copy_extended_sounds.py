#!/usr/bin/env python3
import os

copy_directories = {
    'sound/samples/instruments/': [
        'sound/samples/extended/',
    ],
    'sound/samples/bowser_organ/': [
        'sound/samples/extended/',
    ],
    'sound/samples/course_start/': [
        'sound/samples/extended/',
    ],
    'sound/samples/piranha_music_box/': [
        'sound/samples/extended/',
    ],
}

# If extended folder doesn't exist, create it
if not os.path.exists('sound/samples/extended/'):
    os.makedirs('sound/samples/extended/')
    print('Created extended soundbank folder, as it was missing')

def copy_dir(source, destinations):
    for filename in os.listdir(source):
        if not filename.endswith('.aiff'):
            continue
        src = source + filename

        shortened_name = filename.split('_')[0] + '.aiff'
        for destination in destinations:
            dst = destination + shortened_name
            if os.path.exists(dst):
                continue
            print('Copying instrument samples to the extended soundbank folder: ' + src + ' -> ' + dst)
            os.system('cp ' +  src + ' ' + dst)

def main():
    for source in copy_directories:
        copy_dir(source, copy_directories[source])

if __name__ == "__main__":
    main()
